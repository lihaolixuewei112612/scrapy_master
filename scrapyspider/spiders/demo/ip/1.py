import requests
import re
import time
import random

# 爬取网站：云代理
# http://www.ip3366.net/free/?stype=1&page=1

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"
}
if __name__ == '__main__':
    web_site = '云代理'
    url_tmp = 'http://www.ip3366.net/free/?stype=1&page=%d'
    f = open('./ip_list.txt', mode='a', encoding='utf-8')
    for index in range(1, 8):
        try:
            url = url_tmp % index
            print(url)
            response = requests.get(url=url, headers=headers)
            print(response.status_code)
            response.encoding = 'utf-8'
            tr_pattern = r'<tr>(.*?)</tr>'
            trs = re.findall(tr_pattern, response.text, re.S)[1:]
            for tr in trs:
                td_pattern = r'<td>([\d\.]*)</td>[\s]*' \
                             '<td>([\d\.]*)</td>[\s]*' \
                             '<td>.*?</td>[\s]*' \
                             '<td>([A-Z]*)</td>'  # IP PORT
                Ip, Port, Type = re.findall(td_pattern, tr, re.S)[0]
                print(Ip, Port, Type)
                f.write('%s,%s,%s\n' % (Ip, Port, Type))
        except Exception as e:
            # pass
            with open('./error_log.txt', mode='a', encoding='utf-8') as fp:
                fp.write('%s\n%s\n%s\n' % (web_site, str(e), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        finally:
            time.sleep(random.randint(1, 3))
    f.close()
