# import cookielib
import urllib
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
# import requests

def pic_urls_gen(web_url):
    pic_urls = []

    context = ssl._create_unverified_context()

    request = urllib.request.Request(web_url)
    request.add_header("user-agent","Mozilla/5.0")
    try:
        html_doc = urllib.request.urlopen(request,data=None,timeout=10,context=context)
        html=html_doc.read()
    except:
        return None

    soup = BeautifulSoup(html,"html.parser")
    links = soup.select('div > img')

    for link in links:
        picurl= (link.get('data-src'))
        if ((picurl is not None) and (('jpg' in picurl) or ('JPG' in picurl))):
            pic_urls.append(picurl)
        if ((picurl is not None) and (('gif' in picurl) or ('GIF' in picurl))):
            pic_urls.append(picurl)
    return pic_urls