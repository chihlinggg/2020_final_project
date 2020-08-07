# -*- coding: utf-8 -*-
from agoda.items import AgodaItem
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time
import json

class AgodaSpider(scrapy.Spider):
    name = 'agoda'
    def __init__(self,id):
      self.id = id
      self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
            'Content-Type': 'application/json'
        }
      self.start_urls = 'https://www.agoda.com/NewSite/zh-tw/Review/ReviewComments'
      super().__init__()

    def start_requests(self):
      for page in range(1,2):
        self.payload = "{{\"hotelId\":{id},\"providerId\":332,\"demographicId\":0,\"page\":{page},\"pageSize\":20,\"sorting\":1,\"providerIds\":332,\"isReviewPage\":false,\"isCrawlablePage\":true,\"filters\":{{\"language\":[],\"room\":[]}},\"searchKeyword\":\"\",\"searchFilters\":[]}}".format(id=self.id,page=page)
        yield scrapy.Request(url=self.start_urls, callback=self.parse, method='POST', headers=self.headers, body=self.payload)
        
    def parse(self, response):
      # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
      if response.status != 200:
        print('Error - {} is not available to access'.format(response.url))
        return

      soup = BeautifulSoup(response.text, 'lxml')
      comments = soup.find_all(class_='sub-section individual-review-item')

      for comment in comments:
            
        # 星星
        if comment.find('span',attrs={'data-selenium':'individual-review-rate'}):
          star = comment.find('span',attrs={'data-selenium':'individual-review-rate'}).text.strip()
        else:
          star = ''          
        
        # 住客地點
        if comment.find('span',class_='reviewer-name'):    
          if '（' in comment.find('span',class_='reviewer-name').text.strip():
            customer_loc = comment.find('span',class_='reviewer-name').text.strip().split('（')[1][2:-1]
          else:
            customer_loc = ''
        else:
            customer_loc = ''
                    
        # 旅程類型
        if comment.find('div',attrs={'data-selenium':'reviewer-traveller-type'}):
          trip_type = comment.find('div',attrs={'data-selenium':'reviewer-traveller-type'}).text.strip()
        else:
          trip_type = ""
                    
        # 房型
        if comment.find('div',attrs={'data-selenium':'review-roomtype'}):
          room_type = comment.find('div',attrs={'data-selenium':'review-roomtype'}).text.strip()
        else:
          room_type = ''
                    
        # 住宿日期
        if comment.find('div',attrs={'data-selenium':'reviewer-stay-detail'}):
          if '（' in comment.find('span',class_='reviewer-name').text.strip():
            living_date = comment.find('div',attrs={'data-selenium':'reviewer-stay-detail'}).text.strip().split('（')[1][:-1].replace('年','/').replace('月','')
          else:
            living_date = ''  
        else:
          living_date = ''
                
        # 評論標題
        if comment.find('div',class_='comment-title-text'):
          comment_title = comment.find('div',class_='comment-title-text').text.strip().replace('”','')
        else:
          comment_title = ''
                    
        # 評論主體
        if comment.find('div',class_='comment-text'):
          comment_body = comment.find('div',class_='comment-text').text.strip().replace('\n','')
        else:
          comment_body = ''
                    
        # 評論日期
        if comment.find('span',attrs={'data-selenium':'review-date'}):
          comment_date = comment.find('span',attrs={'data-selenium':'review-date'}).text.strip()[5:].replace('年','/').replace('月','/').replace('日','')
        else:
          comment_date = ''
                    
        # 回應內容
        if comment.find('span',attrs={'data-selenium':'review-response-text'}):
          response_body = comment.find('span',attrs={'data-selenium':'review-response-text'}).text.strip()
        else:
          response_body = ''
                
        # 回應日期
        if comment.find('span',attrs={'data-selenium':'review-response-date'}):
          response_time = comment.find('span',attrs={'data-selenium':'review-response-date'}).text.strip()[4:].replace('年','/').replace('月','/').replace('日','')
        else:
          response_time = ''
                
        # 推薦人數
        if comment.find('span',class_='helpful-btn-state'):
          approve_num = re.sub("\D+","",comment.find('span',class_='helpful-btn-state').text.strip())
        else:
          approve_num = ''
                
        data = AgodaItem()
        data['Hotel_id'] = self.id
        data['Star'] = star
        data['Customer_location'] = customer_loc
        data['Trip_type'] = trip_type
        data['Room_type'] = room_type
        data['Living_date'] = living_date
        data['Comment_title'] = comment_title
        data['Comment_body'] = comment_body
        data['Comment_date'] = comment_date
        data['Response_body'] = response_body
        data['Response_time'] = response_time
        data['Approve_number'] = approve_num
        yield data