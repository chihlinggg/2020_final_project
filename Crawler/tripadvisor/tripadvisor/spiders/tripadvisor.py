# -*- coding: utf-8 -*-
from tripadvisor.items import TripadvisorItem
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    def __init__(self,url):
      self.url = url
      self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36','Content-Type': 'application/json'
      }
      super().__init__()
    
    def start_requests(self):
      yield scrapy.Request(url=self.url, callback=self.parse, headers=self.headers)
      
    def parse(self, response):
      soup = BeautifulSoup(response.text, 'lxml')
      last_page = int(soup.find_all(class_='pageNum cx_brand_refresh_phase2')[-1].text)
      for page in range(5,last_page*5,5):
        new_url = response.url.replace('Reviews-','Reviews-or'+str(page)+'-')
        yield scrapy.Request(url=new_url, callback=self.parse_article, headers=self.headers)
        
    def parse_article(self, response):
      # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
      if response.status != 200:
        print('Error - {} is not available to access'.format(response.url))
        return

       # 將網頁回應的 HTML 傳入 BeautifulSoup 解析器, 方便我們根據標籤 (tag) 資訊去過濾尋找
      soup = BeautifulSoup(response.text, 'lxml')
      
      comments = soup.find_all(class_='_2wrUUKlw _3hFEdNs8')
      for comment in comments:
        if comment.find(class_='IRsGHoPm').find('span'):
          text = comment.find(class_='IRsGHoPm').find('span').text.strip().replace(' ','')
        else:
          text = ''

        data = TripadvisorItem()
        data['text'] = text

        yield data
