#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
out = []
for x in (open("G:/ML/ML-final/html.2023.final.data/sno_test_set.txt").readlines()):
    fh = open(f"G:/ML/ML-final/MLP GPT/log/given_err200/{x[:-1]}.out")
    table = fh.readlines()[-1].split(' ')[-1][:-1]
    out.append(np.float64(table))

print(np.mean(out))