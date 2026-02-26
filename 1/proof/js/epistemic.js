// Epistemic Layer - Navigation with line range matching
// Volume 1: lines 1-20426 (relative = absolute)
// Volume 2: lines 1-17330 (relative), displayed as 20427-37756 (absolute)

const VOLUME_BOUNDARY = 20426;

function getVolumeFromLine(absLine) {
    if (!absLine || absLine <= 0) return 1;
    return absLine <= VOLUME_BOUNDARY ? 1 : 2;
}

function toAbsoluteLine(relLine, volume) {
    if (!relLine || relLine <= 0) return 1;
    if (volume === 2) {
        return relLine + VOLUME_BOUNDARY;
    }
    return relLine;
}

function parseRangeFromElement(el) {
    const rangeStart = el.dataset.rangeStart;
    const rangeEnd = el.dataset.rangeEnd;
    if (rangeStart !== undefined) {
        return { start: parseInt(rangeStart), end: parseInt(rangeEnd) };
    }
    
    const rangeEl = el.querySelector('.line-range');
    if (rangeEl) {
        const match = rangeEl.textContent.match(/\[(\d+)-(\d+)\]/);
        if (match) {
            return { start: parseInt(match[1]), end: parseInt(match[2]) };
        }
    }
    return null;
}

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
    const chapterMap = {
        '01': 1, '02': 635, '03': 1582, '04': 1902, '05': 4172,
        '06': 6801, '07': 9704, '08': 10472, '09': 11335, '10': 12500,
        '11': 13104, '12': 13831, '13': 16025, '14': 17361,
        '15': 20427, '16': 20900, '17': 22654, '18': 24822,
        '19': 26863, '20': 27946, '21': 28946, '22': 29856,
        '23': 31566, '24': 34830, '25': 35191
    };
    const lineNum = chapterMap[parts[1]] || 1;
    window.parent.postMessage({ type: 'chapterChanged', volume: vol, chapter: parseInt(parts[1]), line: lineNum }, '*');
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

function goToLine(lineNum, volume) {
    if (!lineNum) return false;
    
    volume = volume || 1;
    const volPrefix = volume === 1 ? '01-' : '02-';
    
    const relLine = volume === 2 ? lineNum - VOLUME_BOUNDARY : lineNum;
    let lineEl = document.getElementById('line-' + relLine);
    
    if (!lineEl) {
        const volChapters = document.querySelectorAll(`.chapter[data-chapter-key^="${volPrefix}"]`);
        let bestMatch = null;
        let bestScore = -Infinity;
        
        volChapters.forEach(ch => {
            const entries = ch.querySelectorAll('.entry-block');
            entries.forEach(el => {
                const range = parseRangeFromElement(el);
                if (range) {
                    let score = -Infinity;
                    if (relLine >= range.start && relLine <= range.end) {
                        score = 1000 - (range.end - range.start);
                    } else {
                        const dist = Math.min(
                            Math.abs(relLine - range.start),
                            Math.abs(relLine - range.end)
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
    const match = hash.match(/line-(\d+)(?:-(\d+))?/);
    if (match) {
        let relLine, volume;
        if (match[2]) {
            volume = parseInt(match[1]);
            relLine = parseInt(match[2]);
        } else {
            relLine = parseInt(match[1]);
            volume = 1;
        }
        const absLine = toAbsoluteLine(relLine, volume);
        goToLine(absLine, volume);
    }
}

let lastReportedRange = null;
let lastReportedVolume = null;

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
            const chapter = closest.closest('[data-chapter-key]');
            const chapterKey = chapter ? chapter.dataset.chapterKey : '01-01';
            const volume = chapterKey.startsWith('02-') ? 2 : 1;
            
            const absRangeStart = toAbsoluteLine(range.start, volume);
            const absRangeEnd = toAbsoluteLine(range.end, volume);
            const rangeKey = `${absRangeStart}-${absRangeEnd}`;
            
            if (rangeKey !== lastReportedRange || volume !== lastReportedVolume) {
                lastReportedRange = rangeKey;
                lastReportedVolume = volume;
                window.parent.postMessage({ 
                    type: 'rangePosition', 
                    rangeStart: absRangeStart,
                    rangeEnd: absRangeEnd,
                    volume: volume 
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
