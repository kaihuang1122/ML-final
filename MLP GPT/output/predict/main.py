import csv
with open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/submission.csv") as fh:
    table = list(csv.reader(fh))
fout = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/submit.csv", "w")
writter = csv.writer(fout)
writter.writerow(table[0])
for i in range(1, 5762, 20):
    writter.writerow(table[i])