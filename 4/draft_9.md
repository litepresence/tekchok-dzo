<style>
@font-face {
    font-family: 'Jomolhari';
    src: url('Jomolhari-Regular.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}

:root {
    /* Base colors (HEX for solid usage) */
    --color-tibetan-gold: #b8945a;
    --color-tibetan-maroon: #8b4513;
    --color-tibetan-burgundy: #5a2a27;
    --color-tibetan-cream: #f5f0e6;
    --color-text-dark: #333333;
    --color-text-light: #666666;

    /* RGB equivalents for opacity variants (DRY border/gradient patterns) */
    --color-tibetan-maroon-rgb: 139, 69, 19;
    --color-tibetan-cream-rgb: 245, 240, 230;

    /* Typography */
    --font-serif: 'Libre Baskerville', 'Times New Roman', serif;
    --font-tibetan: 'Jomolhari', 'Kailasa', 'Monlam Uni OuChan2',
        'Microsoft Himalaya', 'Noto Sans Tibetan', sans-serif;

    /* Reusable opacity values (semantic naming) */
    --border-opacity-light: 0.1;
    --border-opacity-medium: 0.15;
    --border-opacity-strong: 0.18;
    --border-opacity-heavy: 0.2;
    --bg-opacity-subtle: 0.4;
}

/* ===== Base Utilities ===== */
.tibetan-text {
    font-family: var(--font-tibetan);
    color: var(--color-tibetan-maroon);
    font-style: italic;
}

/* ===== Section Patterns ===== */
.section-title {
    font-family: var(--font-serif);
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--color-tibetan-maroon);
    text-align: center;
    letter-spacing: 0.03em;
    position: relative;
    padding-bottom: 0.8rem;
    margin-bottom: 2.8rem;
}

.section-title::after {
    content: "";
    display: block;
    width: 80px;
    height: 2px;
    background-color: var(--color-tibetan-gold);
    margin: 0.6rem auto 0;
}

/* Context overrides (minimal specificity) */
.cover-page .section-title {
    font-size: 1.8rem;
    text-align: left;
    margin-bottom: 1.2rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-heavy));
}

.root-text-section .section-title {
    padding-bottom: 0.6rem;
    border-bottom: 2px solid var(--color-tibetan-gold);
    margin-bottom: 2.2rem;
}

/* ===== Component Styles ===== */
.cover-page {
    font-family: var(--font-serif);
    background-color: var(--color-tibetan-cream);
    color: var(--color-text-dark);
    padding: 4rem 3rem;
    margin-bottom: 2rem;
}

.tibetan-header {
    font-family: var(--font-tibetan);
    font-size: 1.4rem;
    line-height: 1.7;
    color: #5a3921;
    /* Unique shade - no variable match */
    text-align: center;
    margin-bottom: 2.5rem;
    letter-spacing: 0.03em;
    padding: 0.8rem 0;
    border-top: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-medium));
    border-bottom: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-medium));
}

.title-container {
    text-align: center;
    margin-bottom: 1.8rem;
}

.title-main {
    font-size: 4.3rem;
    font-weight: 900;
    color: var(--color-tibetan-maroon);
    letter-spacing: 0.04em;
    margin-bottom: 0.4rem;
    line-height: 1.2;
}

.title-sub {
    font-size: 2.1rem;
    font-weight: 600;
    color: var(--color-tibetan-burgundy);
    /* Replaced hex */
    margin-bottom: 0.5rem;
    letter-spacing: 0.03em;
    line-height: 1.3;
}

.title-attribution {
    font-size: 1.5rem;
    color: var(--color-text-light);
    letter-spacing: 0.02em;
    padding-bottom:none;
    /*line-height: 1.5;*/
}

.draft-banner {
    display: block;
    background: linear-gradient(135deg, #e8e4e0 0%, #d8d2cc 100%);
    color: var(--color-tibetan-burgundy);
    /* Replaced hex */
    padding: 0.5rem 1.5rem;
    border-radius: 4px;
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    text-align: center;
    margin: 1.5rem auto 2rem;
    border: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-light));
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
}

.attribution {
    font-size: 1.05rem;
    line-height: 1.7;
    color: var(--color-text-light);
    margin-bottom: 1.8rem;
    padding: 1.2rem;
    background-color: rgba(var(--color-tibetan-cream-rgb), var(--bg-opacity-subtle));
    /* DRYed */
    border-radius: 6px;
    border-left: 3px solid var(--color-tibetan-gold);
}

.attribution div {
    margin-bottom: 0.7rem;
}

.copyleft {
    font-size: 0.95rem;
    color: var(--color-text-light);
    line-height: 1.6;
    text-align: center;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-light));
}

.copyleft div:first-child {
    font-style: italic;
    margin-bottom: 0.7rem;
    color: var(--color-tibetan-maroon);
}

.tibetan-source {
    font-size: 0.85rem;
    color: var(--color-text-light);
}

.orientation {
    padding: 1.8rem;
    line-height: 1.8;
    font-size: 1.05rem;
    color: var(--color-text-dark);
}

.orientation p {
    margin-bottom: 1.2rem;
    text-align: justify;
}

.orientation p:last-child {
    margin-bottom: 0;
}

hr {
    border: 0;
    height: 1px;
    background: linear-gradient(to right,
        transparent,
        rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-heavy)),
        transparent);
    margin: 2rem 0;
}

.contents {
    padding: 2.5rem 3rem;
    line-height: 1.6;
}

.root-text-section {
    font-family: var(--font-serif);
    color: var(--color-text-dark);
    padding: 2.5rem 2.8rem;
}

.subheading {
    font-size: 1.35rem;
    font-style: italic;
    color: var(--color-tibetan-burgundy);
    text-align: center;
    margin-bottom: 2.8rem;
    letter-spacing: 0.02em;
}

.part-header {
    text-align: center;
    margin-bottom: 2.5rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-medium));
}

.part-label {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--color-tibetan-maroon);
    letter-spacing: 0.05em;
}

.stanza-group {
    margin-bottom: 3rem;
}

.stanza {
    margin-bottom: 2.4rem;
    padding-bottom: 1.4rem;
    border-bottom: 1px dashed rgba(var(--color-tibetan-maroon-rgb), 0.12);
    /* Unique opacity */
}

.stanza:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.stanza-label {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--color-tibetan-gold);
    margin-bottom: 0.9rem;
    letter-spacing: 0.03em;
}

.stanza-text {
    font-size: 1.28rem;
    line-height: 1.75;
}

.commentary-section {
    padding-top: 2.2rem;
    border-top: 2px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-strong));
}

.commentary-header {
    font-size: 1.65rem;
    font-weight: 700;
    color: var(--color-tibetan-burgundy);
    text-align: center;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 2.4rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-heavy));
}

.commentary-stanza {
    margin-bottom: 2.1rem;
    padding-left: 2.1rem;
    position: relative;
}

.commentary-stanza:last-child {
    margin-bottom: 0;
}

.commentary-stanza::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.8rem;
    bottom: 0.8rem;
    width: 4px;
    background-color: var(--color-tibetan-gold);
    border-radius: 2px;
}

.commentary-label {
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--color-tibetan-maroon);
    margin-bottom: 0.7rem;
    letter-spacing: 0.02em;
}

.commentary-text {
    font-size: 1.18rem;
    line-height: 1.8;
    font-style: italic;
    color: var(--color-text-light);
}

/* ===== Precision Layers: Stanza System ===== */
h4.stanza {
    font-family: var(--font-serif);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--color-tibetan-gold);
    text-align: center;
    letter-spacing: 0.04em;
    margin: 2.8rem auto 1.6rem;
    padding-top: 1.6rem;
    position: relative;
    max-width: 70ch;
    line-height: 1.3;
    break-before: page;
}

/* Top divider for stanza separation (replaces container border) */
h4.stanza::before {
    content: "";
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 1px;
    background: linear-gradient(to right,
        transparent,
        rgba(var(--color-tibetan-maroon-rgb), 0.15),
        transparent);
}

/* Remove divider from first stanza */
h4.stanza:first-of-type {
    margin-top: 1.8rem;
    padding-top: 0;
}

h4.stanza:first-of-type::before {
    display: none;
}

/* Tibetan script - prominent, authentic rendering */
p.tibetan {
    font-family: var(--font-tibetan);
    font-size: 1.85rem;
    line-height: 1.9;
    color: var(--color-tibetan-maroon);
    text-align: center;
    margin: 0 auto 1.7rem;
    max-width: 65ch;
    letter-spacing: 0.015em;
    hyphens: auto;
}

/* Romanized transliteration - elegant scholarly treatment */
p.romanized {
    font-family: var(--font-serif);
    font-size: 1.25rem;
    font-style: italic;
    color: var(--color-text-dark);
    line-height: 1.75;
    text-align: center;
    margin: 0 auto 1.4rem;
    max-width: 68ch;
    letter-spacing: 0.02em;
}

/* Literal translation - subtle scholarly layer */
p.literal {
    font-family: var(--font-serif);
    font-size: 1.27rem;
    color: var(--color-text-dark);
    line-height: 1.7;
    text-align: center;
    margin: 0 auto;
    max-width: 70ch;
    padding-bottom: 0.8rem;
    font-feature-settings: "liga"1, "calt"1;
    /* Enhances readability */
}

/* Responsive refinement */
@media (max-width: 768px) {
    p.tibetan {
        font-size: 1.65rem;
    }

    p.romanized {
        font-size: 1.15rem;
    }

    h4.stanza {
        font-size: 1.25rem;
        margin: 2.4rem auto 1.4rem;
    }

    h4.stanza::before {
        width: 100px;
    }
}

.pagebreak {
    break-after: page;
}

/* ===== Contents Navigation System ===== */
.contents {
    padding: 2.8rem 3rem;
    max-width: 800px; /* Prevents over-wide text blocks */
    margin: 0 auto;   /* Centers within parent container */
}

.contents .section-title {
    font-size: 2.4rem;
    margin-bottom: 2.6rem;
    padding-bottom: 1rem;
}

/* Entry container with thematic separation */
.part-entry {
    position: relative;
    padding: 1.6rem 0 1.8rem 0;
    border-bottom: 1px solid rgba(var(--color-tibetan-maroon-rgb), var(--border-opacity-medium));
    transition: padding-left 0.3s ease;
}

.part-entry:last-child {
    border-bottom: none;
    padding-bottom: 0.5rem;
}

/* PART indicator - gold accent with subtle presence */
.part-number {
    font-family: var(--font-serif);
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--color-tibetan-gold);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.45rem;
    position: relative;
    padding-left: 0.3rem;
}

.part-number::before {
    content: "•";
    position: absolute;
    left: -0.9rem;
    top: -0.1rem;
    color: var(--color-tibetan-gold);
    font-size: 1.4rem;
    line-height: 1;
    opacity: 0.7;
}

/* Title - commanding maroon presence */
.part-title {
    font-family: var(--font-serif);
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--color-tibetan-maroon);
    letter-spacing: 0.025em;
    line-height: 1.25;
    margin-bottom: 0.35rem;
    position: relative;
    padding-right: 1.8rem; /* Space for stanza range alignment */
}

/* Stanza range - elegant burgundy accent */
.stanza-range {
    font-family: var(--font-serif);
    font-size: 1.12rem;
    font-style: italic;
    color: var(--color-tibetan-burgundy);
    letter-spacing: 0.03em;
    margin-bottom: 0.9rem;
    position: absolute;
    right: 0;
    top: 2.15rem;
    text-align: right;
    width: 120px;
    font-weight: 500;
}

/* Description - scholarly indented block */
.part-description {
    font-family: var(--font-serif);
    font-size: 1.15rem;
    line-height: 1.68;
    color: var(--color-text-dark);
    padding-left: 1.4rem;
    border-left: 2px solid rgba(var(--color-tibetan-gold), 0.28);
    margin-top: 0.3rem;
    position: relative;
}

.part-description::before {
    content: "";
    position: absolute;
    left: -0.35rem;
    top: 0.45rem;
    width: 8px;
    height: 8px;
    background: var(--color-tibetan-gold);
    border-radius: 50%;
    opacity: 0.65;
}

/* Subtle visual enhancement on hover (preserves print safety) */
@media (hover: hover) {
    .part-entry:hover {
        padding-left: 0.6rem;
    }
    .part-entry:hover .part-title {
        color: var(--color-tibetan-burgundy);
    }
}

/* Responsive refinement */
@media (max-width: 768px) {
    .contents {
        padding: 2.2rem 1.8rem;
    }
    .part-title {
        font-size: 1.55rem;
        padding-right: 0;
    }
    .stanza-range {
        position: static;
        text-align: left;
        width: auto;
        margin-top: -0.4rem;
        font-size: 1.05rem;
    }
    .part-description {
        font-size: 1.08rem;
        padding-left: 1.2rem;
    }
    .part-number::before {
        left: -0.75rem;
        font-size: 1.25rem;
    }
}

