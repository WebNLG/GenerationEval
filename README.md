# WebNLG Challenge 2020: Evaluation Script for RDF-to-Text

This script evaluates RDF-to-text generation for the [WebNLG Challenge 2020](https://webnlg-challenge.loria.fr/challenge_2020/). Generation is evaluated with automatic metrics: BLEU, METEOR, chrF++, TER, BERTScore, and BLEURT (for English only).


## Dependencies

If you are running this script in Linux, just execute the following command:

```
./install_dependencies.sh
```

Otherwise, follow the following two steps:

1. Download [METEOR](https://www.cs.cmu.edu/~alavie/METEOR/download/meteor-1.5.tar.gz), extract it and place it on the `metrics` folder
2. Run `pip install -r requirements.txt` to install the python dependencies

Moreover, make sure to have `perl` and `java` installed globally in your machine. 

## Usage

To evaluate the performance of your model, run the `eval.py` script which receives as input the following parameters:

```
usage: eval.py [-h] -R REFERENCE -H HYPOTHESIS [-lng LANGUAGE] [-nr NUM_REFS]
               [-m METRICS] [-nc NCORDER] [-nw NWORDER] [-b BETA]

optional arguments:
  -h, --help            show this help message and exit
  -R REFERENCE, --reference REFERENCE
                        reference translation
  -H HYPOTHESIS, --hypothesis HYPOTHESIS
                        hypothesis translation
  -lng LANGUAGE, --language LANGUAGE
                        evaluated language
  -nr NUM_REFS, --num_refs NUM_REFS
                        number of references
  -m METRICS, --metrics METRICS
                        evaluation metrics to be computed
  -nc NCORDER, --ncorder NCORDER
                        chrF metric: character n-gram order (default=6)
  -nw NWORDER, --nworder NWORDER
                        chrF metric: word n-gram order (default=2)
  -b BETA, --beta BETA  chrF metric: beta parameter (default=2)
```

An example on how to run to the evaluation script is available in `example.sh`.

### Multiple References

In case of multiple references, they have to be stored in separated files and named reference0, reference1, reference2, etc.

Please have a look here: https://github.com/WebNLG/GenerationEval/tree/master/data/en/references

References for WebNLG can be generated using `generate_references.py` from this repo: https://gitlab.com/webnlg/corpus-reader

Example of the file format:

There are three instances `a-text`, `b-text`, `c-text` with 2, 3, and 1 reference respectively.
```python
a-text: {a-ref1, a-ref2}
b-text: {b-ref1, b-ref2, b-ref3}
c-text: {c-ref1}
```
Then you need to create 3 files: `reference0`, `reference1`, `reference2` with the following content.

reference0:
```
a-ref1
b-ref1
c-ref1
```
reference1 (the third line is empty):
```
a-ref2
b-ref2

```

reference2 (the first and third lines are empty):
```

b-ref3

```
