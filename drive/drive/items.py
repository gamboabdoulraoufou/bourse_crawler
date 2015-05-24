# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DriveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lien = scrapy.Field()
    canal = scrapy.Field()
    magasin = scrapy.Field()
    categorie1 = scrapy.Field()
    categorie2 = scrapy.Field()
    fabriquant = scrapy.Field()
    produit = scrapy.Field()
    detail_produit = scrapy.Field()
    description_produit = scrapy.Field()
    prix = scrapy.Field()
    detail_prix = scrapy.Field()


