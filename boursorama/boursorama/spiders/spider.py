# -*- coding: utf-8 -*-

# Demo 

#import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from boursorama.items import CoursAction


class MySpider1(CrawlSpider): 
    name = 'boursorama_cours_action' 
    allowed_domains = ['boursorama.com'] 
    start_urls = ['http://www.boursorama.com/bourse/actions/cours_az.phtml'] 

    rules = ( 
        Rule(LinkExtractor(), callback='parse_item'),
    ) 

    def parse_item(self, response):
         
        i = 0
        table = response.xpath('//table[@class="block hover alt list sortserver"]//tbody')
        while(i<len(table)):
            item = CoursAction()
            item['lien'] = response.url
            a = []
            a.append(table.xpath('//td[@class="tdv-libelle"]//a/@title').extract()[i])
            item['entreprise'] = a
            b = []
            b.append(table.xpath('//td[@class="tdv-open"]//span/text()').extract()[i])
            item['valeur_ouverture'] = b
            c = []
            c.append(table.xpath('//td[@class="tdv-last"]//span/text()').extract()[i])
            item['derniere_valeur'] = c
            d = []
            d.append(table.xpath('//td[@class="tdv-high"]//span/text()').extract()[i])
            item['maximum'] = d
            e = []
            e.append(table.xpath('//td[@class="tdv-low"]//span/text()').extract()[i])
            item['minimum'] = e
            f = []
            f.append(table.xpath('//td[@class="tdv-tot_volume"]//span/text()').extract()[i])
            item['volume'] = f

            i+=1

            yield item
