# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelsItem(scrapy.Item):

    hotel_id = scrapy.Field()
    comment_id = scrapy.Field()
    trip_type = scrapy.Field()
    comment_date = scrapy.Field()
    locale = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    pass
