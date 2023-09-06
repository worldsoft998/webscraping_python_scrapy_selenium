# -*- coding: utf-8 -*-

# Scrapy settings for projectextractor project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html



from shutil import which


BOT_NAME = 'scrapyselenium'

SPIDER_MODULES = ['scrapyselenium.spiders']
NEWSPIDER_MODULE = 'scrapyselenium.spiders'


DEPTH_LIMIT= 5
DEPTH_PRIORITY = 1

REACTOR_THREADPOOL_MAXSIZE = 20

#Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=1500
CONCURRENT_REQUESTS_PER_DOMAIN = 200
#CONCURRENT_REQUESTS_PER_IP = 256
CONCURRENT_ITEMS=250

LOG_LEVEL = 'INFO'
LOG_ENABLED = True


RETRY_ENABLED = True
# Retry many times since proxies often fail
RETRY_TIMES = 3
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# The download delay setting will honor only one of:
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
DOWNLOAD_DELAY =  0  # 250 ms of delay
DOWNLOAD_TIMEOUT = 15
DOWNLOAD_MAXSIZE = 1*1024*1024
RANDOMIZE_DOWNLOAD_DELAY = True

REDIRECT_ENABLED = False

#Disable cookies (enabled by default)
COOKIES_ENABLED = False

DNS_TIMEOUT = 180
#DNSCACHE_ENABLED = True

ROBOTSTXT_OBEY = False

AJAXCRAWL_ENABLED = True

# Somewhere in settings.py
#DUPEFILTER_CLASS = "scrapyselenium.bloom_filter.BLOOMDupeFilter"


SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyselenium (+http://www.yourdomain.com)'

USER_AGENTS = [    
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

#proxy settings begins

# https://github.com/aivarsk/scrapy-proxies
# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port

PROXY_LIST = 'C:\\XXXBackup\\00WEBITSettings\\004Emails\\proxylist4mails\\000000proxylist4emailscraping.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"

#proxy settings ends


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'scrapyselenium.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy_selenium.SeleniumMiddleware': 800,
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapyselenium.middlewares.scrapyseleniumSpiderMiddleware': 543,
}


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapyselenium.pipelines.scrapyseleniumPipeline': 300,
}



"""
# for firefox

SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']
"""

# for chrome driver

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']





