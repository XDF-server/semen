#!/usr/bin/python2.7
#*-*coding:utf8*-*

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import settings
from core.loader import loader

if __name__ == '__main__':
    loader.load_color()
    print loader.color.NOTICE('配色方案加载成功!')
    loader.load_config('map.cfg')
    print loader.color.NOTICE('配置加载成功!')
    loader.load_generator()
    print loader.color.NOTICE('生成器加载成功!')
    loader.load_color()
    print loader.color.NOTICE('配色方案加载成功!')
    loader.load_mongo()
    print loader.color.NOTICE('Mongo加载成功!')
    print loader.color.NOTICE('Semen启动!')
    
    

    from core.dna import DNA

    for idx,rule in enumerate(loader.generator.rules):
        print loader.color.ALERT('执行规则%d ...' % (idx + 1))
        cfg = Settings()
        cfg.setmodule(settings)
        pipelines = cfg.getdict('ITEM_PIPELINES')
        pipelines = dict(pipelines,**rule.patch)
        cfg.set('ITEM_PIPELINES',pipelines)
        process = CrawlerProcess(cfg)
        process.crawl(DNA,rule)
        process.start()

    print loader.color.NOTICE('Semen结束!')

