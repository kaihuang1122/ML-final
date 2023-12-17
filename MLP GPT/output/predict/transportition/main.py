from tqdm import tqdm
import csv
out = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/transportition/output.csv", "w")
out.write("id,sbi\n")
out_writer = csv.writer(out)
for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
    with open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/{x[:-1]}.csv") as fin:
        data_input = list(csv.reader(fin))
        i = 0
        while i < len(data_input):
            for time in [0,20,40]:
                
                sum = 0
                num = 0
                if(time == 0):
                    minute = int(data_input[i][0][-2:])
                    while minute < 10 or minute >= 50:
                        sum += float(data_input[i][1])
                        num += 1
                        i += 1
                        if(i >= len(data_input)):
                            break
                        minute = int(data_input[i][0][-2:])
                elif(time == 20):
                    minute = int(data_input[i][0][-2:])
                    while minute < 30 and minute >= 10:
                        sum += float(data_input[i][1])
                        num += 1
                        i += 1
                        if(i >= len(data_input)):
                            break
                        minute = int(data_input[i][0][-2:])

                if(time == 40):
                    minute = int(data_input[i][0][-2:])
                    while minute < 50 and minute >= 30:
                        sum += float(data_input[i][1])
                        num += 1
                        i += 1
                        if(i >= len(data_input)):
                            break
                        minute = int(data_input[i][0][-2:])

                if(i >= len(data_input)):
                    break
                tmp = []
                str_ = "%02d"%time
                tmp.append(str(data_input[i-1][0][:-2] + str_))
                tmp.append(sum/num)
                out_writer.writerow(tmp)



# with open("/Users/kaihuang1122/Downloads/sample_submission.csv") as fh:
#     table = list(csv.reader(fh))
# out_writer.writerows(table)