# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EpisodeItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    index = scrapy.Field()
