# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    hotel_name = scrapy.Field()
    comment_id = scrapy.Field()
    customer_location = scrapy.Field()
    Star = scrapy.Field()
    comment_date = scrapy.Field()
    comment_title = scrapy.Field()
    comment_body = scrapy.Field()
    room_type = scrapy.Field()
    living_date = scrapy.Field()
    pass
