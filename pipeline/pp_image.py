#*-*coding:utf8*-*

import os 
import PIL
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from core.loader import loader
from core.element import Image
from settings import IMAGES_STORE 
from core.obj2json import scrapy_obj2json


class DNAImagePipeline(ImagesPipeline):
    
    def get_media_requests(self,item,info):
        if item['cover']:
            if isinstance(item['cover'],str):
                yield Request(item.cover)

            if isinstance(item['cover'],list):
                for url in item['cover']:
                    yield Request(url)

    def item_completed(self,results,item,info):
        file_paths = [x['path'] for ok,x in results if ok]

        if not file_paths:
            raise DropItem('item contains no files')

        image = Image()
        image['name'] = ''.join(item['name'])
        image['url'] = ''.join(file_paths)
        img = PIL.Image.open(IMAGES_STORE + '/' + ''.join(file_paths))
        image['weight'] = img.size[0]
        image['height'] = img.size[1]  
        item['cover'] = ''.join(file_paths)
        image['cls'] = item['cls']

        image_info = scrapy_obj2json(image)

        if loader.mongo_lock.acquire():
            loader.mongo.select('adapter_image',item['ref'])
            loader.mongo.insert_one(image_info)
            loader.mongo_lock.release()

        return item
