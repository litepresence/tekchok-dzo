// Contents page navigation and dark mode handling - ALN based

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
        if (e.data && e.data.type === 'darkModeChange') {
            document.body.classList.toggle('light-mode', !e.data.enabled);
            localStorage.setItem('darkMode', e.data.enabled);
        }
    });
})();
