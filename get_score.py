from findall import find_all
import requests


hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def get_score():
    start = 0
    res_score = ""
    res_stage = ""
    result = ""
    thisurl = "http://www.varzesh3.com/livescore/"
    temp = 'class="stage-name"'
    lparser=str(requests.get(thisurl,headers=hdr).content,'utf-8')
    begin = lparser.find( temp, 0, len(lparser))
    end = lparser.find("<script>", begin, len(lparser))
    lparser = lparser[begin:end]
    # making string shorter


    temp = 'class="stage-name"'
    temp = find_all(lparser, temp, 0, end)
    if (temp) != "":
        res_stage = temp.split('/')
    else:
        result = u"در حال حاضر بازی ای انجام نمی شود :-)"
    for i in range(0, len(res_stage) - 1):
        temp = "teamname right"
        start = int(res_stage[i])
        begin = int(res_stage[i]) + 19
        end = lparser.find("</d", start, len(lparser))
        res_stage[i] = lparser[begin:end]
        if i < len(res_stage) - 2:
            end = int(res_stage[i + 1])
        else:
            end = len(lparser)
        temp = find_all(lparser, temp, start, end)
        if (temp) == "":
            break
        res_rteamname = temp.split('/')
        for j in range(0, len(res_rteamname) - 1):
            begin = int(res_rteamname[j]) + 16
            end = lparser.find("</d", begin, len(lparser))
            res_rteamname[j] = lparser[begin:end]
        temp = "teamname left"

        if i < len(res_stage) - 2:
            end = int(res_stage[i + 1])
        else:
            end = len(lparser)
        temp = find_all(lparser, temp, start, end)
        if (temp) != "":
            res_lteamname = temp.split('/')
        for j in range(0, len(res_lteamname) - 1):
            begin = int(res_lteamname[j]) + 15
            end = lparser.find("</d", begin, len(lparser))
            res_lteamname[j] = lparser[begin:end]

        temp = "</div><!--/.score.ri"
        if i < len(res_stage) - 2:
            end = int(res_stage[i + 1])
        else:
            end = len(lparser)
        temp = find_all(lparser, temp, start, end)
        if (temp) == "":
            break
        res_score = temp.split('/')
        for j in range(0, len(res_score) - 1):
            begin = int(res_score[j]) - 2
            if lparser[begin] == '>':
                begin += 1
                end = int(res_score[j])

            else:
                begin = int(res_score[j]) - 22
                end = begin + 1
                res_score[j] = " " + lparser[begin - 42] + " (" + lparser[begin:end] + ") "
                continue
            res_score[j] = lparser[begin:end]

        result += res_stage[i] + "\n\n"
        for i in range(0, len(res_lteamname) - 1):
            result += res_rteamname[i] + ": " + res_score[2 * i] + "  -  " + res_score[2 * i + 1] + " :" + \
                      res_lteamname[i] + "\n\n"
    result += " \n."
    return result