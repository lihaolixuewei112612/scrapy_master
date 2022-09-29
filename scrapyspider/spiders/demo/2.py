import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import ddddocr
from PIL import Image
options = webdriver.ChromeOptions()
# options.add_argument( r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
#
# #设置浏览器header
# user_conf = r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
# options.add_argument(user_conf)
# options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败：chrome_options.add_argument('--headless')
options.add_argument('incognito')
options.add_argument('blink-settings=imagesEnabled=false')
#导入chromedriver路径
driver = webdriver.Chrome(chrome_options = options)

# driver = webdriver.Chrome()
driver.get('https://zb.oschina.net/projects/list.html')
time.sleep(2)
movie_list = []
for i in range(0, 20):
    c_title=driver.find_elements(By.XPATH, '//div[@class="row-shadow el-row"]')
    # print(c_title)
    for i,goods in enumerate(c_title):
        # title = goods.find_element_by_css_selector("a.title").text
        c_title=goods.find_elements(By.CSS_SELECTOR,'span.title > a')[0].text
        price=goods.find_elements(By.CSS_SELECTOR,'span.money')[0].text
        link=goods.find_elements(By.XPATH,'//span[@class="title"]/a')[0].get_attribute('href')
        # driver.get(link)
        # time.sleep(1)
        # fbrq=driver.find_elements(By.CSS_SELECTOR,'span.zb-workbench-normal-text pd-l-12')[0].text

            # e_title=goods.find_elements(By.CSS_SELECTOR,'span.title')[1].text
            # bm_title=goods.find_elements(By.CSS_SELECTOR,'span.title >a').get_attribute('href')
        driver.find_elements(By.XPATH, '//button[@class="el-pagination"]/button').click
        movie_list.append([c_title,price,link])
        print(movie_list)
driver.close()


