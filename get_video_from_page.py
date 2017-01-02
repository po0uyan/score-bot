from bs4 import BeautifulSoup
import requests


def get_url(data):
    site='http://video.varzesh3.com'+str(data)
    vid=BeautifulSoup(requests.get(site).content,'html.parser')
    b=vid.find('ul',{'class':'video-options-text'})
    return str(b.findAll('a')[1]['href'])