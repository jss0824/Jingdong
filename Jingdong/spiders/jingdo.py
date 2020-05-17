# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import re
import requests
import json
class JingdoSpider(scrapy.Spider):
    name = 'jingdo'
    # allowed_domains = ['https://www.jd.com/']
    # start_urls = ['http://https://www.jd.com//']

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    def start_requests(self):
        keyword = '裙子'
        url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'.format(keyword)
        yield Request(url, headers=self.headers)

    def parse(self, response):
        # print(response.text)
        info = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for i in info:
            title = ('').join(i.xpath('./div/div[4]/a/em//text()').extract())
            print('标题：', title)
            price = ('').join(i.xpath('./div/div[3]/strong//text()').extract())
            print('价格：',price)
        # comment_count = ('').join(response.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[5]/strong/a//text()').extract())
        # print('评价数：',comment_count)
            store = ('').join(i.xpath('./div/div[7]/span/a/text()').extract())
            print('店铺名称：',store)
            store_url = 'https:' + ('').join(i.xpath('./div/div[7]/span/a/@href').extract())
            print('店铺url:',store_url)
            goods_url = 'https:' + ('').join(i.xpath('./div/div[4]/a/@href').extract())
            print('商品url：',goods_url)
            product_id = ('').join(re.findall('\.com/(\d+)\.html',goods_url))
            print('商品id：',product_id)

            #爬评论
            comment_url = 'https://club.jd.com/comment/productPageComments.action?'
            data = {
                'callback': 'fetchJSON_comment98',
                'productId': product_id,
                'score': '0',
                'sortType':'5',
                'page': '0',
                'pageSize': 10,
                'isShadowSku': 0,
                'fold':1
            }
            res= requests.get(comment_url, params=data, headers=self.headers).text
            data = json.loads(re.findall(r'fetchJSON_comment98\((.*)\)', res)[0])
            comment_count = data['productCommentSummary']['commentCount']
            print('评论数：',comment_count)
            for i in range(len(data['comments'])):
                comment = data['comments'][i]['content']
                print('评论：', comment)