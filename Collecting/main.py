#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

from selenium import webdriver

url = 'https://www.cwa.gov.tw/V8/C/W/OBS_Station.html?ID=A0A01'

driver = webdriver.PhantomJS()  # PhantomJS
driver.get(url)  # 把網址交給瀏覽器 
pageSource = str(driver.page_source) # 取得網頁原始碼
print("get")
new_source = []
pageSource = pageSource.split('tr')
for i in pageSource:
    if i.find('"rain">') != -1:
        temp1 = i.find('tem-C is-active">')
        temp2 = i.find('"rain">')
        temp3 = i.find('"hum">')
        new_source.append([i[55:60], i[84:89], i[temp1+17:temp1+21], i[temp2+7:temp2+10], i[temp3+6:temp3+8]])

fh = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/temp/data.csv", "w")
count = 0
for i in new_source:
    if count > 1 and count < len(new_source)-1:
        if i[3] == "-</":
            i[2] = '-1'
            i[3] = '-1'
            i[4] = '-1'
        fh.write(i[0][0:2]+','+i[0][3:]+','+i[1][0:2]+','+i[1][3:]+','+i[2]+','+i[3]+','+i[4]+'\n')
    count += 1
fh.close()

fh = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/temp/data.csv")

table = list(fh.readlines())
fh.close()
fnew = open("/Users/kaihuang1122/Documents/ML/Final/Collecting/temp/data.csv", "w")
for i in range(len(table)):
    j = len(table) - 1 - i
    fnew.write(table[j])

