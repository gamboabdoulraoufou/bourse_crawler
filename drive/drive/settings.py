# -*- coding: utf-8 -*-

# Scrapy settings for drive project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'drive'

SPIDER_MODULES = ['drive.spiders']
NEWSPIDER_MODULE = 'drive.spiders'



ITEM_PIPELINES = {'drive.pipelines.MySQLPipeline': 300,}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'drive (+http://www.yourdomain.com)'
