import requests
from pip._vendor.html5lib.treebuilders import etree
from xml.etree import ElementTree as etree

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
site = 'http://www.tarafdari.ir/category/all/all/feed.xml'


def get_news():
    req = requests.get(site, headers=hdr)

    taraf = req.text
    reddit_root = etree.fromstring(taraf)
    item = reddit_root.findall('channel/item')
    result = ""
    for entry in item:
        desc = entry.findtext('title')
        list = [u'عکس', u'کلیپ', u'ویدیو', u'تصویر', u'طرفداری', u'بدون شرح', u'خلاصه بازی', u'بسکتبال', u'مچ',
                u'بدمینتون', u'NBA', u'نقل و انتقالات']
        if not any(word in desc for word in list):
            result += desc + "\n\n"
    return result + "\n."
