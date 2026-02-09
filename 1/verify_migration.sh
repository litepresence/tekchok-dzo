#!/bin/bash
# Verify migration success

set -euo pipefail

BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"

verify_volume() {
    local volume=$1
    local errors=0
    
    echo "=== Verifying Volume $volume ==="
    
    for layer in tibetan wylie literal liturgical commentary scholar epistemic delusion cognitive; do
        local layer_dir="$BASE_DIR/volume_$volume/$layer"
        cd "$layer_dir" 2>/dev/null || continue
        
        local old_format=$(ls PAGE\ *.txt 2>/dev/null | wc -l)
        local new_format=$(ls PAGE_*.txt 2>/dev/null | wc -l)
        
        if [ $old_format -gt 0 ]; then
            echo "WARNING: $layer has $old_format old format files"
            errors=$((errors + old_format))
        fi
        
        echo "  $layer: $new_format files OK"
    done
    
    return $errors
}

echo "=== MIGRATION VERIFICATION ==="
verify_volume 1
verify_volume 2
