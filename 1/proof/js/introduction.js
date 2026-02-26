// Introduction Layer - Chapter navigation with line-based position reporting
// Volume 1: lines 1-20426
// Volume 2: lines 20427-37756

const VOLUME_BOUNDARY = 20426;

function getVolumeFromLine(absLine) {
    if (!absLine || absLine <= 0) return 1;
    return absLine <= VOLUME_BOUNDARY ? 1 : 2;
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
    const chapterMap = {
        '1': 1, '2': 635, '3': 1582, '4': 1902, '5': 4172,
        '6': 6801, '7': 9704, '8': 10472, '9': 11335, '10': 12500,
        '11': 13104, '12': 13831, '13': 16025, '14': 17361,
        '15': 20427, '16': 20900, '17': 22654, '18': 24822,
        '19': 26863, '20': 27946, '21': 28946, '22': 29856,
        '23': 31566, '24': 34830, '25': 35191
    };
    
    const activeSection = document.querySelector('.intro-section.active');
    if (!activeSection) return;
    
    const sectionId = activeSection.id;
    let lineNum = 1;
    let volume = 1;
    
    if (sectionId.startsWith('chap-')) {
        const parts = sectionId.replace('chap-', '').split('-');
        if (parts.length >= 2) {
            volume = parseInt(parts[0]);
            const ch = parts[1];
            lineNum = chapterMap[ch] || 1;
        }
    } else if (sectionId.startsWith('vol-')) {
        volume = parseInt(sectionId.replace('vol-', ''));
        lineNum = volume === 1 ? 1 : 20427;
    } else if (sectionId === 'intro-main') {
        lineNum = 1;
        volume = 1;
    }
    
    window.parent.postMessage({ type: 'chapterChanged', volume: volume, chapter: 0, line: lineNum }, '*');
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

function handleHashNavigation() {
    const params = new URLSearchParams(window.location.search);
    const chapter = params.get('chapter');
    const volume = params.get('volume');
    
    if (chapter) {
        const targetId = 'chap-' + chapter.replace(/-/g, '-');
        if (goToLine(targetId)) return;
    }
    if (volume) {
        const targetId = 'vol-' + volume;
        if (goToLine(targetId)) return;
    }
    
    showChapter(0);
}

let lastReportedChapter = null;
let lastReportedVolume = null;

function reportCurrentPosition() {
    const activeSection = document.querySelector('.intro-section.active');
    if (!activeSection) return;
    
    const sectionId = activeSection.id;
    let lineNum = null;
    let volume = 1;
    
    if (sectionId.startsWith('chap-')) {
        const parts = sectionId.replace('chap-', '').split('-');
        if (parts.length >= 2) {
            const vol = parseInt(parts[0]);
            const ch = parseInt(parts[1]);
            
            const chapterMap = {
                '1': 1, '2': 635, '3': 1582, '4': 1902, '5': 4172,
                '6': 6801, '7': 9704, '8': 10472, '9': 11335, '10': 12500,
                '11': 13104, '12': 13831, '13': 16025, '14': 17361,
                '15': 20427, '16': 20900, '17': 22654, '18': 24822,
                '19': 26863, '20': 27946, '21': 28946, '22': 29856,
                '23': 31566, '24': 34830, '25': 35191
            };
            
            lineNum = chapterMap[ch] || 1;
            volume = vol;
        }
    } else if (sectionId.startsWith('vol-')) {
        const vol = sectionId.replace('vol-', '');
        volume = parseInt(vol);
        lineNum = volume === 1 ? 1 : 20427;
    } else if (sectionId === 'intro-main') {
        lineNum = 1;
        volume = 1;
    }
    
    if (lineNum !== null && (sectionId !== lastReportedChapter || volume !== lastReportedVolume)) {
        lastReportedChapter = sectionId;
        lastReportedVolume = volume;
        window.parent.postMessage({ 
            type: 'chapterPosition', 
            line: lineNum, 
            volume: volume 
        }, '*');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    window.addEventListener('scroll', reportCurrentPosition);
    setTimeout(reportCurrentPosition, 500);
    
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
