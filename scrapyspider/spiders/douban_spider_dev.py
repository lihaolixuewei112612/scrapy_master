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
    name = 'douban_movie_top250_dev'
    start_urls = ['https://investorservice.cfmmc.com/login.do']
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
        url = 'https://investorservice.cfmmc.com/logout.do'
        yield Request(url, headers=self.headers, callback=self.parse, meta={"cookiejar": 1})
    def parse(self, response):
        # 首先获取验证图片地址并复制给 imgurl 变量
        imgurl = response.xpath('//img[@id="imgVeriCode"]/@src').extract()
        print('----',imgurl[0])
        # 由于验证码时有时无，因此需要判断如果有就手动输入
        print("有验证码返回...")
        # 将验证图片保存到本地中
        local_path = "D:/workespace/workspace/scrapy-tutorial-master/scrapy-tutorial-master/scrapyspider/spiders/demo/captcha.jpg"
        urllib.request.urlretrieve("https://investorservice.cfmmc.com" + imgurl[0], filename=local_path)
        # 定义接受验证码变量
        img = Image.open(local_path)
        Img = img.convert('L')
        threshold = 175
        table = []
        for i in range(256):
            if i < threshold:
                table.append(1)
            else:
                table.append(0)
        # 图片二值化
        photo = Img.point(table, '1')
        # 最后保存二值化图片
        photo.save("binaryzation.jpg")
        with open("binaryzation.jpg", 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        print('res----'+res)
        # 设置带有验证码的 post 信息
        data = {
            "userID": "006800005088",
            "password": "abc123123",
            "vericode": res,
        }
        print("登录中......")
        # 带参的登录请求
        return [FormRequest.from_response(response,
                                             # 设置 cookie 信息   注：这两项在 settings.py 文件中设置即可
                                             meta={"cookiejar":response.meta["cookiejar"]}, #如果重写 start_requests()方法，那么该值必须对应请求里的 meta 中的键
                                             # 设置请求头模拟成浏览器
                                             headers=self.headers,
                                             # 设置 post 表单中的数据
                                             formdata=data,
                                             # 设置回调函数
                                             callback=self.crawlerdata,
                                             )]

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
