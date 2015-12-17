#*-*coding:utf8*-*

import re
import urllib,urllib2

from core.patch import Patch

class DoubanBook(Patch):

    def process_item(self,item,spider):
        item = self._get_book_info(item)
        item = self._get_book_download_url(item)
        return item

    def _get_book_info(self,item):
        info = ''.join(item['info'])
        soup = self.load(info)
        span = soup.find_all('span',class_ = 'pl')
        for s in span:
            if s.text == ' 作者'.decode('utf8'):
                item.set_value('author',s.next_sibling.next_sibling.text)
            elif s.text == ' 译者'.decode('utf8'):
                item.set_value('translator',s.next_sibling.next_sibling.text)
            elif s.text == '出版社:'.decode('utf8'):
                item.set_value('publisher',s.next_sibling)
            elif s.text == '出版年:'.decode('utf8'):
                item.set_value('publish_year',s.next_sibling)
            elif s.text == '页数:'.decode('utf8'):
                item.set_value('pages',s.next_sibling)
            elif s.text == '定价:'.decode('utf8'):
                item.set_value('price',s.next_sibling)
            elif s.text == '装帧:'.decode('utf8'):
                item.set_value('decor',s.next_sibling)
            elif s.text == 'ISBN:'.decode('utf8'):
                item.set_value('isbn',s.next_sibling)

        item.del_value('info')

        return item

    def _get_book_download_url(self,item):
        data = {'q':''.join(item['name']).encode('utf8'),'entry':'1','s':'10263254841959873673','nsid':'3'}
        search_book_url =  "http://so.chnxp.com.cn/cse/search?%s" % urllib.urlencode(data)
        html = urllib2.urlopen(search_book_url).read()
        soup = self.load(html)
        search_result = soup.find_all(cpos = 'title')
        web_site = 'http://www.chnxp.com.cn/'
        download_url = ''
        print search_book_url
        if (len(search_result) > 0):
            book_url = search_result[0]['href']
            if re.match(r'http://www\.chnxp\.com\.cn/soft/[0-9-]*/(\d)*\.html',book_url):
                book_html = urllib2.urlopen(book_url).read()
                sp = self.load(book_html)
                download_node = sp.find_all('ul',class_ = 'download-list')
                if download_node:
                    downloaded = web_site + download_node[0].li.a['href']
                    #match = re.match(r'/e/DownSys/DownSoft/\?classid=(\d*)&id=(\d*)&pathid=(\d)',downloaded)
                    if downloaded:
                        download_html = urllib2.urlopen(downloaded).read()
                        s = self.load(download_html)
                        download_url = s.find_all('span',class_ = 'date')[0].a['href']
                        download_url = 'http://www.chnxp.com.cn/e/DownSys' + download_url[2:]
            
                        item.set_value('book_name',download_url)
                        headers = {
                                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                    "Accept-Encoding":"gzip, deflate, sdch",
                                    "Accept-Language":"zh-CN,zh;q=0.8",
                                    "Connection":"keep-alive",
                                    "Host":"www.chnxp.com.cn",
                                    "Referer":downloaded,
                                    "Upgrade-Insecure-Requests":1
                                 }

                        print '地址:' + download_url
                        request = urllib2.Request(download_url)
                        for key,value in headers.items():
                            request.add_header(key,value)
                        
                        print urllib2.urlopen(request).read()                    
                        
                        book_header = {
                                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                        "Accept-Encoding":"gzip, deflate, sdch",
                                        "Accept-Language":"zh-CN,zh;q=0.8",
                                        "Connection":"keep-alive",
                                        "Host":"pdf1.chnxp.com.cn",
                                        "Referer":downloaded,
                                        "Upgrade-Insecure-Requests":1
                                      }

                        item.set_value('book_header',book_header)

        return item
