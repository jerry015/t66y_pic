import cookielib
import urllib2
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
import requests

def pic_urls_gen(web_url):
    pic_urls = []

    request = urllib2.Request(web_url)
    request.add_header("user-agent","Mozilla/5.0")
    try:
            html_doc = urllib2.urlopen(request,data=None,timeout=60)
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