# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    Hotel_name = scrapy.Field()
    Customer_name = scrapy.Field()
    Customer_location = scrapy.Field()
    Star = scrapy.Field()
    Comment_date = scrapy.Field()
    Comment_title = scrapy.Field()
    Comment_body = scrapy.Field()
    Room_type = scrapy.Field()
    Living_date = scrapy.Field()
    pass
