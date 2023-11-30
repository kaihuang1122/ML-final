#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# Usage: python3 <MMDD for init> <MMDD for end (not included)>
# 1021 1025 1130
import numpy as np
import sys
import csv
from datetime import datetime
from tqdm import tqdm

# making dictionary of weather
# index:   0   1      2    4                    5            6         7
# headers: ID, month, day, accumulated minutes, temperature, rainfall, relative humidity
matrix = list(csv.reader(open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/Weatherdata.csv")))[1:]
meta = dict()
for row in matrix:
    meta[row[0]] = row

# making combinationing path
# index:   0   1      2    3        4                             5         6
# headers: ID, month, day, weekday, accumulated minutes (0-1439), capacity, bike amount
ca_to_path = [(f'/Users/kaihuang1122/Documents/ML/Final/Data tidy/1129version/{x[:-1]}.csv', f'/Users/kaihuang1122/Documents/ML/Final/Combination/{sys.argv[1]}-{sys.argv[2]}[predict]/{x[:-1]}.csv') for x in open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()]


for fp in tqdm(ca_to_path):
    capacity = open(fp[0]).readlines()[-4].split(',')[-2]
    #print(int(sys.argv[1][:3]), int(sys.argv[1][3:]), int(sys.argv[2][:3]), int(sys.argv[2][3:]))
    start = int(datetime(2023, int(sys.argv[1][:2]), int(sys.argv[1][2:]), 0, 0, 0).timestamp())
    end   = int(datetime(2023, int(sys.argv[2][:2]), int(sys.argv[2][2:]), 0, 0, 0).timestamp())
    cont = True
    bikes = list(csv.reader(open(fp[0])))[1:]
    fh = open(fp[1], "w")
    writter = csv.writer(fh)
    fh.write("ID, month, day, weekday, accumulated minutes, temperature, rainfall, relative humidity, Sun, Mon, Tue, Wed, Thu, Fri, Sat,,,s,i,n,,a,n,d,,c,o,s,,p,o,w,e,r,,, rain is 0, <15, <25, >25, capacity, bike amount\n")
    while start < end:
        time = datetime.fromtimestamp(start)
        spot =[str(x) for x in [start, time.month, time.day, time.weekday(), time.hour*60+time.minute, capacity, -1]]
        # headers: ID, month, day, weekday, accumulated minutes (0-1439), capacity, bike amount
        # for spot in bikes:
        if cont and ((spot[1]+"%02d"%int(spot[2])) != sys.argv[1]):
            continue
        else:
            cont = False
        if((spot[1]+"%02d"%int(spot[2])) == sys.argv[2]):
            break
        #print(spot)
        temp = spot[:-2] + meta[spot[0]][5:]
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
        if (float(meta[spot[0]][-2]) != 0 and float(meta[spot[0]][-2]) < 15):
            temp += [1]
        else:
            temp += [0]
        if (float(meta[spot[0]][-2]) >=15 and float(meta[spot[0]][-2]) < 25):
            temp += [1]
        else:
            temp += [0]
        if (float(meta[spot[0]][-2]) >=25):
            temp += [1]
        else:
            temp += [0]

        temp += spot[-2:]
        writter.writerow(temp)
        start += 60