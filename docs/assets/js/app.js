function renderToggleIcon(element) {
    let icons = element.getElementsByClassName('toggle-icon');
    if (icons.length) {
        icons[0].remove();
    }

    let a = document.createElement('a');
    a.classList.add('toggle-icon');
    element.prepend(a);
    if (element.classList.contains('collapsed')) {
        a.innerHTML = feather.icons['chevron-up'].toSvg();
    } else {
        a.innerHTML = feather.icons['chevron-down'].toSvg();
    }
}

function refreshCollapsed(element) {
    let hide = element.classList.contains('collapsed');
    renderToggleIcon(element);

    let headerLevel = element.tagName.slice(-1);
    let sibling = element.nextElementSibling;
    while (sibling) {
        if (sibling.tagName.slice(0, 1) == 'H' && sibling.tagName.slice(-1) <= headerLevel)  {
            break;
        }
        sibling.style.display = hide ? 'none' : '';
        sibling = sibling.nextElementSibling;
    }
}

function makeHeadersCollapsible() {
    let elements = document.querySelectorAll('h2, h3, h4, h5, h6');
    for (let i=0; i<elements.length; i++) {
        let element = elements[i];
        renderToggleIcon(element);
        refreshCollapsed(element);

        element.onclick = function(e) {
            let target = e.target;
            if (target.classList.contains('feather-link')) {
                return;
            }
            while (target.tagName.slice(0, 1) != "H") {
                target = target.parentNode;
            }
            target.classList.toggle('collapsed');
            refreshCollapsed(target);
        }
    }
}

function generateSectionNavigation() {
    let content = document.getElementById('main-content');
    let nav = document.getElementById('section-navigation');
    let ol = nav.getElementsByTagName('ol')[0];
    Array.from(document.querySelectorAll('h2, h3, h4, h5, h6')).forEach((h2) => {
        let href = null;
        Array.from(h2.getElementsByTagName('a')).forEach((anchor) => {
            if (anchor.getAttribute('href')) {
                href = anchor.getAttribute('href');
            }
        });
        if (href) {
            let name = h2.textContent.trim();
            let subDivs = Array.from(h2.children).filter(el => el.tagName.toLowerCase() === "div");
            let number;
            if (subDivs.length === 2 && subDivs[0].className === 'number') {
                // terms and cond
                [number, name] = subDivs.map(el => el.textContent);
            } else if (h2.tagName.toLowerCase() === 'h2') {
                number = name.split(' ', 1)[0];
                if (name == number || ! /\d/.test(number)) {
                    number = '';
                } else {
                    name = name.substring(number.length);
                }
            } else {
                // to keep behaviour as before we only process h3+ on Ch 3.
                return;
            }
            

            li = document.createElement('li');
            li.setAttribute('number', number);
            a = document.createElement('a');
            a.setAttribute('href', href);
            a.textContent = name;
            li.append(a);
            ol.append(li);
        }
    });
    if (ol.getElementsByTagName('li').length > 1) {
        nav.classList.remove('hidden');
    }
}


function initialiseBackToTopButton() {
    let backToTop = document.getElementById('back-to-top');

    window.onscroll = function() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                backToTop.style.display = "block";
            } else {
                backToTop.style.display = "none";
        }
    };

    backToTop.addEventListener('click', function() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });
}

function setupInheritanceToggle() {
    let showElements = document.getElementsByClassName('show-inherited');
    let hideElements = document.getElementsByClassName('hide-inherited');

    function refreshInheritanceDisplay(type, showInherited) {
        let inheritedRows = document.getElementsByClassName('inherited');
        for (let i=0; i<inheritedRows.length; i++) {
            if (inheritedRows[i].getAttribute('data-type') == type) {
                inheritedRows[i].style.display = showInherited ? 'table-row' : 'none';
            }
        }
        for (let i=0; i<showElements.length; i++) {
            if (showElements[i].getAttribute('data-type') == type) {
                showElements[i].style.display = showInherited ? 'none' : 'block';
            }
        }
        for (let i=0; i<hideElements.length; i++) {
            if (hideElements[i].getAttribute('data-type') == type) {
                hideElements[i].style.display = showInherited ? 'block' : 'none';
            }
        }
    }

    for (let i=0; i<showElements.length; i++) {
        showElements[i].addEventListener('click', function() {
            refreshInheritanceDisplay(showElements[i].getAttribute('data-type'), true);
        });
    }

    for (let i=0; i<hideElements.length; i++) {
        hideElements[i].addEventListener('click', function() {
            refreshInheritanceDisplay(showElements[i].getAttribute('data-type'), false);
        });
    }

    refreshInheritanceDisplay('attribute', false);
    refreshInheritanceDisplay('concept', false);
}

