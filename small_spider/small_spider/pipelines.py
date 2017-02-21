# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib

class SmallSpiderPipeline(object):
    def process_item(self, item, spider):
        for i in item['pic']:
            print(i)
            pic_name = i.split('/')[-1]
            urllib.request.urlretrieve(i,'z_p-'+pic_name)
        # return item
