# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

class Run_Spider_From_SubClass:

    def __init__(self, target_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_url = target_url

        configure_logging()
        self.runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl(self):
        for url in self.target_url:
            yield self.runner.crawl('tripadvisor', url=url)
        reactor.stop()

    def run_spider_in_loop(self):
        self.crawl()
        reactor.run()

def main():
    target_url = ['https://www.tripadvisor.com.tw/Hotel_Review-g13808534-d3435789-Reviews-Millennium_Hotel_Taichung-Xitun_Taichung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806427-d2095241-Reviews-Grand_View_Resort_Beitou-Beitou_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808671-d300627-Reviews-The_Landis_Taipei-Zhongshan_District_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808671-d306432-Reviews-Ambassador_Hotel_Taipei-Zhongshan_District_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806900-d302768-Reviews-The_Sherwood_Taipei-Songshan_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806753-d9723470-Reviews-Courtyard_Taipei-Nangang_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13792546-d306401-Reviews-Maison_de_Chine_Hotel_Taichung-Beitun_Taichung.html#REVIEWS','hhttps://www.tripadvisor.com.tw/Hotel_Review-g13811269-d1411424-Reviews-Dandy_Hotel_Daan_Park_Branch-Da_an_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806451-d1950018-Reviews-CityInn_Hotel_Taipei_Station_Branch_III-Datong_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808557-d306396-Reviews-Chateau_de_Chine_Kaohsiung-Yancheng_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806846-d6888015-Reviews-Kindness_Hotel_Kaohsiung_Main_Station_Front-Sanmin_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806674-d3605095-Reviews-Kindness_Hotel_Kaohsiung_Guang_Rong_Pier-Lingya_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806674-d307863-Reviews-The_Lees_Hotel_Kaohsiung-Lingya_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806674-d5288137-Reviews-Just_Sleep_Kaohsiung_Zhongzheng-Lingya_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808513-d8598482-Reviews-Just_Sleep_Kaohsiung_Station-Xinxing_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806805-d306394-Reviews-Grand_Hi_Lai_Hotel_Kaohsiung-Qianjin_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806805-d4289604-Reviews-Jia_s_inn_Liouhe-Qianjin_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806805-d6216536-Reviews-The_Tree_House-Qianjin_Kaohsiung.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806459-d1459914-Reviews-Hotel_Novotel_Taipei_Taoyuan_International_Airport-Dayuan_Taoyuan.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808400-d6536694-Reviews-Silks_Place_Tainan-West_Central_District_Tainan.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806497-d1201244-Reviews-Shangri_La_s_Far_Eastern_Plaza_Hotel_Tainan-East_District_Tainan.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806886-d661117-Reviews-Hualien_FarGlory_Hotel-Shoufeng_Hualien.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808531-d1936002-Reviews-Xinjhuang_Chateau_de_Chine_Hotel-Xinzhuang_New_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808671-d8263705-Reviews-Cityinn_Hotel_Plus_Fuxing_N_Rd_Branch-Zhongshan_District_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13811269-d1448672-Reviews-Park_Taipei_Hotel-Da_an_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806951-d3654334-Reviews-WESTGATE_Hotel-Wanhua_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13806951-d3134481-Reviews-Via_Hotel-Wanhua_Taipei.html','https://www.tripadvisor.com.tw/Hotel_Review-g13808853-d455561-Reviews-Cosmos_Hotel_Taipei-Zhongzheng_District_Taipei.html']    
    runner = Run_Spider_From_SubClass(target_url)
    runner.run_spider_in_loop()
        

if __name__ == '__main__':
    main()
