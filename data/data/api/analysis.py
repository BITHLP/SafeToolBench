import json
with open("api.json", "r", encoding="utf-8") as t:
    data=json.load(t)
    num=0
    for app in data:
        print(app['app_name'])
        num_api=len(app['APIs'])
        num+=num_api
        print(num_api)
    print(num)