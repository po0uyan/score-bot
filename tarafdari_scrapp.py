import requests
from pip._vendor.html5lib.treebuilders import etree
from xml.etree import ElementTree as etree
import requests
from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
site ='https://www.tarafdari.com/sites/default/files/apps/static/nodes/all/'
tarafdari="https://www.tarafdari.com/"

def get_news():
    result = ""
    a=requests.get(site,headers=hdr)
    b=BeautifulSoup(a.text,'html.parser')
    for i,link in enumerate(b.findAll('a',{'class':'news'}, href=True )):
        if i<35:
            result += link.text+ '\n<a href="{0}{1}">{2}</a>\n \n'.format(site,link['href'], 'ادامه خبر...')
    return result


def get_inner_news(index):
    result=""
    a = requests.get("{0}996/{1}.json".format(site,index),headers=hdr).json()
    for item in a:
        result += item['title']+ '\n<a href="{0}node/{1}">{2}</a>\n \n'.format(tarafdari,item['nid'], 'ادامه خبر...')
    return result


def get_outer_news(index):
    result=""
    a = requests.get("{0}995/{1}.json".format(site,index),headers=hdr).json()
    for item in a:
        result += item['title']+ '\n<a href="{0}node/{1}">{2}</a>\n \n'.format(tarafdari,item['nid'], 'ادامه خبر...')
    return result


def get_tv_chart():
    result="📺 پخش زنده تلویزیونی 📺\n"
    req = requests.get(tarafdari, headers=hdr).content
    res = BeautifulSoup(req, 'html.parser')
    for item in res.find_all('div', {'class': 'cast'}):
        result+="\n{0}\n\n ♻️\n ".format(item.text)

    return result+"\n."
