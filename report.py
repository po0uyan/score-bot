from flask import Flask
from pymongo import MongoClient
import jdatetime

app = Flask(__name__)


@app.route('/')
def report():
    client = MongoClient()
    db = client.get_database('score_bot')
    collec = db.get_collection('sc_dataset')
    contents = collec.find().sort([("date",-1)]).limit(100)
    result = '''<link rel="stylesheet" type="text/css" href="static/style.css">'''
    result += "<table class='responstable'><tr><th >time</th> <th  >firstname</th><th  >lastname</th><th  >username</th><th  >command</th><th  >chat_id</th><th  >chat type</th></tr>"
    client.close()
    for item in contents:
        result += "<tr><td  >" + str(jdatetime.datetime.fromtimestamp(item['date']))
        result += "</td><td  >{0} </td> <td  >{1}</td>  <td  >{2}</td>  <td  >{3}</td>  <td  >{4}</td>  <td  >{5}</td> </tr> ".format(
            item['from']['first_name'], item['from']['last_name'], item['from']['username'], item['text'],
            item['chat']['id'], item['chat']['type'])

    return result + "</table>"


@app.route('/registers')
def registers():
    n=0
    client = MongoClient()
    db = client.get_database('score_bot')
    collec = db.get_collection('sc_dataset')
    with open("log/assets.log","a") as f:
        with open("log/assets.log","r") as h:
            h=h.readline()
        for item in collec.distinct("from.id"):
            if str(item) not in h:
                n+=1
                f.write(str(item)+",")
    with open('log/assets.log','r') as f :
        a=f.readline()
        b=a.split(',')
        res=len(b)
    return "<h1>"+"{0} ids has been inserted".format(n)+"</br>this shit :"+str(len(collec.distinct("from.id")))+"</br>totall: "+str(res)+"</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
