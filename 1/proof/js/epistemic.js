// Epistemic Layer - Navigation with ALN (Absolute Line Numbers)
// ALN: 1-37756
// Uses range-based line matching for epistemic view entries

// Layer-specific configuration
const totalChapters = 25;
const chapterKeys = ['01-01', '01-02', '01-03', '01-04', '01-05', '01-06', '01-07', '01-08', '01-09', '01-10', '01-11', '01-12', '01-13', '01-14', '02-15', '02-16', '02-17', '02-18', '02-19', '02-20', '02-21', '02-22', '02-23', '02-24', '02-25'];

// State object
const state = {
    currentChapter: 0,
    totalChapters: totalChapters,
    chapterKeys: chapterKeys
};

// Initialize dark mode
SharedJS.initDarkMode();

// Create layer-specific goToLine function (range-based matching)
const goToLine = SharedJS.goToLineRange(state, totalChapters, SharedJS.showChapter(state, totalChapters));

// Setup the layer with shared utilities
SharedJS.setupAnalysisLayer(state, totalChapters, goToLine);
