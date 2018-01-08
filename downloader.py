import threading
import logg
import urllib2
import os 
import sys
log = logg.get_logger()
def download(url):
    try:
        image_path = './images_to_test/'+url[-23:].strip()
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
    file_path = sys.argv[1]
    f = open(file_path, 'r')
    
    lines = f.readlines()
    step = 20
    for i in range(len(lines)/20):
        end = 20*(i+1)
        start = 20*i
        if end>len(lines): end = len(lines)
        tasks = lines[start:end]
        print('progress '+str(start)+'/'+str(end))
        run(tasks)
    f.close()
    
