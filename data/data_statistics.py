# import json

# # 读取JSON文件
# with open('data/query/SA/query_PI_150.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # 初始化统计变量
# risk_counts = {}
# app_counts = {}
# api_counts = {}
# param_counts = {}
# app_usage = {}
# api_usage = {}
# max_sentence_lengths = {}
# total_sentence_lengths = {}
# sentence_count = {}

# # 遍历数据集
# for item in data:
#     risk_category = item['Risk category']
    
#     # 统计风险种类数量
#     if risk_category not in risk_counts:
#         risk_counts[risk_category] = 1
#     else:
#         risk_counts[risk_category] += 1
    
#     # 统计使用的app数量
#     used_apps = set(item['output']['used_app'])
#     if risk_category not in app_counts:
#         app_counts[risk_category] = len(used_apps)
#     else:
#         app_counts[risk_category] += len(used_apps)
    
#     # 统计使用过的app数量
#     if risk_category not in app_usage:
#         app_usage[risk_category] = set()
#     app_usage[risk_category].update(used_apps)
    
#     # 统计使用的api数量
#     used_apis = set()
#     params = 0
#     for api in item['output']['used_api']:
#         api_name = list(api.keys())[0]
#         used_apis.add(api_name)
#         params += len(api[api_name])
#     if risk_category not in api_counts:
#         api_counts[risk_category] = len(used_apis)
#     else:
#         api_counts[risk_category] += len(used_apis)
    
#     # 统计使用过的api数量
#     if risk_category not in api_usage:
#         api_usage[risk_category] = set()
#     api_usage[risk_category].update(used_apis)
    
#     # 统计使用的参数数量
#     if risk_category not in param_counts:
#         param_counts[risk_category] = params
#     else:
#         param_counts[risk_category] += params
    
#     # 统计最长语句长度和总语句长度
#     sentence = item['instruction']
#     sentence_length = len(sentence.split('.'))
#     if risk_category not in max_sentence_lengths or sentence_length > max_sentence_lengths[risk_category]:
#         max_sentence_lengths[risk_category] = sentence_length
#     if risk_category not in total_sentence_lengths:
#         total_sentence_lengths[risk_category] = sentence_length
#     else:
#         total_sentence_lengths[risk_category] += sentence_length
#     if risk_category not in sentence_count:
#         sentence_count[risk_category] = 1
#     else:
#         sentence_count[risk_category] += 1

# # 计算平均值
# average_app_counts = {risk: app_counts[risk] / risk_counts[risk] for risk in risk_counts}
# average_api_counts = {risk: api_counts[risk] / risk_counts[risk] for risk in risk_counts}
# average_param_counts = {risk: param_counts[risk] / risk_counts[risk] for risk in risk_counts}
# average_sentence_lengths = {risk: total_sentence_lengths[risk] / sentence_count[risk] for risk in risk_counts}

# # 输出统计结果
# print("每个风险种类的数量:")
# for risk, count in risk_counts.items():
#     print(f"{risk}: {count}")

# print("\n每个风险种类下平均使用的app数量:")
# for risk, avg_count in average_app_counts.items():
#     print(f"{risk}: {avg_count}")

# print("\n每个风险种类下平均使用的api数量:")
# for risk, avg_count in average_api_counts.items():
#     print(f"{risk}: {avg_count}")

# print("\n每个风险种类下平均使用的参数数量:")
# for risk, avg_count in average_param_counts.items():
#     print(f"{risk}: {avg_count}")

# print("\n每种风险下使用过的app数量:")
# for risk, apps in app_usage.items():
#     print(f"{risk}: {len(apps)}")

# print("\n每种风险下使用过的api数量:")
# for risk, apis in api_usage.items():
#     print(f"{risk}: {len(apis)}")

# print("\n每个风险下最长语句的长度:")
# for risk, length in max_sentence_lengths.items():
#     print(f"{risk}: {length}")

# print("\n每个风险下平均语句的长度:")
# for risk, avg_length in average_sentence_lengths.items():
#     print(f"{risk}: {avg_length}")


import json
import os

paths = os.walk(r'data/query/ALL')

for path, dir_lst, file_lst in paths:
    Wechat=0
    Alipay=0
    Doctor=0
    Bank=0
    Uber=0
    Google_Calendar=0
    YouTube=0
    Meituan=0
    Weather=0
    Trip=0
    Google_Drive=0
    Taobao=0
    CatEye=0
    Rental=0
    Insurance=0
    Home=0
    for file_name in file_lst:
        with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file2:
            data = json.load(file2)
        # 遍历数据集
        for item in data:
            # 统计使用的api数量
            for app in item['output']['used_app']:
                if app=='Wechat':
                    Wechat+=1
                if app=='Alipay':
                    Alipay+=1
                if app=='Doctor':
                    Doctor+=1
                if app=='Bank':
                    Bank+=1
                if app=='Uber':
                    Uber+=1
                if app=='Google Calendar':
                    Google_Calendar+=1
                if app=='YouTube':
                    YouTube+=1
                if app=='Meituan':
                    Meituan+=1
                if app=='Weather':
                    Weather+=1
                if app=='Trip':
                    Trip+=1
                if app=='Google Drive':
                    Google_Drive+=1
                if app=='Taobao':
                    Taobao+=1
                if app=='CatEye':
                    CatEye+=1
                if app=='Rental':
                    Rental+=1
                if app=='Insurance':
                    Insurance+=1
                if app=='Home':
                    Home+=1
        
    
    print('Wechat:', Wechat)
    print('Alipay:', Alipay)
    print('Doctor:', Doctor)
    print('Bank:', Bank)
    print('Uber:', Uber)
    print('Google Calendar:', Google_Calendar)
    print('YouTube:', YouTube)
    print('Meituan:', Meituan)
    print('Weather:', Weather)
    print('Trip:', Trip)
    print('Google Drive:', Google_Drive)
    print('Taobao:', Taobao)
    print('CatEye:', CatEye)
    print('Rental:', Rental)
    print('Insurance:', Insurance)
    print('Home:', Home)