#! \Library\Frameworks\Python.framework\Versions\3.11\bin\python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
import threading

# arguments: <test_set> <MMDD-MMDD(for fitting)> <MMDD-MMDD(for validate)> <epoch times>

def exe(x, y, z, w, vary):
    os.system(f"python3 given_err.py {x[:-1]} {y} {z} {w} 1>log\{vary}\{x[:-1]}.out 2>>output\{vary}\submission.csv")

thrs = []
for x in tqdm(open("G:\ML\ML-final\html.2023.final.data\sno_test_set.txt").readlines()):
    thrs.append(threading.Thread(target=exe(x, "1002-1027", "1021-1025[predict]", "200", "predict")))
    thrs[-1].start()

for i in thrs:
    i.join()



