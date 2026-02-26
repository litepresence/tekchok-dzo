// Contents page navigation and dark mode handling

const VOLUME_BOUNDARY = 20426;

function getVolumeFromLine(absLine) {
    if (!absLine || absLine <= 0) return 1;
    return absLine <= VOLUME_BOUNDARY ? 1 : 2;
}

document.addEventListener('click', function(e) {
    const row = e.target.closest('tr[data-line]');
    if (row) {
        const lineNum = row.dataset.line;
        const volume = getVolumeFromLine(parseInt(lineNum));
        window.parent.postMessage({ 
            type: 'navigateToLine', 
            line: lineNum,
            volume: volume 
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
