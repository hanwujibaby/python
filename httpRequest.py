#下面这句重要，一般用来处理在http请求过程中的中文编码
#-*- coding: UTF-8 -*- 
import urllib
import urllib2
import json
import time
import traceback


def requestSingle(id):
    url = 'http://testurl'
    t=0
    flag=True
    #初始化字典
    _jsonResult={} 
    _time=str(time.time())
    while (t<3 and flag):
        try:
            msg='{"vid":'+id+',"status":1,"timestamp":'+_time+'}'
            values = {'topic' : 'testtopic',
                    'token' : 'testtoken',
                    'msg':msg
                    }
            print msg

            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            _jsonResult=json.loads(the_page)
            response.close()
            flag=False
        except Exception as e:
            print e 
            time.sleep(1)
            t=t+1

    return _jsonResult





f=open('tvdvd.txt','rb')
for line in f:
    requestSingle(line)
f.close()

print "done!"