function setupConceptDiagramCanvas() {
    let canvases = document.querySelectorAll('.concept-diagram-canvas');
    canvases.forEach((canvas) => {
        let svg = canvas.querySelector('svg');
        if (!svg) {
            return;
        }

        let stage = document.createElement('div');
        stage.className = 'concept-diagram-stage';
        canvas.appendChild(stage);
        stage.appendChild(svg);

        let state = {
            scale: 1,
            x: 0,
            y: 0
        };

        let clamp = (value, min, max) => Math.min(Math.max(value, min), max);

        let getSvgSize = () => {
            let width = parseFloat(svg.getAttribute('width'));
            let height = parseFloat(svg.getAttribute('height'));
            if (Number.isNaN(width) || Number.isNaN(height)) {
                if (svg.viewBox && svg.viewBox.baseVal) {
                    width = svg.viewBox.baseVal.width;
                    height = svg.viewBox.baseVal.height;
                }
            }
            return {width, height};
        };

        let applyTransform = () => {
            stage.style.transform = `translate(${state.x}px, ${state.y}px) scale(${state.scale})`;
        };

        let fitToCanvas = () => {
            let rect = canvas.getBoundingClientRect();
            let size = getSvgSize();
            if (!size.width || !size.height || !rect.width || !rect.height) {
                applyTransform();
                return;
            }
            let scale = Math.min(rect.width / size.width, rect.height / size.height, 1);
            state.scale = scale;
            state.x = (rect.width - size.width * scale) / 2;
            state.y = (rect.height - size.height * scale) / 2;
            applyTransform();
        };

        fitToCanvas();

        let isPanning = false;
        let hasMoved = false;
        let startX = 0;
        let startY = 0;
        let originX = 0;
        let originY = 0;

        canvas.addEventListener('mousedown', (event) => {
            if (event.button !== 0) {
                return;
            }
            isPanning = true;
            hasMoved = false;
            startX = event.clientX;
            startY = event.clientY;
            originX = state.x;
            originY = state.y;
            canvas.classList.add('is-panning');
        });

        window.addEventListener('mousemove', (event) => {
            if (!isPanning) {
                return;
            }
            let dx = event.clientX - startX;
            let dy = event.clientY - startY;
            if (Math.abs(dx) > 3 || Math.abs(dy) > 3) {
                hasMoved = true;
            }
            state.x = originX + dx;
            state.y = originY + dy;
            applyTransform();
        });

        window.addEventListener('mouseup', () => {
            if (!isPanning) {
                return;
            }
            isPanning = false;
            canvas.classList.remove('is-panning');
        });

        canvas.addEventListener('click', (event) => {
            if (hasMoved) {
                event.preventDefault();
                event.stopPropagation();
                hasMoved = false;
            }
        });

        canvas.addEventListener('wheel', (event) => {
            event.preventDefault();
            let rect = canvas.getBoundingClientRect();
            let cx = event.clientX - rect.left;
            let cy = event.clientY - rect.top;
            let zoomFactor = event.deltaY > 0 ? 0.9 : 1.1;
            let nextScale = clamp(state.scale * zoomFactor, 0.2, 3);
            if (nextScale === state.scale) {
                return;
            }
            let wx = (cx - state.x) / state.scale;
            let wy = (cy - state.y) / state.scale;
            state.scale = nextScale;
            state.x = cx - wx * state.scale;
            state.y = cy - wy * state.scale;
            applyTransform();
        }, { passive: false });
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
if (window.appconfig.resourceApi) {
Array.from(document.querySelectorAll('a')).concat(Array.from(document.querySelectorAll('em'))).forEach((a) => {
    let popup = null;
    let timeout = null;
    let onElem = false;
    let onPopup = false;

    let clearPopup = () => {
        if (onElem || onPopup) {
            return false;
        }
        if (popup) {
            document.body.removeChild(popup);
        }
        popup = null;
    };

    let soonClearPopup = () => {
        setTimeout(clearPopup, 1000.);
    };

    let showPopup = () => {
        if (!onElem) {
            return false;
        }
        fetch(window.appconfig.resourceApi + '/' + encodeURIComponent(a.innerText)).then(r => r.json()).then(data => {
            if (popup) {
                onElem = true;
                return;
            }
            popup = document.createElement('div');
            h1 = document.createElement('h1');
            p = document.createElement('div');
            table = document.createElement('table');
            h1.appendChild(document.createTextNode(data.resource));
            p.innerHTML = data.definition;
            data.attributes.forEach(a => {
                tr = document.createElement('tr');
                let inv = false;
                a.forEach((c,i) => {
                    if (i === 0 && c === '') {
                        inv = true;
                    } else if (i === 3) {
                        // don't add definition
                        return;
                    }
                    td = document.createElement('td');
                    tr.appendChild(td)
                    if (inv) {
                        ii = document.createElement('i');
                        ii.style.opacity = 0.7;
                        td.appendChild(ii);
                        td = ii;
                    }
                    td.appendChild(document.createTextNode(c));
                });
                table.appendChild(tr)
            });
            popup.className = 'popup';
            popup.appendChild(h1);
            popup.appendChild(p);
            popup.appendChild(table);
            document.body.appendChild(popup);

            popup.onmouseenter = () => {
                onPopup = true;
            }

            popup.onmouseleave = () => {
                onPopup = false;
                soonClearPopup();
            };

            let rect = a.getBoundingClientRect();
            popup.style.left = ((rect.left + rect.right) / 2. - 250 + window.scrollX) + 'px';
            popup.style.top = (rect.bottom + 10. + window.scrollY) + 'px';
        });
    }

    let soonShowPopup = () => {
        timeout = setTimeout(showPopup, 1000.);
    };

    a.onmouseenter = () => {
        onElem = true;
        soonShowPopup();
    };

    a.onmouseleave = () => {
        onElem = false;
        soonClearPopup();
        clearTimeout(timeout);
    };

});
}

setupInheritanceToggle();
setupConceptDiagramCanvas();
if (!document.body.classList.contains('terms-and-definitions') && !document.body.classList.contains('cover')) {
    makeHeadersCollapsible();
}
generateSectionNavigation();
initialiseBackToTopButton();
feather.replace();

});

function getCookie(name) {
    var value = `; ${document.cookie}`;
    var parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function filterActiveLanguage() {
    const languageSlug = (getCookie('languagePreference') || 'english-default').trim().toLowerCase();
    const aside = document.getElementById('translations-aside');
  
    const all = document.querySelectorAll('div.translation');
    all.forEach(el => { el.style.display = 'none'; });
  
    const matches = document.querySelectorAll(`div.translation.lang-${languageSlug}`);
  
    const shouldHideAside = (languageSlug === 'english-default') || matches.length === 0;
  
    if (aside) aside.style.display = shouldHideAside ? 'none' : '';
  
    matches.forEach(el => { el.style.display = 'block'; });
  }


const USE_PAGE_RELOAD_FOR_LANGUAGE = false;

document.addEventListener("DOMContentLoaded", () => {
    const sel  = document.getElementById('language-selector');
    const slug = (getCookie('languagePreference') || 'english-default').trim().toLowerCase();
  
    if (sel) sel.value = slug;   
    if (!USE_PAGE_RELOAD_FOR_LANGUAGE) {
      filterActiveLanguage();    
    }
  });

function setLanguagePreference(value) {

    var date = new Date();
    date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000));  // Cookie expires in 30 days
    var expires = "; expires=" + date.toUTCString();

    document.cookie = `languagePreference=${value}${expires}; path=/;`;
    if (USE_PAGE_RELOAD_FOR_LANGUAGE) {
        window.location.reload();
    } else {
        filterActiveLanguage();
    }
}
