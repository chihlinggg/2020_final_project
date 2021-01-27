# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

class Run_Spider_From_SubClass:

    def __init__(self, id_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_list = id_list

        configure_logging()
        self.runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl(self):
        for id in self.id_list:
            yield self.runner.crawl('hotels', id=id)
        reactor.stop()

    def run_spider_in_loop(self):
        self.crawl()
        reactor.run()

def main():
    # 君悅,凱撒,圓山,大倉久和,W,晶華,老爺,君品,香格里拉,喜來登
    #target_id = [120725,113094,143924,415060,369485,121325,126702,352321,134169,105536]
    
    target_id = [120725]
    runner = Run_Spider_From_SubClass(target_id)
    runner.run_spider_in_loop()
        

if __name__ == '__main__':
    main()
