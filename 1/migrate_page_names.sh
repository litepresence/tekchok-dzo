#!/bin/bash
# Page Name Migration Script
# Converts PAGE [number].txt to PAGE_001.txt format

set -euo pipefail

VOLUME=${1:-"all"}
BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
LOG_FILE="$BASE_DIR/migration_$(date +%Y%m%d_%H%M%S).log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

rename_files_in_layer() {
    local volume=$1
    local layer=$2
    local layer_dir="$BASE_DIR/volume_$volume/$layer"
    
    if [ ! -d "$layer_dir" ]; then
        log "ERROR: Directory not found: $layer_dir"
        return 1
    fi
    
    cd "$layer_dir"
    
    local count=0
    local errors=0
    
    for old_file in PAGE\ *.txt; do
        [ -e "$old_file" ] || continue
        
        local num=$(echo "$old_file" | sed 's/PAGE //; s/\.txt$//')
        local padded_num=$(printf "%03d" "$num")
        local new_file="PAGE_${padded_num}.txt"
        
        if mv "$old_file" "$new_file" 2>/dev/null; then
            ((count++))
        else
            ((errors++))
            log "ERROR: Failed to rename: $old_file"
        fi
    done
    
    log "COMPLETED: volume_$volume/$layer - $count files renamed, $errors errors"
    return $errors
}

main() {
    log "=== STARTING PAGE NAME MIGRATION ==="
    
    if [ "$VOLUME" = "all" ]; then
        volumes=(1 2)
    else
        volumes=($VOLUME)
    fi
    
    for vol in "${volumes[@]}"; do
        log "Processing Volume $vol..."
        for layer in tibetan wylie literal liturgical commentary scholar epistemic delusion cognitive; do
            rename_files_in_layer "$vol" "$layer" || true
        done
    done
    
    log "=== MIGRATION COMPLETE ==="
    log "Log file: $LOG_FILE"
}

main "$@"
