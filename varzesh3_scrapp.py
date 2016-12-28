import requests


def get_varzesh3_chart(postfix):

    site = 'http://api.varzesh3.com/v0.2/leaguestat/widget/5/' + postfix
    content = requests.get(site).json()
    result = "{0}\n\n".format(content['Widget']['StageFullName'])
    for item in content['Table']:
        result += "<b>{0}</b>\n".format(item['Team'])
        result += ' بازی: {0} برد:{1} مساوی:{2} باخت:{3} زده:{4} خورده:{5} تفاضل:{6} \n امتیاز:{7}' \
            .format(item['Played'], item['Victories'], item['Draws'], item['Defeats'], item['Made'], item['Let'],
                    item['Diff'], item['Points'])
        result += '\n\n'
    return result +'\n.'