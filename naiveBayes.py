import pandas as pd
import pprint
data = pd.read_csv('./tennis.csv')
training = data.sample(frac=0.75)
test = pd.concat([data, training]).drop_duplicates(keep=False)
print(training)
print(test)
total = len(data)
np = len(training.loc[data['PlayTennis'] == 'Yes'])
nn = total - np
# print(np, nn)
prob = {}
for col in training.columns[:-1]:
    prob[col] = {}
    values = set(training[col])
    for val in values:
        temp = training.loc[training[col] == val]
        pe = len(temp.loc[temp['PlayTennis'] == 'Yes'])
        ne = len(temp) - pe
        prob[col][val] = [pe/np, ne/nn]

pred = []
correct = 0
for i in test.index:
    row = test.loc[i]
    fpp = np/total
    fpn = nn/total
    for col in test.columns[:-1]:
        fpp *= prob[col][row[col]][0]
        fpn *= prob[col][row[col]][1]
    if fpp > fpn:
        pred.append('Yes')
    else:
        pred.append('No')
    if(row['PlayTennis'] == pred[-1]):
        correct += 1

print(pred)
print('accuracy =', (correct/len(test)) * 100)