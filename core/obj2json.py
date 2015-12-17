#coding:utf8

try: 
    import simplejson as json
except ImportError: 
    import json

def scrapy_obj2json(obj):
    rst = json.loads(json.dumps(obj,cls=Obj2JsonEncoder))
    r_rst = _iter(rst)
    return r_rst

def obj2json(obj):
    rst = json.loads(json.dumps(obj,cls=Obj2JsonEncoder))
    return rst

def _iter(rst):
    for k,v in rst.items():
        if isinstance(v,dict):
            r = _iter(v)
            rst[k] = r

        if k == '_values':
            return v


def _obj2dict(obj):
    #基本数据类型          
    if not hasattr(obj,'__dict__'):
        return obj

    rst = {}

    for k,v in obj.__dict__.items():
        #内置属性
        if k.startswith('-'):
            continue
        
        if isinstance(v,list):
            ele = [_obj2dict(item) for item in v]
        else:
            ele = _obj2dict(v)
        
        rst[k] = ele 

    return rst

class Obj2JsonEncoder(json.JSONEncoder):
    
    def default(self,obj):

        return _obj2dict(obj)   
  
if __name__ == '__main__': 
    from scrapy import Field             
    from scrapy import Item
    class A(Item):
        name = Field()
        sex = Field()
        age = Field()
        obj = Field()
        #name = ''
        #sex = ''
        #age = 0
        #obj = None

    class B(Item):
        u = Field()
        d = Field()
        #u = ''
        #d = None

    a = A()
    b = B()
    b['u']= 'jldsjf'
    b['d'] = 132
    a['name'] = 'zhang'
    a['sex'] = 'female'
    a['age'] = 13
    a['obj'] = b

    s = scrapy_obj2json(a)
    print s
