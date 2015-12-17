#*-*coding:utf8*-*
#
# Copyright 2015 Adapter
#

import re

import loader
from base import Base
from rule import Rule
from pprint import pprint

"""
    生成器

"""

class Generator(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self._rules = []

        crawl_config = loader.loader.config

        for name,config in crawl_config.items():
            rule = Rule()
        
            rule.name = name

            if 'site' in config.keys():
                rule.site = config['site']
                print(loader.loader.color.INFO('网站名:')) 
                pprint(rule.site)
            
            if 'start_urls' in config.keys():
                rule.start_urls = Base.pack_empty_split(config['start_urls'],',')
                print(loader.loader.color.INFO('起始地址:')) 
                pprint(rule.start_urls)

            if 'allow_domains' in config.keys():
                rule.allow_domains = Base.pack_empty_split(config['allow_domains'],',')
                print(loader.loader.color.INFO('允许的域名:')) 
                pprint(rule.allow_domains)

            if 'link_extractor_allow' in config.keys():
                link_extractor_allow = Base.pack_split(config['link_extractor_allow'],'>>')

                extractor_allow = []
                
                for allow in link_extractor_allow:
                    extractor_allow.append(map(lambda x:re.compile(x) if not Base.empty(x) else None,[x for x in Base.pack_split(allow,',')]))

                rule.link_extractor_allow = extractor_allow
                print(loader.loader.color.INFO('允许的提取信息规则:'))
                pprint(link_extractor_allow)

            if 'link_extractor_deny' in config.keys():
                link_extractor_deny = Base.pack_split(config['link_extractor_deny'],'>>')

                extractor_deny = []
                
                for deny in link_extractor_deny:
                    extractor_deny.append(map(lambda x:re.compile(x) if not Base.empty(x) else None,[x for x in Base.pack_split(deny,',')]))
                
                rule.link_extractor_deny = extractor_deny
                print(loader.loader.color.INFO('过滤的提取信息规则:'))
                pprint(link_extractor_deny)

            if 'link_extractor_format' in config.keys():
                link_extractor_format = Base.pack_split(config['link_extractor_format'],'>>')

                extractor_format = []
                
                for deep,format in enumerate(link_extractor_format):
                    if len(format):
                        rule.link_format_map.append(True)
                    else:
                        rule.link_format_map.append(False)

                    extractor_format.append(Base.pack_split(format,','))
                
                rule.link_extractor_format = extractor_format
                print(loader.loader.color.INFO('提取格式信息规则:'))
                pprint(rule.link_extractor_format)

            if 'link_extractor_format_data' in config.keys():
                link_extractor_format_data = Base.pack_split(config['link_extractor_format_data'],'>>')

                extractor_format_data = []
                
                for format in link_extractor_format_data:
                    item_format = Base.pack_split(format,',')
                    item_format_data = []
             
                    for item in item_format:
                        item_format_data.append(Base.pack_split(item,'+'))

                    extractor_format_data.append(item_format_data)

                rule.link_extractor_format_data = extractor_format_data
                print(loader.loader.color.INFO('提取格式填充数据规则:'))
                pprint(rule.link_extractor_format_data)

            if 'expire' in config.keys():
                rule.expire = 0 if Base.empty(config['expire']) else int(config['expire'])
                print(loader.loader.color.INFO('网站过期时间:'))
                pprint(rule.expire)

            if 'enable' in config.keys():
                rule.enable = True if Base.empty(config['enable']) else bool(config['enable'])
                print(loader.loader.color.INFO('是否生效:'))
                pprint(rule.enable)

            if 'element' in config.keys():
                element = Base.pack_split(config['element'],'>>')
                rule.element = element
                print(loader.loader.color.INFO('提取元素类型:'))
                pprint(rule.element)

            if 'item_extractor' in config.keys():
                item_extractor = Base.pack_split(config['item_extractor'],'>>')

                extractor_item = []
                
                for item in item_extractor:
                    i_item = Base.pack_split(item,',')
                    i_item_list = []
                
                    for i in i_item:
                        d = Base.pack_split(i,'::')
                        if len(d) == 2:
                            i_item_list.append({d[0]:d[1]})
                        else:
                            i_item_list.append({})

                    extractor_item.append(i_item_list)
                rule.item_extractor = extractor_item
                print(loader.loader.color.INFO('提取元素规则:'))
                pprint(rule.item_extractor)

            if 'cls' in config.keys():
                cls = Base.pack_split(config['cls'],',')
                rule.cls = cls
                print(loader.loader.color.INFO('网站类别:'))
                print rule.cls

            if 'patch' in config.keys():
                patch = Base.pack_split(config['patch'],',')
                patch_dict = {}

                for patch_idx,patch_path in enumerate(patch):
                    patch_dict[patch_path] = patch_idx
                   
                rule.patch = patch_dict
                print(loader.loader.color.INFO('补丁pipeline:'))
                print rule.patch

            self._rules.append(rule)

    @property
    def rules(self):
        return self._rules
            

