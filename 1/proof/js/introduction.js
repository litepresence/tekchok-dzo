// Section navigation for introduction pages
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
    document.getElementById('sectionIndicator').textContent = chapterTitles[currentChapter];
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
    
    // Try to match chapter/volume to section ID
    if (chapter) {
        const targetId = 'chap-' + chapter.replace(/-/g, '-');
        if (goToLine(targetId)) return;
    }
    if (volume) {
        const targetId = 'vol-' + volume;
        if (goToLine(targetId)) return;
    }
    
    // Default to main intro
    showChapter(0);
}

document.addEventListener('DOMContentLoaded', () => {
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    // Listen for messages from parent frame (for radio button sync)
    window.addEventListener('message', (event) => {
        if (event.data && event.data.type === 'navigateIntroduction') {
            if (event.data.chapter) {
                const targetId = 'chap-' + event.data.chapter.replace(/-/g, '-');
                goToLine(targetId);
            } else if (event.data.volume) {
                const targetId = 'vol-' + event.data.volume;
                goToLine(targetId);
            } else if (event.data.main) {
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
