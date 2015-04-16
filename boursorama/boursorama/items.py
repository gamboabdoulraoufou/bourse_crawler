# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoursAction(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lien = scrapy.Field()
    entreprise = scrapy.Field()
    valeur_ouverture = scrapy.Field()
    derniere_valeur = scrapy.Field()
    maximum = scrapy.Field()
    minimum = scrapy.Field()
    volume = scrapy.Field()
