import urls_generator
import pic_share_url_generator
import pic_downloader
import sys
import cookielib
import urllib2
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
import requests

def urls_gen(purl):
    urls = []
    requestall = urllib2.Request(purl)
    requestall.add_header("user-agent","Mozilla/5.0")
    try:
        html_docall = urllib2.urlopen()
    except:
        return None
    
    htmlall=html_docall.read()
    
    soupall = BeautifulSoup(htmlall,"html.parser")
    linksall = soupall.select('h3 > a')

    for links in linksall:
        picurlall= (links.get('href'))
        if picurlall is not None:
            if 'htm_data' in picurlall:
                urls.append(purl.split('/')[0] + '//' + purl.split('/')[2] + '/' + picurlall)
        # if linksall.index(links) > 30:
            # break


purl = sys.argv[1]
print purl

# urls = urls_generator.urls_gen(purl)
# print purl
# print purl.split('/')[0] + '//' + purl.split('/')[2] + '/'
# print urls

# picurls=pic_share_url_generator.pic_urls_gen(urls[0])
# print picurls
# pic_downloader.pic_down(picurls)