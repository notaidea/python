# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from caiji2.items import WangyiItem
from caiji2.itemsCctv import CctvItem

class Caiji2Pipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123456", "aaa")

    def process_item(self, item, spider):
        #不同的item用不同的处理方式
        '''
        if isinstance(item, WangyiItem):
            pass
        elif isinstance(item, CctvItem):
            pass
        '''
        cursor = self.db.cursor()
        db = self.db

        sql = "insert into caiji(type, title, url) values('%s', '%s', '%s')"%(item["type"], item["title"], item["url"])
        cursor.execute(sql)
        db.commit()

        return item