</style>
<div class="cover-page">
    <div class="tibetan-header">གུན་མཁྱེན་ཀློང་ཆེན་རབ་འབྱམས་པའི་གསུང་རབ་མཛོད་བདུན་ལ་བལྟ་བར་བསྐུལ་བ་བཞུགས་སོ།།</div>
    <div class="title-container">
        <h1 class="title-main">EXHORTATION</h1>
        <h2 class="title-attribution">Behold the Omniscient Longchen Rabjam's</h2>
        <h3 class="title-sub">Seven Treasuries Of Teachings</h3>
    </div>
    <div class="attribution">
        <div>Root text: <span class="italic">Kun mkhyen klong chen rab 'byams pa'i gsung rab mdzod bdun la blta bar bskul ba</span></div>
        <div>Author: Paltrül Rinpoche (Dza Paltrül Orgyen Jigme Chökyi Wangpo)</div>
        <div>Translator: litepresence</div>
    </div>
    <div class="copyleft">
        <div>Copyleft: Recognition requires no interval.</div>
        <div class="tibetan-source">Tibetan Source: BDK UT22920_005_0004 (vol. 5, pod 5 "pa", text 4)</div>
    </div>
</div>
<div class="orientation">
    <h2 class="section-title">ORIENTATION</h2>
    <p>This text is an exhortation (bskul ba), not a manual of practice or a formal pointing-out instruction. Exhortations are not generally considered restricted texts.</p>
    <p>Patrul Rinpoche praises scripture as Buddha-activity and speaks from the standpoint of realization in order to inspire confidence and devotion. Without direct introduction from a qualified lineage holder, such words may be understood conceptually, but they are not intended to replace experiential transmission.</p>
    <p>Accordingly, this teaching is not restricted in nature. It presents the Dzogchen view with great force and rhetorical clarity, while deliberately refraining from procedural instruction. Patrul Rinpoche wrote for herders, monastics, and laypeople alike, openly expressing the view without always imparting method. Here, reification is cut through language and confidence, not through technique.</p>
    <p>Read as encouragement to look—rather than as authorization to conclude.</p>
</div>
<div class="pagebreak"></div>
<div class="contents">
    <h1 class="section-title">CONTENTS</h1>
    <div class="part-entry">
        <div class="part-number">PART ONE</div>
        <div class="part-title">HOMAGE</div>
        <div class="stanza-range">Stanzas 1–10</div>
        <div class="part-description">Establishing the ground—field never established, dharma-body's nature, scripture as mirror</div>
    </div>
    <div class="part-entry">
        <div class="part-number">PART TWO</div>
        <div class="part-title">DHARMA-BODY'S DISPLAY</div>
        <div class="stanza-range">Stanzas 11–27</div>
        <div class="part-description">Recognition in practice—meeting Buddha now, liberation without interval, cutting elaboration</div>
    </div>
    <div class="part-entry">
        <div class="part-number">PART THREE</div>
        <div class="part-title">EFFORTLESS ABIDING</div>
        <div class="stanza-range">Stanzas 28–40</div>
        <div class="part-description">Integration—merging mind/scripture, effortless abiding, cutting proliferation of methods</div>
    </div>
    <div class="part-entry">
        <div class="part-number">PART FOUR</div>
        <div class="part-title">DEVOTION AND LINEAGE</div>
        <div class="stanza-range">Stanzas 41–54</div>
        <div class="part-description">Culmination—lineage continuity, Abu Dhraho's humility, simultaneous recognition-liberation</div>
    </div>
</div>
<div class="pagebreak"></div>
<div class="root-text-section">
    <h1 class="section-title">ROOT TEXT</h1>
    <div class="subheading">Liturgy and Commentary</div>
    <div class="part-header">
        <div class="part-label">PART ONE</div>
    </div>
    <div class="stanza-group">
        <div class="stanza">
            <div class="stanza-text">
                Field never established—utterly peaceful,<br>
                Unbroken expanse of pristine awareness,<br>
                Great power of intention, perfection's display,<br>
                To that All-Knowing Lama—prostration. [1]<br>
                Alas—self-nature of supreme qualities,<br>
                Not relying on scripture, not self-made,<br>
                From great ocean the supreme jewel arises,<br>
                In lowly place—where could one find it? [2]<br>
                Even when sun of realization appears,<br>
                Without unbroken blessing-transmission,<br>
                Those entering emptiness-meditation's darkness,<br>
                Rarely proceed correctly on the path. [3]<br>
                Not hearing creates great fault in existence,<br>
                Wrongly hearing creates sin greater still,<br>
                When chance exists to look upon scripture now,<br>
                Why not purify the pupil of hearing? [4]<br>
                In this existence—single wish-fulfilling jewel,<br>
                Precious system of the All-Knowing Lama,<br>
                If no Buddha exists beyond this place,<br>
                Who would not arise in great joy? [5]<br>
                Peak of vehicles—supreme Vajra Essence,<br>
                Hundred-thousand tantras' jewel treasury,<br>
                Vast expression, profound expressed meaning,<br>
                Seeing this—Samantabhadra's face in jewel light. [6]<br>
                Sixty hundred-thousand tantras in the heart,<br>
                Knowing cyclic and peaceful share one nature,<br>
                Realizing profound peak vehicle's mark,<br>
                Therefore hold vigilance seeing this text. [7]<br>
                Dharma-body's nature needs no protection,<br>
                Treasury of Samantabhadra beyond cause,<br>
                Without cutting elaboration with scriptures like this,<br>
                Cutting mind-investigating vehicles' grasp—accomplished by whom? [8]<br>
                Essence of all pith instructions gathered,<br>
                Each six section a complete dharma treasury,<br>
                Path so excellent it meets Victorious One,<br>
                Hearing immediately—not difficult. [9]<br>
                Single treatise containing complete teaching,<br>
                Complete explanation—accomplishment's jewel,<br>
                Scriptures like this, even in India and Tibet,<br>
                Never came before. Never come now. [10]<br>
                Wish-fulfilling guide to abandon-adopt places,<br>
                Treasury of complete dharma—hearing, contemplation,<br>
                Seeing this, know suchness of all teachings,<br>
                Hundred scriptures practiced immediately. [11]<br>
                Peak vehicle's intention—ten words to one,<br>
                Pith instruction concise, meaning penetrating,<br>
                Single treasury of essential practice here,<br>
                Alone courageous cutting existence's root. [12]<br>
                Mind-essence never established as pure or impure,<br>
                Bare—awareness recognizing itself, free from separation,<br>
                Deepest point—awareness self-recognizing, intention's core,<br>
                Dharma-expanse jewel treasury—profound beyond. [13]<br>
            </div>
        </div>
    </div>
    <div class="pagebreak"></div>
    <div class="commentary-section">
        <div class="commentary-header">TRANSLATOR'S COMMENTARY</div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 1</div>
            <div class="commentary-text">
                Field never established—utterly peaceful. Unbroken expanse where prostration lands already rests. Before the name arose.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 2</div>
            <div class="commentary-text">
                Alas—self-nature not relying on scripture, not self-made. From great ocean the supreme jewel arises. In lowly place—where could one find it? Ocean gives the jewel.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 3</div>
            <div class="commentary-text">
                Sunlight alone does not ripen the seed. Blessing carries warmth that opens what light merely illuminates—emptiness-meditation without lineage: thunderbolt-darkness.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 4</div>
            <div class="commentary-text">
                Not hearing leaves obscurity intact. Wrong hearing hardens obscurity into certainty—misapprehension binds tighter than ignorance. Purification occurs when hearing hears itself.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 5</div>
            <div class="commentary-text">
                Wish-fulfilling jewel in this existence—not elsewhere. Great joy already here before the name arose.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 6</div>
            <div class="commentary-text">
                Peak never departed from this place. Hundred-thousand tantras in single stanza—treasury gleaming. Samantabhadra's face in the light.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 7</div>
            <div class="commentary-text">
                Sixty hundred-thousand tantras in the heart—not by compression but because the heart never excluded them. Cyclic existence and peace share one nature. Vigilance is natural clarity itself. Scripture—mirror.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 8</div>
            <div class="commentary-text">
                Dharma-body never stood vulnerable—protection implies threat where none exists. Cause and effect dissolve as display within single expanse. Elaboration cuts itself. Without this scripture's sharp edge—who cuts the grasping.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 9</div>
            <div class="commentary-text">
                Essence gathers because never scattered. Each section holds the whole—not representation but presence. Meeting Victorious One requires no travel. The interval dissolves.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 10</div>
            <div class="commentary-text">
                Teaching never lacked completeness—this treatise reveals what never departed. Never came before—nothing was absent. Never comes now—arrival always already here.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 11</div>
            <div class="commentary-text">
                Abandon and adopt arise within single expanse. Treasury holds entire path—not sequence but recognition. Seeker sought gone. Seeing reveals directly. Hundred scriptures practiced immediately.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 12</div>
            <div class="commentary-text">
                Ten words collapse to one—not reduction but revealing the single source. Meaning penetrates without effort—never stood apart from what it means. Cutting the root requires no blade.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 13</div>
            <div class="commentary-text">
                Mind-essence never established as pure or impure—ka dag is absence of establishment itself. Separation appears without dividing what remains whole. Deepest point is surface—no depth to fathom.
            </div>
        </div>
    </div>
</div>
<div class="pagebreak"></div>
<div class="root-text-section">
    <div class="part-header">
        <div class="part-label">PART TWO</div>
    </div>
    <div class="stanza-group">
        <div class="stanza">
            <div class="stanza-text">
                Scripture where authentic dharma-body arrives,<br>
                Scriptures like this are Buddha actual,<br>
                In this existence accomplishing Victorious One's activity,<br>
                Scripture manifestly showing Victorious One's intention. [14]<br>
                Even meeting Buddha—beyond this exists?<br>
                Scriptures like this treasury of all sacred dharma,<br>
                Final reach of all dharmas' expressed meaning,<br>
                Bare showing dharma-body, awareness self-recognizing. [15]<br>
                Comparing all dharmas—even then, beyond this?<br>
                Scriptures like this are noble assemblies' heart,<br>
                Past-future Victorious Sons of three times,<br>
                Realization-awareness never transcends this. [16]<br>
                Noble ones' pristine awareness—beyond this?<br>
                Three jewels complete in dharma-body field,<br>
                Unsurpassed footprints of all Victorious Ones,<br>
                Display of All-Knowing Lama's realization. [17]<br>
                Who meets this makes existence final,<br>
                Even hearing one word of scriptures like this,<br>
                If able to turn appearances into wandering,<br>
                While obtaining fortune to meet the complete. [18]<br>
                If discarded—how could mind exist?<br>
                Alas, three baskets and nine stages of dharma,<br>
                Generally intend for the diligent—"Liberate<br>
                Through meditation, accomplishment, striving they say; [19]<br>
                No seeing—awareness self-recognizing, free,<br>
                This vajra peak beyond mind, effortless—<br>
                Unmaintained Buddha—awareness empty nature bare,<br>
                Given now even to the lazy as dharma-body. [20]<br>
                No attachment to meditation, accomplishment, striving,<br>
                In this world including gods who show this path,<br>
                The All-Knowing Lama alone is dharma-body,<br>
                From however much dharma-body teaching abides— [21]<br>
                This treasury of dharma-expanse is dharma's essence,<br>
                Therefore scriptures like this in this existence,<br>
                Liberation through seeing—hearing liberation, recollection,<br>
                Connection's moment—measureless Buddha. [22]<br>
                Obtaining intention—you are Buddha now,<br>
                Without losing ear of blessing lineage,<br>
                Placing intention, meaning-lineage's awareness recognizing itself transfers,<br>
                Wide placement established upon future children. [23]<br>
                All-Knowing Lama actually equal to you,<br>
                Even without piercing words' meaning and intention,<br>
                When devotion arises, blessing-lineage's awareness recognizing itself transfers,<br>
                Beyond seeing this scripture—precious word-empowerment. [24]<br>
                Nowhere else—awareness' power complete,<br>
                When tormented by fear of fault or impurity,<br>
                Seeing this scripture—great-joy awareness recognizing itself,<br>
                Heedless joy—awareness clear and luminous. [25]<br>
                Deluded appearances shatter on contact,<br>
                When joy expands and great bliss blazes,<br>
                Seeing this scripture—joy-fatigue attachment gone,<br>
                Expanse unbroken—no boundary abandon-adopt. [26]<br>
                Showing profound intention of All-Knowing Lama,<br>
                When tormented by attachment and striving now,<br>
                Seeing this scripture—pride and pretension shatter,<br>
                Appearances spacious—whatever way you act, fine. [27]<br>
                Doubt's tightness gone—relaxed equal abiding,<br>
                This is Middle Way—this perfection of others,<br>
                This cutting-object pacifies suffering,<br>
                Actual Mahāmudrā and Great Perfection. [28]<br>
            </div>
        </div>
    </div>
    <div class="pagebreak"></div>
    <div class="commentary-section">
        <div class="commentary-header">TRANSLATOR'S COMMENTARY</div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 14</div>
            <div class="commentary-text">
                Dharma-body arrives now—not event but recognition of what never departed. Scripture is Buddha—speech never separates from realization. Activity accomplishes—no agent required. Manifest showing requires no veil.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 15</div>
            <div class="commentary-text">
                Meeting Buddha reveals no beyond. Treasury contains all—nothing ever outside this expanse. Final reach is the source itself. Bare showing: awareness naked without veils.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 16</div>
            <div class="commentary-text">
                Comparison finds no superior—nothing stands outside the expanse that holds comparison. Noble assemblies gather in single heart. Past present future arise within awareness—never moved across time.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 17</div>
            <div class="commentary-text">
                Noble awareness never stood apart to be compared. Three jewels complete within dharma-body—refuge never existed outside the one taking refuge. Footprints mark no path traveled—ground itself appearing as trace.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 18</div>
            <div class="commentary-text">
                Final existence marks end of seeking. Single word holds the ocean—words never separated from what they express. Partial appearances wander—never whole to begin with. Fortune arrives.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 19</div>
            <div class="commentary-text">
                Discarding implies something substantial to cast away—mind never stood as entity. Three baskets and nine stages serve the diligent—skillful means not ultimate truth. Striving liberates—what never stood bound.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 20</div>
            <div class="commentary-text">
                Seeing requires no seer—awareness recognizing itself never stood apart. Vajra peak not summit to ascend—ground never requiring elevation. Unmaintained Buddha always present. Lazy ones receive. Already received. Already complete. Already lazy—and free.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 21</div>
            <div class="commentary-text">
                Attachment never bound what was always free—meditation accomplishment striving arise as display. Gods and humans share one ground—no elevation separates them. Lama alone is dharma-body. Teaching abides as awareness itself.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 22</div>
            <div class="commentary-text">
                Essence never stood apart from display—dharma-expanse holds all without exclusion. Seeing liberates. Hearing frees. Recollection dissolves the interval. No separation between encounter and release.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 23</div>
            <div class="commentary-text">
                Obtaining is recognition of what never departed—Buddha now not after lifetimes. Ear of blessing lineage never broke—transmission never crossed distance. Placing intention needs no location. Student—teacher gone.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 24</div>
            <div class="commentary-text">
                Equality not aspiration—Lama and student share single nature. Piercing words unnecessary—meaning reveals itself through devotion's openness. Blessing transfers—no distance crossed. Word-empowerment: sound becoming awareness.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 25</div>
            <div class="commentary-text">
                Nowhere else—completeness never lacked anything. Fear of fault arises from taking appearance as substantial—fault never stained what was never established. Great-joy awareness—natural radiance. Heedless joy—freedom from maintaining.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 26</div>
            <div class="commentary-text">
                Delusion shatters on contact—no opposition required. Joy expands. Bliss blazes. Both transparent when seen without grasping. Attachment to experience dissolves—bliss never stood apart from awareness. Abandon and adopt dissolve within single expanse.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 27</div>
            <div class="commentary-text">
                Profound intention never concealed itself—shows exactly as it is. Torment arises only when attachment mistakes itself for path. Pride shatters—no position stands apart to be proud. Spacious expanse holds all action.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 28</div>
            <div class="commentary-text">
                Tightness dissolves—contraction releases itself. Relaxed abiding needs no adjustment—what never bound awareness requires no release. Extremes never stood apart to reconcile. Cutting—no blade required. Suffering pacifies itself. Two names—single recognition.
            </div>
        </div>
    </div>
