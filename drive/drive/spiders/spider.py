# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from drive.items import DriveItem
from scrapy.selector import Selector
from selenium import webdriver
from pyvirtualdisplay import Display
import time


class CarrefourDrive1(CrawlSpider):
    name = 'CarrefourDrive1'
    allowed_domains = ['carrefour.fr', 'courses.carrefour.fr']    
    start_urls = ['http://courses.carrefour.fr/drive/accueil']

    #rules = (Rule(LinkExtractor(allow=('(drive|PID1)', )), callback='parse_item'),) 
    #rules = (Rule(SgmlLinkExtractor(), callback='parse_item', follow=True),) 
    #rules = (Rule(callback='parse_item'),)
    rules = (Rule(LinkExtractor(), callback='departement'),)

    def __init__(self):
        CrawlSpider.__init__(self)
        self.display = Display(visible=0, size=(1024, 768)) 
        self.display.start()
        self.browser = webdriver.Firefox()

    def __del__(self):
        self.browser.close()
        self.display.stop()

    def departement(self, response):
        self.browser.get(response.url)
        time.sleep(3)
        hxs = Selector(text=self.browser.page_source)
        liste_departement = hxs.xpath('//div//select[@id="fldDropDepartment"]//option/@value').extract()
        return liste_departement
        
    def parse_item():
        item = DriveItem()

        liste_departement[0]
        item['lien'] = response.url
        item['canal'] = hxs.xpath('//div//select[@id="fldDropDepartment"]//optin/@value').extract() #hxs.xpath('//div[@class="type"]//h3[@class="heading"]//span/text()').extract() 
        item['magasin'] = hxs.xpath('//div[@id="sub-header"]//div//div[@class="shop"]//h3[@class="heading"]//span//a[@class="page"]/text()').extract() 
        item['categorie1'] = 'rr' #hxs.xpath('//div[@class="navBreadcrumb"]//ol//li[@class="last"]//a[@class="page"]/text()').extract()
        item['categorie2'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract() # achanger
        item['fabriquant'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract()
        item['produit'] = 'rr' #hxs.xpath('//div[@class="productHead"]//h1[@class="heading"]//span/text()').extract() 
        item['description_produit'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract() # a changer
        item['detail_produit'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract() # a changer
        item['prix'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract() # a changer
        item['detail_prix'] = 'rr' #hxs.xpath('//div[@class="productHead"]//div[@class="brand"]//div[@class="name"]/text()').extract() # a changer
        
        return item
