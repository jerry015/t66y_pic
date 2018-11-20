import time
import urls_generator
import pic_share_url_generator
import pic_downloader
import sys

# purl = sys.argv[1]
purl="https://cf.cbcb.us/thread0806.php?fid=16&search=&page=3"

urls = urls_generator.urls_gen(purl)


for url in urls:
    print "=== Processing "+ str(urls.index(url)) + "/" + str(len(urls)) + " url ==="
    picurls = pic_share_url_generator.pic_urls_gen(url)
    pic_downloader.pic_down(picurls)
    time.sleep(5)
