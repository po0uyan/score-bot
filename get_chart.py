import string
import requests
from leage_name import *
from findall import find_all
from varzesh3_scrapp import get_varzesh3_chart

def get_chart(text):
    res_name = ""
    result = ""

    if any(word in text for word in laliga):
        postfix = '347'
    elif any(word in text for word in premier_leageu):
        postfix = '334'
    elif any(word in text for word in italy):
        postfix = '351'
    elif any(word in text for word in bondeliga):
        postfix = '335'
    elif any(word in text for word in iran):
        postfix = '346'
    elif any(word in text for word in france):
        postfix = '336'
    else:
        return "در این قسمت میتوانید از کیبورد استفاده کنید و لیگ مورد نظر را انتخاب نمایید و یا اینکه نام لیگ را به صورت زیر وارد نمایید نام لیگ هر شکلی نوشته شود اسکور بات منظور شما را می فهمد ، به عنوان مثال : \n\n /jadval انگلیس \n\n یا \n\n /jadval premier  \n\n  یا \n\n /jadval jazire  \n\n  و یا هر ترکیب دیگر از لیگ های دیگر \n ."

    return get_varzesh3_chart(postfix)
