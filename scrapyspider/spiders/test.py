import scrapy
from scrapy.http import Request, FormRequest
# 导入用于爬取网页验证码
import urllib.request


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['douban.com']
    # 浏览器的header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyspider.pipeline.csvpiple.SomePipeline': 300
            # 'scrapyspider.pipeline.mysqlpiple.LvyouPipeline': 500
        }
    }

    # start_urls = ['http://www.douban.com/']
    # 设置提交登录信息的网址，注意要设置cookie储存登录信息以实现连续爬取
    def start_requests(self):
        url = "https://accounts.douban.com/login"
        yield Request(url, callback=self.parse, meta={"cookiejar": 1})

    # 处理数据的方法
    def parse(self, response):
        print('---------------test')
        # 尝试获取网页中的验证码链接
        captcha = ''

        # 根据是否爬取到了验证码图片执行相关处理
        if len(captcha) > 0:
            print("此时有验证码")
            # 爬取验证码图片至本地，提示用户进行输入
            localpath = "./captcha.png"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看本地验证码图片并输入验证码")
            captcha_value = input()
            # 设置需要提交至登录URL的数据，包括用户名、密码、验证码以及登录成功的回调页
            data = {
                "username": "15952028198",
                "password": "11092618q",
            }
        else:
            print("此时没有验证码")
            # 设置需要提交至登录URL的数据，包括用户名、密码以及登录成功的回调页
            data = {
                "username": "15952028198",
                "password": "11092618q",
            }
        print("登录……")
        # 登录成功后执行后续方法
        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]

    # 登录成功后，提取用户信息
    def next(self, response):
        print("此时已经登陆完成并爬取了个人中心的数据")
        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])