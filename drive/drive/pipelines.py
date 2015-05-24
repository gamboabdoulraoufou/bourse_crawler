# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MySQLPipeline(object):
    
    def __init__(self):
        import MySQLdb
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="drive_database", charset="utf8")


    def process_item(self, item, spider):
        cursor = self.db.cursor()
        
        sql = """insert into drive_database.tt_drive(lien, canal, magasin, categorie1, categorie2, fabriquant, produit, description_produit, detail_produit, prix, detail_prix)
                 values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")""" % (item['lien'], item['canal'], item['magasin'], item['categorie1'], 
                                                                                       item['categorie2'], item['fabriquant'], item['produit'], 
                                                                                       item['description_produit'], item['detail_produit'], item['prix'], item['detail_prix'])
                
        if cursor.execute(sql):
            self.db.commit()
            print 'Insered'
        else:
            print 'Something wrong'
            #self.db.commit()
        return item
        
    def spider_closed(self, spider):
        self.db.commit()
