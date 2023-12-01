from tqdm import tqdm
import csv
import json
import numpy as np

for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    fd = open(f"/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/release/20231020/{x[:-1]}.json")
    data = dict(json.load(fd))
    out = ([[data[i] for i in data.keys()]])
    print(out)
    