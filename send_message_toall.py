import ast
import telegram
bot = telegram.Bot(token='95539936:AAH-GnoFYItZ5mQHXkIqUxFYwG6EnUzC0k0')


def send_to_all(message):
    x = set()
    with open('log/loginfo.log', encoding='utf-8') as file:
        contents = file.readlines()
        for item in contents:
            res_dic = ast.literal_eval(item[28:-1].strip())
            x.add(res_dic['chat']['id'])
        for item in x:
            bot.sendMessage(chat_id=item,text=message)