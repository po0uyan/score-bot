import requests
from pip._vendor.html5lib.treebuilders import etree
from xml.etree import ElementTree as etree

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
site = 'http://www.tarafdari.ir/category/all/all/feed.xml'

import requests
from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
site ='https://www.tarafdari.com/'


def get_news():
    result = ""
    a=requests.get(site,headers=hdr)
    b=BeautifulSoup(a.text,'html.parser')
    for i,link in enumerate(b.findAll('a',{'class':'news'}, href=True )):
        if i<35:
            result += link.text+ '\n<a href="{0}{1}">{2}</a>\n \n'.format(site,link['href'], 'ادامه خبر...')
    return result
# def get_news():
#     req = requests.get(site, headers=hdr)
#
#     taraf = req.text
#     try:
#         reddit_root = etree.fromstring(taraf)
#     except :
#
#     item = reddit_root.findall('channel/item')
#     for entry in item:
#         desc = entry.findtext('title')
#
#         list = [u'عکس', u'کلیپ', u'ویدیو', u'تصویر', u'طرفداری', u'بدون شرح', u'خلاصه بازی', u'بسکتبال', u'مچ',
#                 u'بدمینتون', u'NBA', u'نقل و انتقالات']
#         if not any(word in desc for word in list):
#
#     return result
