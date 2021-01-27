import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
import logging
from datetime import datetime
today = datetime.now()
#log_file_path = "/home/chihling/hotel_mix/log/{}_{}_{}.log".format(today.year, today.month, today.day)
#FORMAT = '%(asctime)s %(levelname)s: %(message)s'
#logging.basicConfig(level=logging.ERROR, filename=log_file_path, filemode='a', format=FORMAT)

class Run_Spider_From_SubClass:

    def __init__(self, id_list, crawl_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_list = id_list
        self.crawl_list = crawl_list
        configure_logging()
        self.runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl(self):
        for crawl_ in self.crawl_list:
          for id in range(0,10):
            yield self.runner.crawl(crawl_, id=self.id_list[id][crawl_], hotel_name=self.id_list[id]['hotel_name'])
        reactor.stop()

    def run_spider_in_loop(self):
        self.crawl()
        reactor.run()

def main():

    target_id = [
        {   # 君悅
            'hotel_name':'GrandHyattTaipei',
            'Hotels':120725,
            'Booking':'grand-hyatt-taipei-taipei50',
            'Agoda':736992
        },
        {   # 大地
            'hotel_name':'GaiaHotelTaipei',
            'Hotels':454171,
            'Booking':'the-gaia-hotel',
            'Agoda':569079
        },
        {   # 圓山
            'hotel_name':'GrandHotelTaipei',
            'Hotels':143924,
            'Booking':'grand-hotel-taipei',
            'Agoda':1885
        },
        {   # 大倉久和
            'hotel_name':'OkuraPrestigeTaipei',
            'Hotels':415060,
            'Booking':'the-okura-prestige-taipei',
            'Agoda':400142
        },
        {   # W
            'hotel_name':'W_Taipei',
            'Hotels':369485,
            'Booking':'w-taipei',
            'Agoda':335043
        },
        {   # 晶華
            'hotel_name':'RegentTaipei',
            'Hotels':121325,
            'Booking':'the-regent-taipei',
            'Agoda':5718
        },
        {   # 老爺
            'hotel_name':'RoyalNikkoTaipei',
            'Hotels':126702,
            'Booking':'royal-taipei',
            'Agoda':8885
        },
        {   # 君品
            'hotel_name':'PalaisDeChineHotel',
            'Hotels':352321,
            'Booking':'palais-de-chine',
            'Agoda':186460
        },
        {   # 香格里拉
            'hotel_name':'EasternPlazaHotelTaipei',
            'Hotels':134169,
            'Booking':'shangri-la-s-far-eastern-plaza-taipei',
            'Agoda':7767
        },
        {   # 喜來登
            'hotel_name':'SheratonGrandTaipei',
            'Hotels':105536,
            'Booking':'sheraton-taipei',
            'Agoda':149
        }
    ]
    
    target_crawl = ['Booking']
    #target_crawl = ['hotels','booking','agoda']
    runner = Run_Spider_From_SubClass(target_id,target_crawl)
    runner.run_spider_in_loop()
        

if __name__ == '__main__':
    main()
