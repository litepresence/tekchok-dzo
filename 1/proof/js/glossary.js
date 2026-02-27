// Dark mode handling - sync with parent
(function() {
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    let currentLetter = 'A';
    
    function navigateToLetter(letter) {
        currentLetter = letter;
        const target = document.getElementById('letter-' + letter);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
    
    function getNextLetter(direction) {
        const currentIndex = letters.indexOf(currentLetter);
        if (direction === 'next') {
            return letters[(currentIndex + 1) % letters.length];
        } else {
            return letters[(currentIndex - 1 + letters.length) % letters.length];
        }
    }
    
    document.addEventListener('DOMContentLoaded', function() {
        const isDark = localStorage.getItem('darkMode') !== 'false';
        if (!isDark) document.body.classList.add('light-mode');
        
        // Set initial letter from URL hash
        const hash = window.location.hash;
        if (hash && hash.startsWith('#letter-')) {
            currentLetter = hash.replace('#letter-', '');
        }
    });
    
    window.addEventListener('message', function(e) {
        if (e.data) {
            if (e.data.type === 'darkModeChange') {
                document.body.classList.toggle('light-mode', !e.data.enabled);
                localStorage.setItem('darkMode', e.data.enabled);
            } else if (e.data.type === 'prevLetter') {
                navigateToLetter(getNextLetter('prev'));
            } else if (e.data.type === 'nextLetter') {
                navigateToLetter(getNextLetter('next'));
            }
        }
    });
})();