</div>
<div class="pagebreak"></div>
<div class="root-text-section">
    <div class="part-header">
        <div class="part-label">PART THREE</div>
    </div>
    <div class="stanza-group">
        <div class="stanza">
            <div class="stanza-text">
                All dharmas gathered here—surpassing all,<br>
                If son entering All-Knowing Lama's footsteps,<br>
                Never separate from this excellent scripture,<br>
                Entrusting awareness self-recognizing—constant supreme companion. [29]<br>
                Core mind-placing like this exists?<br>
                Immediate ease—Buddha obtained at core,<br>
                Not tormented by striving, mind's fetters gone,<br>
                Happy—ascend; suffering—weariness finds companionship. [30]<br>
                Scriptures like this singularly undeceiving,<br>
                Therefore sing in melody, take as song,<br>
                Cut into verses, recite smoothly, look,<br>
                If never separate from this— [31]<br>
                Deluded saṃsāra appearances scatter to pieces,<br>
                When blessing-lineage transfers realization's point,<br>
                Inexpressible—awareness self-recognizing arises,<br>
                Meeting face to face All-Knowing dharma-body Lama. [32]<br>
                Mind at ease upon ground of ease, unbroken,<br>
                Beyond seeing this scripture, no other practice,<br>
                This itself is essence of meditation, accomplishment,<br>
                For however long you spend with these scriptures— [33]<br>
                For that long, dharma-body's intention arises naturally,<br>
                Therefore do not multiply striving mind's agitation,<br>
                From spacious relaxedness behold these excellent supports,<br>
                Profound meaning not distant at all. [34]<br>
                Mind's thread cut—self-settling enough for me,<br>
                Difficult to realize like logical treatises,<br>
                No need to construct, arrange, seek word-meaning,<br>
                In self-settling naturally merge mind with scripture. [35]<br>
                Barely moving through spacious expanse, nakedly,<br>
                Introduction—awareness recognizing itself, never established,<br>
                All-Knowing Lama's pith instruction—yourself,<br>
                This expressed object is actual empowerment itself. [36]<br>
                Essence practice—who needs beyond oneself?<br>
                Pierce certain words or leave them whole—either way,<br>
                Know profound meaning or remain unknowing—<br>
                Obtain intention's core or wander empty-handed— [37]<br>
                Doubt cut—look without distraction, naturally,<br>
                Look again, mix with experience and look,<br>
                Merge scripture and mind—mind obtains scripture's expansion,<br>
                From inseparability, sing with joyful resonance. [38]<br>
                Devotion's power blazes—realization's pristine awareness arises,<br>
                Alas, essence of essence itself,<br>
                Profound beyond profound—nowhere else like this,<br>
                Treasury of blessing, essence teaching itself. [39]<br>
                Teacher actual—Buddha held in hand,<br>
                Eons describing qualities like this,<br>
                My small mind's intelligence cannot exhaust them,<br>
                What of other great minds' confidence? [40]<br>
                No path like this brings joy to noble ones,<br>
                Alas, jewel precious like this,<br>
                When obtaining good fortune through self-power now,<br>
                Even abiding in existence—no weariness. [41]<br>
                Having generated devotion, why not enter spacious expanse?<br>
                Heart-companion, cast your mind into this scripture,<br>
                From spacious relaxedness—cut mind's thread now,<br>
                Pacify here agitation of doer, deed, striving mind. [42]<br>
                Cut elaboration of many scriptures here,<br>
                What use many pleasant-sounding systems?<br>
                What use many profoundly profound instructions?<br>
                What use many elaborated practices? [43]<br>
                What use many explanations affirming "yes, yes"?<br>
                Spacious relaxed samādhi—this sleeping dharma is yourself,<br>
                Mind at ease in spacious expanse—this self-throne is yourself,<br>
                Knowing a single excellent scripture—this all-liberation is yourself. [44]<br>
            </div>
        </div>
    </div>
    <div class="pagebreak"></div>
    <div class="commentary-section">
        <div class="commentary-header">TRANSLATOR'S COMMENTARY</div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 29</div>
            <div class="commentary-text">
                All dharmas gather—source never scattered across separate territories. Following Lama's footsteps means walking where no path was laid—recognition itself is the entrance. Never separating from scripture—words dissolve boundary between reader and read. Awareness's constant companion never departed.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 30</div>
            <div class="commentary-text">
                Core-placement requires no location. Ease arrives not as reward—effort never substantially contributed to what was always complete. Fetters dissolve—never tied, only believed to bind. Happiness ascends. Suffering finds companionship. Both within single expanse.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 31</div>
            <div class="commentary-text">
                Undeceiving—concealment never stood between word and meaning. Scripture functions as mirror not veil. Singing dissolves distance—sound becomes the awareness it carries. Smooth recitation lets words fall away—only recognition remains.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 32</div>
            <div class="commentary-text">
                Deluded appearances scatter—never whole to begin with. No destruction required—only recognition of what never substantially assembled. Blessing transfers not across space—student teacher one taste. Inexpressible awareness arises—expression never stood apart.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 33</div>
            <div class="commentary-text">
                Ground of ease never departed from ease itself—mind settles not by effort but by recognizing it never left. No practice stands apart—practice never separate from realization. Essence of meditation and accomplishment—single recognition wearing two names.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 34</div>
            <div class="commentary-text">
                Intention arises naturally—not through force but as uncontrived expression of what never departed. Striving mind agitates—transparent display taken as substantial. Relaxation not technique—effort never substantially contributed to what was always present. Spacious relaxedness ground already beneath agitation.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 35</div>
            <div class="commentary-text">
                Mind's thread cuts itself when seen without grasping—no external agent required. Self-settling needs no method—recognition is sufficient. Logical treatises proliferate—seeking what never departed from the seeker. Construction obscures what stands already complete.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 36</div>
            <div class="commentary-text">
                Bare movement needs no clothing—naked passage through spacious expanse requires no preparation. Introduction reveals what never stood apart to be introduced—awareness always present. Pith instruction your own nature—no transmission crosses distance because none existed to cross. Empowerment actualizes—authorization never departed.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 37</div>
            <div class="commentary-text">
                Essence practice requires nothing added—what was never elsewhere cannot be acquired. Pierce words or leave them whole—both arrive where no path was laid. Know the meaning or remain in unknowing—recognition precedes both.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 38</div>
            <div class="commentary-text">
                Doubt cuts itself when reinforcement stops—no technique required. Awareness rests as itself. Seeing again—mixed with experience. Scripture mind merge—boundaries never substantially enclosed what was always whole.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 39</div>
            <div class="commentary-text">
                Devotion blazes as openness itself—not emotional fervor but collapse of resistance. Realizing awareness dawns—not as new event but as what never departed from its source. Essence of essence marks no hierarchy—depth collapses when seen without interval.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 40</div>
            <div class="commentary-text">
                Teacher actual—speech never separates from realization. Buddha held in hand—not object grasped but recognition holder and held share one nature. Eons of description cannot exhaust—qualities arise from inexhaustible source. Small mind acknowledges limitation—not deficiency but recognition completeness never required comprehension.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 41</div>
            <div class="commentary-text">
                Joy arises as recognition itself—not emotional reaction but natural radiance. The jewel fulfills—wishing never stood apart from fulfillment. Seeker sought gone. Self-power is recognition's autonomy—no validation required from outside.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 42</div>
            <div class="commentary-text">
                Devotion opens what was never closed—no barrier stood between recognition and recognizer. Mind meeting scripture—words dissolve the boundary between reader and read. Mind's thread cuts itself when seen without grasping. Doer, deed, striving—dissolve into spacious relaxedness already present.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 43</div>
            <div class="commentary-text">
                Elaboration cuts itself. Pleasant systems please the ear—obscure recognition. Profound instructions multiply when recognition is missed. Practices generate distance through effort to close it. Simplicity never elsewhere.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 44</div>
            <div class="commentary-text">
                Affirmations proliferate where certainty never departed—yes-yes explanations multiply only when recognition is obscured. Sleeping dharma abides without effort—natural clarity remains. Self-throne requires no elevation—already seated where no throne was laid.
            </div>
        </div>
    </div>
