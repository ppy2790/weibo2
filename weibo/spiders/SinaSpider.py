#coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

import re


import sys
from weibo.items import WeiboItem

reload(sys)
sys.setdefaultencoding('utf-8')

class SinaSpider(CrawlSpider):

    name = 'weibo'

    start_urls=[
        'http://weibo.cn/1737614557/profile?filter=1&page=1'
    ]


    def start_requests(self):
        #url = 'http://weibo.cn/1737614557/profile?filter=1&page=1'
        ##微博搜索"简书"关键字
        #url ='http://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E7%AE%80%E4%B9%A6&page=1'
        url='http://weibo.cn/qinyangwinning'

        return [FormRequest(url=url,callback=self.parse)]


    def parse(self,response):

        item = WeiboItem()

        selector = Selector(response)


        tweets = selector.xpath('body/div[@class="c" and @id]')
        for tweet in tweets:

            device = 'None'

            #id = tweet.xpath('@id').extract_first()  # 微博ID
            id = tweet.xpath('div/a/text()').extract_first()
            #content = tweet.xpath('div/span[@class="ctt"]/text()').extract_first()  # 微博内容
            content = tweet.xpath('div/span[@class="ctt"]')
            info = content[0].xpath('string(.)').extract_first()

            cooridinates = tweet.xpath('div/a/@href').extract_first()  # 定位坐标
            like = re.findall(u'\u8d5e\[(\d+)\]', tweet.extract())  # 点赞数
            transfer = re.findall(u'\u8f6c\u53d1\[(\d+)\]', tweet.extract())  # 转载数
            comment = re.findall(u'\u8bc4\u8bba\[(\d+)\]', tweet.extract())  # 评论数
            others = tweet.xpath('div/span[@class="ct"]/text()').extract_first()  # 求时间和使用工具（手机或平台）

            print id
            print info



            if others :
                others = others.split(u"\u6765\u81ea")
                pubday = others[0]
                if len(others)>1:
                    device= others[1]


            if like :

                like = int(like[0])
                print like

            if transfer:
                transfer = int(transfer[0])
                print transfer

            if comment:
                comment = int(comment[0])
                print comment

            item['nickname']=id
            item['content'] = info
            item['pubday'] = pubday
            item['device'] = device
            item['like'] = like
            item['transfer'] = transfer
            item['comment'] = comment

            yield item



        # for pg in range(2,201):
        #
        #     nurl = 'http://weibo.cn/search/mblog?hideSearchFrame=&keyword=简书&page=%s'%pg
        #
        #
        #
        #     yield Request(nurl,callback=self.parse)




