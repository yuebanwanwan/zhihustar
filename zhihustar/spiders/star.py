# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import json
from scrapy import Request
from queue import Queue
from zhihustar.items import ZhihustarItem
import requests

#  思路分析
# 1 首先获取每个用户的用户名
# 2 进入其主页获取其关注者
class StarSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['www.zhihu.com']
    #start_urls = ['http://www.zhihu.com/']
    #这是轮子哥关注者的json格式的信息
    base_url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0'
    urlqueue = Queue()



    def start_requests(self):
        self.urlqueue.put(self.base_url)
        #该页面是不需要js渲染是能直接得到的数据

        yield Request(url=self.base_url,callback=self.parse)


    # 注意没有粉丝怎么办
    def parse(self, response):

        data = json.loads(response.text)

        #获取下一组用户的url,需要先判断data关键字对应的value不能为None
        if len(data.get('data'))!=0:
            next_url = data.get('paging').get('next')
            yield Request(url=next_url,callback=self.parse)
            # 得到用户数组
            users = data.get('data')
            # 每组用户信息由一个字典组成
            for user in users:
                user_name = user.get('url_token')
                # print(user_url)
                # print(type(user_url)) --str
                # 获取粉丝的粉丝
                user_url = 'https://www.zhihu.com/api/v4/members/' + user_name + '/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0'
                # 得到每个用户的主页链接
                user_main_url = 'https://www.zhihu.com/people/' + user_name + '/activities'
                yield Request(url=user_url, callback=self.parse)

                # proxy_pool_flash = 'http://127.0.0.1:5555/random'
                # ip = requests.get(proxy_pool_flash).text
                # proxy = 'http://' + ip

                yield SplashRequest(url=user_main_url, callback=self.parse_each_user)


    #解析每个用户的主页获取其关注数
    def parse_each_user(self,response):
        number_of_followers = response.xpath('//strong[@class="NumberBoard-itemValue"]')
        if number_of_followers:
            Item = ZhihustarItem()
            Item['url'] = response.url
            Item['followers'] = number_of_followers[1].xpath('./text()').extract_first().strip()
            number = Item['followers'].replace(',','')
            if int(number) > 10000:
                yield Item

































