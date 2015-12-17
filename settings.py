#*-*coding:utf8*-*

#爬虫名称
BOT_NAME = 'semen'

#日志路径
LOG_FILE = 'log/semen.log'
#日志级别
#LOG_LEVEL = 'INFO'

#防ban，禁止cookie
COOKIES_ENABLED=False

#防ban，设置下载延时
DOWNLOAD_DELAY=1
#并行处理items数量
CONCURRENT_ITEMS = 100
#最大并行request数量
CONCURRENT_REQUESTS = 16
#每个域名最大并行请求数量
CONCURRENT_REQUESTS_PER_DOMAIN = 20
CONCURRENT_REQUESTS_PER_IP = 0

DEPTH_LIMIT = 0
DEPTH_PRIORITY = 0
DNSCACHE_ENABLED = True

#跟据网络延迟，分析出scrapy服务器和网站的响应速度，动态改变网站下载延迟
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3.0
AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 10

#防ban，设置下载中间件
DOWNLOADER_MIDDLEWARES = {
    'middleware.user_agent.RandomUserAgent':1,
    'scrapy_crawlera.CrawleraMiddleware': 600,
}

#pipeline
ITEM_PIPELINES = {
#    'pipeline.pp_image.DNAImagePipeline': 900,
#    'pipeline.pp_essay.DNAEssayPipeline': 901,
    'pipeline.pp_book.DNABookPipeline' : 902
}

#图片下载设置
IMAGES_STORE = '/adapter/image'
#书籍下载地址
BOOKS_STORE = '/adapter/book'

#缩略图设置
IMAGES_THUMBS = {
    'small': (100,100),
    'big': (270,270),
}
#使用crawlera作为第三方proxy
CRAWLERA_ENABLED = False 
CRAWLERA_USER = 'e6e515cdefbb41dfa7ec5f4b755c368b'
CRAWLERA_PASS = 'zhang1990'


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

#mongo设置
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_TIMEOUT = 2

#redis设置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_AUTH = 'adapter2015'
REDIS_DB = 8
REDIS_TIMEOUT = 2
REDIS_CHARSET = 'utf8'

#任务调度器设置
SCHEDULER_PERSIST = False
QUEUE_KEY = '%(spider)s:request'
QUEUR_CLASS = ''
DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

#使用graphite做监控
#STATS_CLASS = 'scrapygraphite.GraphiteStatsCollector'
#GRAPHITE_HOST = "localhost"
#GRAPHITE_PORT = 2003

#增加DNS解析的线程池数量
REACTOR_THREADPOOL_MAXSIZE = 20

#禁止重试
RETRY_ENABLED = False

#减少超时时间
DOWNLOAD_TIMEOUT = 15

#重定向设置
REDIRECT_ENABLED = True

#ajax设置
AJAXCRAWL_ENABLED = False
