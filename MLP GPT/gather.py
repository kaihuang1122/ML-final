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

def exe(x, y, z, w, u, vary):
    os.system(f"python3 given_err.py {x[:-1]} {y} {z} {w} {u} 1>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/log/{vary}/{x[:-1]}.out 2>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/output/{vary}/{x[:-1]}.csv")
    #os.system(f"python3 given_err.py 500119051 hours/1002-1202 hours/1202-1209 0 64")
result = []
fh = open("epoch\ count.csv", "w")

for units in range(1, 2):
    if os.fork() == 0:
        for epoch in range(1, 11):
            thrs = []
            for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
            #for x in tqdm(["500119051 ", "500119075 "]):
                thrs.append(threading.Thread(target=exe(x, "hours/1002-1202", "hours/1202-1209", str(epoch), str(units), "predict")))
                
                break

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

                break
            print(np.mean(out))
            result += out

        li = [1]*1 #+ [2]*112 + [3]*112 + [4]*112 + [5]*112 + [6]*112 + [7]*112 + [8]*112 + [9]*112 + [10]*112
        for i in range(100):
            li += [i]*112

        plt.scatter(li,result)
        plt.savefig(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/graph/units_{units}.png")


# plt.show()

# python3 given_err.py 500101001 "hours/1002-1128" "hours/total[predict]" "1" 1>log/predict/500101001.out