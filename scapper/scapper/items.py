# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):

    title = scrapy.Field()
    text = scrapy.Field()
    subtitle = scrapy.Field()
    # A semicolon separated list of the article tags, if they exist
    tags = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()