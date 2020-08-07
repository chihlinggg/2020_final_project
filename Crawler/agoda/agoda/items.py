# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AgodaItem(scrapy.Item):
    hotel_id = scrapy.Field()
    locale = scrapy.Field()
    approve_number = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    time = scrapy.Field()
    trip_type = scrapy.Field()
    room_type = scrapy.Field()
    response_body = scrapy.Field()
    

class TimeItem(scrapy.Item):
    comment = scrapy.Field()
    checkin = scrapy.Field()
    response = scrapy.Field()