#!/usr/bin/env python
import scrapy
# from spider_demo.items import TireItem
from bots.spiderbot.spiderbot.items import TuhuTireItem
from scrapy.linkextractors import LinkExtractor


class TuhuTireSpider(scrapy.Spider):
    name = 'tuhu_tire'

    # custom_settings = {
    #     "ITEM_PIPELINES": {
    #         'spider_demo.pipelines.TirePipeline': 403,
    #     },
    #     'MONGODB_URL': 'mongodb://localhost:27017',
    #     'MONGODB_DB_NAME': 'tuhu_tire_db',
    # }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_link = 'https://item.tuhu.cn'
        self.allowed_domains = ['item.tuhu.cn']
        self.start_urls = ['https://item.tuhu.cn/Search.html?s=米其林轮胎 215/55R16 93V',
                           'https://item.tuhu.cn/Search.html?s=普利司通轮胎 215/55R16 93V']

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
        tire = TuhuTireItem()
        sel = response.xpath('//div[@id="product_introduce"]/div[@class="block"]/div[@class="properties"]')
        tire['brand'] = sel.xpath('./ul/li[1]/text()').extract_first()
        tire['specifications'] = sel.xpath('./ul/li[2]/text()').extract_first()
        tire['speed_level'] = sel.xpath('./ul/li[3]/text()').extract_first()
        tire['load_index'] = sel.xpath('./ul/li[4]/text()').extract_first()
        tire['tire_category'] = sel.xpath('./ul/li[5]/text()').extract_first()
        tire['tire_pattern'] = sel.xpath('./ul/li[6]/text()').extract_first()

        sel = response.xpath('//div[@class="pro_price normal_price"]')
        tire['price'] = sel.xpath('./div[@class="price"]/strong/text()').extract_first()
        tire['evaluate_count'] = sel.xpath('./div[@class="buy_person"]/a/span[@class="person_shu"]/text()').extract_first()
        yield tire
