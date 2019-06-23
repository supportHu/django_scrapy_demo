#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from bots.spiderbot.spiderbot.items import JingDongItem


class JingdongSpider(Spider):
    name = 'jingdong'
    allowed_domains = ['jd.com']

    # 需要爬取的 类目
    keyword_list = ['轮胎', '轮毂', '刹车鼓', '刹车片', '刹车盘', '雨刷', '机油', '火花塞', '电瓶', '玻璃水', '防冻液']
    # keyword_list = ['轮胎']

    # 商品列表页 的请求地址
    base_url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1&page=%d&click=0'

    def start_requests(self):
        for keyword in self.keyword_list:
            for page in range(1, 201, 2):
                url = self.base_url % (keyword, page)
                yield Request(url=url, callback=self.parse, meta={'keyword': keyword})

    def parse(self, response):
        keyword = response.meta['keyword']
        print('Begin parse', response.url)
        products = response.xpath('.//ul[@class="gl-warp clearfix"]/li')
        for product in products:
            sku = ''.join(product.xpath('./@data-sku').extract()).strip()
            item = JingDongItem()
            item['keyword'] = keyword
            item['sku'] = sku
            item['brand'] = ''.join(
                product.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract_first()).strip()
            item['property'] = ''.join(
                product.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract()[-1]).strip()
            item['price'] = ''.join(product.xpath('.//div[@class="p-price"]/strong/*/text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[@class="p-shop"]/span/a/text()').extract()).strip()
            yield item
            # print(item)

