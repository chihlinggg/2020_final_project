# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AgodaItem(scrapy.Item):
    Hotel_id = scrapy.Field()
    Star = scrapy.Field()
    Customer_location = scrapy.Field()
    Trip_type = scrapy.Field()
    Room_type = scrapy.Field()
    Living_date = scrapy.Field()
    Comment_title = scrapy.Field()
    Comment_body = scrapy.Field()
    Comment_date = scrapy.Field()
    Response_body = scrapy.Field()
    Response_time = scrapy.Field()
    Approve_number = scrapy.Field()