</div>
<div class="pagebreak"></div>
<div class="root-text-section">
    <div class="part-header">
        <div class="part-label">PART FOUR</div>
    </div>
    <div class="stanza-group">
        <div class="stanza">
            <div class="stanza-text">
                A hundred pith instructions—this single bridge is yourself,<br>
                Having placed it within yourself, do not seek elsewhere,<br>
                Do not discard essence and gather straw,<br>
                Do not abandon effortlessness and accomplish through diligence. [45]<br>
                Send forth doerless—do not multiply action,<br>
                Merely born in All-Knowing Lama's lineage,<br>
                Holds like this reach ancestors' hands,<br>
                Paths like this placed by forefathers. [46]<br>
                Descend heedless—even here descend,<br>
                Alas mother, alas mother—three lineages' great compassion,<br>
                Good fortune exists to see excellent scripture,<br>
                Great treasure exists to accomplish excellent path. [47]<br>
                Buddha within yourself—true even for you,<br>
                Therefore on this excellent path delighting Victor,<br>
                Heart-companion, merge mind with dharma,<br>
                Absorb heart-speech into heart's center. [48]<br>
                Placed in heart—it is essence even so,<br>
                Heedless sūtra-keeper, I Abu Dhraho,<br>
                Explaining oral dharma not within myself,<br>
                Without joy—yet All-Knowing lineage's scripture. [49]<br>
                Faith obtained—unique experience,<br>
                Five poisons blaze as fire, distraction to turmoil,<br>
                Though I resemble one for whom delusion hard to reverse,<br>
                When hearing seeing scriptures like this— [50]<br>
                Existence's partial appearances go—unravel or not,<br>
                Therefore mind stable, five poisons' conceptions small,<br>
                You good-fortuned samaya-keeper and those like you,<br>
                Scripture seen—supreme awareness self-recognizing, blessing essence. [51]<br>
                Again generate certainty of certain attainment,<br>
                All-Knowing Lama, that perfect Buddha's<br>
                Blessing radiance—wherever it touches,<br>
                Recognition and liberation simultaneous—direct measure. [52]<br>
                Common ancestor of hundred accomplished—All-Knowing Lama,<br>
                Lord of realization, great deity-venerable,<br>
                Expanse-transcendent awareness-holder Jigme Lingpa,<br>
                Owner of teachings, great treasure Lama and others— [53]<br>
                From All-Knowing's scripture, blessing lineage obtained,<br>
                Heart-companion, you hold treasury of that intention,<br>
                Similarly supreme—All-Knowing's excellent speech,<br>
                Seeing that manner, eightfold meaning as awareness recognizing itself. [54]<br>
            </div>
        </div>
    </div>
    <div class="pagebreak"></div>
    <div class="commentary-section">
        <div class="commentary-header">TRANSLATOR'S COMMENTARY</div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 45</div>
            <div class="commentary-text">
                Hundred instructions condense to single bridge—recognition stands on both banks simultaneously. No river ever divided them. Seeking elsewhere generates distance it seeks to close—movement away assumes source was elsewhere. Discarding essence for straw reveals only what was never lost.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 46</div>
            <div class="commentary-text">
                Doerless action moves without agent—no one stands apart to send or receive. Born into lineage through recognition alone—not blood but continuity of recognition itself. Ancestral holds remain exactly where placed—in the nature of mind itself.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 47</div>
            <div class="commentary-text">
                Heedless descent lands within recognition's expanse—no fall exists outside it. Ground never departed from falling. Three lineages manifest as single compassion—past present future collapse into single continuum. Seeing scripture recognition dawning—not visual perception.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 48</div>
            <div class="commentary-text">
                Buddha within not as potential but as actual presence—no becoming required. Path delights the Victor—never led elsewhere. Joy is recognition itself—seeker and sought collapse. Merging mind with dharma—subject-object dissolves without technique.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 49</div>
            <div class="commentary-text">
                Essence placed in heart—recognition of what never departed. The Carefree One's heedlessness not deficiency—flow of teaching without adherence to teacher. Oral dharma not owned—words move through lineage like breath through lungs. Joy absent not depression—transcendence of fluctuation.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 50</div>
            <div class="commentary-text">
                Faith unique—recognition never standing apart from recognizer. Five poisons blaze as raw material—fire transforms without rejecting fuel. Impurity never stained what was never established as pure. Habit's thickness.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 51</div>
            <div class="commentary-text">
                Appearances go. Unraveling or not—both dissolve in single movement. Neither ever substantially bound awareness. Mind stable not through suppression—disturbance never anchored what was always free. Five poisons' conceptions small—transparent when seen.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 52</div>
            <div class="commentary-text">
                Certainty of what never departed—repeated generation not accumulation but continuous recognition. Blessing radiance touches—no outside, no inside, no boundary. Recognition liberation simultaneous—no interval ever divided them.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 53</div>
            <div class="commentary-text">
                Single source—hundred accomplished flow from one recognition. No fork ever divided the stream. Realization's lord abides beyond elevation—power is freedom from position. The Awareness-Holder—intention's expanse transcended location—no center holds the continuum.
            </div>
        </div>
        <div class="commentary-stanza">
            <div class="commentary-label">Stanza 54</div>
            <div class="commentary-text">
                Treasury of intention rests in heart—not acquired, not transmitted across distance. Excellent speech reveals what never stood apart from hearing. Meanings arise—not objects to grasp but awareness knowing its own nature before names appear. No interval between text and reader. No separation between blessing and the one blessed.
            </div>
        </div>
    </div>
</div>
<div class="pagebreak"></div>
<h1 class="section-title">Tibetan, Wylie, and Literal</h1>
<h4 class="stanza" style="break-before:avoid;">1 - ༡།</h4>
<p class="tibetan">
    གདོད་ནས་རབ་ཞི་གཉུག་མ་བརྡལ་བའི་ཞིང་།། <br>
    །རྟག་ཏུ་མི་གཡོ་ཡེ་ཤེས་ཆོས་སྐུའི་ཀློང་།། <br>
    །དགོངས་པའི་རྩལ་ཆེན་རྫོགས་པའི་སྣང་འགྲོས་ཅན།། <br>
    །ཀུན་མཁྱེན་བླ་མ་དེ་ལ་ཕྱག་འཚལ་ལོ།། <br>
</p>
<p class="romanized">
    gdod nas rab zhi gnyug ma brdal ba'i zhing <br>
    rtag tu mi g.yo ye shes chos sku'i klong <br>
    dgongs pa'i rtsal chen rdzogs pa'i snang 'gros can <br>
    kun mkhyen bla ma de la phyag 'tshal lo<br>
</p>
<p class="literal">
    never-established-from utterly-peaceful primordial unbroken field <br>
    always unchanging pristine-awareness dharma-body expanse <br>
    intention power great perfection appearance-movement possessing <br>
    all-knowing Lama that-to prostration-offer<br>
</p>
<h4 class="stanza">2 - ༢།</h4>
<p class="tibetan">
    ཀྱེ་ལགས་ཡོན་ཏན་མཆོག་གི་རང་བཞིན་ནི།། <br>
    །དམ་པའི་གཞུང་ལ་མ་བརྟེན་རང་བཟོས་མིན།། <br>
    །རྒྱ་མཚོ་ཆེ་ལས་ནོར་བུ་མཆོག་འབྱུང་གི།། <br>
    །དམན་པའི་ཡུལ་ལས་རང་གར་ཅི་ཞིག་རྙེད།། <br>
</p>
<p class="romanized">
    kye lags yon tan mchog gi rang bzhin ni <br>
    dam pa'i gzhung la ma brten rang bzos min <br>
    rgya mtsho che las nor bu mchog 'byung gi <br>
    dman pa'i yul las rang gar ci zhig rnyed<br>
</p>
<p class="literal">
    alas qualities supreme-of self-nature <br>
    excellent scripture on not-relying self-made not <br>
    great ocean from jewel supreme arising <br>
    lowly place in self where something find<br>
</p>
<h4 class="stanza">3 - ༣།</h4>
<p class="tibetan">
    རྟོགས་པའི་ཡེ་ཤེས་ཉི་མ་སྣང་བ་ཡང་།། <br>
    །བྱིན་བརྒྱུད་མ་ཉམས་བླ་མའི་མན་ངག་ལས།། <br>
    །ངེས་པར་འོང་གི་སྟོང་སྒོམ་མུན་རྡོ་བ།། <br>
    །ལེགས་པའི་ལམ་དུ་རྣམ་མར་འགྲོ་བ་ཉུང་།། <br>
</p>
<p class="romanized">
    rtogs pa'i ye shes nyi ma snang ba yang <br>
    byin brgyud ma nyams bla ma'i man ngag las <br>
    nges par 'ong gi stong sgom mun rdo ba <br>
    legs pa'i lam du rnam mar 'gro ba nyung<br>
</p>
<p class="literal">
    even realization sun appearing <br>
    unbroken blessing-transmission without <br>
    emptiness-meditation darkness to coming those <br>
    path on correctly proceeding rare<br>
</p>
<h4 class="stanza">4 - ༤།</h4>
<p class="tibetan">
    ཐོས་པ་མེད་པ་སྲིད་ན་སྐྱོན་ཆེ་ཡང་།། <br>
    །ལོག་པར་ཐོས་པ་དེ་བས་སྡིག་ཆེ་བས།། <br>
    །མཁས་པའི་གཞུང་ལ་བལྟ་བ་ཡོད་དུས་འདིར།། <br>
    །ཐོས་པའི་མིག་དཀྱུས་ཅི་ཕྱིར་དག་མི་བགྱིད།། <br>
</p>
<p class="romanized">
    thos pa med pa srid na skyon che yang <br>
    log par thos pa de bas sdig che bas <br>
    mkhas pa'i gzhung la blta ba yod dus 'dir <br>
    thos pa'i mig dkyus ci phyir dag mi bgyid<br>
</p>
<p class="literal">
    not-hearing existence great fault <br>
    wrongly-hearing sin greater still <br>
    scripture this upon looking chance existing now <br>
    hearing pupil purify why-not<br>
</p>
<h4 class="stanza">5 - ༥།</h4>
<p class="tibetan">
    སྲིད་པ་འདི་ན་ཡིད་བཞིན་ནོར་གཅིག་པུ།། <br>
    །ཀུན་མཁྱེན་བླ་མའི་གཞུང་ལུགས་རིན་པོ་ཆེ།། <br>
    །འདི་ལས་གཞན་ལ་སངས་རྒྱས་ཡོད་མིན་ན།། <br>
    །འདི་ལ་རབ་དགའ་མི་སྐྱེ་སུ་ཞིག་ཡོད།། <br>
</p>
<p class="romanized">
    srid pa 'di na yid bzhin nor gcig pu <br>
    kun mkhyen bla ma'i gzhung lugs rin po che <br>
    'di las gzhan la sangs rgyas yod min na <br>
    'di la rab dga' mi skyе su zhig yod<br>
</p>
<p class="literal">
    existence this in wish-fulfilling jewel single <br>
    all-knowing Lama-of system precious <br>
    this from other Buddha exists-not if <br>
    this in great-joy not-arising who<br>
</p>
<h4 class="stanza">6 - ༦།</h4>
<p class="tibetan">
    ཐེག་པའི་ཡང་རྩེ་རྡོ་རྗེ་སྙིང་པོའི་མཆོག། <br>
    །འབུམ་ཕྲག་རྒྱུད་སྡེའི་དགོངས་དོན་རིན་ཆེན་མཛོད།། <br>
    །རྗོད་བྱེད་རྒྱ་ཆེ་བརྗོད་བྱ་དོན་ཟབ་པ།། <br>
    །འདི་མཐོང་ཀུན་ཏུ་བཟང་པོ་དངོས་ཞལ་མཇལ།། <br>
</p>
<p class="romanized">
    theg pa'i yang rtse rdo rje snying po'i mchog <br>
    'bum phrag rgyud sde'i dgongs don rin chen mdzod <br>
    rjod byed rgya che brjod bya don zab pa <br>
    'di mthong kun tu bzang po dngos zhal mjal<br>
</p>
<p class="literal">
    peak vehicles-of supreme vajra-essence <br>
    hundred-thousand tantras jewel treasury <br>
    vast expression profound expressed-meaning <br>
    this seeing Samantabhadra face meeting<br>
</p>
<h4 class="stanza">7 - ༧།</h4>
<p class="tibetan">
    འབུམ་ཕྲག་དྲུག་ཅུའི་རྒྱུད་དོན་ཁོང་དུ་ཆུད།། <br>
    །སྲིད་ཞི་འཁོར་འདས་ཡོངས་ཀྱི་གནས་ལུགས་ཤེས།། <br>
    །ཟབ་ལམ་ཐེག་རྩེའི་དགོངས་པའི་ཁྱད་ཆོས་རྟོགས།། <br>
    །དེ་ཕྱིར་གཞུང་འདི་མཇལ་བ་ནན་ཏན་མཛོད།། <br>
</p>
<p class="romanized">
    'bum phrag drug cu'i rgyud don khong du chud <br>
    srid zhi 'khor 'das yongs kyi gnas lugs shes <br>
    zab lam theg rtse'i dgongs pa'i khyad chos rtogs <br>
    de phyir gzhung 'di mjal ba nan tan mdzod<br>
</p>
<p class="literal">
    sixty hundred-thousand tantras heart in <br>
    cyclic-existence peace one-nature knowing <br>
    profound peak-vehicle mark realizing <br>
    this text seeing vigilance hold therefore<br>
</p>
<h4 class="stanza">8 - ༨།</h4>
<p class="tibetan">
    བསྲུང་དུ་མེད་པ་ཆོས་སྐུའི་གནས་ལུགས་ནི།། <br>
    །རྒྱུ་འབྲས་ལས་འདས་ཀུན་བཟང་དགོངས་པའི་མཛོད།། <br>
    །གཞུང་བཟང་འདི་འདྲས་སྤྲོས་པ་མ་བཅད་ན།། <br>
    །ཡིད་དཔྱོད་ཐེག་པའི་ངན་ཞེན་སུ་ཡིས་གཞིག། <br>
</p>
<p class="romanized">
    bsrung du med pa chos sku'i gnas lugs ni <br>
    rgyu 'bras las 'das kun bzang dgongs pa'i mdzod <br>
    gzhung bzang 'di 'dras spros pa ma bcad na <br>
    yid dpyod theg pa'i ngan zhen su yis gzhig<br>
</p>
<p class="literal">
    protection without dharma-body-of nature <br>
    cause beyond Samantabhadra intention-treasury <br>
    scriptures like-this with elaboration not-cutting <br>
    mind-investigating vehicles bad-grasping who-by causal-connector<br>
</p>
<h4 class="stanza">9 - ༩།</h4>
<p class="tibetan">
    མན་ངག་ཀུན་གྱི་སྙིང་པོ་བསྡུས་བསྡུས་བ།། <br>
    །དྲུག་ཚན་རེས་ཀྱང་དམ་ཆོས་མཛོད་རྫོགས་པའི།། <br>
    །ལམ་བཟང་འདི་འདྲ་རྒྱལ་བ་དངོས་མཇལ་ཀྱང་།། <br>
    །ཅིག་ཆར་ཐོས་པ་དཀའ་བ་མ་ཡིན་ནམ།། <br>
</p>
<p class="romanized">
    man ngag kun gyi snying po bsdus bsdus ba <br>
    drug tshan res kyang dam chos mdzod rdzogs pa'i <br>
    lam bzang 'di 'dra rgyal ba dngos mjal kyang <br>
    cig char thos pa dka' ba ma yin nam<br>
</p>
<p class="literal">
    all pith-instructions essence gathered <br>
    each six section complete dharma-treasury <br>
    path excellent this Victorious-One meeting <br>
    hearing immediate not-difficult<br>
