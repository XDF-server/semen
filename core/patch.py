#*-*coding:utf8*-*

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '请安装beautiful soup'

class Patch(object):

    def load(self,html):
        soup = BeautifulSoup(html,'lxml')
        return soup
