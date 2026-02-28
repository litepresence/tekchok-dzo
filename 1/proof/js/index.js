// ==========================================================================
// UNIFIED STATE MANAGEMENT - ALN (Absolute Line Numbers)
// ==========================================================================
// All line numbers are ALN (Absolute Line Numbers 1-37756)
// Volume is derived from ALN: line <= 20426 ? 1 : 2

// ALN is now loaded from ../js/aln_data.js (embedded, file:// compatible)

// Initialize chapter dropdown on load
document.addEventListener('DOMContentLoaded', function() {
    populateChapterDropdown();
    // If there's a saved line in state, update the chapter dropdown
    if (state.line) {
        updateChapterDropdown();
    }
});

// Chapter names mapping
const chapterNames = {
    '01-01': '1. The Perfect Teacher',
    '01-02': '2. Container and Contents',
    '01-03': '3. Aggregates and Elements',
    '01-04': '4. Vehicle Enumeration',
    '01-05': '5. Empowerment and Samaya',
    '01-06': '6. Samaya Discipline',
    '01-07': '7. Samaya Restoration',
    '01-08': '8. Ground, Path, Fruit',
    '01-09': '9. Delusion and Liberation',
    '01-10': '10. Arising of Elements',
    '01-11': '11. Body Formation',
    '01-12': '12. Bindu, Channels, Winds',
    '01-13': '13. Luminosity',
    '01-14': '14. Mind and Awareness',
    '02-15': '15. Elements Place',
    '02-16': '16. Kaya and Wisdom',
    '02-17': '17. Path and Signs',
    '02-18': '18. Luminosity Path',
    '02-19': '19. Cutting Through',
    '02-20': '20. Leap-Over',
    '02-21': '21. Introduction',
    '02-22': '22. Signs of Liberation',
    '02-23': '23. Intermediate State',
    '02-24': '24. Emanation Field',
    '02-25': '25. Fruition'
};

// Populate chapter dropdown from ALN.chapterMap
function populateChapterDropdown() {
    const dropdown = document.getElementById('chapter-select');
    if (!dropdown) return;
    
    // Wait for ALN to be ready
    if (!ALN || !ALN.chapterMap) {
        setTimeout(populateChapterDropdown, 200);
        return;
    }
    
    dropdown.innerHTML = '<option value="">Select Chapter...</option>';
    
    // Sort chapter map keys
    const sortedKeys = Object.keys(ALN.chapterMap).sort();
    
    for (const key of sortedKeys) {
        const info = ALN.chapterMap[key];
        const volChap = `${String(info.volume).padStart(2, '0')}-${String(info.chapter).padStart(2, '0')}`;
        const startLine = info.startLine;
        const chapterName = chapterNames[volChap] || `Chapter ${info.chapter}`;
        
        const option = document.createElement('option');
        option.value = startLine;
        option.textContent = chapterName;
        dropdown.appendChild(option);
    }
}

// Handle chapter selection
function handleChapterSelect(value) {
    if (!value) return;
    const targetLayer = state.selectedLayer || state.layer || 'liturgical';
    const startLine = parseInt(value);
    if (!isNaN(startLine)) {
        window.location.hash = buildHash(targetLayer, startLine);
    }
}

// Handle prev button click
function handlePrev() {
    if (!state.layer) return;
    
    // Handle conventions tab - cycle through layers
    if (state.layer === 'conventions') {
        const conventionsLayers = ['tibetan', 'wylie', 'literal', 'liturgical', 'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive'];
        const iframe = document.querySelector('#conventions-frame');
        const currentParams = new URLSearchParams(iframe.src.split('?')[1] || '');
        const currentLayer = currentParams.get('layer') || 'liturgical';
        const currentIndex = conventionsLayers.indexOf(currentLayer);
        const prevIndex = (currentIndex - 1 + conventionsLayers.length) % conventionsLayers.length;
        const newLayer = conventionsLayers[prevIndex];
        
        iframe.src = iframe.dataset.src + '?layer=' + newLayer;
        sendDarkModeStatus();
        
        // Update layer dropdown
        document.getElementById('layer-select').value = '#' + newLayer;
        return;
    }
    
    // Handle contents tab - scroll to previous chapter
    if (state.layer === 'contents') {
        const iframe = document.querySelector('#contents-frame');
        if (iframe && iframe.contentWindow) {
            iframe.contentWindow.postMessage({ type: 'prevChapter' }, '*');
        }
        return;
    }
    
    // Handle glossary tab - cycle through letters
    if (state.layer === 'glossary') {
        const iframe = document.querySelector('#glossary-frame');
        if (iframe && iframe.contentWindow) {
            iframe.contentWindow.postMessage({ type: 'prevLetter' }, '*');
        }
        return;
    }
    
    const iframe = document.querySelector(`#${state.layer} .layer-frame`);
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage({ type: 'prevChapter' }, '*');
    }
}

