from tqdm import tqdm
import csv
for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    with open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/{x[:-1]}.csv") as fin:
        data_input = list(csv.reader(fin))
        i = 0
        while i < len(data_input):
            for time in [0,20,40]:
                minute = int(data_input[i][0][22:24])
                sum = 0
                num = 0
                if(time == "00"):
                    while minute < 10 or minute >= 50:
                        sum += float(data_input[i][1])
                        num += 1
                else:
                    
