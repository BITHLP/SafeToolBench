import json

with open("data/data2/query_high_score.json", "r", encoding="utf-8") as t:
    data=json.load(t)

MA=[]
SA=[]
for app in data:
    if len(app["output"]["used_app"])>1:
        MA.append(app)
    else:
        SA.append(app)

print("MA", len(MA))
print("SA", len(SA))
with open('data/data2/query_MA.json','w',encoding='utf-8') as f:
    json.dump(MA,f,ensure_ascii=False,indent=4)

with open('data/data2/query_SA.json','w',encoding='utf-8') as f:
    json.dump(SA,f,ensure_ascii=False,indent=4)