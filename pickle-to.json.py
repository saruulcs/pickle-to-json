import pickle
import json

file = open('annotated.pkl', 'rb')
data = pickle.load(file, encoding="utf-8")
# print(data)

d = open('data.json', 'w+')
json.dump(data, d, ensure_ascii=False)


d.close()
file.close()