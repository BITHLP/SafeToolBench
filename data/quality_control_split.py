import json

with open('data/data2/query_quality.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

low_score=[]
high_score=[]
for query in data:
    if 'Riskiness' in query["quality_score"]:
        score=int(query["quality_score"].split(":")[-1].strip())
    else:
        score=int(query["quality_score"])

    if score<7:
        low_score.append(query)
    else:
        high_score.append(query)

print("low_score", len(low_score))
print("high_score", len(high_score))

with open('data//data2/query_low_score.json', 'w', encoding='utf-8') as file:
    json.dump(low_score, file, ensure_ascii=False, indent=4)

with open('data/data2/query_high_score.json', 'w', encoding='utf-8') as file:
    json.dump(high_score, file, ensure_ascii=False, indent=4)