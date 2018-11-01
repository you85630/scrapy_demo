# -*- coding: utf-8 -*-
import scrapy

from scrapy_demo.items import ScrapyDemoItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=' + str(x) for x in range(0,226,25)]

    def parse(self, response):
        movie = ScrapyDemoItem()
        mlist = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for item in mlist:
            movie['rank'] = item.xpath('div/div[1]/em/text()').extract()[0]
            movie['title'] = item.xpath('div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            movie['cover'] = item.xpath('div/div[1]/a/img/@src').extract()[0]
            movie['director'] = item.xpath('div/div[2]/div[2]/p[1]/text()').extract()[0].replace("\n", "").split("/")[0].replace(" ", "").split("   ")[0]
            movie['online_date'] = item.xpath('div/div[2]/div[2]/p[1]/text()').extract()[1].replace("\n", "").split("/")[0].replace(" ", "").split(" ")[0]
            movie['country'] = item.xpath('div/div[2]/div[2]/p[1]/text()').extract()[1].replace("\n", "").split("/")[1].replace(" ", "").split(" ")[1]
            movie['category'] = item.xpath('div/div[2]/div[2]/p[1]/text()').extract()[1].replace("\n", "").split("/")[2].replace(" ", "").split(" ")[1]
            movie['star'] = item.xpath('div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            movie['info'] = item.xpath('div/div[2]/div[2]/p[2]/span/text()').extract()[0]

            yield movie
