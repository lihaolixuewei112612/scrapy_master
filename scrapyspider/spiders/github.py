import scrapy

class LoginSpider(scrapy.Spider):
    name = 'login_dev'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']  # 首先访问登录页面
    P = "15175857475a"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyspider.pipeline.csvpiple.SomePipeline': 300,
            'scrapyspider.pipeline.mysqlpiple.LvyouPipeline': 500
        }
    }

    def parse(self, response):
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
        print("-----"+authenticity_token)
        timestamp = response.xpath('//input[@name="timestamp"]/@value').extract()[0]
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').extract()[0]
        required_field = response.xpath('//input[@type="text"]/@name').extract()[1]
        form_data = {
            "commit": "Sign in",
            "authenticity_token": authenticity_token,
            "login": "lihaolixuewei",
            "trusted_device": "",
            "password": "11092618qQ$",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "unsupported",
            "return_to": "https://github.com/login",
            "allow_signup": "",
            "client_id": "",
            "integration": "",
            required_field: "",
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret,
        }
        yield scrapy.FormRequest(url="http://github.com/session", callback=self.verify_login, formdata=form_data)

    def verify_login(self, response):
        if "lihaolixuewei" in response.text:
            print("登录成功")
        else:
            print("不成功")
        if "Following" in response.text:
            print("111登录成功")
        else:
            print("111不成功")
        list = response.xpath("/html/body/div[5]/div/aside/div/div[3]/h2/text()").extract()
        print(list)
        print(response.url)
        if 'Following' in list:
            self.logger.info('我已经登录成功了，这是我获取的关键字：Browse activity')
        print(response.xpath('/html/head/title/text()').extract())



# 登录github
# 请求流程 向 https://github.com/session 提交post 用户名密码等数据 获取登录页面
# 1.访问 https://github.com/login获取https://github.com/session 需要的参数

"""commit: Sign in   忽略
需要购造
authenticity_token: qx0N300eRt+thwVSihcr93xQOhYLRGsdEEBXf0twTZXS8lCV9e58/neVLLBY0/v1A7zAhASGyIeuJdSR28oBRA==
login: 2418917657@qq.com  用户名
password: 15175857475a1  密码
trusted_device:   
webauthn-support: supported   忽略
webauthn-iuvpaa-support: unsupported  忽略
return_to: https://github.com/login
allow_signup:    
client_id: 
integration: 
required_field_f9a9:  不太一样，但是没有数据 
timestamp: 1641002690912   时间戳 需要枸造
需要枸造
timestamp_secret: b539cdfd359669612d24768a002e4f3ccca2f52ccba8217aefc4eb6485ccf9f5"""

"""
参数获取的方式：
1.之前请求的页面中获取
2.js代码动态生成
"""