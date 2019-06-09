#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from bots.spiderbot.spiderbot.items import JingDongItem


class JingdongSpider(Spider):
    name = 'jingdong'
    base_url = 'https://search.jd.com/Search?keyword=轮胎&enc=utf-8'
    # base_url = 'https://search.jd.com/Search?keyword=刹车片&enc=utf-8'
    # base_url = 'https://search.jd.com/Search?keyword=雨刷&enc=utf-8'
    # base_url = 'https://search.jd.com/Search?keyword=机油&enc=utf-8'

    def start_requests(self):
        for page in range(1, 101):
            yield Request(url=self.base_url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        print('Begin parse', response.url)
        products = response.xpath('.//ul[@class="gl-warp clearfix"]/li')
        for product in products:
            item = JingDongItem()
            item['brand'] = ''.join(product.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract_first()).strip()
            item['property'] = ''.join(product.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract()[-1]).strip()
            item['price'] = ''.join(product.xpath('.//div[@class="p-price"]/strong/*/text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[@class="p-shop"]/span/a/text()').extract()).strip()
            # item['commit'] = ''.join(product.xpath('.//div[@class="p-commit"]/strong/a/text()').extract()).strip()
            yield item
            print(item)

