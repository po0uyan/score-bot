from flask import Flask
import ast

app = Flask(__name__)


@app.route('/')
def hello_world():
    result='''<link rel="stylesheet" type="text/css" href="static/style.css">'''
    result += "<table class='responstable'><tr><th >time</th> <th  >firstname</th><th  >lastname</th><th  >username</th><th  >command</th><th  >chat_id</th><th  >chat type</th></tr>"
    with open('log/loginfo.log', encoding='utf-8') as file:
        contents = file.readlines()
    for item in contents[len(contents)-30:len(contents)]:
        result += "<tr><td  >"+item[0:28]
        res_dic = ast.literal_eval(item[28:-1].strip())
        result += "</td><td  >{0} </td> <td  >{1}</td>  <td  >{2}</td>  <td  >{3}</td>  <td  >{4}</td>  <td  >{5}</td> </tr> ".format(
            res_dic['from']['first_name'], res_dic['from']['last_name'], res_dic['from']['username'], res_dic['text'],
            res_dic['chat']['id'], res_dic['chat']['type'])

    return result+"</table>"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
