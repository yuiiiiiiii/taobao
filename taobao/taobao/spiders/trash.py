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
import chardet
reload(sys)
sys.setdefaultencoding('utf8') 



class TaobaoSpider(scrapy.Spider):
	name = "taobao"
	cnt = 1
	i = 1
	chrome_opt = webdriver.ChromeOptions()
	prefs = {"profile.managed_default_content_settings.images": 2}
	chrome_opt.add_experimental_option("prefs", prefs)
	id = urllib.quote("阔腿裤")
	url = 'https://s.taobao.com/search?q='+id+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180530&ie=utf8'
	

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
		yield scrapy.Request(url = self.url,callback = self.parse)

	def spider_closed(self):
	    self.browser.close()

	def parse(self, response):
		target = re.findall(r'"nid":"(.*?)"',response.body)
		title = re.findall(r'"raw_title":"(.*?)"',response.body)
		shipping = re.findall(r'"view_fee":"(.*?)"',response.body)
		prices = re.findall(r'"view_price":"(.*?)"',response.body)
		places = re.findall(r'"item_loc":"(.*?)"',response.body)
		sales = re.findall(r'"view_sales":"(.*?)"',response.body)
		shops = re.findall(r'"nick":"(.*?)"',response.body)


		for i in range(len(target)):
			url = 'https://item.taobao.com/item.htm?id='+str(target[i])+'&ns=1&abbucket=8'
			comment_url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+str(target[i])+'&currentPageNum=1'
			data = {
		    'title': title[i],
		    'price': prices[i],
		    'free_shipping': shipping[i],
		    'month_sale':sales[i],
		    'shop': shops[i],
		    'addr': places[i],
		    'url': comment_url
			}

			print url
			yield scrapy.Request(url=url,meta={'data':data},callback=self.parse_prop)

    # 获取下一页链接
	# if i < 100:
	#     next_url = self.urlbcoffset+"&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s="+str(i*44)
	#     self.i += 1
	#     yield scrapy.Request(next_url, callback=self.parse)


	def parse_comment(self, response):
		item = TaobaoItem()
		data = response.meta['data']
		# print data['url']
		item['title'] = data['title']
		item['price'] = data['price']
		item['free_shipping'] = data['free_shipping']
		item['month_sale'] = data['month_sale']
		item['shop'] = data['shop']
		item['addr'] = data['addr']		
		item['prop'] = data['prop']

		jc = json.loads(response.body.strip().strip('()'))
		max = jc['total']
		print max


		jc = jc['comments']


		if jc is None:
			self.cnt += 1
			while self.cnt < max - 3:
				url = response.meta['url']
				next_url = url[:-1] + str(self.cnt)
				yield scrapy.Request(next_url, meta={'data': item,'url':url},callback=self.parse_comment)
		else:
			for j in jc:
				# users.append(j['user']['nick'])
				print j
				comment = {}
				comment['product'] = j['auction']['sku']
				comment['date'] = j['date']
				comment['user'] = j['user']['nick']
				comment['anony'] = j['user']['anony']
				comment['content'] = j['content']
				item['comment'] = comment
				# if not (comment['content'] == '此用户没有填写评价。' or '系统默认' in comment['content']):
				yield item

		self.cnt += 1
		while self.cnt < max - 3:
			url = response.meta['url']
			next_url = url[:-1] + str(self.cnt)
			yield scrapy.Request(next_url, meta={'data': item,'url':url},callback=self.parse_comment)


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