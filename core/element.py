#*-*coding:utf8*-*

from scrapy import Item
from scrapy import Field

class Adapter(Item):
    
    def set_value(self,key,value):
        self._values[key] = value

    def del_value(self,key):
        return self._values.pop(key)

class Cls(Adapter):
    cls_id = 0
    name = ''

class Text(Adapter):
    text_id = ''
    element = 'text'
    content = ''
    style = 0
    format = 0
    datail = ''


class Image(Adapter):
    imgage_id = ''
    element = 'image'
    name = Field()
    url = Field()
    cls = Field()
    height = Field()
    weight = Field()
    style = Field()
    format = Field()
    expand = Field()
    ref = Field()

class Formula(Adapter):
    formula_id = ''
    element = 'formula'
    conent = ''
    cls = []
    schema = ''
    detail = ''

class Music(Adapter):
    music_id = ''
    element = 'music'
    url = ''
    name = ''
    album = None
    cls = []
    artist = None
    ref = ''

class Video(Adapter):
    video_id = ''
    element = 'video'
    url = ''
    name = ''
    cls = []
    director = None
    artist = None
    bgm = None
    ref = ''

class Paragraph(Adapter):
    paragraph_id = 0
    element = 'paragraph'
    content = []

class Essay(Adapter):
    essay_id = ''
    element = 'essay'
    title = ''
    cover = None
    schema = ''
    subtitle = ''
    cls = []
    cover = None
    author = None
    content = []
    ref = []

class Book(Adapter):
    book_id = ''
    element = 'book'
    name = Field()
    schema = Field()
    cover = Field()
    author = Field()
    cls = Field()
    catalog = Field()
    ref = Field()
    cls = Field()
    rank = Field()

class Person(Adapter):
    person_id = ''
    element = 'person'
    name = ''
    schema = ''
    cover = None
    gender = 0
    age = 0
    phone = ''
    email = ''
    school = []
    job = []
    friend = []
    read = []
        
class School(Adapter):
    school_id = ''
    element = 'school'
    name = ''
    cover = None
    schema = ''
    country = ''
    city = ''
    address = ''
    
class Job(Adapter):
    job_id = ''
    element = 'job'
    name = ''
    schema = ''
    cover = None

class Album(Adapter):
    album_id = ''
    element = 'album'
    artist = None
    music = []
