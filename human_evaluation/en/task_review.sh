#!/bin/sh

count=0

while (( count < 100000 ));

    do

    echo 'results'

    python get_results.py --hit_ids_file ./inputs/hit_ids_id_SYSID.txt\
    --output_file ./outputs/hit_out_id_SYSID.json --prod

    echo 'qual'

    #python approve_hits.py --hit_ids_file ./01/inputs/hit_ids_4567_merged.txt --prod

    python hitcount_assign.py --hit_ids_file ./inputs/hit_ids_id_SYSID.txt\
    --submission_id SYSID --prod

    (( count++ ))
    done
