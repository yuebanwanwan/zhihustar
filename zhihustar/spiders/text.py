import json
from lxml import etree
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}

response = requests.get('https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=20',headers=headers)
data = json.loads(response.text)
users = data.get('data')
print(users)
if response.status_code == 200:
    print('111')
    data = json.loads(response.text)
    print(type(data))
    next_url = data.get('paging').get('next')
    print(next_url)
    print(type(next_url))
    print('222')
    #得到用户数组
    users = data.get('data')
    #每组用户信息由一个字典组成
    for user in users:
        user_url = user.get('url_token')
        print(user_url)
        print(type(user_url))
