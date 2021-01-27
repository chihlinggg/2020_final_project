# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelMixItem(scrapy.Item):
    
    #hotel_name = scrapy.Field()
    website = scrapy.Field()
    id = scrapy.Field()
    locale = scrapy.Field()
    approve_number = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    comment_date = scrapy.Field()
    checkin_date = scrapy.Field()
    response_date = scrapy.Field()
    response_body = scrapy.Field()
    travel_type = scrapy.Field()
    room_type = scrapy.Field()
    condition = scrapy.Field()
    reply = scrapy.Field()
