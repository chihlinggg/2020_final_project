# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
from pathlib import Path
from datetime import datetime
from scrapy.exceptions import DropItem
import pymongo  
from urllib import parse
#from scrapy.conf import settings 

class ItemPipeline(object):
    def process_item(self, item, spider):
        # 把資料轉成字典格式
        if not isinstance(item, dict):
            item = dict(item)
        # 轉結構
        new_item = item.copy()
        del new_item['comment_date']
        del new_item['checkin_date']
        del new_item['response_date']
        new_item.update({'time':{}})
        new_item['time'].update({'comment':item['comment_date'],'checkin':item['checkin_date'],'response':item['response_date']})
        new_item.update({'labels':{}})
        return new_item

class MongoDBPipeline(object):

    def open_spider(self, spider):
        user = parse.quote_plus("root")
        passwd = parse.quote_plus("tu3@49cgjw")
        self.client = pymongo.MongoClient('mongodb://{}:{}@localhost:27017/'.format(user,passwd))
        self.db = self.client['test']
        self.coll = self.db[spider.name]
        # 取得資料庫已有的評論
        myquery = { 'hotel_id': spider.id }
        mydoc = self.coll.find(myquery)
        self.record = []
        for com_id in mydoc:
            self.record.append(com_id['comment_id'])

    def process_item(self, item, spider):
        if item['comment_id'] not in self.record:
            self.insert_article(item)
            return item
        else:
            raise DropItem('Already have %s' % item)

    def insert_article(self, item):
        item = dict(item)
        self.coll.insert_one(item)

    def close_spider(self, spider):
        self.client.close()


class JSONPipeline(object):
    def open_spider(self, spider):
        self.start_crawl_datetime = datetime.now().strftime('%Y%m%dT%H:%M:%S')

        # 在開始爬蟲的時候建立暫時的 JSON 檔案
        # 避免有多筆爬蟲結果的時候，途中發生錯誤導致程式停止會遺失所有檔案
        self.dir_path = Path(__file__).resolve().parents[1] / 'crawled_data' / spider.name
        self.runtime_file_path = str(self.dir_path / '.tmp.json.swp')
        if not self.dir_path.exists():
            self.dir_path.mkdir(parents=True)
        spider.log('Create temp file for store JSON - {}'.format(self.runtime_file_path))

        # 設計 JSON 存的格式為
        # [
        #  {...}, # 一筆爬蟲結果
        #  {...}, ...
        # ]
        self.runtime_file = open(self.runtime_file_path, 'w+', encoding='utf8')
        self.runtime_file.write('[\n')
        self._first_item = True

    def process_item(self, item, spider):
        if self._first_item:
            self._first_item = False
        else:
            self.runtime_file.write(',\n')

        self.runtime_file.write(json.dumps(item, ensure_ascii=False))
        return item

    def close_spider(self, spider):
        # 儲存 JSON 格式
        self.runtime_file.write('\n]')
        self.runtime_file.close()
    
        # 以爬蟲的 board name + 日期當作存檔檔名
        self.store_file_path = self.dir_path / '{id}-{datetime}.json'.format(id=spider.id,datetime=datetime.now().strftime('%Y%m%d%H%M%S'))

        self.store_file_path = str(self.store_file_path)
        os.rename(self.runtime_file_path, self.store_file_path)
        spider.log('Save result at {}'.format(self.store_file_path))