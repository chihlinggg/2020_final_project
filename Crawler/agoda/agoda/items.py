# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AgodaItem(scrapy.Item):
    
    hotel_id = scrapy.Field()
    comment_id = scrapy.Field()
    locale = scrapy.Field()
    approve_number = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    comment_date = scrapy.Field()
    checkin_date = scrapy.Field()
    response_date = scrapy.Field()
    response_body = scrapy.Field()
    trip_type = scrapy.Field()
    room_type = scrapy.Field()

    