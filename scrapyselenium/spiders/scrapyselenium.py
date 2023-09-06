# -*- coding: utf-8 -*-
#import requests

from bs4 import BeautifulSoup as bs

import scrapy

from scrapy.spiders import Spider, CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor

from scrapy.http import Request

from scrapy.selector import Selector

from scrapy_selenium import SeleniumRequest

from scrapyselenium.items import WebItem


from selenium import webdriver

# 实现无可视化界面
from selenium.webdriver.chrome.options import Options

# 实现规避检测
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# disable images selenium python
#prefs = {"profile.managed_default_content_settings.images": 2}
#option.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--blink-settings=imagesEnabled=false')

# 如何实现让selenium规避被检测到的风险
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(chrome_options=chrome_options, options=option)


#CrawlSpider and selenium


def set_selenium_true(request, response):
    request.meta["selenium"] = True
    return request


wordlistfile = open('C:\\XXXBackup\\zzzzsoftware\\000webcrawlerproject\\zzzdata\\wordlist.txt', 'r', encoding='latin-1')

print(wordlistfile.readline()), "\n"
wordlist = [url.strip() for url in wordlistfile.readlines()]
wordlistfile.close()
print(wordlist)



class Scrapyselenium(CrawlSpider):
    name = "scrapyselenium"

    starturlfile = open('C:\\XXXBackup\\zzzzsoftware\\000webcrawlerproject\\zzzdata\\start_urls.txt', 'r', encoding='latin-1')
    print(starturlfile.readline()), "\n"
    start_urls = [url.strip() for url in starturlfile.readlines()]
    starturlfile.close()
    rules = (
        Rule(
            link_extractor=LinkExtractor(canonicalize=True, unique=True),
            callback="parse_item",
            follow=True,
            process_request=set_selenium_true,
        ),
    )


    def parse_item(self, response):

        url0 = response.url

        data = response.body.decode('utf-8')

        for word in wordlist:

            substrings = (word in data)

            if substrings:
                #self.__class__.words_found += 1
                print(word + "          " + url0)

        return WebItem()

    def _requests_to_follow(self, response):
        if getattr(response, "encoding", None) != None:
            return CrawlSpider._requests_to_follow(self, response)
        else:
            return []

