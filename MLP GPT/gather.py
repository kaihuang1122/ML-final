#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
import threading
import multiprocessing as mp

# arguments: <test_set> <MMDD-MMDD(for fitting)> <MMDD-MMDD(for validate)> <epoch times>

def exe(x, y, z, w, vary):
    os.system(f"python3 given_err.py {x[:-1]} {y} {z} {w} 1>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/log/{vary}/{x[:-1]}.out 2>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/output/{vary}/{x[:-1]}.csv")
    #os.system(f"python3 calculate.py")

thrs = []

#for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
for x in tqdm(["500119051 ", "500119075 "]):
    thrs.append(threading.Thread(target=exe(x, "hours/1002-1202", "hours/1021-1025[predict]", "200", "predict")))
    #thrs.append(mp.Process(target=exe, args=(x, "1002-1121", "1028-1029", "20", "predict")))
    
for i in thrs:
    i.start()

for i in thrs:
    i.join()

# python3 given_err.py 500101001 "1002-1127" "1021-1025[predict]" "50" 1>log/predict/500101001.out