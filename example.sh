# English
python3 eval.py -R data/en/references/reference -H data/en/hypothesis -nr 4 -m bleu,meteor,chrf++,ter,bert,bleurt
# Russian
python3 eval.py -R data/ru/reference -H data/ru/hypothesis -lng ru -nr 1 -m bleu,meteor,chrf++,ter,bert