# The WebNLG Challenge 2020: Evalutation Script

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