</p>
<h4 class="stanza">10 - ༡༠།</h4>
<p class="tibetan">
    བསྟན་པ་ཡོངས་རྫོགས་བསྟན་བཅོས་གཅིག་ཁོ་ནར།། <br>
    །ཚང་བའི་རྣམ་བཤད་གྲུབ་མཐའ་རིན་ཆེན་མཛོད།། <br>
    །གཞུང་བཟང་འདི་འདྲ་རྒྱ་བོད་གཉིས་ཆར་ཡང་།། <br>
    །སྔར་ཡང་མ་བྱོན་ད་ཡང་འབྱོན་རེ་ཀན།། <br>
</p>
<p class="romanized">
    bstan pa yongs rdzogs bstan bcos gcig kho nar <br>
    tshang ba'i rnam bshad grub mtha' rin chen mdzod <br>
    gzhung bzang 'di 'dra rgya bod gnyis char yang <br>
    sngar yang ma byon da yang 'byon re kan<br>
</p>
<p class="literal">
    single treatise complete-teaching containing <br>
    complete explanation accomplishment jewel <br>
    scriptures like-this even India or Tibet in <br>
    never before-came never now-come<br>
</p>
<h4 class="stanza">11 - ༡༡།</h4>
<p class="tibetan">
    སྤང་བླང་གནས་ཀུན་ཡིད་བཞིན་ལེགས་སྟོན་པ།། <br>
    །ཆོས་ཚུལ་ཡོངས་རྫོགས་ཐོས་བསམ་སྒོམ་པའི་མཛོད།། <br>
    །འདི་མཐོང་བསྟན་པ་ཀུན་གྱི་དེ་ཉིད་ཤེས།། <br>
    །བརྒྱ་ཕྲག་གཞུང་ལ་ཅིག་ཆར་སྦྱངས་པར་འགྱུར།། <br>
</p>
<p class="romanized">
    spang blang gnas kun yid bzhin legs ston pa <br>
    chos tshul yongs rdzogs thos bsam sgom pa'i mdzod <br>
    'di mthong bstan pa kun gyi de nyid shes <br>
    brgya phrag gzhung la cig char sbayngs par 'gyur<br>
</p>
<p class="literal">
    wish-fulfilling guide abandon-adopt places <br>
    complete dharma treasury hearing contemplation <br>
    this seeing all-teachings suchness know <br>
    hundred scriptures practiced immediate<br>
</p>
<h4 class="stanza">12 - ༡༢།</h4>
<p class="tibetan">
    ཐེག་རྩེའི་དགོངས་དོན་ཚིག་དོན་བཅུ་གཅིག་ཏུ།། <br>
    །ལེགས་བསྡུས་ཁ་ཚང་དོན་འདྲིལ་མན་ངག་གི།། <br>
    །ཉམས་ལེན་གནད་ཀྱི་མཛོད་གཅིག་སྲིད་པ་ན།། <br>
    །སྲིད་པའི་རྩ་བ་གཅོད་ལ་གཅིག་ཏུ་དཔའ།། <br>
</p>
<p class="romanized">
    theg rtse'i dgongs don tshig don bcu gcig tu <br>
    legs bsdus kha tshang don 'dril man ngag gi <br>
    nyams len gnad kyi mdzod gcig srid pa na <br>
    srid pa'i rtsa ba gcod la gcig tu dpa'<br>
</p>
<p class="literal">
    peak-vehicle intention ten words to-one <br>
    pith-instruction concise meaning penetrating <br>
    single treasury essential-practice here <br>
    alone courageous existence root cutting<br>
</p>
<h4 class="stanza">13 - ༡༣།</h4>
<p class="tibetan">
    ཁྱད་པར་གཉུག་མའི་སེམས་ཉིད་ཆོས་སྐུའི་དོན།། <br>
    །བསལ་བཞག་བྲལ་བའི་ཡེ་ཤེས་རྗེན་པ་རུ།། <br>
    །ལེགས་སྟོན་ཀུན་མཁྱེན་བླ་མའི་དགོངས་པའི་མཐིལ།། <br>
    །ཟབ་ལས་ཆེས་ཟབ་ཆོས་དབྱིངས་རིན་ཆེན་མཛོད།། <br>
</p>
<p class="romanized">
    khyad par gnyug ma'i sems nyid chos sku'i don <br>
    bsal bzhag bral ba'i ye shes rjen pa ru <br>
    legs ston kun mkhyen bla ma'i dgongs pa'i mthil <br>
    zab las ches zab chos dbyings rin chen mdzod<br>
</p>
<p class="literal">
    mind-essence never-established pure-or-impure <br>
    bare pristine-awareness separation free-from <br>
    all-knowing Lama intention point-of-points <br>
    dharma-expanse jewel treasury profound beyond<br>
</p>
<h4 class="stanza">14 - ༡༤།</h4>
<p class="tibetan">
    ཡང་དག་ཆོས་སྐུ་དངོས་སུ་བྱོན་པའི་གཞུང་།། <br>
    །གཞུང་བཟང་འདི་འདྲ་སངས་རྒྱས་དངོས་ཡིན་ཏེ།། <br>
    །སྲིད་པ་འདི་ན་རྒྱལ་བའི་མཛད་པ་སྒྲུབ།། <br>
    །རྒྱལ་བའི་དགོངས་པ་མངོན་སུམ་སྟོན་པའི་གཞུང་།། <br>
</p>
<p class="romanized">
    yang dag chos sku dngos su byon pa'i gzhung <br>
    gzhung bzang 'di 'dra sangs rgyas dngos yin te <br>
    srid pa 'di na rgyal ba'i mdzad pa sgrub <br>
    rgyal ba'i dgongs pa mngon sum ston pa'i gzhung<br>
</p>
<p class="literal">
    scripture where authentic dharma-body arriving <br>
    scriptures like-this Buddha actual <br>
    existence this in Victorious-One activity accomplishing <br>
    scripture manifestly Victorious-One intention showing<br>
</p>
<h4 class="stanza">15 - ༡༥།</h4>
<p class="tibetan">
    སངས་རྒྱས་མཇལ་ཀྱང་འདི་ལས་ཡོད་རེ་ཀན།། <br>
    །གཞུང་བཟང་འདི་འདྲ་དམ་ཆོས་ཀུན་གྱི་མཛོད།། <br>
    །ཆོས་རྣམས་ཀུན་གྱི་བརྗོད་བྱ་མཐར་ཐུག་པ།། <br>
    །ཆོས་སྐུའི་ཡེ་ཤེས་རྗེན་པར་སྟོན་པ་སྟེ།། <br>
</p>
<p class="romanized">
    sangs rgyas mjal kyang 'di las yod re kan <br>
    gzhung bzang 'di 'dra dam chos kun gyi mdzod <br>
    chos rnams kun gyi brjod bya mthar thug pa <br>
    chos sku'i ye shes rjen par ston pa ste<br>
</p>
<p class="literal">
    even Buddha meeting beyond this exists <br>
    scriptures like-this all sacred-dharma treasury <br>
    all dharmas expressed-meaning final-reach <br>
    barely dharma-body pristine-awareness showing<br>
</p>
<h4 class="stanza">16 - ༡༦།</h4>
<p class="tibetan">
    ཆོས་ཀུན་བསྡུར་ཀྱང་འདི་ལས་ཡོད་རེ་ཀན།། <br>
    །གཞུང་བཟང་འདི་འདྲ་འཕགས་ཚོགས་ཀུན་གྱི་ཐུགས།། <br>
    །དུས་གསུམ་སྔ་ཕྱིའི་རྒྱལ་སྲས་འཕགས་རྣམས་ཀྱི།། <br>
    །རྟོགས་པའི་ཡེ་ཤེས་འདི་ལས་མ་འདས་ཏེ།། <br>
</p>
<p class="romanized">
    chos kun bsdur kyang 'di las yod re kan <br>
    gzhung bzang 'di 'dra 'phags tshogs kun gyi thugs <br>
    dus gsum snga phyi'i rgyal sras 'phags rnams kyi <br>
    rtogs pa'i ye shes 'di las ma 'das te<br>
</p>
<p class="literal">
    all dharmas comparing even-then beyond this <br>
    scriptures like-this noble-assemblies heart <br>
    past-future Victorious-Sons three-times <br>
    realization-awareness never-transcends this<br>
</p>
<h4 class="stanza">17 - ༡༧།</h4>
<p class="tibetan">
    འཕགས་པའི་ཡེ་ཤེས་འདི་ལས་ཡོད་རེ་ཀན།། <br>
    །མཆོག་གསུམ་ཡོངས་རྫོགས་ཆོས་སྐུའི་མཆོད་སྡོང་ནི།། <br>
    །རྒྱལ་བ་ཀུན་གྱི་གཤེགས་ཤུལ་བླ་ན་མེད།། <br>
    །ཀུན་མཁྱེན་བླ་མའི་རྟོགས་པའི་འདྲ་འབག་སྟེ།། <br>
</p>
<p class="romanized">
    'phags pa'i ye shes 'di las yod re kan <br>
    mchog gsum yongs rdzogs chos sku'i mchod sdong ni <br>
    rgyal ba kun gyi gshegs shul bla na med <br>
    kun mkhyen bla ma'i rtogs pa'i 'drab 'bag ste<br>
</p>
<p class="literal">
    noble-ones pristine-awareness beyond this <br>
    three jewels complete dharma-body field <br>
    unsurpassed all Victorious-Ones footprints <br>
    all-knowing Lama realization display<br>
</p>
<h4 class="stanza">18 - ༡༨།</h4>
<p class="tibetan">
    འདི་ལ་སུ་མཇལ་སྲིད་པ་ཐ་མ་ཡིན།། <br>
    །གཞུང་བཟང་འདི་འདྲ་ཚིག་གཅིག་ཐོས་པས་ཀྱང་།། <br>
    །སྲིད་པའི་སྣང་ཤས་ཧྲུལ་པོར་བགྱིད་ནུས་ན།། <br>
    །ཡོངས་རྫོགས་མཇལ་བའི་སྐལ་བ་རྙེད་བཞིན་དུ།། <br>
</p>
<p class="romanized">
    'di la su mjal srid pa tha ma yin <br>
    gzhung bzang 'di 'dra tshig gcig thos pas kyang <br>
    srid pa'i snang shas hrul por bgyid nus na <br>
    yongs rdzogs mjal ba'i skal ba rnyed bzhin du<br>
</p>
<p class="literal">
    this meeting who existence final-makes <br>
    even scriptures like-this one-word hearing <br>
    appearances wandering turning able-if <br>
    complete meeting fortune obtaining while<br>
</p>
<h4 class="stanza">19 - ༡༩།</h4>
<p class="tibetan">
    འདོར་བར་བགྱིད་ན་སེམས་ཡོད་ཇི་ལྟར་ཡིན།། <br>
    །ཀྱེ་ལགས་སྡེ་སྣོད་གསུམ་དང་རིམ་དགུའི་ཆོས།། <br>
    །ཕལ་ཆེར་བརྩོན་འགྲུས་ཅན་ལ་དགོངས་པ་སྟེ།། <br>
    །སྒོམ་དང་སྒྲུབ་དང་རྩོལ་བས་གྲོལ་ལོ་ཞེས།། <br>
</p>
<p class="romanized">
    'dor bar bgyid na sems yod ji ltar yin <br>
    kye lags sde snod gsum dang rim dgu'i chos <br>
    phal cher brtson 'grus can la dgongs pa ste <br>
    sgom dang sgrub dang rtsol bas grol lo zhes<br>
</p>
<p class="literal">
    discarded-if mind how-exist <br>
    alas three baskets nine stages dharma <br>
    generally diligent-for intending <br>
    liberate meditation accomplishment striving they-say<br>
</p>
<h4 class="stanza">20 - ༢༠།</h4>
<p class="tibetan">
    བསལ་བཞག་བྲལ་བའི་ཡེ་ཤེས་མཐོང་བ་མེད།། <br>
    །རྩོལ་མེད་བློ་འདས་རྡོ་རྗེ་རྩེ་མོ་འདི།། <br>
    །མ་བསྒོམས་སངས་རྒྱས་རིག་སྟོང་རྗེན་པའི་ཀློང་།། <br>
    །ལེ་ལོ་ཅན་དང་ཆོས་སྐུར་དེང་སྤྲོད་དེ།། <br>
</p>
<p class="romanized">
    bsal bzhag bral ba'i ye shes mthong ba med <br>
    rtsol med blo 'das rdo rje rtse mo 'di <br>
    ma bsgoms sangs rgyas rig stong rjen pa'i klong <br>
    le lo can dang chos skur deng sprod de<br>
</p>
<p class="literal">
    seeing-not pristine-awareness separation free-from <br>
    this vajra peak mind-beyond effortless <br>
    unmaintained Buddha pristine-awareness-emptiness bare <br>
    lazy ones to dharma-body now-given<br>
</p>
<h4 class="stanza">21 - ༢༡།</h4>
<p class="tibetan">
    སྒོམ་དང་སྒྲུབ་དང་རྩོལ་བློའི་ཞེན་པ་མེད།། <br>
    །ལམ་འདི་སྟོན་ལ་ལྷར་བཅས་འཇིག་རྟེན་ན།། <br>
    །ཀུན་མཁྱེན་བླ་མ་ཆོས་སྐུ་ཉག་གཅིག་ཡིན།། <br>
    །ཆོས་སྐུའི་བསྟན་པ་ཇི་སྙེད་གནས་པ་ལས།། <br>
