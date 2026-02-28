// Contents page navigation and dark mode handling - ALN based

// Navigate between chapters
function navigateChapter(direction) {
    const chapters = Array.from(document.querySelectorAll('.chapter'));
    if (chapters.length === 0) return;
    
    // Find current chapter in viewport
    const viewportCenter = window.innerHeight / 2;
    let currentIndex = 0;
    
    for (let i = 0; i < chapters.length; i++) {
        const rect = chapters[i].getBoundingClientRect();
        if (rect.top <= viewportCenter && rect.bottom >= viewportCenter) {
            currentIndex = i;
            break;
        }
    }
    
    // Navigate to prev/next
    let newIndex;
    if (direction === 'prev') {
        newIndex = currentIndex > 0 ? currentIndex - 1 : chapters.length - 1;
    } else {
        newIndex = currentIndex < chapters.length - 1 ? currentIndex + 1 : 0;
    }
    
    chapters[newIndex].scrollIntoView({ behavior: 'smooth', block: 'start' });
}

document.addEventListener('click', function(e) {
    const row = e.target.closest('tr[data-line]');
    if (row) {
        const lineNum = row.dataset.line;
        // Send ALN directly to parent
        window.parent.postMessage({ 
            type: 'navigateToLine', 
            line: lineNum
        }, '*');
    }
});

// Dark mode handling - sync with parent
(function() {
    const isDark = localStorage.getItem('darkMode') !== 'false';
    if (!isDark) document.body.classList.add('light-mode');
    
    window.addEventListener('message', function(e) {
        if (e.data) {
            if (e.data.type === 'darkModeChange') {
                if (e.data.enabled) {
                    document.body.classList.remove('light-mode');
                } else {
                    document.body.classList.add('light-mode');
                }
                localStorage.setItem('darkMode', e.data.enabled);
            } else if (e.data.type === 'prevChapter') {
                navigateChapter('prev');
            } else if (e.data.type === 'nextChapter') {
                navigateChapter('next');
            }
        }
    });
})();
