# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#coding=utf-8
import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    free_shipping = scrapy.Field()
    month_sale = scrapy.Field()
    prop = scrapy.Field()
    shop = scrapy.Field()
    addr = scrapy.Field()
    comment = scrapy.Field()