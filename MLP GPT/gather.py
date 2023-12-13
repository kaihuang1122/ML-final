#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import sys
import os
import numpy as np
from tqdm import tqdm
import threading
import matplotlib.pyplot as plt
from multiprocessing import Pool

# arguments: <test_set> <MMDD-MMDD(for fitting)> <MMDD-MMDD(for validate)> <epoch times>

def exe(x, y, z, w, u, vary):
    os.system(f"python3 given_err.py {x[:-1]} {y} {z} {w} {u} 1>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/log/{vary}/{x[:-1]}.out 2>/Users/kaihuang1122/Documents/ML/Final/MLP\ GPT/output/{vary}/{x[:-1]}.csv")
    #os.system(f"python3 given_err.py 500119051 hours/1002-1202 hours/1202-1209 0 64")


if __name__ == '__main__':
    for units in range(6, 11):
        #if os.fork() == 0:
        li = []
        result = []
        for epoch in range(1, 6):
            thrs = []
            #for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
                #exe(x, "hours/1002-1202", "hours/1202-1209", str(epoch), str(units), f"predict{units}")
            pbar = tqdm(total=112)
            upd = lambda *args: pbar.update()
            itr = [ (x, "hours/1002-1202", "hours/1202-1209", str(epoch), str(units), f"predict{units}") for x in open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:] ]
            
            with Pool(10) as p:
                for x in itr:
                    p.apply_async(exe, x, callback=upd)
                p.close()
                p.join()

            
            # collect error
            out = []
            for x in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
                fh = open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/log/predict{units}/{x[:-1]}.out")
                table = fh.readlines()[-1].split(' ')[-1][:-1]
                out.append(np.float64(table))

            print(np.mean(out))
            result += out
            li += [epoch]*112
            print(len(li), len(result))
            plt.scatter(li,result)
            plt.savefig(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/graph/units_{units}.png")


# python3 given_err.py 500101001 "hours/1002-1128" "hours/total[predict]" "1" 1>log/predict/500101001.out