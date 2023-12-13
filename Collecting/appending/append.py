#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
fold = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/appending/data.csv")
old_table = fold.readlines()
fold.close()
fnew = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/temp/data.csv")
new_table = fnew.readlines()
fnew.close()
fwrite = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/appending/data.csv", "a")
idx = 0
stop = 1
while stop != 0:
    stop = 0
    for i in old_table:
        if i == new_table[idx]:
            idx+=1
            stop+=1
print(idx)
while idx < len(new_table):
    fwrite.write(new_table[idx])
    idx+=1