</p>
<p class="romanized">
    sgom dang sgrub dang rtsol blo'i zhen pa med <br>
    lam 'di ston la lhar bcas 'jig rten na <br>
    kun mkhyen bla ma chos sku nyag gcig yin <br>
    chos sku'i bstan pa ji snyed gnas pa las<br>
</p>
<p class="literal">
    meditation accomplishment striving attachment not <br>
    path this showing gods-including world this in <br>
    all-knowing Lama alone dharma-body <br>
    however-much dharma-body teaching abiding-from<br>
</p>
<h4 class="stanza">22 - ༢༢།</h4>
<p class="tibetan">
    ཆོས་དབྱིངས་མཛོད་འདི་ཆོས་ཀྱི་ཉིང་ཁུ་ཡིན།། <br>
    །དེ་ཕྱིར་གཞུང་བཟང་འདི་འདྲ་སྲིད་འདི་ན།། <br>
    །མཐོང་གྲོལ་ཡིན་ཏེ་ཐོས་གྲོལ་དྲན་གྲོལ་ཡིན།། <br>
    །འབྲེལ་པ་ཐོག་ཚད་མ་འོངས་སངས་རྒྱས་ཡིན།། <br>
</p>
<p class="romanized">
    chos dbyings mdzod 'di chos kyi snying khu yin <br>
    de phyir gzhung bzang 'di 'dra srid 'di na <br>
    mthong grol yin te thos grol dran grol yin <br>
    'brel pa thog tshad ma 'ongs sangs rgyas yin<br>
</p>
<p class="literal">
    this dharma-expanse treasury dharma essence <br>
    therefore scriptures like-this existence this in <br>
    seeing-liberation hearing-liberation recollection-liberation <br>
    connection moment measureless Buddha<br>
</p>
<h4 class="stanza">23 - ༢༣།</h4>
<p class="tibetan">
    དགོངས་པ་རྙེད་ན་ད་ལྟའི་སངས་རྒྱས་ཡིན།། <br>
    །བྱིན་བརླབས་བརྒྱུད་པའི་རྣོ་སོ་མ་ཉམས་ཤིང་།། <br>
    །དགོངས་པ་གཏད་པས་དོན་བརྒྱུད་ཡེ་ཤེས་འཕོ།། <br>
    །ཕྱི་རབས་བུ་ལ་གཏད་རྒྱས་རྒྱས་བཏབ་པས།། <br>
</p>
<p class="romanized">
    dgongs pa rnyed na da ltai'i sangs rgyas yin <br>
    byin rlabs brgyud pa'i rno so ma nyams shing <br>
    dgongs pa gtad pas don brgyud ye shes 'pho <br>
    phyi rabs bu la gtad rgyas rgyas btab pas<br>
</p>
<p class="literal">
    intention obtaining you-are Buddha now <br>
    blessing-lineage ear not-losing <br>
    intention placing meaning-lineage pristine-awareness transferring <br>
    future children on wide-placement established<br>
</p>
<h4 class="stanza">24 - ༢༤།</h4>
<p class="tibetan">
    ཀུན་མཁྱེན་བླ་མ་དངོས་དང་མཚུངས་པ་ཡིན།། <br>
    །ཇི་བཞིན་ཚིག་དོན་དགོངས་པ་མ་ཁྲོལ་ཡང་།། <br>
    །མོས་གུས་ཐོབ་ན་བྱིན་བརྒྱུད་ཡེ་ཤེས་འཕོ།། <br>
    །གཞུང་འདི་མཇལ་ལས་ཚིག་དབང་རིན་པོ་ཆེ།། <br>
</p>
<p class="romanized">
    kun mkhyen bla ma dngos dang mtshungs pa yin <br>
    ji bzhin tshig don dgongs pa ma khrol yang <br>
    mos gus thob na byin brgyud ye shes 'pho <br>
    gzhung 'di mjal las tshig dbang rin po che<br>
</p>
<p class="literal">
    all-knowing Lama actual equal you <br>
    words meaning intention piercing-not even <br>
    devotion obtaining blessing-lineage pristine-awareness transferring <br>
    scripture this seeing beyond word-empowerment precious<br>
</p>
<h4 class="stanza">25 - ༢༥།</h4>
<p class="tibetan">
    གཞན་ན་མེད་དེ་རིག་པའི་རྩལ་དབང་རྫོགས།། <br>
    །སྐྱོན་སུ་འཇིགས་དང་མི་དགས་གདུང་བའི་ཚེ།། <br>
    །གཞུང་འདི་མཇལ་ན་དགའ་ཆེན་ཡེ་ཤེས་སྐྱེ།། <br>
    །བག་དྲོ་ཉམས་དགའ་རིག་པ་དྭངས་ཤིང་གསལ།། <br>
</p>
<p class="romanized">
    gzhan na med de rig pa'i rtsal dbang rdzogs <br>
    skyon su 'jigs dang mi dags gdung ba'i tshe <br>
    gzhung 'di mjal na dga' chen ye shes skyе <br>
    bag dro nyams dga' rig pa dwangs shing gsal<br>
</p>
<p class="literal">
    elsewhere-not awareness power complete <br>
    fault impurity fear tormented-when <br>
    scripture this seeing great-joy pristine-awareness arising <br>
    heedless joy awareness clear luminous<br>
</p>
<h4 class="stanza">26 - ༢༦།</h4>
<p class="tibetan">
    ཡུལ་སྣང་འཁྲུལ་པ་ཐུག་ཕྲད་འཇིག་པ་ཡིན།། <br>
    །ཉམས་དགའ་རྒྱས་དང་བདེ་ཆེན་འབར་བའི་ཚེ།། <br>
    །གཞུང་འདི་མཇལ་ན་དགའ་བྲོད་ཞེན་པ་འཇིག། <br>
    །སྤང་བླང་རིས་མེད་གཉུག་མ་བརྡལ་བའི་ཀློང་།། <br>
</p>
<p class="romanized">
    yul snang 'khrul pa thug phrad 'jig pa yin <br>
    nyams dga' rgyas dang bde chen 'bar ba'i tshe <br>
    gzhung 'di mjal na dga' brod zhen pa 'jig <br>
    spang blang ris med gnyug ma brdal ba'i klong<br>
</p>
<p class="literal">
    deluded appearances contact-on shattering <br>
    joy expanding great-bliss blazing-when <br>
    scripture this seeing joy-fatigue attachment gone <br>
    expanse unbroken abandon-adopt boundary not<br>
</p>
<h4 class="stanza">27 - ༢༧།</h4>
<p class="tibetan">
    ཀུན་མཁྱེན་བླ་མའི་དགོངས་ཟབ་སྟོན་པ་ཡིན།། <br>
    །ཚེ་འདིར་ཞེན་དང་རྩོལ་བས་གདུང་བའི་ཚེ།། <br>
    །གཞུང་འདི་མཇལ་ནས་ཨ་འཐས་མངོན་རློམ་འཇིག། <br>
    །སྣང་བ་གུ་ཡངས་གང་ལྟར་བྱས་ཀྱང་ཆོག། <br>
</p>
<p class="romanized">
    kun mkhyen bla ma'i dgongs zab ston pa yin <br>
    tshe 'dir zhen dang rtsol bas gdung ba'i tshe <br>
    gzhung 'di mjal nas a 'thas mngon rlom 'jig <br>
    snang ba gu yangs gang ltar byas kyang chog<br>
</p>
<p class="literal">
    all-knowing Lama profound intention showing <br>
    attachment striving tormented-when now <br>
    scripture this seeing pride pretension shattering <br>
    appearances spacious whatever-way acting fine<br>
</p>
<h4 class="stanza">28 - ༢༨།</h4>
<p class="tibetan">
    རེ་དོགས་ཁྲིགས་མེད་མཉམ་གཞག་ལྷོད་ཀྱིས་འགྲོ།། <br>
    །དབུ་མ་འདི་ཡིན་ཕ་རོལ་ཕྱིན་པ་འདི།། <br>
    །གཅོད་ཡུལ་འདི་ཡིན་སྡུག་བསྔལ་ཞི་བྱེད་དེ།། <br>
    །ཕྱག་རྒྱ་ཆེ་དང་རྫོགས་པ་ཆེན་པོ་དངོས།། <br>
</p>
<p class="romanized">
    re dogs khriks med mnyam gzhag lhod kyis 'gro <br>
    dbu ma 'di yin pha rol phyin pa 'di <br>
    gcod yul 'di yin sdug bsngal zhi byed de <br>
    phyag rgya chen dang rdzogs pa chen po dngos<br>
</p>
<p class="literal">
    doubt tightness gone equal-abiding relaxed <br>
    this Middle-Way this perfection-others <br>
    this cutting-object suffering pacifying <br>
    Mahāmudrā Great-Perfection actual<br>
</p>
<h4 class="stanza">29 - ༢༩།</h4>
<p class="tibetan">
    ཆོས་ཀུན་འདིར་འདུས་ཀུན་ལས་ཁྱད་དུ་འཕགས།། <br>
    །ཀུན་མཁྱེན་བླ་མའི་རྗེས་འཇུག་སྲས་ཡིན་ན།། <br>
    །གཞུང་བཟང་འདི་དང་ནམ་ཡང་མི་འབྲལ་ཏེ།། <br>
    །རིག་པའི་གཏན་གྲོགས་འདི་ལ་བཅོལ་པས་མཆོག། <br>
</p>
<p class="romanized">
    chos kun 'dir 'dus kun las khyad du 'phags <br>
    kun mkhyen bla ma'i rjes 'jug sras yin na <br>
    gzhung bzang 'di dang nam yang mi 'bral te <br>
    rig pa'i gtan grogs 'di la bcol pas mchog<br>
</p>
<p class="literal">
    all dharmas gathered here surpassing all <br>
    son all-knowing Lama footsteps entering-if <br>
    this excellent scripture from never-separate <br>
    awareness self-awareness constant-companion supreme entrusting<br>
</p>
<h4 class="stanza">30 - ༣༠།</h4>
<p class="tibetan">
    ཕུག་གི་བློ་གཏད་འདི་འདྲ་ཡོད་རེ་ཀན།། <br>
    །འཕྲལ་དུ་བློ་བདེ་ཕུགས་སུ་སངས་རྒྱས་ཐོབ།། <br>
    །རྩོལ་བས་མི་གདུང་བློ་ཡི་འཆིང་བ་འཇིག། <br>
    །སྐྱིད་ན་གོང་ནོན་སྡུག་ན་སྐྱོ་གྲོགས་བྱེད།། <br>
</p>
<p class="romanized">
    phug gi blo gtad 'di 'dra yod re kan <br>
    'phral du blo bde phugs su sangs rgyas thob <br>
    rtsol bas mi gdung blo yi 'ching ba 'jig <br>
    skyid na gong non sdug na skyo grogs byed<br>
</p>
<p class="literal">
    core mind-placing like-this exists <br>
    immediate ease Buddha core-obtained <br>
    striving-not tormented mind fetters gone <br>
    happy ascending suffering weariness companionship finding<br>
</p>
<h4 class="stanza">31 - ༣༡།</h4>
<p class="tibetan">
    གཞུང་བཟང་འདི་འདྲ་མི་བསླུ་ཉག་གཅིག་ཡིན།། <br>
    །དེ་ཕྱིར་དབྱངས་སུ་གྱེར་ཞིང་མགུར་དུ་འཐེན།། <br>
    །ཚིགས་སུ་བཅད་ཅིང་ལྷུག་པོར་འདོན་ཞིང་བལྟ།། <br>
    །ནམ་ཡང་འདི་དང་འབྲལ་བར་མ་བྱས་ན།། <br>
</p>
<p class="romanized">
    gzhung bzang 'di 'dra mi bsllu nyag gcig yin <br>
    de phyir dbyangs su gyer zhing mgur du 'then <br>
    tshigs su bcad cing lhug por 'don zhing blta <br>
    nam yang 'di dang 'bral bar ma byas na<br>
</p>
<p class="literal">
    scriptures like-this singularly undeceiving <br>
    therefore melody-in singing song-as-taking <br>
    verses-into cutting smoothly reciting looking <br>
    this from never-separate-if<br>
</p>
<h4 class="stanza">32 - ༣༢།</h4>
<p class="tibetan">
    འཁོར་བའི་འཁྲུལ་སྣང་དུམ་བུ་དུམ་བུར་འགྲོ།། <br>
    །ནམ་ཞིག་བྱིན་བརྒྱུད་རྟོགས་པའི་གནད་འཕོས་ནས།། <br>
    །བརྗོད་དུ་མེད་པའི་ཡེ་ཤེས་ཁོང་ནས་སྐྱེ།། <br>
    །ཀུན་མཁྱེན་ཆོས་སྐུའི་བླ་མ་དངོས་ཞལ་མཇལ།། <br>
</p>
<p class="romanized">
    'khor ba'i 'khrul snang dum bu dum bur 'gro <br>
    nam zhig byin brgyud rtogs pa'i gnad 'phos nas <br>
    brjod du med pa'i ye shes khong nas skyе <br>
    kun mkhyen chos sku'i bla ma dngos zhal mjal<br>
