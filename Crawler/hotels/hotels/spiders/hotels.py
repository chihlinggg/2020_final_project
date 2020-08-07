# -*- coding: utf-8 -*-
from hotels.items import HotelsItem
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
import json

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    def __init__(self,id):
      self.id = id
      super().__init__()

    def start_requests(self):
      for page in range(1,2):
        url = 'https://tw.hotels.com/ho{}-tr-p{}?ajax=true&ajax=true&reviewTab=brand-reviews&ajax=true'.format(self.id,page)
        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
      # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
      if response.status != 200:
        print('Error - {} is not available to access'.format(response.url))
        return

      data = HotelsItem()
      jsonresponse = json.loads(response.text)
      # 旅館名字(id)

      hotel_id = jsonresponse['data']['common']['injected_data']['commonDataBlock']['property']['hotelId']
      
      items = jsonresponse['data']['body']['reviewContent']['reviews']['hermes']['groups'][0]['items']

      for item in items:
        if item['genuineMsg'] == 'Hotels.com 真實旅客評語':
          
          # 旅行類型
          if item['tripType']:
            trip_type = item['tripType']
          else:
            trip_type = ''

          # 評論日期
          if item['reviewDate']:
            comment_date = item['reviewDate'].replace('年','/').replace('月','/').replace('日','')
          else:
            comment_date = ''
          
          # 住客名字
          if item['reviewer']['name']:
            customer_name = item['reviewer']['name']
          else:
            customer_name = ''

          # 住客地點
          if item['reviewer']['locality']:
            customer_location = item['reviewer']['locality']
          else:
            customer_location = ''

          # 星星
          if item['rating']:
            star = item['rating']
          else:
            star = ''
          
          # 評論標題
          if item['summary']:
            comment_title = item['summary']
          else:
            comment_title = ''

          # 評論內容
          if item['description']:
            comment_body = item['description']
          else:
            comment_body = ''
          
          data['Hotel_id'] = hotel_id
          data['Trip_type'] = trip_type
          data['Comment_date'] = comment_date
          data['Customer_name'] = customer_name
          data['Customer_location'] = customer_location
          data['Star'] = star
          data['Comment_title'] = comment_title
          data['Comment_body'] = comment_body

          yield data
        else:
          pass
