# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pickle
import json
import codecs
from json_tricks import dumps

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

class TaobaoPipeline(object):
	# def _init_(self):
	# 	self.file = open('items.pkl','wb')

    def __init__(self):
        self.file = codecs.open('items.json', 'wb',encoding='utf-8')

    def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode("unicode_escape"))

		return item