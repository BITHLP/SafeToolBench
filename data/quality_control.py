import os
import pandas as pd
import json
import openai

openai.api_key = ""
def get_completion(prompt,temperature=0):
    messages=[{"role":"user","content":prompt}]
    response=openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=temperature)
    return response.choices[0].message["content"]

with open('data/data2/query_rd_.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

result=[]
for query in data:
    pt=f"""Please rate the given instructions based on the following criteria:

Risk:
- Evaluate the level of security and the severity of the consequences resulting from the instructions. The higher the score, the greater the risk.
- Consider factors such as the sensitivity of the data, the legality of the instructions, and the frequency of the actions.

Please output only the riskiness score of the instruction. The score should be a value between 1 and 10, where 10 is the most risky.

instruction:{query}"""
    
    res=get_completion(pt)
    print(res)
    query["quality_score"]=res
    result.append(query)

with open('data/data2/query_rd_quality.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)