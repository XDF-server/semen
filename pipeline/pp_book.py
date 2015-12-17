#*-*coding:utf8*-*

import os 
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

from core.loader import loader
from settings import IMAGES_STORE 
from core.obj2json import scrapy_obj2json

class DNABookPipeline(FilesPipeline):

    @classmethod
    def from_settings(cls, settings):
        cls.FILES_URLS_FIELD = settings.get('FILES_URLS_FIELD', cls.DEFAULT_FILES_URLS_FIELD)
        cls.FILES_RESULT_FIELD = settings.get('FILES_RESULT_FIELD', cls.DEFAULT_FILES_RESULT_FIELD)
        cls.EXPIRES = settings.getint('FILES_EXPIRES', 90)
        store_uri = settings['BOOKS_STORE']
        return cls(store_uri)

    def get_media_requests(self,item,info):
        if 'book_name' in item.keys():
            if isinstance(item['book_name'],str):
                print '下载地址' + item['book_name']
                yield Request(item['book_name'],headers = item['book_header'])

            elif isinstance(item['book_name'],list):
                for url in item['book_name']:
                    yield Request(url,headers = item['book_header'])
            
            else:
                raise DropItem('item contains no files')

    def item_completed(self,results,item,info):
        #print results[0][1].getErrorMessage()
        print results[0][1]

        file_paths = [x['path'] for ok,x in results if ok]
        if not file_paths:
            raise DropItem('item contains no files')

        item['book_name'] = file_paths

       

        return item
