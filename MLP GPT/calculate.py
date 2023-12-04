#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
out = []
black = []
for x in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    fh = open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/log/predict/{x[:-1]}.out")
    table = fh.readlines()
    temp = ""
    for i in table:
        temp += i
    
    table = np.float64(temp.split('us/step - loss: ')[-1][0:6])
    if table > 1.5:
        black.append(x[:-1])
    out.append(np.float64(table))

print(black)
plt.hist(out, bins=25)
plt.show()