// Handle next button click
function handleNext() {
    if (!state.layer) return;
    
    // Handle conventions tab - cycle through layers
    if (state.layer === 'conventions') {
        const conventionsLayers = ['tibetan', 'wylie', 'literal', 'liturgical', 'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive'];
        const iframe = document.querySelector('#conventions-frame');
        const currentParams = new URLSearchParams(iframe.src.split('?')[1] || '');
        const currentLayer = currentParams.get('layer') || 'liturgical';
        const currentIndex = conventionsLayers.indexOf(currentLayer);
        const nextIndex = (currentIndex + 1) % conventionsLayers.length;
        const newLayer = conventionsLayers[nextIndex];
        
        iframe.src = iframe.dataset.src + '?layer=' + newLayer;
        sendDarkModeStatus();
        
        // Update layer dropdown
        document.getElementById('layer-select').value = '#' + newLayer;
        return;
    }
    
    // Handle contents tab - scroll to next chapter
    if (state.layer === 'contents') {
        const iframe = document.querySelector('#contents-frame');
        if (iframe && iframe.contentWindow) {
            iframe.contentWindow.postMessage({ type: 'nextChapter' }, '*');
        }
        return;
    }
    
    // Handle glossary tab - cycle through letters
    if (state.layer === 'glossary') {
        const iframe = document.querySelector('#glossary-frame');
        if (iframe && iframe.contentWindow) {
            iframe.contentWindow.postMessage({ type: 'nextLetter' }, '*');
        }
        return;
    }
    
    const iframe = document.querySelector(`#${state.layer} .layer-frame`);
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage({ type: 'nextChapter' }, '*');
    }
}

// Update chapter dropdown based on current line
function updateChapterDropdown() {
    const dropdown = document.getElementById('chapter-select');
    if (!dropdown || !ALN || !state.line) return;
    
    // Find current chapter from line number
    const info = ALN.getInfo(state.line);
    if (!info) return;
    
    const volChap = `${String(info.volume).padStart(2, '0')}-${String(info.chapter).padStart(2, '0')}`;
    const startLine = ALN.getStartLineForChapter(info.volume, info.chapter);
    
    // Find and select the option with this startLine
    const options = dropdown.querySelectorAll('option');
    for (const option of options) {
        if (parseInt(option.value) === startLine) {
            dropdown.value = option.value;
            return;
        }
    }
}

// Go to text - switch from glossary/contents/conventions to current text layer
function goToText() {
    if (!state.selectedLayer) {
        state.selectedLayer = 'liturgical';
    }
    
    // Get the line to navigate to (default to chapter start if no current line)
    let targetLine = state.line;
    if (!targetLine) {
        // Default to start of chapter 1
        targetLine = 1;
    }
    
    // Navigate to the selected layer at the current line
    window.location.hash = buildHash(state.selectedLayer, targetLine);
}


// Unified state object - stored in sessionStorage for persistence
const state = {
    layer: null,           // Current active layer
    volume: 1,            // Current volume (1 or 2)
    line: null,           // Current absolute line number
    chapter: null,        // Current chapter number
    selectedLayer: null   // Last selected translation/analysis layer
};

// Load state from sessionStorage
function loadState() {
    try {
        const saved = sessionStorage.getItem('dzoState');
        if (saved) {
            const parsed = JSON.parse(saved);
            state.volume = parsed.volume || 1;
            state.line = parsed.line || null;
            state.chapter = parsed.chapter || null;
            state.selectedLayer = parsed.selectedLayer || localStorage.getItem('selectedLayer') || 'liturgical';
        } else {
            state.selectedLayer = localStorage.getItem('selectedLayer') || 'liturgical';
        }
    } catch (e) {
        state.selectedLayer = localStorage.getItem('selectedLayer') || 'liturgical';
    }
}

