// Epistemic Layer - Navigation with ALN (Absolute Line Numbers)
// ALN: 1-37756

// Parse range from element (looks for .line-range child or data attributes)
function parseRangeFromElement(el) {
    // First check for data attributes
    const rangeStart = el.dataset.rangeStart;
    const rangeEnd = el.dataset.rangeEnd;
    if (rangeStart !== undefined) {
        return { start: parseInt(rangeStart), end: parseInt(rangeEnd) };
    }
    
    // Fall back to parsing .line-range text
    const rangeEl = el.querySelector('.line-range');
    if (rangeEl) {
        const match = rangeEl.textContent.match(/\[(\d+)-(\d+)\]/);
        if (match) {
            return { start: parseInt(match[1]), end: parseInt(match[2]) };
        }
    }
    return null;
}

// Build data attributes for range elements (call on load)
function buildRangeDataAttributes() {
    const entries = document.querySelectorAll('.entry-block');
    entries.forEach(el => {
        const range = parseRangeFromElement(el);
        if (range) {
            el.dataset.rangeStart = range.start;
            el.dataset.rangeEnd = range.end;
        }
    });
}

function showChapter(index) {
    const chapters = document.querySelectorAll('.chapter');
    chapters.forEach((ch, i) => {
        ch.classList.toggle('active', i === index);
    });
    currentChapter = index;
    updateNavButtons();
    updateIndicator();
    window.scrollTo({ top: 0, behavior: 'instant' });
}

function nextChapter() {
    if (currentChapter < totalChapters - 1) {
        showChapter(currentChapter + 1);
        notifyParentOfChapterChange();
    }
}

function prevChapter() {
    if (currentChapter > 0) {
        showChapter(currentChapter - 1);
        notifyParentOfChapterChange();
    }
}

function notifyParentOfChapterChange() {
    const key = chapterKeys[currentChapter];
    const parts = key.split('-');
    const vol = parseInt(parts[0]);
    const chapter = parseInt(parts[1]);
    
    const firstALN = getFirstALNForChapter(vol, chapter);
    window.parent.postMessage({ type: 'chapterChanged', line: firstALN }, '*');
}

function getFirstALNForChapter(volume, chapter) {
    const chapterMap = {
        '01-01': 1, '01-02': 635, '01-03': 1582, '01-04': 1902, '01-05': 4172,
        '01-06': 6801, '01-07': 9704, '01-08': 10472, '01-09': 11335, '01-10': 12500,
        '01-11': 13104, '01-12': 13831, '01-13': 16025, '01-14': 17361,
        '02-15': 20427, '02-16': 20900, '02-17': 22180, '02-18': 24348,
        '02-19': 26389, '02-20': 28509, '02-21': 29839, '02-22': 30637,
        '02-23': 32437, '02-24': 35701, '02-25': 36061
    };
    const key = `${String(volume).padStart(2, '0')}-${String(chapter).padStart(2, '0')}`;
    return chapterMap[key] || 1;
}

function updateNavButtons() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    if (prevBtn) prevBtn.disabled = currentChapter === 0;
    if (nextBtn) nextBtn.disabled = currentChapter === totalChapters - 1;
}

function updateIndicator() {
    const indicator = document.getElementById('chapterIndicator');
    if (!indicator) return;
    
    const key = chapterKeys[currentChapter];
    const parts = key.split('-');
    const volume = parts[0];
    const chapter = parts[1];
    indicator.textContent = `Volume ${parseInt(volume)}, Chapter ${parseInt(chapter)}`;
}

function goToLine(aln) {
    if (!aln) return false;
    
    // First try exact match on line ID
    let lineEl = document.getElementById('line-' + aln);
    
    if (!lineEl) {
        // Find best match - prefer entries where line is within range
        const allChapters = document.querySelectorAll('.chapter');
        let bestMatch = null;
        let bestScore = -Infinity;
        
        allChapters.forEach(ch => {
            const entries = ch.querySelectorAll('.entry-block');
            entries.forEach(el => {
                const range = parseRangeFromElement(el);
                if (range) {
                    let score = -Infinity;
                    if (aln >= range.start && aln <= range.end) {
                        score = 1000 - (range.end - range.start);
                    } else {
                        const dist = Math.min(
                            Math.abs(aln - range.start),
                            Math.abs(aln - range.end)
                        );
                        score = -dist;
                    }
                    
                    if (score > bestScore) {
                        bestScore = score;
                        bestMatch = el;
                    }
                }
            });
        });
        lineEl = bestMatch;
    }
    
    if (lineEl) {
        const chapter = lineEl.closest('.chapter');
        if (chapter) {
            const chapterIndex = parseInt(chapter.dataset.chapter);
            showChapter(chapterIndex);
            setTimeout(() => {
                document.querySelectorAll('.highlighted-line').forEach(el => {
                    el.classList.remove('highlighted-line');
                    el.style.animation = '';
                });
                lineEl.classList.add('highlighted-line');
                void lineEl.offsetWidth;
                lineEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 100);
            return true;
        }
    }
    return false;
}

function handleHashNavigation() {
    const hash = window.location.hash;
    // Format: #line-ALN (e.g., #line-5000)
    const match = hash.match(/line-(\d+)/);
    if (match) {
        const aln = parseInt(match[1]);
        goToLine(aln);
    }
}

let lastReportedRange = null;

function reportCurrentRange() {
    const entries = document.querySelectorAll('.entry-block');
    if (!entries.length) return;
    
    const viewportMiddle = window.innerHeight / 2;
    
    let closest = null;
    let closestDist = Infinity;
    
    for (const entry of entries) {
        const rect = entry.getBoundingClientRect();
        const entryMiddle = (rect.top + rect.bottom) / 2;
        const dist = Math.abs(entryMiddle - viewportMiddle);
        if (dist < closestDist) {
            closestDist = dist;
            closest = entry;
        }
    }
    
    if (closest) {
        const range = parseRangeFromElement(closest);
        if (range) {
            const rangeKey = `${range.start}-${range.end}`;
            
            if (rangeKey !== lastReportedRange) {
                lastReportedRange = rangeKey;
                window.parent.postMessage({ 
                    type: 'rangePosition', 
                    rangeStart: range.start,
                    rangeEnd: range.end
                }, '*');
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    buildRangeDataAttributes();
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    window.addEventListener('scroll', reportCurrentRange);
    setTimeout(reportCurrentRange, 500);
    
    // Listen for navigation from parent (index.html)
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'prevChapter') {
            prevChapter();
        } else if (e.data && e.data.type === 'nextChapter') {
            nextChapter();
        }
    });
});

window.addEventListener('hashchange', handleHashNavigation);

// Dark mode handling - sync with parent
(function() {
    const isDark = localStorage.getItem('darkMode') !== 'false';
    if (!isDark) document.body.classList.add('light-mode');
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'darkModeChange') {
            document.body.classList.toggle('light-mode', !e.data.enabled);
            localStorage.setItem('darkMode', e.data.enabled);
        }
    });
})();
