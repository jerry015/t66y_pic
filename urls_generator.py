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
        html_docall = urllib2.urlopen(requestall,data=None,timeout=10)
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
    
    return urls