#*-*coding:utf8*-*

import re
import time
from scrapy.exceptions import DropItem
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import sys

from base import Base
from element import *
from loader import loader

class DNA(Spider):
    
    name = ''

    inc_exp = re.compile('INC\((\d*)\|(\d*)\|(\d*)\)')

    def __init__(self,rule):
        self.name = rule.name
        self.site = rule.site

        self.allowed_domains = rule.allow_domains
        self.start_urls = rule.start_urls

        self.inc_list = []
        self.data_list = []

        self.link_allow_exp = rule.link_extractor_allow
        self.link_deny_exp = rule.link_extractor_deny
        self.link_format = rule.link_extractor_format
        self.link_format_data_xpath = rule.link_extractor_format_data
        self.link_format_map = rule.link_format_map

        self.expire = rule.expire
        self.element = rule.element 
        self.item_extractor = rule.item_extractor
        self.cls = rule.cls

        super(DNA,self).__init__()
    
    def parse(self,response):
        print loader.color.ALERT('执行中 ... [%s]' % response.url)
        
        #cur_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        #if expire > 0:
        #    loader.redis.setex(response.url,expire,cur_time)
        #else:
        #    loader.redis.set(response.url,cur_time)

        deep = self._parse_deep(response.url) 
        ret_list = []
        item = self._extract_data(deep,response)
        ret_list.append(item)

        url_list = self._extract_url(deep,response)          
        for url in url_list:
            ret_list.append(Request(url))
    
        return ret_list
    
    def _parse_deep(self,url):
        if url in self.start_urls:
            return 1

        for deep,exp_list in enumerate(self.link_allow_exp):
            for exp in exp_list:
                if exp and exp.match(url):
                    return deep+1

    #链接分析
    def _extract_url(self,deep,response):
        ret_list = []

        if deep < len(self.link_format_map) and self.link_format_map[deep]:
            if len(self.link_format[deep]) and len(self.link_format_data_xpath[deep]):
                for index,link_format in enumerate(self.link_format[deep]):
                    for xpath in self.link_format_data_xpath[deep][index]:
                        inc_match = self.inc_exp.match(xpath)

                        if inc_match:
                            s = int(inc_match.group(1))
                            e = int(inc_match.group(2))
                            i = int(inc_match.group(3))
                            
                            if self.inc_list:
                                for i,y in enumerate([x for x in range(s,e,i)]):
                                    if isinstance(self.inc_list[i],list):
                                        self.inc_list[i].append(y)
                                    else:
                                        tmp_list = [].append(self.inc_list[i])
                                        tmp_list.append(y)
                                        self.inc_list[i] = tmp_list
                            else:
                                self.inc_list = [x for x in range(s,e,i)]
                        else:
                            link_format_data = response.xpath(xpath).extract()
                            #self.data_list = link_format_data
                            self.data_list.append('兴趣')

                    for p in self.data_list:
                        for q in self.inc_list:
                            url = link_format % (p,q)
                            ret_list.append(url)

        if deep < len(self.link_allow_exp):                   
            url_list = response.xpath('//a/@href').extract()
            
            for url in url_list:
                for allow_exp in self.link_allow_exp[deep]:
                    if allow_exp and allow_exp.match(url):
                        allow_flag = True
                        if deep < len(self.link_deny_exp):
                            for deny_exp in self.link_deny_exp[deep]:
                                if deny_exp and deny_exp.match(url):
                                    allow_exp = False

                            if allow_flag:
                                ret_list.append(url)
                        else:
                            ret_list.append(url)
        return ret_list

    #数据分析
    def _extract_data(self,deep,response):
        if deep < len(self.element) and not Base.empty(self.element[deep]):
            eval_str = self.element[deep] + '()'
            item = eval(eval_str)
        else:
            return None

        item['ref'] = self.name

        if deep < len(self.item_extractor):
            for item_dict in self.item_extractor[deep]:
                for key,value in item_dict.items():
                    try:
                        item[key] = response.xpath(value).extract()
                    except KeyError:
                        item.set_value(key,response.xpath(value).extract())

        item.set_value('time',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        return item
