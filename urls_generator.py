# import cookielib
import urllib
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
# import requests

def urls_gen(purl):
    urls = []
    context = ssl._create_unverified_context()

    requestall = urllib.request.Request(purl)
    requestall.add_header("user-agent","Mozilla/5.0")
    try:
        html_docall = urllib.request.urlopen(requestall,data=None,timeout=10,context=context)
        htmlall= html_docall.read()
    except:
        return None
    
    
    soupall = BeautifulSoup(htmlall,"html.parser")
    linksall = soupall.select('h3 > a')

    for links in linksall:
        picurlall= (links.get('href'))
        if picurlall is not None:
            if 'htm_data' in picurlall:
                urls.append(purl.split('/')[0] + '//' + purl.split('/')[2] + '/' + picurlall)
        # if linksall.index(links) > 13:
        #     break
    
    return urls