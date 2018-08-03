# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class Wangyi163Pipeline(object):

    def __init__(self):
        db = pymysql.connect("localhost", "root", "123456", "dede", charset='utf8')
        self.db = db

    def process_item(self, item, spider):
        sql = "insert into wangyi (url, title) values ('%s', '%s')"%(item["url"], item["title"])
        print("---%s---"%(sql))
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

        return item
