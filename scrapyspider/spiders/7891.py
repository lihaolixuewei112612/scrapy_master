# -*- coding: utf-8 -*-
# @Time     : 2017/1/7 17:04
# @Author   : woodenrobot
import ddddocr
from PIL import Image
ocr = ddddocr.DdddOcr(old=True)

from PIL import Image


from scrapy.spiders import Spider
from scrapy.http import Request, FormRequest
import urllib.request


class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250_test'
    start_urls = ['https://zb.oschina.net/projects/list.html']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyspider.pipeline.csvpiple.SomePipeline': 300,
            'scrapyspider.pipeline.mysqlpiple.LvyouPipeline': 500
        }
    }

    def start_requests(self):
        url = 'https://zb.oschina.net/projects/list.html'
        yield Request(url, headers=self.headers, callback=self.parse, meta={"cookiejar": 1})
    def parse(self, response):
        abc=response.xpath('//div[@class="row-shadow el-row"]')
        print(abc)
        # 首先获取验证图片地址并复制给 imgurl 变量


    def crawlerdata(self,response):
        print("完成登录.........")
        href = response.xpath('//*[@id="waitBody"]/table/@border').extract()
        if "退出登录" in response.text:
            print("111登录成功")
        print(href)
        # title = response.xpath("/html/head/title/text()").extract()
        # content2 = response.xpath("//meta[@name='description']/@content").extract()
        # print(title[0])
        # print(content2[0])
