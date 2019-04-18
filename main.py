# execute to run brickset_spider.py

import subprocess

if __name__ == '__main__':

    scrapy_command = 'scrapy runspider {spider_name}'.format(spider_name='brickset_spider.py')

    process = subprocess.Popen(scrapy_command, shell=True)
