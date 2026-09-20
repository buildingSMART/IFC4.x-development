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

    function buildSnippet(text, match) {
        if (!match || !match.indices || !match.indices.length) {
            return text.length > 100 ? text.slice(0, 100) + '...' : text;
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
            summary.textContent = buildSnippet(item.text, textMatch);
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
        let params = new URLSearchParams(window.location.search);
        let query = normaliseQuery(params.get('query'));
        document.querySelectorAll('input[name="query"]').forEach((element) => {
            element.value = query;
        });

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

            let matches = query ? fuse.search(query, { limit: 100 }) : [];
            renderResults(resultsElement, statusElement, query, matches);
        } catch (error) {
            console.error(error);
            statusElement.textContent = 'Failed to load the search index.';
        }
    }

    document.addEventListener('DOMContentLoaded', initialiseSearch);
}());
