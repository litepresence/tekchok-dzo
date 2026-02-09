#!/bin/bash
# Create directory structure for partitioned content
# Phase 1 of migration

set -e

echo "Creating partitioned directory structure..."
echo "=============================================="

# Layers to create
LAYERS=("tibetan" "wylie" "literal" "liturgical" "commentary" "scholar" "epistemic" "delusion" "cognitive")

# Volume 1 chapters (1-13)
V1_CHAPTERS=(
    "01:1:1"
    "02:6:A,B,C,D,E,F"
    "03:4:A,B,C,D"
    "04:6:A-i,A-ii,B,C-i,C-ii,C-iii"
    "05:4:A,B,C-i,C-ii"
    "06:4:A,B,C,D"
    "07:5:A,B-i,B-ii,B-iii,B-iv"
    "08:4:A,B,C,D"
    "09:3:A,B,C"
    "10:3:A,B,C"
    "11:6:A-i,A-ii,A-iii,B,C,D"
    "12:4:A,B,C,D"
    "13:3:A,B,C"
)

# Volume 2 chapters (14-19)
V2_CHAPTERS=(
    "14:8:A-i,A-ii,B-i,B-ii,B-iii,C-i,C-ii,C-iii"
    "15:8:A-i,A-ii,A-iii,B-i,B-ii,B-iii,C-i,C-ii"
    "16:3:A,B-i,B-ii"
    "17:4:A,B,C,D"
    "18:4:A-i,A-ii,B,C"
    "19:7:A,B-i,B-ii,B-iii,C,D,E"
)

create_chapter_structure() {
    local volume=$1
    local chapter_info=$2
    local layer=$3
    
    IFS=':' read -r ch_num ch_count ch_sections <<< "$chapter_info"
    
    ch_dir="partitioned_${volume}/${layer}/chapter_${ch_num}"
    mkdir -p "$ch_dir"
    
    # Create section files
    IFS=',' read -ra sections <<< "$ch_sections"
    for section in "${sections[@]}"; do
        touch "${ch_dir}/section_${section}.txt"
    done
    
    echo "  ${layer}/chapter_${ch_num}/ - ${#sections[@]} sections"
}

# Create partitioned_v1
echo ""
echo "Volume 1 (partitioned_v1):"
echo "--------------------------"
for layer in "${LAYERS[@]}"; do
    echo "Creating ${layer}/..."
    for chapter in "${V1_CHAPTERS[@]}"; do
        create_chapter_structure "v1" "$chapter" "$layer"
    done
done

# Create partitioned_v2
echo ""
echo "Volume 2 (partitioned_v2):"
echo "--------------------------"
for layer in "${LAYERS[@]}"; do
    echo "Creating ${layer}/..."
    for chapter in "${V2_CHAPTERS[@]}"; do
        create_chapter_structure "v2" "$chapter" "$layer"
    done
done

echo ""
echo "=============================================="
echo "✓ Directory structure created successfully!"
echo ""
echo "Next step: Run ./02_extract_content.py"
