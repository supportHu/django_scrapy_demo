#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from bots.spiderbot.spiderbot.items import TmallItem


class TmallSpider(Spider):
    name = 'tmall'
    base_url = 'https://list.tmall.com/search_product.htm?q=轮胎&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=刹车片&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=雨刷&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=机油&enc=utf-8'

    def start_requests(self):
        for page in range(1, 81):
            yield Request(url=self.base_url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        print('Begin parse', response.url)
        products = response.xpath('.//div[@id="J_ItemList"]/div')
        for product in products:
            item = TmallItem()
            item['title'] = ''.join(product.xpath('.//p[@class="productTitle"]/a/text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//a[@class="productShop-name"]/text()').extract()).strip()
            item['price'] = ''.join(product.xpath('.//p[@class="productPrice"]/em/text()').extract()).strip()
            item['status'] = ''.join(product.xpath('.//p[@class="productStatus"]/span/em/text()').extract()).strip()
            yield item
            print(item)