// Save state to sessionStorage
function saveState() {
    try {
        sessionStorage.setItem('dzoState', JSON.stringify({
            volume: state.volume,
            line: state.line,
            chapter: state.chapter,
            selectedLayer: state.selectedLayer
        }));
    } catch (e) {}
}

// Update line - ALN is already absolute
function setLine(absLine) {
    if (absLine && !isNaN(parseInt(absLine))) {
        state.line = parseInt(absLine);
        // Derive volume from ALN
        if (ALN) {
            const info = ALN.getInfo(state.line);
            state.volume = info ? info.volume : (state.line <= 20426 ? 1 : 2);
            state.chapter = info ? info.chapter : null;
        } else {
            state.volume = state.line <= 20426 ? 1 : 2;
        }
        saveState();
        updateChapterDropdown();
        updateHeaderIndicator();
    }
}

// Update header indicator with current volume and chapter
function updateHeaderIndicator() {
    const indicator = document.querySelector('.layer-content.active .header-indicator');
    if (!indicator || !state.volume || !state.chapter) {
        return;
    }


    if (state.layer === 'conventions')  {
        const iframe = document.querySelector('#conventions-frame');
        const currentParams = new URLSearchParams(iframe.src.split('?')[1] || '');
        const currentLayer = currentParams.get('layer') || 'liturgical';
        indicator.textContent = currentLayer.toUpperCase();
    } else {
        indicator.textContent = 'VOLUME ' + state.volume + ' - CHAPTER ' + state.chapter;
    }
}

// Set volume (derived from ALN, but can be set explicitly for backward compat)
function setVolume(vol) {
    if (vol === 1 || vol === 2) {
        // When setting volume, adjust line to be in that volume's range
        // This is for backward compatibility - prefer using ALN directly
        if (state.line) {
            if (vol === 1 && state.line > 20426) {
                // Moving to volume 1 - not really valid, just derive
                state.volume = 1;
            } else if (vol === 2 && state.line <= 20426) {
                // Moving to volume 2 - find first line of volume 2
                state.line = 20427;
                state.volume = 2;
            } else {
                state.volume = vol;
            }
            if (ALN) {
                const info = ALN.getInfo(state.line);
                state.chapter = info ? info.chapter : null;
            }
        } else {
            state.volume = vol;
        }
        saveState();
    }
}

// Set layer
function setLayer(layerId) {
    state.layer = layerId;
    if (layerId && layerId !== 'contents' && layerId !== 'glossary' && 
        layerId !== 'conventions' && layerId !== 'introduction') {
        state.selectedLayer = layerId;
        localStorage.setItem('selectedLayer', layerId);
    }
    saveState();
}

// Build hash from current state - ALN format: #layer:LINE
function buildHash(layer, line) {
    if (line && !isNaN(line)) {
        return `#${layer}:${line}`;
    }
    return `#${layer}`;
}

// Initialize state
loadState();

// ==========================================================================
// LAYER CONFIGURATION
// ==========================================================================

const layers = {
    'introduction': { type: 'nav', hasLineRange: false },     // Chapter-based navigation
    'contents': { type: 'nav', hasLineRange: false },         // Table of contents
    'conventions': { type: 'info', hasLineRange: false },    // Static info page
    'glossary': { type: 'nav', hasLineRange: false },        // Glossary
    // Translation layers - exact line matching
    'tibetan': { type: 'translation', hasLineRange: false },
    'wylie': { type: 'translation', hasLineRange: false },
    'literal': { type: 'translation', hasLineRange: false },
    'liturgical': { type: 'translation', hasLineRange: false },
    // Analysis layers - range-based matching
    'commentary': { type: 'analysis', hasLineRange: true },
    'scholar': { type: 'analysis', hasLineRange: true },
    'epistemic': { type: 'analysis', hasLineRange: true },
    'delusion': { type: 'analysis', hasLineRange: true },
    'cognitive': { type: 'analysis', hasLineRange: true }
};

// Translation/analysis layers that support line navigation
const lineLayers = ['tibetan', 'wylie', 'literal', 'liturgical', 
                    'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive'];

// Nav layers that should preserve line when leaving
const navLayers = ['contents', 'glossary', 'conventions', 'introduction'];

