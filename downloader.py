import threading
import logg
import urllib2
import os 

log = logg.get_logger()
def download(url):
    try:
        image_path = './images_to_test/'+url[-23:]
        if os.path.exists(image_path):
            log.info("file exist!! " +image_path)
            return
        f = open(image_path, 'w')
        response = urllib2.urlopen(url, data=None, timeout=3)
        image_data = response.read()
        f.write(image_data)
        f.close()
        
        if len(image_data) < 100:
            log.error('exception url is '+url+ '   downloading failed: content len < 100')
            return
    except Exception,e:
        #raise Exception('downloading failed: '+str(e) + ' url: '+url)
        return

def run(urls):
    image_datas = {}
    thread_list = []
    for url in urls:
        if len(url.strip())<10:
            log.error('url is too short--'+url+'--end')
            continue
        thread = threading.Thread(target=download,args=(url,))
        thread.start()
        thread_list.append(thread)

    for i in thread_list:
        i.join()



if __name__=='__main__':
    urls = ['http://n.sinaimg.cn/translate/20171113/BQRV-fynshev5746586.jpg','http://n.sinaimg.cn/translate/20171023/LwT2-fymzzpw0275380.jpg']
    run(urls)
    
