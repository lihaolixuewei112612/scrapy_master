import requests
import time
import threading

fp = open('./ip_list.txt', mode='r', encoding='utf-8')  # 总的iplist
fp2 = open('./verify_proxies.txt', mode='a', encoding='utf-8')  # 经过验证的ip
num = 0
site = '验证代理'


def verify_proxy():
    global num
    while True:
        line = fp.readline().strip('\n')  # 去掉结尾换行符
        if line != '':
            ip, host, protocol = line.split(',')
            # print(ip, host, protocol)
            # 要访问的网站如果是HTTPS，那么代理也要是HTTPS，如果不对应，则不会使用代理，转而使用本地IP
            # 要访问的网站如果是HTTP，那么代理也要是HTTP，如果不对应，则不会使用代理，转而使用本地IP
            url1 = 'http://ip.tool.chinaz.com/'
            url2 = 'https://ip.cn/'
            try:
                if protocol == 'HTTPS':
                    requests.get(url2, proxies={'https': '%s:%s' % (ip, host)}, timeout=5)
                    print('该 %s ip-> %s:%s 验证通过' % (protocol, ip, host))
                    num += 1
                    fp2.write('%s,%s,%s\n' % (ip, host, protocol))
                else:
                    requests.get(url1, proxies={'http': '%s:%s' % (ip, host)}, timeout=5)
                    print('该 %s ip-> %s:%s 验证通过' % (protocol, ip, host))
                    num += 1
                    fp2.write('%s,%s,%s\n' % (ip, host, protocol))
            except Exception as e:
                print('该 %s ip-> %s:%s 验证失败' % (protocol, ip, host))
                with open('./error_log.txt', mode='a', encoding='utf-8') as fe:
                    fe.write('%s\n%s\n%s\n' % (site, str(e), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        else:
            break
    return num


if __name__ == '__main__':
    threads = []
    for i in range(100):
        t = threading.Thread(target=verify_proxy)
        t.start()
        threads.append(t)

    # join必须单独写，目的：线程启动
    for t in threads:
        t.join()  # 所有的子线程结束任务，主线程才开始继续执行
    # verify_proxy()
    fp.close()
    fp2.close()
    print('可用ip的数量是%d' % num)