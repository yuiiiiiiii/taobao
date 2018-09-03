#coding=utf8
import json
import codecs

data = []
for line in codecs.open('items.json','rb',encoding='utf8'):
    print line
    data.append(json.loads(line))

cnt = {}
cnt['bag']=0
cnt['pants']=0
cnt['shirt']=0
cnt['sneakers']=0
for item in data:
    if u'书包' in item['label']:
        cnt['bag'] += 1
    else: 
        if item['label'] == u'阔腿裤':
            cnt['pants'] += 1
        else:
            if item['label'] == u'运动鞋':
                cnt['sneakers'] += 1
            else:
                cnt['shirt'] += 1

print cnt.items()
