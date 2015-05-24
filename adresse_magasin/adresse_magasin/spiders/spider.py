# -*- coding: utf-8 -*-


from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from adresse_magasin.items import AdresseItem
from scrapy.selector import Selector


class CarrefourAdresse(CrawlSpider):
    name = 'CarrefourAdresse'
    allowed_domains = ['carrefour.fr']
    
    start_urls = ['http://www.carrefour.fr/nos-magasins/liste-carrefour',
                  'http://www.carrefour.fr/nos-magasins/liste-carrefour-market',
                  'http://www.carrefour.fr/nos-magasins/liste-carrefour-contact',
                  'http://www.carrefour.fr/nos-magasins/liste-carrefour-city',
                  'http://www.carrefour.fr/nos-magasins/liste-carrefour-montagne',
                  'http://www.carrefour.fr/nos-magasins/liste-carrefour-express',
                  'http://www.carrefour.fr/nos-magasins/liste-market']

    rules = (Rule(LinkExtractor(allow=('magasin', )), callback='parse_item'),) 

    def parse_item(self, response):

        item = AdresseItem()
        item['lien'] = response.url
        item['enseigne'] = 'Carrefour'
        item['magasin'] = response.xpath('//div[@class="store-header-sec"]//div[@id="header-showtitle"]//div[@id="header-title"]//h1/text()').extract() 
        item['adresse'] = " | ".join([response.xpath('//div[@class="store-header-sec"]//div[@id="header-content"]//div[@class="inline"]//p[1]/text()').extract()[0], response.xpath('//div[@class="store-header-sec"]//div[@id="header-content"]//div[@class="inline"]//p[3]/text()').extract()[0]]) 
        
        return item
