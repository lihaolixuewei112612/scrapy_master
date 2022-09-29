import requests
from bs4 import BeautifulSoup

link = "https://zb.oschina.net/projects/list.html"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text,"lxml")
first_title = soup.find("span", class_="title").a.text.strip()
print ("第1篇文章的标题是：", first_title)
