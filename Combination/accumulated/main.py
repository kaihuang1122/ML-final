#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# Usage: python3 <MMDD for init> <MMDD for end (not included)> <MMDD for version>
# 1127 1202 1202
import numpy as np
import sys
import csv
from datetime import datetime
from tqdm import tqdm
import threading


# making dictionary of weather
# index:   0   1      2    3                    4            5         6
# headers: ID, month, day, accumulated minutes, temperature, rainfall, relative humidity
matrix = list(csv.reader(open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/Weatherdata.csv")))[1:]

meta = dict()
for row in matrix:
    meta[row[0]] = row
# making combinationing path
# index:   0   1      2    3        4                             5         6
# headers: ID, month, day, weekday, accumulated minutes (0-1439), capacity, bike amount
from_to_path = [(f'/Users/kaihuang1122/Documents/ML/Final/Data tidy/{sys.argv[3]}version/{x[:-1]}.csv', f'/Users/kaihuang1122/Documents/ML/Final/Combination/accumulated/{sys.argv[1]}-{sys.argv[2]}/{x[:-1]}.csv') for x in open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()]


#for fp in tqdm(from_to_path):
def exec(fp):
    cont = True
    bikes = list(csv.reader(open(fp[0])))[1:]
    fh = open(fp[1], "w")
    writter = csv.writer(fh)
    fh.write("ID, month, day, weekday, accumulated minutes, temperature, accu rainfall, past rainfall, relative humidity, Sun, Mon, Tue, Wed, Thu, Fri, Sat,,,s,i,n,,a,n,d,,c,o,s,,p,o,w,e,r,, rain is 0, <15, <25, >25, rain is 0, <1, <2, >2, capacity, bike amount\n")
    for spot in bikes:
        if cont and ((spot[1]+"%02d"%int(spot[2])) != sys.argv[1]):
            continue
        else:
            cont = False
        if((spot[1]+"%02d"%int(spot[2])) == sys.argv[2]):
            break
        #print(spot)
        temp = spot[:-2] + meta[spot[0]][-3:]
        for wd in range(7):
            if (int(spot[3]) == wd):
                temp += [1]
            else:
                temp += [0]
        for i in range(10):
            temp += [np.sin(int(spot[4])/np.power(2,i)), np.cos(int(spot[4])/np.power(2,i))]
        
        if (float(meta[spot[0]][-2]) == 0):
            temp += [1]
        else:
            temp += [0]
        if (float(meta[spot[0]][-2]) != 0 and float(meta[spot[0]][-2]) < 1):
            temp += [1]
        else:
            temp += [0]
        if (float(meta[spot[0]][-2]) >=1 and float(meta[spot[0]][-2]) < 2):
            temp += [1]
        else:
            temp += [0]
        if (float(meta[spot[0]][-2]) >=2):
            temp += [1]
        else:
            temp += [0]

        temp += spot[-2:]
        writter.writerow(temp)

thrs = []
for fp in tqdm(from_to_path): 
    thrs.append(threading.Thread(target=exec(fp)))
    
for i in thrs:
    i.start()

for i in thrs:
    i.join()

# transformed headders:
# ID, month, day, weekday, accumulated minutes, temperature, rainfall, relative humidity, Sun, Mon, Tue, Wed, Thu, Fri, Sat,,,s,i,n,,a,n,d,,c,o,s,,p,o,w,e,r,, rain is 0, <15, <25, >25, capacity, bike amount