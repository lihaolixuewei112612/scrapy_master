import schedule, subprocess
import time, sys
import datetime
import logging, os
from os import path


def job():
    logging.info('*' * 10 + '开始执行定时爬虫' + '*' * 10)
    subprocess.Popen('scrapy runspider ./spiders/douban_spider.py', shell=True, cwd=os.getcwd())


if __name__ == '__main__':
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        # time.sleep(120*60)
        time.sleep(1)