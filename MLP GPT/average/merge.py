
target = ['500101020', '500101022', '500101025', '500101181']

f1 = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/output/predict/transportition/output.csv")
table1 = f1.readlines()[1:]
table1 = [x.split('_') for x in table1]
for i in range(len(table1)):
    table1[i][0] = int(table1[i][0])
table1 = sorted(table1)

print(table1)


f2 = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/average/touput.csv")


table = []
for i, j in zip(table1, f2.readlines()[1:]):
    if(i[1] in target):
        table.append(j)
    else:
        table.append(f'{str(i[0])}_{i[1]}_{i[2]}')
    
fout = open("/Users/kaihuang1122/Documents/ML/Final/MLP GPT/average/merge.csv", "w")
fout.write("id,sbi\n")
fout.writelines(table)