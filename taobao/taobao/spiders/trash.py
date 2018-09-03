#coding=utf-8
# from __future__ import unicode_literals
import scrapy
from selenium import webdriver
from ..settings import QUESTION, DEFAULT_BROWSER,FEED_EXPORT_ENCODING
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from ..items import TaobaoItem
import re
import json
from urlparse import urljoin
import urllib
from selenium.webdriver.support.ui import WebDriverWait
import sys
import emoji
import chardet
reload(sys)
sys.setdefaultencoding('utf8') 


def extract_emojis(str):
    for c in str:
        if c in emoji.UNICODE_EMOJI:
            str.replace(c,'')
    return str


class TaobaoSpider(scrapy.Spider):
	name = "taobao"
	cnt = 1
	i = 1
	chrome_opt = webdriver.ChromeOptions()
	prefs = {"profile.managed_default_content_settings.images": 2}
	chrome_opt.add_experimental_option("prefs", prefs)
        query_list = ["运动鞋"]
	urls = []

	for item in query_list:
		id = urllib.quote(item)
                url = 'https://s.taobao.com/search?q='+id+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180530&ie=utf8'
		urls.append(url)

	

	def __init__(self):
		super(TaobaoSpider, self).__init__()

		if DEFAULT_BROWSER == 'Chrome':
		    # self.browser = webdriver.Chrome(chrome_options=self.chrome_opt)
		    self.browser = webdriver.Chrome(chrome_options=self.chrome_opt)
		elif DEFAULT_BROWSER == 'PhantomJS':
		    self.browser = webdriver.PhantomJS()
		self.browser.set_window_size(800, 600)
		# self.browser.maximize_window()
		self.wait = WebDriverWait(self.browser, 5)
		dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

	def start_requests(self):
		# url = 'https://s.taobao.com/search?q=%E9%98%94%E8%85%BF%E8%A3%A4&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180530&ie=utf8'
            for i in range(1):
                link = self.urls[i]
                label = self.query_list[i]	
                yield scrapy.Request(url = link,meta={'label':label},callback = self.parse)

	def spider_closed(self):
	    self.browser.close()

	def parse(self, response):
	    target = re.findall(r'"nid":"(.*?)"',response.body)
            label = response.meta['label']

	    for i in range(len(target)):
		url = 'https://item.taobao.com/item.htm?id='+str(target[i])+'&ns=1&abbucket=8'
		comment_url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+str(target[i])+'&currentPageNum=1'
		    

	        print label
		yield scrapy.Request(url=comment_url,meta={'label':label,'url':comment_url},callback=self.parse_comment)

    # 获取下一页链接
	# if i < 100:
	#     next_url = self.urlbcoffset+"&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+str(i*44)
	#     self.i += 1
	#     yield scrapy.Request(next_url, callback=self.parse)


	def parse_comment(self, response):
		item = TaobaoItem()
		label = response.meta['label']
		# print data['url']
		item['label'] = label

		jc = json.loads(response.body.strip().strip('()'))
		max = jc['total']
		print max


		jc = jc['comments']


		if jc is None:
			self.cnt += 1
			while self.cnt < max - 3:
				url = response.meta['url']
				next_url = url[:-1] + str(self.cnt)
                                yield scrapy.Request(next_url, meta={'label':label,'url':url},callback=self.parse_comment)
                        if self.cnt >= max - 3:
                            self.cnt = 1
                            return
		else:
			for j in jc:
                                comment = j['content']
                                comment = extract_emojis(comment)
                                item['comment' ]= comment
				# users.append(j['user']['nick'])
				if not ( '此用户没有填写评价' in comment  or '系统默认' in comment):
				    yield item

		self.cnt += 1
		while self.cnt < max - 3:
			url = response.meta['url']
			next_url = url[:-1] + str(self.cnt)
                        yield scrapy.Request(next_url, meta={'label':label,'url':url},callback=self.parse_comment)


	def parse_prop(self,response):
		data = response.meta['data']

		prop = {}
		pro = r'<li title=".*">(.*?)</li>'
		props = re.findall(pro,response.text)
		# print len(props)

		for p in props:
			tmp = p.split(':')
			# print tmp[0]
			# print tmp[1]
			tmp[0].encode('gbk')
			tmp[1].encode('gbk')
			re.sub('&nbsp;','',tmp[0])
			re.sub('&nbsp;','',tmp[1])
			# print chardet.detect(tmp[0])
			# print tmp[0]
			# print tmp[1]

			prop[tmp[0]] = tmp[1]


		data = response.meta['data']
		raw = {
		    'title': data['title'],
		    'price': data['price'],
		    'free_shipping': data['free_shipping'],
		    'month_sale' : data['month_sale'],
		    'shop': data['shop'],
		    'addr': data['addr'],
		    'url': data['url'],
	    	'prop': prop
		}



		yield scrapy.Request(data['url'], meta={'data': raw,'url':data['url']}, callback=self.parse_comment)
