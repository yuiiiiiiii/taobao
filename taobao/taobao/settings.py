# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'

DOWNLOADER_MIDDLEWARES = {
    'taobao.middlewares.PhantomJSDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
    'taobao.pipelines.TaobaoPipeline': 300,
}

QUESTION = 'Python'
#设置默认浏览器
DEFAULT_BROWSER = 'PhantomJS'
FEED_EXPORT_ENCODING = 'utf-8'
USER_AGENT ="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'connection': 'keep-alive',
    # 'host': 'list.tmall.com',
    # 'referer': 'https://list.tmall.com',
    'cookie':'_med=dw:1916&dh:821&pw:1916&ph:821&ist:0; pnm_cku822=098%23E1hvSQvUvbpvUvCkvvvvvjiPPLqplj1URFS9ljivPmPpzjtnPsLZtj3RPsS9zjr8RphvCvvvphvPvpvhvv2MMQhCvvOvChCvvvvEvpCWvkTa5BzvPbU1%2BoOokXyA%2Bi9AUpkQrBwgKdyIvWAyHdOcR2xVI4vXDC4AVAilYE4OHFDI7q2UHd8reC66%2BE7re8TJbpPCSL9ZDCOrvTyCvv9vvhh3DP7qTIyCvv4CvhEvlRmtvpvIvvCvpvvvvvvvvhaGvvvCUpvvBs%2BvvUVGvvCjNvvv9fvvvhaGvvmC%2B8wCvvpvvhHh; cna=tsuhEls5P24CATtOMhnRn/tV; isg=AqKiGYQFDNvNaxA7wR3gbYdO8CHEW9GzReLxqOw6epXAv0A51IFxHdo9y8G8; cq=ccp%3D0; hng=; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; _m_h5_tk=17cab6a38b7475e2c8045094b8883251_1512309043460; _m_h5_tk_enc=7ee264d52313471a7d66615566e2161f; res=scroll%3A1841*5569-client%3A1841*578-offset%3A1841*5569-screen%3A1916*889; uc1=cookie14=UoTdeYfKtuLYug%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=UtASsssmeW6lpyd%2BBROh&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; uc3=nk2=CN5XhmRNUVw%3D&id2=UUtJZXW6X3owtw%3D%3D&vt3=F8dBzLQLYp8NLS3op0U%3D&lg2=W5iHLLyFOGW7aA%3D%3D; tracknick=kiwisher; ck1=; lgc=kiwisher; cookie2=2d219e023d8205d6766d2b6e0686d9c4; t=1c02433ee3f74ce3c9d16f43a9e48874; skt=ff1885224e9d72f7; _tb_token_=733dbf0ee8e4b; swfstore=74476; whl=-1%260%260%260'
    }

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'taobao.pipelines.TaobaoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
