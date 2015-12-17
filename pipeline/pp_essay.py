#*-*coding:utf8*-*

import PIL

from core.loader import loader
from core.element import Essay
from core.obj2json import scrapy_obj2json


class DNAEssayPipeline(object):

    def process_item(self,item,spider):
        essay_info = scrapy_obj2json(item) 

        if loader.mongo_lock.acquire():
            loader.mongo.select('adapter_essay',item['ref'])
            loader.mongo.insert_one(essay_info)
            loader.mongo_lock.release()
       
        return item
