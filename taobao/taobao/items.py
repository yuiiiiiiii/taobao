# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#coding=utf-8
import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    label = scrapy.Field()
    comment = scrapy.Field()
