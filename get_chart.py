import string
import requests
from leage_name import *


def find_all(a_str, sub, start, end):
    res = ""
    while True:
        start = a_str.find( sub, start, end)

        if start == -1:
            return res
        res += str(start) + "/"
        start += 1


def get_chart(text):
    start = 0
    res_name = ""
    result = ""

    if any(word in text for word in laliga):
        postfix = u'جدول-لیگ-اسپانیا-لالیگا'
    elif any(word in text for word in premier_leageu):
        postfix = u'جدول-لیگ-برتر-لیگ-انگلیس-جزیره'
    elif any(word in text for word in italy):
        postfix = u'جدول-سری-آ-لیگ-ایتالیا'
    elif any(word in text for word in bondeliga):
        postfix = u'جدول-لیگ-آلمان-بوندس-لیگا'
    elif any(word in text for word in iran):
        postfix = u'جدول-لیگ-برتر-خلیج-فارس'
    elif any(word in text for word in france):
        postfix = u'جدول-لیگ-فرانسه-لوشامپیونه'
    else:
        return "  نام لیگ مورد نظر شناسایی نشد :-( \n لطفا نام لیگ مورد نظر را در کنار jadval/ وارد نمایید\n به عنوان مثال:  \n\n /jadval لیگ جزیره \n یا  \n /jadval premier league\n یا \n/jadval englis \n  یا\n/jadval هر چیزی مربوط به لیگ مورد نظر \n\n با تشکر\n ."

    site = 'http://www.tarafdari.ir/' + postfix
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req = requests.get(site, headers=hdr)
    lparser=req.text
    temp = 'class="name"'
    begin = lparser.find( temp, 0, len(lparser))
    endall = lparser.find( "</div>\n</div>\n</div>", begin, len(lparser))
    lparser = lparser[begin:endall]
    # making string shorter
    begin = lparser.find( '</i>', 0, endall) + 4
    end = lparser.find('</s', begin, endall)
    result += lparser[begin:end] + "\n"
    begin = lparser.find('nament">', begin, endall) + 8
    end = lparser.find( '<', begin, endall)
    result += lparser[begin:end] + "\n\n"
    temp = 'ass="name"><a'
    temp = find_all(lparser, temp, 0, endall)
    if (temp) != "":
        res_name = temp.split('/')
    else:
        result = u"جدول مورد نظر موجود نيست"
    for i in range(0, len(res_name) - 1):
        start = int(res_name[i]) + 13
        begin = lparser.find('">', start, len(lparser)) + 2
        end = lparser.find( '<', start, len(lparser))
        res_name[i] = str(i + 1) + "-" + lparser[begin:end] + "\n"
        if i < len(res_name) - 2:
            endall = int(res_name[i + 1])
        else:
            endall = len(lparser)
        temp = '="match">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" بازی:" + lparser[begin:end]
        temp = '="won">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" برد:" + lparser[begin:end]
        temp = '="drawn">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" مساوی:" + lparser[begin:end]
        temp = '="lost">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" باخت:" + lparser[begin:end]
        temp = '"goal_scored">'
        begin = lparser.find(temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" زده:" + lparser[begin:end]
        temp = '"goal_allowed">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" خورده:" + lparser[begin:end]
        temp = '"goal_discord">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find('<', begin, endall)
        res_name[i] += u" تفاضل:" + lparser[begin:end] + "\n"
        temp = '"point">'
        begin = lparser.find( temp, begin, endall) + len(temp)
        end = lparser.find( '<', begin, endall)
        res_name[i] += u" امتیاز:" + lparser[begin:end]
        result += res_name[i] + "\n\n"
    return result + "\n."
