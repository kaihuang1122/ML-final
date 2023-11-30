#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import csv
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K

def K_err(b, b_hat):
    s = 28
    return 3*K.abs((b-b_hat)/s)*(K.abs(b/s-1/3)+K.abs(b/s-2/3))
def np_err(b, b_hat):
    s = 28
    return 3*np.abs((b-b_hat)/s)*(np.abs(b/s-1/3)+np.abs(b/s-2/3))

# 讀取CSV數據
with open(f"G:/ML/ML-final/Combination/{sys.argv[2]}/{sys.argv[1]}.csv", "r") as fin:
    reader = csv.reader(fin)
    next(reader)  # 跳過標題行
    data = [row for row in reader]

# 提取特徵和標籤
X = np.array([row[:-2] for row in data], dtype=float)  # 排除capacity
y = np.array([row[-1] for row in data], dtype=float)

# 標準化特徵
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 切分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 建立MLP模型
model = Sequential()
model.add(Dense(units=128, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=1, activation='linear'))

# 編譯模型
model.compile(optimizer='adam', loss=K_err, metrics=['mae'])

# 訓練模型
model.fit(X_train, y_train, epochs=int(sys.argv[4]), batch_size=32, validation_split=0.1)

# 評估模型
loss, mae = model.evaluate(X_test, y_test)
print(f'Mean Absolute Error on Test Set: {mae}')

# 進行預測
predictions = model.predict(X_test)

import csv
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import load_model


# 讀取新的CSV數據
with open(f"G:/ML/ML-final/Combination/{sys.argv[3]}/{sys.argv[1]}.csv", "r") as fin:
    reader = csv.reader(fin)
    next(reader)  # 跳過標題行
    new_data = [row for row in reader]
    reader = list(reader)

# 提取特徵
X_new = np.array([row[:-2] for row in new_data], dtype=float)  # 排除capacity

# 標準化特徵，注意這裡使用之前模型的標準化器
X_new_scaled = scaler.transform(X_new)

# 使用之前訓練好的模型進行預測
predictions = model.predict(X_new_scaled)

counting = []
# 打印預測結果

with open(f"G:/ML/ML-final/Combination/{sys.argv[3]}/{sys.argv[1]}.csv", "r") as fin:
    table = list(csv.reader(fin))[1:]
#sys.stderr.write("id, sbi/n")
for i, prediction in enumerate(predictions):
    str = "2023%02d%02d_%s_%02d:%02d, %f/n"%(int(table[i][1]), int(table[i][2]), sys.argv[1], int(int(int(table[i][4])/60)), int(int(table[i][4])%60), prediction[0])
    sys.stderr.write(str)
    #print(f"Prediction for sample {i + 1}: {prediction[0]}")
    counting.append(np_err(int(table[i][-1]), prediction[0]))

#"2023%02d%02d_%s_%02d%02d, %f"%(int(table[i][1]), int(table[i][2]), sys.argv[1], int(int(int(table[i][4])/60)), int(int(table[i][4])%60), prediction[0])
print("The testing err =", np.mean(counting))
