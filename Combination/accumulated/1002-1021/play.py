from tqdm import tqdm
import csv
import json
import numpy as np

num_dict = {}

for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    fd = open(f"/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/release/20231020/{x[:-1]}.json")
    data = dict(json.load(fd))
    out = [data[i] for i in data.keys()]
    out2 = []
    for i in list(out):
        if "sbi" in i:
            out2.append(i["sbi"])
    out = out2
    num_dict[x[:-1]] = np.mean(out)

fd = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/transportition/output.csv",'r')
sample = list(csv.reader(fd))
sample.pop(0)
fd = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/transportition/output2.csv",'w')
out_writer = csv.writer(fd)
out_writer.writerow(['id','sbi'])

for i in sample:
    tmp = []
    tmp.append(i[0])
    tmp.append(num_dict[i[0].split("_")[1]])
    out_writer.writerow(tmp)
