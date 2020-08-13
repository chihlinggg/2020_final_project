# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    
    hotel_id = scrapy.Field()
    comment_id = scrapy.Field()
    locale = scrapy.Field()
    rating = scrapy.Field()
    comment_date = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    room_type = scrapy.Field()
    checkin_date = scrapy.Field()
    pass
