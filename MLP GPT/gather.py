#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
import threading
import multiprocessing as mp
import matplotlib.pyplot as plt

# arguments: <test_set> <MMDD-MMDD(for fitting)> <MMDD-MMDD(for validate)> <epoch times>

def exe(x, y, z, w, vary):
    os.system(f"python3 given_err.py {x[:-1]} {y} {z} {w} 1>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/log/{vary}/{x[:-1]}.out 2>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/output/{vary}/{x[:-1]}.csv")
    #os.system(f"python3 calculate.py")
result = []
fh = open("epoch\ count.csv", "w")

for epoch in [2]:
    thrs = []
    for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
    #for x in tqdm(["500119051 ", "500119075 "]):
        thrs.append(threading.Thread(target=exe(x, "hours/1002-1210", "hours/1021-1025[predict]", str(epoch), "predict")))
        #thrs.append(mp.Process(target=exe, args=(x, "1002-1121", "1028-1029", "20", "predict")))
    for i in thrs:
        i.start()
    for i in thrs:
        i.join()
    out = []
    # collect error
    for x in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
        fh = open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/log/predict/{x[:-1]}.out")
        table = fh.readlines()[-1].split(' ')[-1][:-1]
        out.append(np.float64(table))
    print(np.mean(out))
    result += out
    # csv.writer(fh).writerow([result[-1])

li = [0]*112 #+ [1]*112 + [2]*112 + [3]*112 + [4]*112
plt.scatter(li,result)
plt.show()

# python3 given_err.py 500101001 "hours/1002-1128" "hours/total[predict]" "1" 1>log/predict/500101001.out