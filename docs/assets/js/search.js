// The site is published under a sub-path, so absolute URLs cannot be used.
// #site-root carries the (refiner-relativised) path back to the site root.
function siteRoot() {
    const el = document.getElementById('site-root');
    return el ? el.href : document.baseURI;
}

(function () {
    function normaliseQuery(value) {
        return (value || '').trim();
    }

    function currentQuery() {
        return normaliseQuery(new URLSearchParams(window.location.search).get('query'));
    }

    function updateLocation(query) {
        let url = new URL(window.location.href);
        if (query) {
            url.searchParams.set('query', query);
        } else {
            url.searchParams.delete('query');
        }
        if (url.href !== window.location.href) {
            history.pushState(null, '', url);
        }
    }

    function buildSnippet(text, summary, match) {
        if (!match || !match.indices || !match.indices.length) {
            return summary || '';
        }

        let first = match.indices[0];
        let start = Math.max(0, first[0] - 90);
        let end = Math.min(text.length, first[1] + 91);
        let snippet = text.slice(start, end).trim();
        if (start > 0) {
            snippet = '...' + snippet;
        }
        if (end < text.length) {
            snippet += '...';
        }
        return snippet;
    }

    function renderResults(resultsElement, statusElement, query, matches) {
        resultsElement.innerHTML = '';

        if (!query) {
            statusElement.textContent = 'Enter a search term.';
            return;
        }

        statusElement.textContent = matches.length ? `${matches.length} result(s)` : 'No results match your query.';

        matches.forEach((result) => {
            let item = result.item;
            let li = document.createElement('li');
            li.className = 'search-result';

            let title = document.createElement('a');
            title.className = 'search-result-title';
            title.href = new URL(item.path.replace(/^\//, ''), siteRoot()).href;
            title.textContent = item.title;
            li.appendChild(title);

            let meta = document.createElement('div');
            meta.className = 'search-result-meta';
            meta.textContent = item.kind;
            li.appendChild(meta);

            let textMatch = (result.matches || []).find((match) => match.key === 'text' || match.key === 'headings');
            let summary = document.createElement('p');
            summary.className = 'search-result-summary';
            summary.textContent = buildSnippet(item.text, item.summary, textMatch);
            li.appendChild(summary);

            resultsElement.appendChild(li);
        });
    }

    async function initialiseSearch() {
        let app = document.getElementById('search-app');
        if (!app) {
            return;
        }

        let statusElement = document.getElementById('search-status');
        let resultsElement = document.getElementById('search-results');
        let input = document.getElementById('page-search-input');
        let form = app.querySelector('.search-page-form');

        function syncInputs(query) {
            document.querySelectorAll('input[name="query"]').forEach((element) => {
                element.value = query;
            });
        }

        syncInputs(currentQuery());

        try {
            let response = await fetch(new URL('assets/search/search-index.json', siteRoot()));
            if (!response.ok) {
                throw new Error(`Failed to load search index: ${response.status}`);
            }

            let documents = await response.json();
            let fuse = new Fuse(documents, {
                includeMatches: true,
                ignoreLocation: true,
                minMatchCharLength: 2,
                threshold: 0.3,
                keys: [
                    { name: 'title', weight: 3 },
                    { name: 'headings', weight: 2 },
                    { name: 'text', weight: 1 },
                ],
            });

            function runSearch(query, updateHistory) {
                syncInputs(query);
                resultsElement.innerHTML = '';

                if (updateHistory) {
                    updateLocation(query);
                }

                if (!query) {
                    renderResults(resultsElement, statusElement, '', []);
                    return;
                }

                statusElement.textContent = 'Searching...';

                // rAF runs just before a paint and the timeout inside it just
                // after, so the emptied list and the "Searching..." status are
                // painted before the synchronous Fuse search blocks the thread.
                requestAnimationFrame(() => {
                    setTimeout(() => {
                        let matches = fuse.search(query, { limit: 100 });
                        renderResults(resultsElement, statusElement, query, matches);
                    }, 0);
                });
            }

            // The search index is kept in memory, so once it has loaded we
            // handle the form here instead of navigating to this page again
            // (which would reload and re-parse the index).
            if (form) {
                form.addEventListener('submit', (event) => {
                    event.preventDefault();
                    runSearch(normaliseQuery(input.value), true);
                });
            }

            window.addEventListener('popstate', () => {
                runSearch(currentQuery(), false);
            });

            runSearch(currentQuery(), false);
        } catch (error) {
            console.error(error);
            statusElement.textContent = 'Failed to load the search index.';
        }
    }

    document.addEventListener('DOMContentLoaded', initialiseSearch);
}());
