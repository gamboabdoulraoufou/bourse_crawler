# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MySQLPipeline(object):
    def __init__(self): # commentire
        import MySQLdb
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="boursorama_database", charset="utf8")

    def process_item(self, item, spider):
        cursor = self.db.cursor()
        print item['lien'][0]
        sql = """insert into boursorama_database.cours_action(lien, entreprise, valeur_ouverture, derniere_valeur, maximum, minimum, volume) 
                 values ("%s","%s","%s","%s","%s","%s", "%s")""" % (item['lien'], item['entreprise'][0], item['valeur_ouverture'][0], 
                                                                    item['derniere_valeur'][0], item['maximum'][0], item['minimum'][0], item['volume'][0])
        if cursor.execute(sql):
            self.db.commit()
            print 'Insered' # commentaire
        else:
            print 'Something wrong'

        #self.db.commit()
        return item

    def spider_closed(self, spider):
        self.db.commit()
