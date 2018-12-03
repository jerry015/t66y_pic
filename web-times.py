import time
import urls_generator
# import pic_share_url_generator
import pic_downloader
import sys
import ssl
import urllib
import urllib.request
from bs4 import BeautifulSoup

def pic_urls_gen(web_url):
    pic_urls = []

    context = ssl._create_unverified_context()

    try:
        request = urllib.request.Request(web_url)
    except:
        continue
    request.add_header("user-agent","Mozilla/5.0")
    try:
            html_doc = urllib.request.urlopen(request,data=None,timeout=10,context=context)
            html=html_doc.read()
    except:
            return None

    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all('input')

    for link in links:
        picurl= (link.get('data-src'))
        if ((picurl is not None) and (('jpg' in picurl) or ('JPG' in picurl))):
            pic_urls.append(picurl)

    return pic_urls

# purl = sys.argv[1]
x = sys.argv[1]
y = sys.argv[2]
www = "hh.flexui.win"
pages = range(int(x), int(y)+1)

for page in pages:
    print('################  ShiDai Processing Page ' + str(page) + '  ##################')
    purl="https://" + www + "/thread0806.php?fid=8&search=&page=" + str(page)

    urls = urls_generator.urls_gen(purl)
    if urls:
        urls = list(set(urls))
        folder_path = './photo/time_' + str(time.time()).split('.')[0] + "/"

        for url in urls:
            print ("=== Processing "+ str(urls.index(url)+1) + "/" + str(len(urls)) + " url ===")
            picurls = pic_urls_gen(url)
            if picurls:
                # picurls = list(set(picurls))
                pic_downloader.pic_down(picurls,folder_path)
                time.sleep(5)
