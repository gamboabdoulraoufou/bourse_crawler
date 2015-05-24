# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MySQLPipeline(object):
    
    def __init__(self):
        import MySQLdb
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="adresse_database", charset="utf8")
        

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = """insert into adresse_database.tt_adresse_magasin(lien, enseigne, magasin, adresse) 
                                                         values ("%s", "%s", "%s", "%s")""" % (item['lien'], item['enseigne'][0], item['magasin'][0], item['adresse'])
                  
        if cursor.execute(sql):
            self.db.commit()
            print 'Insered'
        else:
            print 'Something wrong'
            #self.db.commit()
        return item
        
    def spider_closed(self, spider):
        self.db.commit()
