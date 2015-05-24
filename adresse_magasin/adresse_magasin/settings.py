# -*- coding: utf-8 -*-

# Scrapy settings for adresse_magasin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'adresse_magasin'

SPIDER_MODULES = ['adresse_magasin.spiders']
NEWSPIDER_MODULE = 'adresse_magasin.spiders'

ITEM_PIPELINES = {'adresse_magasin.pipelines.MySQLPipeline': 300,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'adresse_magasin (+http://www.yourdomain.com)'
