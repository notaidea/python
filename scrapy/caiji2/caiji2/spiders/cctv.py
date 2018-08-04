# -*- coding: utf-8 -*-
import scrapy
from caiji2.itemsCctv import CctvItem

class CctvSpider(scrapy.Spider):
    name = 'cctv'
    allowed_domains = ['cctv.cn']
    start_urls = ['http://cctv.cn/']

    def parse(self, response):
        for each in response.xpath("//div[@class='mbox_151116_04_151127']"):
            for index in each.xpath("./div[@class='text_box']/h4/a"):
                item = CctvItem()

                url = index.xpath("@href").extract()[0]
                title = index.xpath("text()").extract()[0]
                type = "cctv"

                item["url"] = url
                item["title"] = title
                item["type"] = type

                yield item