// Tibetan Layer - Navigation with ALN (Absolute Line Numbers)
// ALN: 1-37756

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
    
    // Get first ALN for this chapter from chapter key
    const firstALN = getFirstALNForChapter(vol, chapter);
    
    window.parent.postMessage({ type: 'chapterChanged', line: firstALN }, '*');
}

function getFirstALNForChapter(volume, chapter) {
    // Map chapter keys to first ALN
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
    
    // Try exact match first (line IDs are ALN)
    let lineEl = document.getElementById('line-' + aln);
    
    if (!lineEl) {
        // Find best match
        const allChapters = document.querySelectorAll('.chapter');
        let bestMatch = null;
        let bestDiff = Infinity;
        
        allChapters.forEach(ch => {
            const lines = ch.querySelectorAll('[id^="line-"]');
            for (const el of lines) {
                const elLine = parseInt(el.id.replace('line-', ''));
                const diff = Math.abs(elLine - aln);
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
    // Format: #line-ALN (e.g., #line-5000)
    const match = hash.match(/line-(\d+)/);
    if (match) {
        const aln = parseInt(match[1]);
        goToLine(aln);
    }
}

let lastReportedALN = null;

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
        // Line IDs are ALN
        const aln = parseInt(closest.id.replace('line-', ''));
        
        if (aln !== lastReportedALN) {
            lastReportedALN = aln;
            window.parent.postMessage({ 
                type: 'linePosition', 
                line: aln
            }, '*');
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
