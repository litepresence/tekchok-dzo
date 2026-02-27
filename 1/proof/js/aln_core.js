const ALN = {
    map: null,
    sections: null,
    chapterMap: null,

    async init() {
        const resp = await fetch('ALN_map.json');
        this.map = await resp.json();
        this.sections = this._buildSections();
        this.chapterMap = this._buildChapterMap();
    },

    _buildSections() {
        const sections = [];
        for (const [key, range] of Object.entries(this.map)) {
            const parts = key.split('-');
            const volume = parseInt(parts[0]);
            const chapter = parseInt(parts[1]);
            sections.push({
                key: key,
                first: range[0],
                last: range[1],
                volume: volume,
                chapter: chapter
            });
        }
        sections.sort((a, b) => a.first - b.first);
        return sections;
    },

    _buildChapterMap() {
        const map = {};
        for (const section of this.sections) {
            const volChap = `${String(section.volume).padStart(2, '0')}-${String(section.chapter).padStart(2, '0')}`;
            if (!map[volChap] || section.first < map[volChap].startLine) {
                map[volChap] = {
                    volume: section.volume,
                    chapter: section.chapter,
                    startLine: section.first
                };
            }
        }
        return map;
    },

    getSection(aln) {
        if (!this.sections) return null;
        let lo = 0, hi = this.sections.length - 1;
        while (lo <= hi) {
            const mid = Math.floor((lo + hi) / 2);
            const sec = this.sections[mid];
            if (aln >= sec.first && aln <= sec.last) {
                return sec;
            } else if (aln < sec.first) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return this.sections[0];
    },

    getInfo(aln) {
        const section = this.getSection(aln);
        if (!section) return null;
        return {
            sectionKey: section.key,
            volume: section.volume,
            chapter: section.chapter,
            relativeLine: aln
        };
    },

    getChapterFromALN(aln) {
        const info = this.getInfo(aln);
        return info ? info.chapter : null;
    },

    getVolumeFromALN(aln) {
        if (!aln || aln <= 0) return 1;
        return aln <= 20426 ? 1 : 2;
    },

    getStartLineForChapter(volume, chapter) {
        const volChap = `${String(volume).padStart(2, '0')}-${String(chapter).padStart(2, '0')}`;
        return this.chapterMap[volChap] ? this.chapterMap[volChap].startLine : 1;
    },

    getSectionKeyFromIntroId(introId) {
        if (introId === 'intro-main') return '01-01-01-01';
        if (introId === 'vol-01') return '01-01-01-01';
        if (introId === 'vol-02') return '02-15-01-01';
        if (introId.startsWith('chap-')) {
            const parts = introId.replace('chap-', '').split('-');
            if (parts.length >= 2) {
                const vol = parts[0];
                const ch = parts[1];
                return `${vol}-${ch}-01-01`;
            }
        }
        return null;
    },

    getALNFromIntroId(introId) {
        const sectionKey = this.getSectionKeyFromIntroId(introId);
        if (sectionKey && this.map[sectionKey]) {
            return this.map[sectionKey][0];
        }
        return 1;
    }
};
