__author__='thiagocastroferreira'

import json
import os
import eval

NUM_REFS = 5
lng = 'en'
metrics='bleu,meteor,ter,chrf++,bert,bleurt'

rdfs = json.load(open('data/human_evaluation/data_REF.json'))
results = json.load(open('data/human_evaluation/human_eval_result_sample_rdf2textEN.json'))

data = []
for result in results:
    for hit in result:
        hit_csv = {
            'hit_id': hit,
            'worker_id': [],
            'fluency': [],
            'relevance': [],
            'correctness': [],
            'text_structure': [],
            'data_coverage': []
        }
        for assign in result[hit]:
            hit_csv['assignment_id'] = assign['assignment_id']
            hit_csv['submission_id'] = assign['submission_id']
            hit_csv['triplet_size'] = assign['triplet_size']
            
            sample_id = assign['sample_id']
            hit_csv['sample_id'] = sample_id
            entry = [w for w in rdfs['entries'] if list(w.keys())[0] == sample_id][0]
            hit_csv['category'] = entry[sample_id]['category']
            hit_csv['type'] = entry[sample_id]['shape_type']
            hit_csv['lexicalisations'] = [w['lex'] for w in entry[sample_id]['lexicalisations']]
            
            hit_csv['worker_id'].append(assign['worker_id'])
            hit_csv['correctness'].append(assign['output']['Correctness'])
            hit_csv['data_coverage'].append(assign['output']['DataCoverage'])
            hit_csv['fluency'].append(assign['output']['Fluency'])
            hit_csv['relevance'].append(assign['output']['Relevance'])
            hit_csv['text_structure'].append(assign['output']['TextStructure'])
            
            
        hypothesis = 'The dog is the bar king'# TO DO: hit_csv['hypothesis']
        with open('hypothesis', 'w') as f:
            f.write(hypothesis)
        
        references = hit_csv['lexicalisations']
        if not os.path.exists('references'):
            os.mkdir('references')
        
        for j in range(NUM_REFS):
            with open('references/reference' + str(j), 'w') as f:
                if j < len(references):
                    f.write(references[j])
                else:
                    f.write('EMPTY')

        results = eval.run(refs_path='references/reference', hyps_path='hypothesis', num_refs=NUM_REFS, lng=lng, metrics=metrics)   