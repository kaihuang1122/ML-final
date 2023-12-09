import csv
from tqdm import tqdm
# with open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/submission.csv") as fh:
#     table = list(csv.reader(fh))
# fout = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/submit.csv", "w")
# writter = csv.writer(fout)
# writter.writerow(table[0])

# for i in range(112):#times 5761
#     for j in range(1, 5761, 20):
#         writter.writerow(table[i*5761+j])

# fout.close()

table = []
for x in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    table += list(open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/{x[:-1]}.csv").readlines())

newtable = []
for i in range(len(table)):
    if(i % 20 == 0):
        newtable.append(table[i])


fout = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/submit.csv", "w")
fout.write("id,sbi\n")
fout.writelines(newtable)

with open("/Users/kaihuang1122/Downloads/sample_submission.csv") as fh:
    table = list(csv.reader(fh))
writter = csv.writer(fout)
writter.writerows(table)

