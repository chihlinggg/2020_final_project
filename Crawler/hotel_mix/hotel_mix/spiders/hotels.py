# -*- coding: utf-8 -*-
from hotel_mix.items import HotelMixItem
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
import json
import math

class HotelsSpider(scrapy.Spider):
    name = 'Hotels'
    def __init__(self,id,hotel_name):
      self.id = id
      self.hotel_name = hotel_name
      super().__init__()

    def start_requests(self):
      url = 'https://tw.hotels.com/ho{}-tr-p0?ajax=true&ajax=true&reviewTab=brand-reviews&ajax=true'.format(self.id)
      yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
      json_response = json.loads(response.text)
      last_page= math.ceil(int(json_response['data']['common']['injected_data']['commonDataBlock']['property']['numTotalReviews'])/50)
      for page in range(1,last_page+1):
        new_url = 'https://tw.hotels.com/ho{}-tr-p{}?ajax=true&ajax=true&reviewTab=brand-reviews&ajax=true'.format(self.id,page)
        yield scrapy.Request(url=new_url, callback=self.parse_article)
    
    def parse_article(self, response):
      # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
      if response.status != 200:
        print('Error - {} is not available to access'.format(response.url))
        return

      json_response = json.loads(response.text)
      # 旅館名字(id)
      
      items = json_response['data']['body']['reviewContent']['reviews']['hermes']['groups'][0]['items']

      for item in items:
        if item['genuineMsg'] == 'Hotels.com 真實旅客評語':
          
          # 評論id
          if item.get('itineraryId'):
            comment_id = item['itineraryId']
          else:
            comment_id = ''

          # 旅行類型
          if item.get('tripType'):
            trip_type = item['tripType']
          else:
            trip_type = ''

          # 評論日期
          if item.get('reviewDate'):
            comment_date = item['reviewDate'].replace('年','/').replace('月','/').replace('日','')
          else:
            comment_date = ''
          
          # 住客地點
          if item.get('reviewer'):
            customer_location = item['reviewer']['locality']
          else:
            customer_location = ''

          # 星星
          if item.get('rating'):
            star = item['rating']
          else:
            star = ''
          
          # 評論標題
          if item.get('summary'):
            comment_title = item['summary']
          else:
            comment_title = ''

          # 評論內容
          if item.get('description'):
            comment_body = item['description']
          else:
            comment_body = ''

          # 回覆內容
          if item.get('response'):
            response_body = item['response']['text'].strip()
            condition = '2'
            reply = '1'
          else:
            response_body = ''
            condition = '0'
            reply = '0'

          data = HotelMixItem()
          
          data['website'] = self.name
          data['id'] = comment_id
          data['travel_type'] = trip_type
          data['comment_date'] = comment_date
          data['locale'] = customer_location
          data['rating'] = star
          data['title'] = comment_title
          data['text'] = comment_body
          data['approve_number'] = ''
          data['checkin_date'] = ''
          data['response_date'] = ''
          data['response_body'] = response_body
          data['room_type'] = ''
          data['condition'] = condition
          data['reply'] = reply
          yield data
        else:
          pass
