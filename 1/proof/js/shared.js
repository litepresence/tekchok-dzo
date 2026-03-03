// ==========================================================================
// SHARED.JS - Common utilities for all layer pages
// Provides: dark mode sync, chapter navigation, ALN helpers, line highlighting
// ==========================================================================

(function(global) {
    'use strict';

    // ==========================================================================
    // CHAPTER MAP - Maps chapter keys to first ALN (Absolute Line Number)
    // ==========================================================================
    const CHAPTER_MAP = {
        '01-01': 1, '01-02': 635, '01-03': 1582, '01-04': 1902, '01-05': 4172,
        '01-06': 6801, '01-07': 9704, '01-08': 10472, '01-09': 11335, '01-10': 12500,
        '01-11': 13104, '01-12': 13831, '01-13': 16025, '01-14': 17361,
        '02-15': 20427, '02-16': 20900, '02-17': 22180, '02-18': 24348,
        '02-19': 26389, '02-20': 28509, '02-21': 29839, '02-22': 30637,
        '02-23': 32437, '02-24': 35701, '02-25': 36061
    };

    // ==========================================================================
    // DARK MODE - Sync with parent page
    // ==========================================================================
    function initDarkMode() {
        // Default to dark mode initially, parent will send correct state
        window.addEventListener('message', function(e) {
            if (e.data && e.data.type === 'darkModeChange') {
                if (e.data.enabled) {
                    document.body.classList.remove('light-mode');
                } else {
                    document.body.classList.add('light-mode');
                }
                localStorage.setItem('darkMode', e.data.enabled);
            }
        });
    }

    // ==========================================================================
    // CHAPTER NAVIGATION - Common functions for all layer pages
    // ==========================================================================
    function showChapter(state, totalChapters) {
        return function(index) {
            const chapters = document.querySelectorAll('.chapter');
            chapters.forEach((ch, i) => {
                ch.classList.toggle('active', i === index);
            });
            state.currentChapter = index;
            updateNavButtons(state);
            updateIndicator(state);
            window.scrollTo({ top: 0, behavior: 'instant' });
        };
    }

    function nextChapter(state, totalChapters, notifyParent) {
        if (state.currentChapter < totalChapters - 1) {
            showChapter(state, totalChapters)(state.currentChapter + 1);
            if (notifyParent) notifyParent();
        }
    }

    function prevChapter(state, notifyParent) {
        if (state.currentChapter > 0) {
            showChapter(state, state.totalChapters)(state.currentChapter - 1);
            if (notifyParent) notifyParent();
        }
    }

    function getFirstALNForChapter(volume, chapter) {
        const key = `${String(volume).padStart(2, '0')}-${String(chapter).padStart(2, '0')}`;
        return CHAPTER_MAP[key] || 1;
    }

    function updateNavButtons(state) {
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        if (prevBtn) prevBtn.disabled = state.currentChapter === 0;
        if (nextBtn) nextBtn.disabled = state.currentChapter === state.totalChapters - 1;
    }

    function updateIndicator(state) {
        const indicator = document.getElementById('chapterIndicator');
        if (!indicator) return;

        const key = state.chapterKeys[state.currentChapter];
        const parts = key.split('-');
        const volume = parts[0];
        const chapter = parts[1];
        indicator.textContent = `Volume ${parseInt(volume)}, Chapter ${parseInt(chapter)}`;
    }

    function notifyParentOfChapterChange(state) {
        const key = state.chapterKeys[state.currentChapter];
        const parts = key.split('-');
        const vol = parseInt(parts[0]);
        const chapter = parseInt(parts[1]);
        const firstALN = getFirstALNForChapter(vol, chapter);
        window.parent.postMessage({ type: 'chapterChanged', line: firstALN }, '*');
    }

    // ==========================================================================
    // LINE NAVIGATION - For translation layers (exact line matching)
    // ==========================================================================
    function goToLineExact(state, totalChapters, showChapterFn) {
        return function(aln) {
            if (!aln) return false;

            // Try exact match first (line IDs are ALN)
            let lineEl = document.getElementById('line-' + aln);

            if (!lineEl) {
                // Find best match
                const allChapters = document.querySelectorAll('.chapter');
                let bestMatch = null;
                let bestDiff = Infinity;

                allChapters.forEach(ch => {
                    const lines = ch.querySelectorAll('[id^="line-"]');
                    for (const el of lines) {
                        const elLine = parseInt(el.id.replace('line-', ''));
                        const diff = Math.abs(elLine - aln);
                        if (diff < bestDiff) {
                            bestDiff = diff;
                            bestMatch = el;
                        }
                    }
                });
                lineEl = bestMatch;
            }

            if (lineEl) {
                const chapter = lineEl.closest('.chapter');
                if (chapter) {
                    const chapterIndex = parseInt(chapter.dataset.chapter);
                    showChapterFn(chapterIndex);
                    setTimeout(() => {
                        highlightAndScroll(lineEl);
                    }, 100);
                    return true;
                }
            }
            return false;
        };
    }

    // ==========================================================================
    // LINE NAVIGATION - For analysis layers (range-based matching)
    // ==========================================================================
    function parseRangeFromElement(el) {
        // First check for data attributes
        const rangeStart = el.dataset.rangeStart;
        const rangeEnd = el.dataset.rangeEnd;
        if (rangeStart !== undefined) {
            return { start: parseInt(rangeStart), end: parseInt(rangeEnd) };
        }

        // Fall back to parsing .line-range text
        const rangeEl = el.querySelector('.line-range');
        if (rangeEl) {
            const match = rangeEl.textContent.match(/\[(\d+)-(\d+)\]/);
            if (match) {
                return { start: parseInt(match[1]), end: parseInt(match[2]) };
            }
        }
        return null;
    }

    function buildRangeDataAttributes() {
        const entries = document.querySelectorAll('.entry-block');
        entries.forEach(el => {
            const range = parseRangeFromElement(el);
            if (range) {
                el.dataset.rangeStart = range.start;
                el.dataset.rangeEnd = range.end;
            }
        });
    }

    function goToLineRange(state, totalChapters, showChapterFn) {
        return function(aln) {
            if (!aln) return false;

            // First try exact match on line ID
            let lineEl = document.getElementById('line-' + aln);

            if (!lineEl) {
                // Find best match - prefer entries where line is within range
                const allChapters = document.querySelectorAll('.chapter');
                let bestMatch = null;
                let bestScore = -Infinity;

                allChapters.forEach(ch => {
                    const entries = ch.querySelectorAll('.entry-block');
                    entries.forEach(el => {
                        const range = parseRangeFromElement(el);
                        if (range) {
                            let score = -Infinity;
                            if (aln >= range.start && aln <= range.end) {
                                score = 1000 - (range.end - range.start);
                            } else {
                                const dist = Math.min(
                                    Math.abs(aln - range.start),
                                    Math.abs(aln - range.end)
                                );
                                score = -dist;
                            }

                            if (score > bestScore) {
                                bestScore = score;
                                bestMatch = el;
                            }
                        }
                    });
                });
                lineEl = bestMatch;
            }

            if (lineEl) {
                const chapter = lineEl.closest('.chapter');
                if (chapter) {
                    const chapterIndex = parseInt(chapter.dataset.chapter);
                    showChapterFn(chapterIndex);
                    setTimeout(() => {
                        highlightAndScroll(lineEl);
                    }, 100);
                    return true;
                }
            }
            return false;
        };
    }

    // ==========================================================================
    // HIGHLIGHT AND SCROLL - Common animation for line highlighting
    // ==========================================================================
    function highlightAndScroll(element) {
        document.querySelectorAll('.highlighted-line').forEach(el => {
            el.classList.remove('highlighted-line');
            el.style.animation = '';
        });
        // Force reflow to restart animation
        void element.offsetWidth;
        element.style.animation = '';
        element.classList.add('highlighted-line');
        void element.offsetWidth;
        element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // ==========================================================================
    // HASH NAVIGATION - Handle URL hash changes
    // ==========================================================================
    function handleHashNavigation(goToLineFn) {
        const hash = window.location.hash;
        // Format: #line-ALN (e.g., #line-5000)
        const match = hash.match(/line-(\d+)/);
        if (match) {
            const aln = parseInt(match[1]);
            goToLineFn(aln);
        }
    }

    // ==========================================================================
    // LINE POSITION REPORTING - For translation layers
    // ==========================================================================
    function createReportCurrentLine() {
        let lastReportedALN = null;

        return function() {
            const lines = document.querySelectorAll('[id^="line-"]');
            if (!lines.length) return;

            const viewportMiddle = window.innerHeight / 2;
            let closest = null;
            let closestDist = Infinity;

            for (const line of lines) {
                const rect = line.getBoundingClientRect();
                const lineMiddle = (rect.top + rect.bottom) / 2;
                const dist = Math.abs(lineMiddle - viewportMiddle);
                if (dist < closestDist) {
                    closestDist = dist;
                    closest = line;
                }
            }

            if (closest) {
                const aln = parseInt(closest.id.replace('line-', ''));
                if (aln !== lastReportedALN) {
                    lastReportedALN = aln;
                    window.parent.postMessage({
                        type: 'linePosition',
                        line: aln
                    }, '*');
                }
            }
        };
    }

    // ==========================================================================
    // RANGE POSITION REPORTING - For analysis layers
    // ==========================================================================
    function createReportCurrentRange() {
        let lastReportedRange = null;

        return function() {
            const entries = document.querySelectorAll('.entry-block');
            if (!entries.length) return;

            const viewportMiddle = window.innerHeight / 2;
            let closest = null;
            let closestDist = Infinity;

            for (const entry of entries) {
                const rect = entry.getBoundingClientRect();
                const entryMiddle = (rect.top + rect.bottom) / 2;
                const dist = Math.abs(entryMiddle - viewportMiddle);
                if (dist < closestDist) {
                    closestDist = dist;
                    closest = entry;
                }
            }

            if (closest) {
                const range = parseRangeFromElement(closest);
                if (range) {
                    const rangeKey = `${range.start}-${range.end}`;
                    if (rangeKey !== lastReportedRange) {
                        lastReportedRange = rangeKey;
                        window.parent.postMessage({
                            type: 'rangePosition',
                            rangeStart: range.start,
                            rangeEnd: range.end
                        }, '*');
                    }
                }
            }
        };
    }

    // ==========================================================================
    // SETUP HELPERS - Common DOMContentLoaded setup
    // ==========================================================================
    function setupTranslationLayer(state, totalChapters, goToLineFn) {
        const showChapterFn = showChapter(state, totalChapters);
        const reportCurrentLine = createReportCurrentLine();

        document.addEventListener('DOMContentLoaded', () => {
            updateNavButtons(state);
            updateIndicator(state);
            handleHashNavigation(goToLineFn);

            window.addEventListener('scroll', reportCurrentLine);
            setTimeout(reportCurrentLine, 500);

            // Listen for navigation from parent (index.html)
            window.addEventListener('message', function(e) {
                if (e.data && e.data.type === 'prevChapter') {
                    prevChapter(state, () => notifyParentOfChapterChange(state));
                } else if (e.data && e.data.type === 'nextChapter') {
                    nextChapter(state, totalChapters, () => notifyParentOfChapterChange(state));
                }
            });
        });

        window.addEventListener('hashchange', () => handleHashNavigation(goToLineFn));

        return { showChapterFn, reportCurrentLine };
    }

    function setupAnalysisLayer(state, totalChapters, goToLineFn) {
        const showChapterFn = showChapter(state, totalChapters);
        const reportCurrentRange = createReportCurrentRange();

        document.addEventListener('DOMContentLoaded', () => {
            buildRangeDataAttributes();
            updateNavButtons(state);
            updateIndicator(state);
            handleHashNavigation(goToLineFn);

            window.addEventListener('scroll', reportCurrentRange);
            setTimeout(reportCurrentRange, 500);

            // Listen for navigation from parent (index.html)
            window.addEventListener('message', function(e) {
                if (e.data && e.data.type === 'prevChapter') {
                    prevChapter(state, () => notifyParentOfChapterChange(state));
                } else if (e.data && e.data.type === 'nextChapter') {
                    nextChapter(state, totalChapters, () => notifyParentOfChapterChange(state));
                }
            });
        });

        window.addEventListener('hashchange', () => handleHashNavigation(goToLineFn));

        return { showChapterFn, reportCurrentRange };
    }

    // ==========================================================================
    // EXPORT TO GLOBAL SCOPE
    // ==========================================================================
    global.SharedJS = {
        CHAPTER_MAP,
        initDarkMode,
        showChapter,
        nextChapter,
        prevChapter,
        getFirstALNForChapter,
        updateNavButtons,
        updateIndicator,
        notifyParentOfChapterChange,
        goToLineExact,
        parseRangeFromElement,
        buildRangeDataAttributes,
        goToLineRange,
        highlightAndScroll,
        handleHashNavigation,
        createReportCurrentLine,
        createReportCurrentRange,
        setupTranslationLayer,
        setupAnalysisLayer
    };

})(typeof window !== 'undefined' ? window : this);
