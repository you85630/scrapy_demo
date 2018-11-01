# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    director = scrapy.Field()
    online_date = scrapy.Field()
    country = scrapy.Field()
    category = scrapy.Field()
    star = scrapy.Field()
    info = scrapy.Field()

    image_url = scrapy.Field()
    image_name = scrapy.Field()
