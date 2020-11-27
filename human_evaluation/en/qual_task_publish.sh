#!/bin/sh

while true
do
    echo "publish qual"

    python publish_qual_hits.py --hit_properties_file ./hit_properties/qualification_hit_properties.json\
    --html_template ./hit_properties/qualification_page.html --input_json_file ./inputs/hit_inputs_id_qual.json\
    --hit_ids_file ./inputs/hit_ids_id_qual.txt --prod

done
