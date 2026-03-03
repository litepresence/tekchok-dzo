// Introduction Layer - Chapter navigation with ALN-based position reporting
// ALN (Absolute Line Numbers): 1-37756
// Uses window.ALN from aln_data.js (embedded, file:// compatible)

// Initialize dark mode from shared.js
SharedJS.initDarkMode();

// Layer-specific configuration
const totalChapters = 27; // Main + 2 volumes + 24 chapters
const chapterKeys = ['intro-main', 'vol-01', 'vol-02', 'chap-01-01', 'chap-01-02', 'chap-01-03', 'chap-01-04', 'chap-01-05', 'chap-01-06', 'chap-01-07', 'chap-01-08', 'chap-01-09', 'chap-01-10', 'chap-01-11', 'chap-01-12', 'chap-01-13', 'chap-01-14', 'chap-02-15', 'chap-02-16', 'chap-02-17', 'chap-02-18', 'chap-02-19', 'chap-02-20', 'chap-02-21', 'chap-02-22', 'chap-02-23', 'chap-02-24', 'chap-02-25'];
const chapterTitles = ['Main Introduction', 'Volume 01', 'Volume 02', 'Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6', 'Chapter 7', 'Chapter 8', 'Chapter 9', 'Chapter 10', 'Chapter 11', 'Chapter 12', 'Chapter 13', 'Chapter 14', 'Chapter 15', 'Chapter 16', 'Chapter 17', 'Chapter 18', 'Chapter 19', 'Chapter 20', 'Chapter 21', 'Chapter 22', 'Chapter 23', 'Chapter 24', 'Chapter 25'];

// State object
const state = {
    currentChapter: 0,
    totalChapters: totalChapters,
    chapterKeys: chapterKeys
};

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
    state.currentChapter = index;
    updateNavButtons(state);
    updateIndicator(state);
    window.scrollTo({ top: 0, behavior: 'instant' });
}

function nextChapter() {
    if (state.currentChapter < totalChapters - 1) {
        showChapter(state.currentChapter + 1);
        notifyParentOfChapterChange();
    }
}

function prevChapter() {
    if (state.currentChapter > 0) {
        showChapter(state.currentChapter - 1);
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

function updateNavButtons(state) {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    if (prevBtn) prevBtn.disabled = state.currentChapter === 0;
    if (nextBtn) nextBtn.disabled = state.currentChapter === state.totalChapters - 1;
}

function updateIndicator(state) {
    const indicator = document.getElementById('sectionIndicator');
    if (indicator && chapterTitles[state.currentChapter]) {
        indicator.textContent = chapterTitles[state.currentChapter];
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
    updateNavButtons(state);
    updateIndicator(state);
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
