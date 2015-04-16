# -*- coding: utf-8 -*-

# Scrapy settings for boursorama project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'boursorama'

SPIDER_MODULES = ['boursorama.spiders']
NEWSPIDER_MODULE = 'boursorama.spiders'

ITEM_PIPELINES = {'boursorama.pipelines.MySQLPipeline': 300,}

#FEED_URI='mycrawler-results3.csv'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'boursorama (+http://www.yourdomain.com)'
