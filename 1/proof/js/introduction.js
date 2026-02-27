// Introduction Layer - Chapter navigation with ALN-based position reporting
// ALN (Absolute Line Numbers): 1-37756
// Uses window.ALN from aln_data.js (embedded, file:// compatible)

function getVolumeFromALN(aln) {
    return window.ALN.getVolumeFromALN(aln);
}

function getChapterFromALN(aln) {
    return window.ALN.getChapterFromALN(aln);
}

function showChapter(index) {
    const sections = document.querySelectorAll('.intro-section');
    sections.forEach((sec, i) => {
        sec.classList.toggle('active', i === index);
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
    const activeSection = document.querySelector('.intro-section.active');
    if (!activeSection) return;
    
    // Use data-aln-start attribute if available
    let aln = activeSection.dataset.alnStart;
    if (!aln) {
        // Fallback: derive from section ID
        aln = getALNFromSectionId(activeSection.id);
    }
    
    if (aln) {
        window.parent.postMessage({ type: 'chapterChanged', line: parseInt(aln) }, '*');
    }
}

function getALNFromSectionId(sectionId) {
    // Map section IDs to intro IDs for ALN lookup
    const mapping = {
        'intro-main': 'intro-main',
        'vol-01': 'vol-01',
        'vol-02': 'vol-02',
    };
    
    if (sectionId.startsWith('chap-')) {
        mapping[sectionId] = sectionId.replace('chap-', '');
    }
    
    const introId = mapping[sectionId] || sectionId;
    return window.ALN.getALNFromIntroId(introId);
}

function updateNavButtons() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    if (prevBtn) prevBtn.disabled = currentChapter === 0;
    if (nextBtn) nextBtn.disabled = currentChapter === totalChapters - 1;
}

function updateIndicator() {
    const indicator = document.getElementById('sectionIndicator');
    if (indicator && chapterTitles[currentChapter]) {
        indicator.textContent = chapterTitles[currentChapter];
    }
}

function goToLine(id) {
    const index = chapterKeys.indexOf(id);
    if (index !== -1) {
        showChapter(index);
        setTimeout(() => {
            const el = document.getElementById(id);
            if (el) {
                el.classList.add('highlighted-section');
                el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }, 100);
        return true;
    }
    return false;
}

function goToALN(aln) {
    // Find the section containing this ALN
    const sections = document.querySelectorAll('.intro-section');
    for (let i = 0; i < sections.length; i++) {
        const sec = sections[i];
        const start = sec.dataset.alnStart;
        const end = sec.dataset.alnEnd;
        if (start && end) {
            if (aln >= parseInt(start) && aln <= parseInt(end)) {
                showChapter(i);
                return true;
            }
        }
    }
    return false;
}

function handleHashNavigation() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#chapter-')) {
        const chapterId = hash.replace('#chapter-', '');
        if (goToLine('chap-' + chapterId)) return;
        if (goToLine('vol-' + chapterId)) return;
    }
    
    // Try to navigate to ALN from parent
    const params = new URLSearchParams(window.location.search);
    const line = params.get('line');
    if (line) {
        if (goToALN(parseInt(line))) return;
    }
    
    showChapter(0);
}

let lastReportedALN = null;

function reportCurrentPosition() {
    const activeSection = document.querySelector('.intro-section.active');
    if (!activeSection) return;
    
    // Use data-aln-start attribute if available
    let aln = activeSection.dataset.alnStart;
    if (!aln) {
        aln = getALNFromSectionId(activeSection.id);
    }
    
    if (aln && aln !== lastReportedALN) {
        lastReportedALN = aln;
        window.parent.postMessage({ 
            type: 'chapterPosition', 
            line: parseInt(aln)
        }, '*');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    window.addEventListener('scroll', reportCurrentPosition);
    setTimeout(reportCurrentPosition, 500);
    
    // Listen for navigation from parent (index.html)
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'prevChapter') {
            prevChapter();
        } else if (e.data && e.data.type === 'nextChapter') {
            nextChapter();
        }
    });
    
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'navigateIntroduction') {
            if (e.data.chapter) {
                const targetId = 'chap-' + e.data.chapter.replace(/-/g, '-');
                goToLine(targetId);
            } else if (e.data.volume) {
                const targetId = 'vol-' + e.data.volume;
                goToLine(targetId);
            } else if (e.data.main) {
                showChapter(0);
            } else if (e.data.line) {
                goToALN(parseInt(e.data.line));
            }
        }
    });
});

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
