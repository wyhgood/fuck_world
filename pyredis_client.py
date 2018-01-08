#coding=utf-8
'''批量读取redis内key value数据'''

import redis
import json
import logg

r = redis.StrictRedis(host='rm22930.eos.grid.sina.com.cn', port=22930, db=0)

log = logg.get_logger()

def scan_keys(number_keys):
    assert type(number_keys) is int  
    print(type(r))
    count = 0
    for key in r.scan_iter():
        value = r.get(key)
        if len(value) <10: continue
        value2 = value.replace("'", '"')
        d = json.loads(value2)
        print(d['url'] + "####"+str(d['value']))
        log.info(d['url'] + "####"+str(d['value']))
        count+=1
        if count >= number_keys: return

    

def run():
    pass




if __name__ == '__main__':
    scan_keys(270000)
