#!/bin/bash

output_file="samples.csv"
echo "sample_name,illumina_fwd,illumina_rev" > "$output_file"

for r1_file in /path/to/samples/season*_part*_fastp/*fastp/*_R1_fastp.fq.gz; do
    sample_name=$(basename "$(dirname "$r1_file")")
    r2_file="${r1_file/_R1_/_R2_}"
    if [ -f "$r1_file" ] && [ -f "$r2_file" ]; then
        echo "$sample_name,$r1_file,$r2_file" >> "$output_file"
    fi
done
