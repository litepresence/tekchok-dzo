// Conventions page - dark mode and layer switching
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
        if (e.data && e.data.type === 'layerChange') {
            let newLayer = e.data.layer;
            if (newLayer === 'introduction') newLayer = 'liturgical';
            window.location.href = '?layer=' + newLayer;
        }
    });
})();

document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    let layer = params.get('layer') || 'liturgical';
    
    // Default introduction to liturgical
    if (layer === 'introduction') layer = 'liturgical';
    
    // Map layer names to display names
    const layerNames = {
        'tibetan': 'Tibetan',
        'wylie': 'Wylie',
        'literal': 'Literal',
        'liturgical': 'Liturgical',
        'commentary': 'Commentary',
        'scholar': 'Scholar',
        'epistemic': 'Epistemic',
        'delusion': 'Delusion',
        'cognitive': 'Cognitive'
    };
    
    // Update header subtitle with layer name
    const subtitle = document.querySelector('header .subtitle');
    if (subtitle && layerNames[layer]) {
        subtitle.textContent = layerNames[layer] + ' Layer';
    }
    
    // Hide all sections except the selected one
    const sections = document.querySelectorAll('.convention-section');
    sections.forEach(section => {
        if (section.id === layer) {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });
    
    // Hide TOC since we're showing only one layer
    const toc = document.querySelector('.toc');
    if (toc) toc.style.display = 'none';

    // Listen for dropdown changes from parent and reload with new layer
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'layerChange') {
            let newLayer = e.data.layer;
            if (newLayer === 'introduction') newLayer = 'liturgical';
            window.location.href = '?layer=' + newLayer;
        }
    });
});
