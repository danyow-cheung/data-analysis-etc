# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv 
class DoubanPipeline:
    def __init__(self):
        self.fp = open("TOP250.csv","w",encoding="utf-8")
        self.wrt = csv.DictWriter(self.fp,["name","fen","words"])
        self.wrt.writeheader()

    def __del__(self):
        self.fp.close()
    
    def process_item(self, item, spider):
        self.wrt.writerow(item)    
        return item
        
