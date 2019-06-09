#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from scrapy.linkextractors import LinkExtractor
from bots.spiderbot.spiderbot.items import TuhuItem


class TuhuSpider(Spider):
    name = 'tuhu'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_link = 'https://item.tuhu.cn'
        self.allowed_domains = ['item.tuhu.cn']
        self.start_urls = ['https://item.tuhu.cn/Search.html?s=轮胎&enc=utf-8']
        # self.start_urls = ['https://item.tuhu.cn/Search.html?s=刹车片&enc=utf-8']
        # self.start_urls = ['https://item.tuhu.cn/Search.html?s=雨刷&enc=utf-8']
        # self.start_urls = ['https://item.tuhu.cn/Search.html?s=机油&enc=utf-8']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//td[@class="td1"]/a')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_item)

        le = LinkExtractor(restrict_xpaths='//div[@class="pager"]/a[@class="last-child"]')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    @staticmethod
    def parse_item(response):
        item = TuhuItem()
        item['displayName'] = ''.join(response.xpath(
            './/div[@class="proudct_info"]/h1[@class="DisplayName"]/text()').extract_first()).strip()
        item['price'] = ''.join(response.xpath('.//div[@class="price"]/strong/text()').extract_first()).strip()
        yield item
        print(item)
