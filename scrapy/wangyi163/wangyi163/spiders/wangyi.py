# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from wangyi163.items import Wangyi163Item

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        '''
        for each in response.xpath("//div[@class='news_default_yw']/ul[@class='cm_ul_round'] | //div[@class='news_yw_show']/ul[@class='cm_ul_round']"):
            for index in each.xpath("./li"):
                try :
                    print(index.xpath("./a/text()").extract()[0])
                except Exception:
                    continue
        '''
        for each in response.xpath("//div[@class='news_default_yw']/ul[@class='cm_ul_round']/li | //div[@class='news_yw_show']/ul[@class='cm_ul_round']/li"):
            item = Wangyi163Item()

            '''
            try :
                print(each.xpath("./a/text()").extract()[0])
            except Exception:
                continue
           '''
            title = each.xpath("./a/*/text()").extract()
            if title == [] :
                title = each.xpath("./a/text()").extract()

            url = each.xpath("./a/@href").extract()
            print(url[0])
            print(title[0])

            item["url"] = url[0]
            item["title"] = title[0]

            yield item
