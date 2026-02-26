// Navigation and chapter management
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
    }
}

function prevChapter() {
    if (currentChapter > 0) {
        showChapter(currentChapter - 1);
    }
}

function updateNavButtons() {
    document.getElementById('prevBtn').disabled = currentChapter === 0;
    document.getElementById('nextBtn').disabled = currentChapter === totalChapters - 1;
}

function updateIndicator() {
    const key = chapterKeys[currentChapter];
    const parts = key.split('-');
    const volume = parts[0];
    const chapter = parts[1];
    document.getElementById('chapterIndicator').textContent = 
        `Volume ${volume}, Chapter ${chapter}`;
}

function goToLine(lineNum, volume) {
    volume = volume || 1;
    const volPrefix = volume === 1 ? '01-' : '02-';
    
    let lineEl = document.getElementById('line-' + lineNum);
    
    if (!lineEl) {
        const volChapters = document.querySelectorAll(`.chapter[data-chapter-key^="${volPrefix}"]`);
        let bestMatch = null;
        let bestDiff = Infinity;
        
        volChapters.forEach(ch => {
            const lines = ch.querySelectorAll('[id^="line-"]');
            for (const el of lines) {
                const elLine = parseInt(el.id.replace('line-', ''));
                const diff = Math.abs(elLine - lineNum);
                if (diff < bestDiff) {
                    bestDiff = diff;
                    bestMatch = el;
                }
            }
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
        let lineNum, volume;
        if (match[2]) {
            volume = parseInt(match[1]);
            lineNum = parseInt(match[2]);
        } else {
            lineNum = parseInt(match[1]);
            volume = 1;
        }
        goToLine(lineNum, volume);
    }
}

// Report visible line to parent on scroll
let lastReportedLine = null;
function reportCurrentLine() {
    const lines = document.querySelectorAll('[id^="line-"]');
    if (!lines.length) return;
    
    const viewportMiddle = window.innerHeight / 2;
    
    let closest = null;
    let closestDist = Infinity;
    
    for (const line of lines) {
        const rect = line.getBoundingClientRect();
        const lineMiddle = (rect.top + rect.bottom) / 2;
        const dist = Math.abs(lineMiddle - viewportMiddle);
        if (dist < closestDist) {
            closestDist = dist;
            closest = line;
        }
    }
    
    if (closest) {
        const lineNum = closest.id.replace('line-', '');
        if (lineNum !== lastReportedLine) {
            lastReportedLine = lineNum;
            const chapter = closest.closest('[data-chapter-key]');
            const chapterKey = chapter ? chapter.dataset.chapterKey : '01-01';
            const volume = chapterKey.startsWith('02-') ? 2 : 1;
            window.parent.postMessage({ type: 'linePosition', line: lineNum, volume: volume }, '*');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    window.addEventListener('scroll', reportCurrentLine);
    setTimeout(reportCurrentLine, 500);
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
