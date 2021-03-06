import requests
from bs4 import BeautifulSoup
import jdatetime
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def get_varzesh3_chart(postfix):

    site = 'http://api.varzesh3.com/v0.2/leaguestat/widget/5/' + postfix
    content = requests.get(site).json()
    result = "{0}\n\n".format(content['Widget']['StageFullName'])
    for i,item in enumerate(content['Table']):

        result += "<b>{1}) {0}</b>\n".format(item['Team'],i+1)
        result += ' بازی: {0} برد:{1} مساوی:{2} باخت:{3} زده:{4} خورده:{5} تفاضل:{6} \n امتیاز:{7}' \
            .format(item['Played'], item['Victories'], item['Draws'], item['Defeats'], item['Made'], item['Let'],
                    item['Diff'], item['Points'])
        result += '\n\n'
    return result +'\n.'


def get_stage_name():
    hresult = []
    day = ""
    score = str(requests.get('http://www.varzesh3.com/livescore', headers=hdr).content, 'utf-8')

    b = BeautifulSoup(score, 'html.parser')

    for link in b.findAll('div', {'class': 'stage-wrapper sport0'}):
        match = link.find('div', {'class': 'stage-name'}).text.strip()
        if match not in hresult:
            hresult.append(match)

    return hresult


def get_score(stage_name):
    result=""
    score = str(requests.get('http://www.varzesh3.com/livescore', headers=hdr).content, 'utf-8')

    b = BeautifulSoup(score, 'html.parser')
    for link in b.findAll('div', {'class': 'stage-wrapper sport0'}):
        match = link.find('div', {'class': 'stage-name'}).text.strip()
        sdate = (link.find('div', {'class': 'start-date'}))
        if match in stage_name:
            result+="<b>✅✅{0}✅✅ </b> \nتاریخ: {1}\n\n".format(match,sdate.text.strip())
            score=(link.findAll('div', {'class': 'scores-container'}))
            rname=(link.findAll('div', {'class': 'teamname right'}))
            lname=(link.findAll('div', {'class': 'teamname left'}))
            stime=(link.findAll('div', {'class': 'start-time'}))

            status=(link.findAll('div', {'class': 'match-status'}))
            for sc, r, l, st, stat in zip(score, rname, lname, stime, status):
                if stat.text.strip() not in ['پایان نیمه اول' , 'نتیجه نهایی']:
                    stat="دقیقه: "+stat.text.strip()
                else:
                    stat=stat.text
                result += "{0} {1} ⚽️ {2} {3} \n{4} \nزمان برگزاری: {5}\n\n".format(r.text.strip(), sc.text.split()[0], sc.text.split()[2], l.text,stat.strip(), st.text.strip())
            result += "\n."

    return result


def get_video():
    a=[]
    video = str(requests.get('http://video.varzesh3.com/', headers=hdr).content, 'utf-8')

    b = BeautifulSoup(video, 'html.parser')

    for link in b.findAll('div', {'class': 'group-bar-clips last-games'}):
        for asb in link.findAll('li'):
            temp=asb.find('a')
            if  'خلاصه بازی ' in temp['title']:
                a.append(temp)
    return a