</p>
<p class="literal">
    deluded saṃsāra appearances pieces-to scattering <br>
    blessing-lineage realization-point transferring-when <br>
    inexpressible pristine-awareness within arising <br>
    all-knowing dharma-body Lama face-to-face meeting<br>
</p>
<h4 class="stanza">33 - ༣༣།</h4>
<p class="tibetan">
    གཞི་བདེའི་སྟེང་དུ་བློ་བདེ་རྒྱུན་ཆད་མེད།། <br>
    །གཞུང་འདི་མཇལ་ལས་ཉམས་ལེན་གཞན་མེད་དེ།། <br>
    །སྒོམ་དང་སྒྲུབ་པའི་སྙིང་པོ་དེ་ཉིད་ཡིན།། <br>
    །གཞུང་བཟང་འདི་དག་ཅི་ཙམ་མཇལ་བའི་ཡུན།། <br>
</p>
<p class="romanized">
    gzhi bde'i steng du blo bde rgyun chad med <br>
    gzhung 'di mjal las nyams len gzhan med de <br>
    sgom dang sgrub pa'i snying po de nyid yin <br>
    gzhung bzang 'di dag ci tsam mjal ba'i yun<br>
</p>
<p class="literal">
    mind ease ground-of ease-upon unbroken <br>
    scripture this seeing beyond other practice not <br>
    this itself meditation accomplishment essence <br>
    however-long scriptures these with spending-for<br>
</p>
<h4 class="stanza">34 - ༣༤།</h4>
<p class="tibetan">
    དེ་སྲིད་ཆོས་སྐུའི་དགོངས་པ་ངང་གིས་སྐྱེ།། <br>
    །དེ་སླད་རྩོལ་བློའི་བློ་ཚུབ་མ་མང་བར།། <br>
    །བག་ཡངས་ངང་ནས་གཟུང་བཟང་འདི་དག་གཟིགས།། <br>
    །བརྗོད་བྱའི་དོན་ཟབ་རྒྱང་ན་ཅང་མེད་ཀྱི།། <br>
</p>
<p class="romanized">
    de srid chos sku'i dgongs pa ngang gis skyе <br>
    de slad rtsol blo'i blo tshub ma mang bar <br>
    bag yangs ngang nas gzung bzang 'di dag gzigs <br>
    brjod bya'i don zab rgyang na cang med kyi<br>
</p>
<p class="literal">
    that-long dharma-body intention naturally-by arising <br>
    that-reason striving-mind agitation not-multiplying <br>
    spacious-relaxed naturally-from excellent-holds these beholding <br>
    expressed-object meaning profound distance-in not-at-all<br>
</p>
<h4 class="stanza">35 - ༣༥།</h4>
<p class="tibetan">
    བློ་ཐག་ཆོད་ལ་རང་བབ་ང་ལ་ཞོག། <br>
    །རྟོགས་པར་དཀའ་བ་རྟོག་གེའུ་བསྟན་བཅོས་བཞིན།། <br>
    །བསྒྲིམས་ཤིང་བསྒྲིགས་ནས་ཚིག་དོན་ཚོལ་མི་དགོས།། <br>
    །རང་བབ་ངང་ལ་གཞུང་སེམས་སྲེས་ཤིག་དང་།། <br>
</p>
<p class="romanized">
    blo thag chod la rang bab nga la zhog <br>
    rtogs par dka' ba rtog ge'u bstan bcos bzhin <br>
    bsgrims shing bsgrigs nas tshig don tshol mi dgos <br>
    rang bab ngang la gzhung sems sres shig dang<br>
</p>
<p class="literal">
    mind thread cutting self-settling enough for-me <br>
    logical treatises like difficult-to-realize <br>
    construct not-need arrange not-need word-meaning seeking-not <br>
    self-settling naturally scripture mind merging<br>
</p>
<h4 class="stanza">36 - ༣༦།</h4>
<p class="tibetan">
    གུ་ཡངས་རྗེན་པ་ཟང་མ་ཐལ་གྱིས་འགྲོ།། <br>
    །ངོ་སྤྲོད་དེ་ཡིན་གཉུག་མའི་ཡེ་ཤེས་དེ།། <br>
    །ཀུན་མཁྱེན་བླ་མའི་གདམས་ངག་དེར་རང་ཡིན།། <br>
    །བརྗོད་བྱ་དེ་ཡིན་དབང་བསྐུར་དངོས་ཀྱང་དེ།། <br>
</p>
<p class="romanized">
    gu yangs rjen pa zang ma thal gyis 'gro <br>
    ngo sprod de yin gnyug ma'i ye shes de <br>
    kun mkhyen bla ma'i gdams ngag der rang yin <br>
    brjod bya de yin dbang bskur dngos kyang de<br>
</p>
<p class="literal">
    spacious expanse through barely-moving nakedly <br>
    this itself introduction pristine-awareness never-established pure-or-impure <br>
    all-knowing Lama pith-instruction yourself <br>
    this expressed-object actual empowerment itself<br>
</p>
<h4 class="stanza">37 - ༣༧།</h4>
<p class="tibetan">
    སྙིང་པོའི་ཉམས་ལེན་དེ་ག་རང་གིས་ཆོག། <br>
    །ངེས་ཚིག་ཚིག་དོན་ཁྲོལ་རུང་མ་ཁྲོལ་རུང་།། <br>
    །བརྗོད་བྱའི་དོན་ཟབ་ཤེས་རུང་མ་ཤེས་རུང་།། <br>
    །དགོངས་པའི་ཞེ་ཕུག་རྙེད་རུང་མ་རྙེད་རུང་།། <br>
</p>
<p class="romanized">
    snying po'i nyams len de ga rang gis chog <br>
    nges tshig tshig don khrol rung ma khrol rung <br>
    brjod bya'i don zab shes rung ma shes rung <br>
    dgongs pa'i zhe phug rnyed rung ma rnyed rung<br>
</p>
<p class="literal">
    essence practice who beyond-self needs <br>
    certain words piercing-or whole-leaving either-way <br>
    profound meaning knowing-or unknowing remaining <br>
    intention core obtaining-or empty-handed wandering<br>
</p>
<h4 class="stanza">38 - ༣༨།</h4>
<p class="tibetan">
    རེ་དོགས་ཆོད་ལ་མ་ཡེངས་ངང་ནས་གཟིགས།། <br>
    །ཡང་ལྟོས་ཡང་ལྟོས་ཉམས་དང་བསྲེས་ལ་ལྟོས།། <br>
    །གཞུང་དང་སེམས་སྲེས་སེམས་ལ་གཞུང་རྒྱས་ཐོབ།། <br>
    །དབྱེར་མེད་ངང་ནས་ཉམས་དགའ་གདངས་སུ་གྱེར།། <br>
</p>
<p class="romanized">
    re dogs chod la ma yengs ngang nas gzigs <br>
    yang ltos yang ltos nyams dang bsres la ltos <br>
    gzhung dang sems sres sems la gzhung rgyas thob <br>
    dbyer med ngang nas nyams dga' gdangs su gyer<br>
</p>
<p class="literal">
    doubt cutting look distraction-without naturally <br>
    again-looking experience-with mixing look <br>
    scripture mind merging mind scripture expansion obtaining <br>
    inseparability from joyful-resonance singing<br>
</p>
<h4 class="stanza">39 - ༣༩།</h4>
<p class="tibetan">
    མོས་གུས་རྩལ་འབར་རྟོགས་པའི་ཡེ་ཤེས་སྐྱེ།། <br>
    །ཀྱེ་ལགས་སྙིང་པོའི་སྙིང་པོ་འདི་ཡིན་ཏེ།། <br>
    །ཟབ་པའི་ཡང་ཟབ་འདི་འདྲ་གཞན་ན་མེད།། <br>
    །བྱིན་རླབས་མཛོད་ཡིན་སྙིང་པོའི་བསྟན་པ་ཡིན།། <br>
</p>
<p class="romanized">
    mos gus rtsal 'bar rtogs pa'i ye shes skyе <br>
    kye lags snying po'i snying po 'di yin te <br>
    zab pa'i yang zab 'di 'dra gzhan na med <br>
    byin rlabs mdzod yin snying po'i bstan pa yin<br>
</p>
<p class="literal">
    devotion power blazing realization pristine-awareness arising <br>
    alas essence-of-essence itself <br>
    profound beyond-profound nowhere-else like-this <br>
    blessing treasury essence teaching-itself<br>
</p>
<h4 class="stanza">40 - ༤༠།</h4>
<p class="tibetan">
    སྟོན་པ་དངོས་ཡིན་སངས་རྒྱས་ལག་བཅངས་ཡིན།། <br>
    །འདི་འདྲའི་ཡོན་ཏན་བསྐལ་པར་བརྗོད་ན་ཡང་།། <br>
    །བློ་ཆུང་བདག་གི་བློ་གྲོས་མི་འཛད་ན།། <br>
    །བློ་ཆེན་གཞན་གྱི་སྤོབས་པ་ལྟ་ཅི་སྟེ།། <br>
</p>
<p class="romanized">
    ston pa dngos yin sangs rgyas lag bchangs yin <br>
    'di 'dra'i yon tan bskal par brjod na yang <br>
    blo chung bdag gi blo gros mi 'dzad na <br>
    blo chen gzhan gyi spobs pa lta ci ste<br>
</p>
<p class="literal">
    teacher actual Buddha hand-in held <br>
    eons describing qualities like-this <br>
    my small mind intelligence not-exhausting <br>
    other great minds confidence what-of<br>
</p>
<h4 class="stanza">41 - ༤༡།</h4>
<p class="tibetan">
    འཕགས་པ་དགྱེས་པའི་ལམ་བཟང་འདི་འདྲ་མེད།། <br>
    །ཀྱེ་ལགས་འདི་འདྲའི་ནོར་བུ་རིན་པོ་ཆེ།། <br>
    །རང་དབང་མཇལ་བའི་སྐལ་བཟང་རྙེད་དུས་འདིར།། <br>
    །སྲིད་ན་གནས་ཀྱང་ཧ་ཅང་མི་སྐྱོ་སྟེ།། <br>
</p>
<p class="romanized">
    'phags pa dgyes pa'i lam bzang 'di 'dra med <br>
    kye lags 'di 'dra'i nor bu rin po che <br>
    rang dbang mjal ba'i skal bzang rnyed dus 'dir <br>
    srid na gnas kyang ha cang mi skyo ste<br>
</p>
<p class="literal">
    path like-this not noble-ones joy-bringing <br>
    alas jewel precious like-this <br>
    self-power through good-fortune obtaining now <br>
    existence in abiding-even weariness not<br>
</p>
<h4 class="stanza">42 - ༤༢།</h4>
<p class="tibetan">
    མོས་གུས་བསྐྱེད་ནས་གུ་ཡངས་ཅིས་མི་ཆོག། <br>
    །སྙིང་གི་གྲོགས་ཁྱེད་གཞུང་འདིར་བློ་ཕོབ་ལ།། <br>
    །བག་ཡངས་ངང་ནས་བློ་ཐག་འདི་རུ་ཆོད།། <br>
    །བྱ་བྱེད་རྩོལ་བློའི་བློ་ཚུབ་འདི་རུ་ཤིག། <br>
</p>
<p class="romanized">
    mos gus bskyed nas gu yangs cis mi chog <br>
    snying gi grogs khyed gzhung 'dir blo phob la <br>
    bag yangs ngang nas blo thag 'di ru chod <br>
    bya byed rtsol blo'i blo tshub 'di ru shig<br>
</p>
<p class="literal">
    devotion generated-having spacious-expanse entering why-not <br>
    heart-companion your mind this scripture into casting <br>
    spacious-relaxedness from mind thread cutting right-here <br>
    doer deed striving-mind agitation here pacifying<br>
</p>
<h4 class="stanza">43 - ༤༣།</h4>
<p class="tibetan">
    གཞུང་མང་གདམས་པའི་སྤྲོས་པ་འདི་རུ་ཆོད།། <br>
    །སྙན་སྙན་གཞུང་ལུགས་མང་པོས་ཅི་ཞིག་བྱ།། <br>
    །ཟབ་ཟབ་མན་ངག་མང་པོས་ཅི་ཞིག་བྱ།། <br>
    །སྤྲོས་སྤྲོས་ཉམས་ལེན་མང་པོས་ཅི་ཞིག་བྱ།། <br>
</p>
<p class="romanized">
    gzhung mang gdams pa'i spros pa 'di ru chod <br>
    snyan snyan gzhung lugs mang pos ci zhig bya <br>
    zab zab man ngag mang pos ci zhig bya <br>
    spros spros nyams len mang pos ci zhig bya<br>
</p>
<p class="literal">
    scriptures many instructions-many elaboration this in cutting <br>
    pleasant-sounding systems many what-use <br>
    profoundly profound instructions many what-use <br>
    elaborated practices many what-use<br>
</p>
<h4 class="stanza">44 - ༤༤།</h4>
<p class="tibetan">
    ཡིན་ཡིན་ཁ་བཤད་མང་པོས་ཅི་ཞིག་བྱ།། <br>
    །བག་ཡངས་བསམ་གཏན་ཉལ་ཆོས་འདི་རང་ཡིན།། <br>
    །བློ་བདེ་གུ་ཡངས་རང་གྲལ་འདི་རང་ཡིན།། <br>
    །གཞུང་བཟང་གཅིག་ཤེས་ཀུན་གྲོལ་འདི་རང་ཡིན།། <br>
