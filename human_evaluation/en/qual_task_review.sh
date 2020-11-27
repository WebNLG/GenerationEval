#!/bin/sh

count=0

while (( count < 100000 ));
    do

    sleep 10

    echo 'results'

    python get_results_qual.py --hit_ids_file ./inputs/hit_ids_id_qual.txt --output_file ./outputs/hit_out_id_qual.json --prod

    echo 'qual'

    python qual_distribute.py

    echo 'notify'

    python qual_assign.py --hit_ids_file ./inputs/hit_ids_id_qual.txt --prod

    (( count++ ))
    done
