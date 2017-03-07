#coding=utf-8

from scrapy.http import FormRequest,Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import  Selector

class WeiboSprider(CrawlSpider):

    name = 'weibo2'

    start_urls=['http://weibo.cn']


    def start_requests(self):

        url = 'http://weibo.cn/qinyangwinning'

        ### 以下换成你自己的cookie
        Cookie = {
            'SINAGLOBAL':'9358208361608.756.1481404188100',
            'wb_publish_fist100_1737614557':'1',
            'wb_g_upvideo_1737614557':'1',
            'YF-Ugrow-G0':'ad06784f6deda07eea88e095402e4243',
            'SSOLoginState':'1485121080',
            'YF-V5-G0':'694581d81c495bd4b6d62b3ba4f9f1c8',
            'YF-Page-G0':'19f6802eb103b391998cb31325aed3bc',
            '_s_tentry':'weibo.com/',
            'Apache':'6797863994735.178.1485121533563',
            'ULV':'1485121533614:9:6:1:6797863994735.178.1485121533563:1485009556762',
            'TC-Page-G0':'fd45e036f9ddd1e4f41a892898506007',
            'TC-V5-G0':'7975b0b5ccf92b43930889e90d938495',
            'TC-Ugrow-G0':'0149286e34b004ccf8a0b99657f15013',
            'wvr':'6',
            'UOR':',,login.sina.com.cn',
            'SCF':'ArBTqQRIliTY4mMxevHwNBS-QCdz_m5pa0GGz9Td7S0yoB4q2e8qSiECTy-82IoZI3SIl2SmupwiBkmqUYpwJmo.',
            'SUHB':'0cSWv8HY-rf1D1',
            'ALF':'1517091532',
            'SUB':'_2AkMv0MR8dcPhrAJWm_8TzW_naYpH-jycBa2KAn7uJhMyOhh77moKqSUlmN10rtmcgHPEjiFOI4Wg7g7E-Q..',
            'SUBP':'0033WrSXqPxfM72wWs9jqgMF55529P9D9WFkJh8533ol.oFZpZYck-uo5JpX5o2p5NHD95QpS0eNSo2XSK-NWs4Dqcj.i--fiK.7iK.pi--fiKysi-z0i--fi-2fiK.Xi--Ri-zNiK.p',
            'login_sid_t':'b4218d2d28b77d1419ea2669638efe12',
            'WBStorage':'1ffbf906cea1ff551|undefined'
        }
        yield FormRequest(url,cookies=Cookie,callback=self.parse)

    def parse(self, response):

        print response.body

        selector = Selector(response)

        infos = selector.xpath('//a/text()').extract()


        print len(infos)


        for info in infos:
            print info

