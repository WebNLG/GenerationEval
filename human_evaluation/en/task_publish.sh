#!/bin/sh

while true
do
    echo "publish original"

    python publish.py --hit_properties_file ./hit_properties/task_hit_properties.json\
     --html_template ./hit_properties/task_page.html\
     --input_json_file ./inputs/hit_inputs_id_SYSID.json\
     --hit_ids_file ./inputs/hit_ids_id_SYSID.txt --prod

done
