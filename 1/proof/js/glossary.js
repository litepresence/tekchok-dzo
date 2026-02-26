// Dark mode handling - sync with parent
(function() {
    document.addEventListener('DOMContentLoaded', function() {
        const isDark = localStorage.getItem('darkMode') !== 'false';
        if (!isDark) document.body.classList.add('light-mode');
    });
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'darkModeChange') {
            document.body.classList.toggle('light-mode', !e.data.enabled);
            localStorage.setItem('darkMode', e.data.enabled);
        }
    });
})();