</p>
<p class="romanized">
    yin yin kha bshad mang pos ci zhig bya <br>
    bag yangs bsam gtan nyal chos 'di rang yin <br>
    blo bde gu yangs rang gral 'di rang yin <br>
    gzhung bzang gcig shes kun grol 'di rang yin<br>
</p>
<p class="literal">
    explanations many affirming yes-yes what-use <br>
    spacious relaxed samādhi this sleeping-dharma yourself <br>
    mind ease spacious-expanse in this self-throne yourself <br>
    single excellent scripture knowing this all-liberation yourself<br>
</p>
<h4 class="stanza">45 - ༤༥།</h4>
<p class="tibetan">
    མན་ངག་ཆུ་བརྒྱ་ཟམ་གཅིག་འདི་རང་ཡིན།། <br>
    །རང་ལ་བཞག་ནས་གཞན་ལ་མ་ཚོལ་ཀྱེ།། <br>
    །སྙིང་པོ་དོར་ནས་ཤུན་པ་མ་བསྡུ་ཀྱེ།། <br>
    །རྩོལ་མེད་བོར་ནས་བརྩོན་པས་མ་བསྒྲུབ་ཀྱེ།། <br>
</p>
<p class="romanized">
    man ngag chu brgya zam gcig 'di rang yin <br>
    rang la bzhag nas gzhan la ma tshol kye <br>
    snying po dor nas shun pa ma bsdus kye <br>
    rtsol med bor nas brtson pas ma bsgrubs kye<br>
</p>
<p class="literal">
    hundred pith-instructions this single bridge yourself <br>
    yourself within placing-having elsewhere not-seeking <br>
    essence discarding straw gathering not <br>
    effortlessness abandoning diligence-through accomplishing not<br>
</p>
<h4 class="stanza">46 - ༤༦།</h4>
<p class="tibetan">
    བྱར་མེད་བསྐྱུར་ནས་བྱ་བྱེད་མ་མང་ཀྱེ།། <br>
    །ཀུན་མཁྱེན་བླ་མའི་བརྒྱུད་དུ་སྐྱེས་ཙམ་ནས།། <br>
    །གཟུང་བཟང་འདི་འདྲ་མེས་པོའི་ཕ་ཕོག་ཡིན།། <br>
    །ལམ་བཟང་འདི་འདྲ་ཕ་མེས་བཞག་པ་ཡིན།། <br>
</p>
<p class="romanized">
    byar med bskyur nas bya byed ma mang kye <br>
    kun mkhyen bla ma'i brgyud du skyes tsam nas <br>
    gzung bzang 'di 'dra mes po'i pha phog yin <br>
    lam bzang 'di 'dra pha mes bzhag pa yin<br>
</p>
<p class="literal">
    doerless sending-forth action multiplying not <br>
    merely all-knowing Lama lineage in born <br>
    holds like-this ancestors hands reaching <br>
    paths like-this forefathers by placed<br>
</p>
<h4 class="stanza">47 - ༤༧།</h4>
<p class="tibetan">
    བག་ཞིག་ཕབ་ན་འདི་རུ་ལོས་ཀྱང་ཕབ།། <br>
    །ཀྱེ་མ་ཀྱེ་མ་བརྒྱུད་གསུམ་ཐུགས་རྗེ་ཆེ།། <br>
    །གཞུང་བཟང་མཇལ་དུ་ཡོད་པ་སྐལ་བ་བཟང་།། <br>
    །ལམ་བཟང་བསྒྲུབ་ཏུ་ཡོད་པ་ཁ་རྗེ་ཆེ།། <br>
</p>
<p class="romanized">
    bag zhig phab na 'di ru los kyang phab <br>
    kye ma kye ma brgyud gsum thugs rje che <br>
    gzhung bzang mjal du yod pa skal ba bzang <br>
    lam bzang bsgrub tu yod pa kha rje che<br>
</p>
<p class="literal">
    heedless descending even-here descend <br>
    alas mother alas mother three lineages great-compassion <br>
    excellent scripture seeing fortune exists <br>
    excellent path accomplishing great-treasure exists<br>
</p>
<h4 class="stanza">48 - ༤༨།</h4>
<p class="tibetan">
    སངས་རྒྱས་རང་ལ་ཡོད་པ་ལོས་ཀྱང་བདེན།། <br>
    །དེ་སླད་རྒྱལ་བ་དགྱེས་པའི་ལམ་བཟང་འདིར།། <br>
    །སྙིང་གི་གྲོགས་ཁྱེད་བློ་དང་ཆོས་སུ་སྲེས།། <br>
    །སྙིང་གཏམ་ལགས་ཀྱིས་སྙིང་གི་དབུས་སུ་སྟིམས།། <br>
</p>
<p class="romanized">
    sangs rgyas rang la yod pa los kyang bden <br>
    de slad rgyal ba dgyes pa'i lam bzang 'dir <br>
    snying gi grogs khyed blo dang chos su sres <br>
    snying gtam lags kyis snying gi dbus su stims<br>
</p>
<p class="literal">
    Buddha within-yourself true even-for you <br>
    therefore excellent path Victor-delighting <br>
    heart-companion mind dharma merging <br>
    heart-speech heart-center into absorbing<br>
</p>
<h4 class="stanza">49 - ༤༩།</h4>
<p class="tibetan">
    སྙིང་ལ་བཅངས་ན་སྙིང་པོ་ཡིན་ཀྱང་སྲིད།། <br>
    །བག་མེད་མདོ་སྟོར་ཨ་བུ་ཧྲལ་པོ་བདག། <br>
    །རང་ལ་མེད་པའི་ཁ་ཆོས་འཆད་པ་ལ།། <br>
    །སྤྲོ་བ་མེད་ཀྱང་ཀུན་མཁྱེན་བརྒྱུད་པའི་གཞུང་།། <br>
</p>
<p class="romanized">
    snying la bcangs na snying po yin kyang srid <br>
    bag med mdo stor a bu hral po bdag <br>
    rang la med pa'i kha chos 'chad pa la <br>
    spro ba med kyang kun mkhyen brgyud pa'i gzhung<br>
</p>
<p class="literal">
    heart in placed-it essence even-so is <br>
    heedless sūtra-keeper I Abu-Dhraho <br>
    oral-dharma within-myself not explaining <br>
    joy-without yet all-knowing lineage scripture<br>
</p>
<h4 class="stanza">50 - ༥༠།</h4>
<p class="tibetan">
    ཡིད་ཆེས་ཐོབ་པ་ཉམས་མྱོང་ཉག་གཅིག་ཡིན།། <br>
    །དུག་ལྔ་མེ་འབར་རྣམ་གཡེང་ཁོལ་པོར་འཕྱན།། <br>
    །འཁྲུལ་སྣང་བཟློག་དཀའ་ལས་ངན་བདག་འདྲ་ཡང་།། <br>
    །གཞུང་བཟང་འདི་འདྲ་ཐོས་དང་མཇལ་བའི་ཚེ།། <br>
</p>
<p class="romanized">
    yid ches thob pa nyams myong nyag gcig yin <br>
    dug lnga me 'bar rnam g.yeng khol por 'phyen <br>
    'khrul snang bzlog dka' las ngan bdag 'dra yang <br>
    gzhung bzang 'di 'dra thos dang mjal ba'i tshe<br>
</p>
<p class="literal">
    faith obtained unique experience <br>
    five poisons blazing fire-as distraction turmoil-to <br>
    delusion reversing difficult-for whom I-resemble <br>
    scriptures like-this hearing-seeing when<br>
</p>
<h4 class="stanza">51 - ༥༡།</h4>
<p class="tibetan">
    སྲིད་པའི་སྣང་ཤས་ཁྲལ་མ་ཁྲོལ་དུ་འགྲོ།། <br>
    །དེས་ན་བློ་བརྟན་དུག་ལྔའི་རྟོག་པ་ཆུང་།། <br>
    །སྐལ་བཟང་དམ་གཙང་ཁྱེད་དང་ཁྱེད་འདྲ་བས།། <br>
    །གཞུང་འདི་མཇལ་ན་བྱིན་བརྒྱུད་ཡེ་ཤེས་མཆོག། <br>
</p>
<p class="romanized">
    srid pa'i snang shas khral ma khrol du 'gro <br>
    des na blo brtan dug lnga'i rtog pa chung <br>
    skal bzang dam gtsang khyed dang khyed 'dra bas <br>
    gzhung 'di mjal na byin brgyud ye shes mchog<br>
</p>
<p class="literal">
    existence partial-appearances going unravel-or-not <br>
    therefore mind stable five-poisons conceptions small <br>
    you good-fortune samaya-keeper and those-like-you <br>
    scripture this seeing supreme pristine-awareness blessing<br>
</p>
<h4 class="stanza">52 - ༥༢།</h4>
<p class="tibetan">
    ཐོབ་པར་ངེས་ཀྱི་ངེས་ཤེས་ཡང་ཡང་སྐྱེད།། <br>
    །ཀུན་མཁྱེན་བླ་མ་རྫོགས་པའི་སངས་རྒྱས་དེའི།། <br>
    །བྱིན་རླབས་འོད་སྣང་གང་ལ་རེག་གྱུར་པ།། <br>
    །རྟོགས་གྲོལ་དུས་མཉམ་མངོན་སུམ་ཚད་མ་སྟེ།། <br>
</p>
<p class="romanized">
    thob par nges kyi nges shes yang yang skyed <br>
    kun mkhyen bla ma rdzogs pa'i sangs rgyas de'i <br>
    byin rlabs 'od snang gang la reg gyur pa <br>
    rtogs grol dus mnyam mngon sum tshad ma ste<br>
</p>
<p class="literal">
    again certainty certain-attainment generating <br>
    all-knowing Lama that perfect-Buddha <br>
    blessing radiance wherever touching <br>
    recognition pristine-awareness liberation simultaneous direct-measure<br>
</p>
<h4 class="stanza">53 - ༥༣།</h4>
<p class="tibetan">
    གྲུབ་བརྒྱའི་སྤྱི་མེས་ཀུན་མཁྱེན་བླ་མ་ཡིན།། <br>
    །རྟོགས་པའི་དབང་ཕྱུག་ལྷ་བཙུན་ཆེན་པོ་དང་།། <br>
    །དགོངས་པའི་ཀློང་བརྡོལ་རིག་འཛིན་འཇིགས་མེད་གླིང་།། <br>
    །བསྟན་པའི་མངའ་བདག་གཏེར་ཆེན་བླ་མ་སོགས།། <br>
</p>
<p class="romanized">
    grub brgya'i spyi mes kun mkhyen bla ma yin <br>
    rtogs pa'i dbang phyug lha btsun chen po dang <br>
    dgongs pa'i klong brdol rig 'dzin 'jigs med gling <br>
    bstan pa'i mnga' bdag gter chen bla ma sogs<br>
</p>
<p class="literal">
    hundred accomplished common-ancestor all-knowing Lama <br>
    realization lord great deity-venerable <br>
    expanse-transcendent awareness-holder Jigme-Lingpa <br>
    teachings owner great-treasure Lama and others<br>
</p>
<h4 class="stanza">54 - ༥༤།</h4>
<p class="tibetan">
    ཀུན་མཁྱེན་གཞུང་ལས་བྱིན་བརྒྱུད་ཐོབ་པ་ཡིན།། <br>
    །དེ་ཚུལ་དགོངས་མཛོད་སྙིང་གི་གྲོགས་པོ་ཁྱེད།། <br>
    །དེ་དང་འདྲ་བར་ཀུན་མཁྱེན་ལེགས་བཤད་མཆོག། <br>
    །དེ་ཚུལ་མཐོང་ནས་དོན་བརྒྱད་ཡེ་ཤེས་ཐོབ།། <br>
</p>
<p class="romanized">
    kun mkhyen gzhung las byin brgyud thob pa yin <br>
    de tshul dgongs mdzod snying gi grogs po khyed <br>
    de dang 'dra bar kun mkhyen legs bshad mchog <br>
    de tshul mthong nas don brgyad ye shes thob<br>
</p>
<p class="literal">
    all-knowing scripture-from blessing-lineage obtaining <br>
    heart-companion you that intention treasury holding <br>
    similarly supreme all-knowing excellent-speech <br>
    that manner seeing eightfold-meaning pristine-awareness obtaining<br>
</p>
<h4 class="stanza">Colophon - ༄༅།།</h4>
<p class="tibetan">
    དེ་བཞིན་ཉིད་དབྱིངས་དགོངས་ཀློང་གྲོལ་གྱུར་ཅིག། <br>
    དཔལ་སྤྲུལ་གསུང་།། <br>
    སརྦ་མངྒ་ལཾ།། <br>
</p>
<p class="romanized">
    de bzhin nyid dbyings dgongs klong grol gyur cig <br>
    dpal sprul gsung <br>
    sarba mangga lam<br>
</p>
<p class="literal">
    suchness-expanse intention-expanse liberation becoming <br>
    Paltrül by spoken <br>
    sarva maṅgalaṃ<br>
</p>
