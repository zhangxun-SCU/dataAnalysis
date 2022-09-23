"""
破解百度翻译
    - post请求（携带参数）
    - 响应数据json
"""
import requests
import json

if __name__ == '__main__':
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
    }
    # post参数处理
    word = input("输入单词：")
    data = {
        'kw': word,
    }
    # 请求发生
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据：json方法返回一个字典对象(确认响应数据是json类型才能使用json方法)
    response_obj = response.json()
    print(response_obj)
    with open(f"data/translation/{data['kw']}.json", 'w', encoding='utf-8') as f:
        json.dump(response_obj, fp=f, ensure_ascii=False)
        print("over")
