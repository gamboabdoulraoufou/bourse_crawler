# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AdresseItem(scrapy.Item):
    lien = scrapy.Field()
    enseigne = scrapy.Field()
    magasin = scrapy.Field()
    adresse = scrapy.Field()


