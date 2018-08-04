# -*- coding: utf-8 -*-
import scrapy
from caiji2.items import WangyiItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        for each in response.xpath("//div[@class='news_default_yw']/ul | //div[@class='news_yw_show']/ul"):
            for index in each.xpath("./li/a"):
                item = WangyiItem()
                type = "163"
                url = index.xpath("@href").extract()
                title = index.xpath("text()").extract()

                if title == []:
                    title = index.xpath("./em/text()").extract()

                '''
                try :
                    print(index.extract())
                except Exception:
                    pass
                '''

                item["url"] = url[0]
                item["title"] = title[0]
                item["type"] = type
                yield item