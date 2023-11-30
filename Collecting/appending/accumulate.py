#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import csv
import numpy as np
fin = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/appending/data.csv")
fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/weather_data.csv", "w")

table = list(csv.reader(fin))
for i in table:
    i[2] = str(int(i[2])*60+int(i[3]))
    i[3] = i[4]
    i[4] = i[5]
    i[5] = i[6]
    i.pop()
    
writer = csv.writer(fout)

writer.writerows(table)