// Helper to get chapter from ALN (uses ALN module)
function getChapterFromALN(lineNum) {
    if (ALN) {
        return ALN.getChapterFromALN(lineNum);
    }
    // Fallback without ALN
    return lineNum <= 20426 ? Math.ceil(lineNum / 1500) : 14 + Math.ceil((lineNum - 20426) / 1500);
}

// ==========================================================================
// DOM ELEMENTS
// ==========================================================================

const welcomeScreen = document.getElementById('welcome');
const lineIndicator = document.getElementById('line-indicator');
const navTabs = document.querySelectorAll('.nav-tab');
const consentModal = document.getElementById('consent-modal');
const consentImage1 = document.getElementById('consent-image-1');
const consentImage2 = document.getElementById('consent-image-2');

document.querySelectorAll('.layer-frame').forEach(iframe => { iframe.src = 'about:blank'; });

// ==========================================================================
// CONSENT HANDLING
// ==========================================================================

if (localStorage.getItem('consentAccepted') === 'true' &&
    localStorage.getItem('imageConsent1Accepted') === 'true' &&
    localStorage.getItem('imageConsent2Accepted') === 'true') {
    consentModal.classList.add('hidden');
    consentImage1.classList.add('hidden');
    consentImage2.classList.add('hidden');
} else if (localStorage.getItem('consentAccepted') === 'true' &&
           localStorage.getItem('imageConsent1Accepted') === 'true') {
    consentModal.classList.add('hidden');
    consentImage1.classList.add('hidden');
    consentImage2.classList.remove('hidden');
} else if (localStorage.getItem('consentAccepted') === 'true') {
    consentModal.classList.add('hidden');
    consentImage1.classList.remove('hidden');
}

function acceptConsent() {
    localStorage.setItem('consentAccepted', 'true');
    consentModal.classList.add('hidden');
    consentImage1.classList.remove('hidden');
}

function acceptImageConsent1() {
    localStorage.setItem('imageConsent1Accepted', 'true');
    consentImage1.classList.add('hidden');
    consentImage2.classList.remove('hidden');
}

function acceptImageConsent2() {
    localStorage.setItem('imageConsent2Accepted', 'true');
    consentImage2.classList.add('hidden');
}

// ==========================================================================
// LAYER SELECTION (Dropdown)
// ==========================================================================

function handleLayerSelect(value) {
    if (!value) return;
    const targetLayer = value.slice(1);
    
    // Handle conventions specially - it loads different content based on layer param
    if (state.layer === 'conventions') {
        const iframe = document.querySelector('#conventions-frame');
        if (iframe) {
            let effectiveLayer = targetLayer;
            if (effectiveLayer === 'introduction') effectiveLayer = 'liturgical';
            iframe.src = iframe.dataset.src + '?layer=' + effectiveLayer;
            sendDarkModeStatus();
        }
        // Don't call setLayer() - keep state.layer as 'conventions' for subsequent changes
        return;
    }
    
    // If we have a current line and target is a line layer, navigate with line preserved
    if (state.line && lineLayers.includes(targetLayer)) {
        window.location.hash = buildHash(targetLayer, state.line);
    } else {
        window.location.hash = '#' + targetLayer;
    }
}

function updateLayerDropdown(layerId) {
    const dropdown = document.getElementById('layer-select');
    if (!dropdown) return;
    
    const allLayers = ['introduction', 'tibetan', 'wylie', 'literal', 'liturgical', 
                      'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive'];
    if (allLayers.includes(layerId)) {
        dropdown.value = '#' + layerId;
    } else {
        const lastLayer = state.selectedLayer || localStorage.getItem('selectedLayer');
        if (lastLayer && allLayers.includes(lastLayer)) {
            dropdown.value = '#' + lastLayer;
        } else {
            dropdown.value = '#liturgical';
        }
    }
}

// ==========================================================================
// HASH PARSING & NAVIGATION
// ==========================================================================

// Hash format: #layer:ALN
// Examples:
//   #tibetan:5000    -> tibetan layer, ALN 5000
//   #liturgical:20500 -> liturgical layer, ALN 20500
//   #contents        -> contents page (no line)
//   #tibetan         -> tibetan layer (no line specified)

