# Page Naming Convention

## Format
All page files now follow: **PAGE_XXX.txt** (underscore, zero-padded)

## Examples
- Page 1: `PAGE_001.txt`
- Page 10: `PAGE_010.txt` 
- Page 100: `PAGE_100.txt`
- Page 415: `PAGE_415.txt`
- Page 479: `PAGE_479.txt`

## Benefits
1. **Consistent pattern matching** - `PAGE_*.txt` matches all files
2. **Numerical sorting** - Files sort correctly in `ls`
3. **No quoting needed** - No spaces in filenames
4. **Scalable** - Works for 001-999

## Shell Commands
```bash
# List all pages in a layer
ls volume_1/literal/PAGE_*.txt

# Access specific page
cat volume_1/literal/PAGE_001.txt

# Iterate through pages
for i in {1..100}; do
    padded=$(printf "%03d" $i)
    cat "volume_1/literal/PAGE_${padded}.txt"
done
```

## Migration Complete
- **Date:** 2026-02-08
- **Files renamed:** 8,046
- **Format:** PAGE [number].txt → PAGE_XXX.txt
- **Status:** ✓ Complete and verified
