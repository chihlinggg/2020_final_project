# -*- coding: utf-8 -*-
from booking.items import BookingItem
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

class BookingSpider(scrapy.Spider):
    name = 'booking'
    def __init__(self,id):
      self.id = id
      self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36','Content-Type': 'application/json'
      }
      super().__init__()
    
    def start_requests(self):
      url = "https://www.booking.com/reviewlist.zh-tw.html?aid=376396;label=bdot-gOdtIr17IC7mDJ2ewBK1sAS267725091117%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp9040380%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt1O4nYvDr1lms;srpvid=d8b3302d5f840108&;cc1=tw&pagename={}&r_lang=&review_topic_category_id=&type=total&score=&dist=1&offset=&rows=10&rurl=&sort=f_recent_desc&text=&translate=&_=1596178336681".format(self.id)
      yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
      
      
    def parse(self, response):
      soup = BeautifulSoup(response.text, 'lxml')
      last_page = int(soup.find_all(class_='bui-u-sr-only')[-1].text[1:-1].replace(' ',''))
      for offset in range(0,last_page*10,10):
        new_url = response.url.replace('offset=','offset='+str(offset)+'')
        yield scrapy.Request(url=new_url, callback=self.parse_article, headers=self.headers)
        
    def parse_article(self, response):
      # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
      if response.status != 200:
        print('Error - {} is not available to access'.format(response.url))
        return

      # 旅館名字
      hotel_name = re.split('&pagename=|&r_lang',response.url)[1]
        
       # 將網頁回應的 HTML 傳入 BeautifulSoup 解析器, 方便我們根據標籤 (tag) 資訊去過濾尋找
      soup = BeautifulSoup(response.text, 'lxml')
      data = BookingItem()

      comments = soup.find_all(class_="c-review-block")
      for comment in comments:
        # 住客名字
        if comment.find(class_="bui-avatar-block__title"):
          customer_name = comment.find(class_="bui-avatar-block__title").text
        else:
          customer_name = ''

        # 住客地點
        if comment.find(class_="bui-avatar-block__subtitle"):
          customer_location = comment.find(class_="bui-avatar-block__subtitle").text.strip()
        else:
          customer_location = ''

        # 星星
        if comment.find(class_="bui-review-score__badge"):
          star = comment.find(class_="bui-review-score__badge").text.strip()
        else:
          star = ''

        # 評論日期
        if comment.find(class_="c-review-block__date"):
          comment_date = comment.find(class_="c-review-block__date").text.strip()[:-4].replace(' ','').replace('年','/').replace('月','/').replace('日','')
        else:
          comment_date = ''
        
        # 評論標題
        if comment.find(class_="c-review-block__title c-review__title--ltr"):
          comment_title = comment.find(class_="c-review-block__title c-review__title--ltr").text.strip()
        else:
          comment_title = ''

        # 評論內容
        if comment.find_all(class_="c-review__body"):
          comment_body = ''
          for c in comment.find_all(class_="c-review__body"):
            comment_body = comment_body +c.text.strip()+','
        else:
          comment_body = ''

        if comment.find(class_="c-review-block__room-info__name"):
          # 房型
          if comment.find(class_="room_info_heading"):
            room_type = comment.find(class_="room_info_heading").text[3:]
          else:
            room_type = ''

          # 住宿日期
          if comment.find_all(class_="c-review-block__date"):
            living_date = comment.find_all(class_="c-review-block__date")[1].text.strip().replace(' ','').replace('年','/').replace('月','')
          else:
            living_date = ''
        
        data['Hotel_name'] = hotel_name
        data['Customer_name'] = customer_name
        data['Customer_location'] = customer_location
        data['Star'] = star
        data['Comment_date'] = comment_date
        data['Comment_title'] = comment_title
        data['Comment_body'] = comment_body
        data['Room_type'] = room_type
        data['Living_date'] = living_date

        yield data
