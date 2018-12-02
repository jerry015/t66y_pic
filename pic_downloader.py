# import cookielib
import urllib
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
# import requests
import urls_generator


def pic_down(picurls,folder_path):
    for picurl in picurls:
        request2 = urllib.request.Request(picurl) 
        request2.add_header('User-Agent', 'Mozilla/5.0')
        request2.add_header('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5')
        request2.add_header('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
        request2.add_header('Connection', 'keep-alive')

        print ('=== Processing ' + str(picurls.index(picurl)+1) + '/'+ str(len(picurls)) + ' picture ===')
        # print picurl

        context = ssl._create_unverified_context()

        try:
            picc = urllib.request.urlopen(request2,data=None,timeout=30,context=context)
            picc_content = picc.read()
        except:
            print ("Errors, skipping...")
            time.sleep(1)
            continue

        # folder_path = './photo/' + picurls[0].split("/")[-1].split('.')[0] + "/"
        if os.path.exists(folder_path) == False:
            os.makedirs(folder_path)  
                
        img_name = folder_path + str(time.time()).split('.')[0] + '.' + picurl.split("/")[-1].split('.')[-1]
        if os.path.exists(img_name) == True:
            continue
            
        with open(img_name, 'wb') as file:  
            file.write(picc_content)
            file.flush()
            file.close()  
            print ("=== Download Finished ===")
        
        time.sleep(1) 