function parseHash(hash) {
    const result = { layer: null, line: null };
    
    if (!hash) return result;
    
    // Remove leading #
    const str = hash.replace(/^#/, '');
    const parts = str.split(':');
    
    result.layer = parts[0] || null;
    
    // New format: #layer:ALN
    if (parts.length >= 2 && parts[1]) {
        result.line = parseInt(parts[1]);
    }
    
    return result;
}

function handleNavigation() {
    const hashData = parseHash(window.location.hash);
    
    if (!hashData.layer) {
        showWelcome();
        return;
    }
    
    if (!layers[hashData.layer]) {
        showWelcome();
        return;
    }
    
    // Always use URL line when it exists in the hash
    let lineToUse = null;
    
    if (hashData.line) {
        setLine(hashData.line);
        lineToUse = hashData.line;
    }
    
    showLayer(hashData.layer, lineToUse);
}

function showWelcome() {
    welcomeScreen.style.display = 'flex';
    document.querySelectorAll('.layer-content').forEach(el => el.classList.remove('active'));
    
    navTabs.forEach(tab => {
        const href = tab.getAttribute('href');
        if (!href) return; // Skip buttons without href
        if (href === '#' + state.selectedLayer) {
            tab.classList.add('active');
        } else if (href !== '#contents' && href !== '#introduction') {
            tab.classList.remove('active');
        }
    });
    
    updateLayerDropdown(state.selectedLayer);
    state.layer = null;
    hideLineIndicator();
}

function showLayer(layerId, targetLine) {
    welcomeScreen.style.display = 'none';
    
    // Update state - ALN is already absolute
    if (targetLine) setLine(targetLine);
    setLayer(layerId);
    
    // Update nav tabs
    navTabs.forEach(tab => {
        const href = tab.getAttribute('href');
        if (!href) return; // Skip buttons without href
        const tabLayer = href.slice(1);
        
        if (navLayers.includes(layerId)) {
            // On nav layer - highlight selected translation layer
            if (href === '#' + state.selectedLayer) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        } else {
            // On line layer - highlight current layer
            tab.classList.toggle('active', tabLayer === layerId);
        }
    });

    document.querySelectorAll('.layer-content').forEach(el => {
        el.classList.toggle('active', el.id === layerId);
    });

    const iframe = document.querySelector(`#${layerId} .layer-frame`);
    const lineToUse = targetLine || state.line;

    if (iframe) {
        const needsLoad = iframe.src === 'about:blank' || !iframe.src || iframe.src === 'about:blank';
        let src = iframe.dataset.src;
        
        if (layerId === 'conventions') {
            let dropdownLayer = document.getElementById('layer-select').value.replace('#', '');
            if (dropdownLayer === 'introduction') dropdownLayer = 'liturgical';
            src += '?layer=' + dropdownLayer;
            if (!needsLoad) {
                iframe.src = src;
                sendDarkModeStatus();
                updateLayerDropdown(layerId);
                return;
            }
        } else if (layerId === 'introduction') {
            // Use ALN to get chapter ID
            const aln = lineToUse || 1;
            let chapterId = '01-01';
            if (ALN) {
                const info = ALN.getInfo(aln);
                if (info) {
                    chapterId = `${String(info.volume).padStart(2, '0')}-${String(info.chapter).padStart(2, '0')}`;
                }
            }
            src += '#chapter-' + chapterId;
            if (!needsLoad) {
                iframe.contentWindow.location.hash = '#chapter-' + chapterId;
            }
        } else if (lineLayers.includes(layerId) && lineToUse && !isNaN(lineToUse)) {
            // Pass ALN directly to iframe - layers now use ALN
            src += `#line-${lineToUse}`;
        }
        
        // Always update src when line changes, not just on initial load
        if (needsLoad) {
            iframe.src = src;
            sendDarkModeStatus();
        } else if (lineLayers.includes(layerId) && lineToUse && !isNaN(lineToUse)) {
            // Iframe already loaded - always update its hash to navigate to correct position
            try {
                iframe.contentWindow.location.hash = `#line-${lineToUse}`;
            } catch(e) {
                // Cross-origin or other error - reload instead
                iframe.src = src;
                sendDarkModeStatus();
            }
        }
    }

    updateLayerDropdown(layerId);
    updateChapterDropdown();
    updateHeaderIndicator();
    
    // // Hide chapter dropdown and nav buttons when on conventions (they don't apply)
    // const chapterSelect = document.getElementById('chapter-select');
    // const navBtns = document.querySelectorAll('.toolbar-nav-btn');
    // if (layerId === 'conventions') {
    //     if (chapterSelect) chapterSelect.style.display = 'none';
    //     navBtns.forEach(btn => btn.style.display = 'none');
    // } else if (layerId) {
    //     if (chapterSelect) chapterSelect.style.display = '';
    //     navBtns.forEach(btn => btn.style.display = '');
    // }
}

// ==========================================================================
// GET LINE FROM IFRAME (for preserving position when switching)
// ==========================================================================

function getCurrentLineFromIframe(layerId) {
    const iframe = document.querySelector(`#${layerId} .layer-frame`);
    if (!iframe || !iframe.contentDocument) {
        return null;
    }
    try {
        const doc = iframe.contentDocument;
        
        // Try to find line element at top of viewport
        const topElement = doc.elementFromPoint(50, 100);
        if (topElement) {
            let el = topElement;
            while (el && el !== doc.body) {
                if (el.id && el.id.startsWith('line-')) {
                    const lineNum = el.id.replace('line-', '');
                    // For range-based layers, we need range data
                    if (layers[layerId] && layers[layerId].hasLineRange) {
                        const rangeStart = el.dataset.rangeStart;
                        const rangeEnd = el.dataset.rangeEnd;
                        if (rangeStart) {
                            return { 
                                line: parseInt(rangeStart), 
                                isRange: true,
                                rangeStart: parseInt(rangeStart),
                                rangeEnd: parseInt(rangeEnd)
                            };
                        }
                    }
                    return { line: parseInt(lineNum), isRange: false };
                }
                el = el.parentElement;
            }
        }
        
        // Fallback: find any line element near top of viewport
        const lines = doc.querySelectorAll('[id^="line-"]');
        const iframeRect = iframe.getBoundingClientRect();
        for (const line of lines) {
            const lineRect = line.getBoundingClientRect();
            if (lineRect.top >= iframeRect.top && lineRect.top <= iframeRect.top + 200) {
                if (layers[layerId] && layers[layerId].hasLineRange) {
                    const rangeStart = line.dataset.rangeStart;
                    const rangeEnd = line.dataset.rangeEnd;
                    if (rangeStart) {
                        return { 
                            line: parseInt(rangeStart), 
                            isRange: true,
                            rangeStart: parseInt(rangeStart),
                            rangeEnd: parseInt(rangeEnd)
                        };
                    }
                }
                return { line: parseInt(line.id.replace('line-', '')), isRange: false };
            }
        }
        return null;
    } catch (e) {
        console.log('Error getting line from iframe:', e);
        return null;
    }
}

// ==========================================================================
// TAB CLICK HANDLERS
// ==========================================================================

document.querySelectorAll('.nav-tab').forEach(tab => {
    tab.addEventListener('click', function(e) {
        const targetLayer = this.getAttribute('href').slice(1);
        
        // Already on target layer
        if (state.layer === targetLayer) return;
        
        // Going TO a nav layer (contents/glossary/conventions/introduction)
        if (navLayers.includes(targetLayer)) {
            // If coming from a line layer, state.line is already being updated via postMessage
            // Let normal navigation proceed - it will handle the hash change
            return;
        }
        
        // Going TO a line layer
        if (lineLayers.includes(targetLayer)) {
            e.preventDefault();
            
            // ALWAYS use state.line which is being continuously updated via postMessage from scroll
            // Don't try to get from iframe at click time - it's unreliable
            if (state.line) {
                window.location.hash = buildHash(targetLayer, state.line);
            } else {
                window.location.hash = '#' + targetLayer;
            }
        }
    });
});

// ==========================================================================
// MESSAGE HANDLING (from iframes)
// ==========================================================================

let scrollSyncDebounce = null;

window.addEventListener('message', function(e) {
    if (!e.data || !e.data.type) return;
    
    // Handle navigateToLine (from contents page) - ALN only
    if (e.data.type === 'navigateToLine') {
        const lineNum = parseInt(e.data.line);
        if (!isNaN(lineNum)) {
            setLine(lineNum);
            const targetLayer = state.selectedLayer || 'liturgical';
            window.location.hash = buildHash(targetLayer, state.line);
        }
        return;
    }
    
    // Handle linePosition updates (from translation/analysis layers) - ALN only
    if (e.data.type === 'linePosition') {
        const lineNum = parseInt(e.data.line);
        if (!isNaN(lineNum)) {
            // Debounce scroll updates to avoid excessive processing
            clearTimeout(scrollSyncDebounce);
            scrollSyncDebounce = setTimeout(() => {
                setLine(lineNum);
            }, 100);
        }
        return;
    }
    
    // Handle rangePosition (from analysis layers) - ALN only
    if (e.data.type === 'rangePosition') {
        const rangeStart = parseInt(e.data.rangeStart);
        if (!isNaN(rangeStart)) {
            clearTimeout(scrollSyncDebounce);
            scrollSyncDebounce = setTimeout(() => {
                setLine(rangeStart);
            }, 100);
        }
        return;
    }
    
    // Handle chapterPosition (from introduction) - ALN only
    if (e.data.type === 'chapterPosition') {
        const lineNum = parseInt(e.data.line);
        if (!isNaN(lineNum)) {
            setLine(lineNum);
        }
        return;
    }
    
    // Handle chapterChanged (from prev/next buttons in iframes) - ALN only
    if (e.data.type === 'chapterChanged') {
        const lineNum = parseInt(e.data.line);
        if (lineNum) {
            setLine(lineNum);
            // Update URL to reflect new chapter position
            if (state.layer && lineLayers.includes(state.layer)) {
                window.location.hash = buildHash(state.layer, state.line);
            }
        }
        return;
    }
});

// ==========================================================================
// LINE INDICATOR
// ==========================================================================

function showLineIndicator(layer, line, type) {
    const names = {
        introduction: 'Introduction',
        tibetan: 'Tibetan',
        glossary: 'Glossary',
        wylie: 'Wylie',
        literal: 'Literal',
        liturgical: 'Liturgical',
        commentary: 'Commentary',
        scholar: 'Scholar',
        epistemic: 'Epistemic',
        delusion: 'Delusion',
        cognitive: 'Cognitive',
        contents: 'Contents'
    };
    const volumeText = state.volume ? ` (Vol ${state.volume})` : '';
    lineIndicator.textContent = `${names[layer] || layer}: Line ${line}${type === 'range' ? ' (range)' : ''}${volumeText}`;
    lineIndicator.classList.add('visible');
    setTimeout(() => lineIndicator.classList.remove('visible'), 3000);
}

function hideLineIndicator() { 
    lineIndicator.classList.remove('visible'); 
}

// ==========================================================================
// HASH CHANGE & INITIALIZATION
// ==========================================================================

window.addEventListener('hashchange', handleNavigation);

document.querySelectorAll('.layer-frame').forEach(iframe => {
    iframe.addEventListener('load', function() {
        if (!state.layer) return;
        try {
            const doc = this.contentDocument;
            // Ensure line IDs exist for tibetan/wylie
            if (state.layer === 'tibetan' || state.layer === 'wylie') {
                doc.querySelectorAll('[class*="line-num"]').forEach(el => {
                    const t = el.textContent.trim();
                    if (t && /^\d+$/.test(t)) el.id = 'line-' + t;
                });
            }
            if (state.line && lineLayers.includes(state.layer)) {
                const type = layers[state.layer].hasLineRange ? 'range' : 'exact';
                showLineIndicator(state.layer, state.line, type);
            }
        } catch (e) {}
    });
});

// ==========================================================================
// DARK MODE
// ==========================================================================

function sendDarkModeStatus() {
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    
    document.querySelectorAll('.layer-frame').forEach(iframe => {
        try {
            iframe.contentWindow.postMessage({
                type: 'darkModeChange',
                enabled: document.body.classList.contains('dark-mode')
            }, '*');
        } catch (e) {}
    });
}


function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const btn = document.querySelector('.dark-mode-toggle');
    btn.textContent = document.body.classList.contains('dark-mode') ? 'Light' : 'Dark';
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    
    document.querySelectorAll('.layer-frame').forEach(iframe => {
        try {
            iframe.contentWindow.postMessage({
                type: 'darkModeChange',
                enabled: document.body.classList.contains('dark-mode')
            }, '*');
        } catch (e) {}
    });
}

if (localStorage.getItem('darkMode') === 'false') {
    document.body.classList.remove('dark-mode');
    document.querySelector('.dark-mode-toggle').textContent = 'Dark';
} else {
    document.body.classList.add('dark-mode');
    document.querySelector('.dark-mode-toggle').textContent = 'Light';
}

// Initialize
handleNavigation();
