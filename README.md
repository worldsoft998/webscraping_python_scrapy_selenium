Webscraping in Python with Scrapy & Selenium

(Repo webscraping_python_scrapy_selenium)

Web scraping in Python with Scrapy crawler and Selenium browser automation.

Pieces of Python codes to find pages containing certain keywords or list of keywords in a list of websites and  print out to the screen the page list with keywords in front of the links. The crawler runs per a proxy pool configued through a proxy list file. You may also modify them to save the results to files. With little more efforts, the scraper can also perform more promising scraping with varying uses.


Follow the steps below to set your scraping project.

Go to your folder where you plan to run the scraper
======================================================
This is the top level project folder when you download it from this repo and this is also where you find the file scrapy.cfg.


Initiate Your Project and Install Packages for the Scraper
===========================================================
Install whatever the prompt instructions tell you to do when you run the scraper as below.

For example:

bs4
scrapy
selenium 


Prepare for 3 Input Files
===========================
.txt files of the following names in the code: (One entry per line, the github does not pertain to this format, be careful!!!)

keywordslist.txt (see wordlistfile  of scrapyselenium.py)
---------------------------------------------------------------------
example entries:

artificial intelligence
money
finance
investment


start_urls.txt  (see starturlfile of scrapyselenium.py)
---------------------------------------------------------------
example entries:

https://money.com/
https://easywithai.com/
https://openaimaster.com/
https://www.fool.com/
https://towardsdatascience.com
https://aiforfinance.artefact.com/
https://aibusiness.com/
https://www.aifinancial.ca
https://aiinvestments.pl/


proxylist.txt  (see PROXY_LIST of settings.py)
----------------------------------------------------------
example entris:

http://50.218.57.67:80
http://50.168.163.183:80
http://50.171.32.224:80
http://50.173.140.147:80
http://50.207.199.87:80
http://50.168.72.119:80
http://178.21.163.24:80
http://50.171.2.11:80
http://50.168.72.122:80
http://107.1.93.208:80


Run the Code in Commandline
============================

Go to  the top level project folder where you find the file scrapy.cfg and issue the following command:

scrapy crawl scrapyselenium

CTRL+ C to interrupt the crawler and exit.


