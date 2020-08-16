import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

class Run_Spider_From_SubClass:

    def __init__(self, id_list, crawl_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_list = id_list
        self.crawl_list = crawl_list
        configure_logging()
        self.runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl(self):
        for i,crawl in enumerate(self.crawl_list):
          for id in self.id_list[i]:
            yield self.runner.crawl(crawl, id=id)
        reactor.stop()

    def run_spider_in_loop(self):
        self.crawl()
        reactor.run()

def main():
    # hotels
    # 君悅,凱撒,圓山,大倉久和,W,晶華,老爺,君品,香格里拉,喜來登
    #target_id = [120725,113094,143924,415060,369485,121325,126702,352321,134169,105536]
    
    # booking
    # 君悅,凱撒,圓山,大倉久和,W,晶華,老爺,君品,香格里拉,喜來登
    #target_id = ['grand-hyatt-taipei-taipei50','caesarpark-taipei','grand-hotel-taipei','the-okura-prestige-taipei','w-taipei','the-regent-taipei','royal-taipei','palais-de-chine','shangri-la-s-far-eastern-plaza-taipei','sheraton-taipei']

    # agoda
    # 君悅,凱撒,圓山,大倉久和,W,晶華,老爺,君品,香格里拉,喜來登
    #target_id = [736992,1368,1885,400142,335043,5718,8885,186460,7767,149]

    target_id = [[120725,113094],['grand-hyatt-taipei-taipei50','caesarpark-taipei']]
    target_crawl = ['hotels','booking']
    runner = Run_Spider_From_SubClass(target_id,target_crawl)
    runner.run_spider_in_loop()
        

if __name__ == '__main__':
    main()
