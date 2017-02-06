from telegram import ParseMode
import ast
import logging , os
from keyboards_layout import getrow_markup,getmag_markup,start_markup,rate_inline_keyboard_markup,admin_inline_keyboard_markup, \
    get_video_keyboard , get_score_keyboard ,back_to_list_markup,getnews_markup,\
    get_news_keyboard
from telegram.ext import Updater,CommandHandler , MessageHandler, Filters , CallbackQueryHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest,TimedOut, ChatMigrated, NetworkError)
from bot_logger import error_logger , info_logger
import get_chart ,tarafdari_scrapp
from magdictionary import mags
import jdatetime
import requests
from varzesh3_scrapp import get_stage_name, get_score , get_video
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR,filename='log/error.log')
from get_video_from_page import get_url
from pymongo import MongoClient
client=MongoClient()
db=client.get_database('score_bot')
collec=db.get_collection('sc_dataset')


def start(bot, update):
    update.message.reply_text("سلام من اسکور بات هستم؛ اگه حال نداری هر دقیقه سایتای سنگین و پر از تبلیغ ورزشیو چک کنی در خدمتم\n .",reply_markup=start_markup)
    collec.insert_one(ast.literal_eval(str(update.message)))


def get_photo(name,url):
    paper="{0}{1}.jpg".format(name,str(get_valid_date()))
    if os.path.isfile(paper):
        return paper

    with open(paper, mode='wb') as e:
        e.write(requests.get(url).content)
        return paper


def echo(bot, update,user_data):
    if update.message.text== 'جداول رده بندی' :
        bot.sendMessage(chat_id=update.message.chat_id, text="لطفا لیگ مورد نظر را انتخاب کنید",reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text=='آخرین خبر ها':
        bot.sendMessage(chat_id=update.message.chat_id,text="لطفا از بین اخبار داخلی یا خارجی انتخاب نمایید",parse_mode=ParseMode.HTML,reply_markup=getnews_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text=='جدول پخش tv':
        bot.sendMessage(chat_id=update.message.chat_id,text=tarafdari_scrapp.get_tv_chart(),parse_mode=ParseMode.HTML,reply_markup=start_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))


    elif update.message.text == 'داخلی':
        bot.sendMessage(chat_id=update.message.chat_id, text=tarafdari_scrapp.get_inner_news("0"), parse_mode=ParseMode.HTML, reply_markup=get_news_keyboard("i0"))
        user_data['intend'] = "inner"
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text == 'خارجی':
        bot.sendMessage(chat_id=update.message.chat_id, text=tarafdari_scrapp.get_outer_news("0"), parse_mode=ParseMode.HTML, reply_markup=get_news_keyboard("o0"), hide_keyboard=True)
        user_data['intend'] = "outer"
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text== 'نتایج زنده' :
        user_data['lives'] = get_stage_name()
        user_data['intend']="live"
        score_markup=get_score_keyboard(user_data['lives'])
        update.message.reply_text('لطفا دسته مورد نظر را انتخاب نمایید:\n .', reply_markup=score_markup)
        user_data['score_markup']=score_markup
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text == 'دریافت آخرین خلاصه بازی ها':
        user_data['intend']="summary"
        user_data['videos'] = get_video()
        video_markup=get_video_keyboard(user_data['videos'])
        update.message.reply_text('لطفا بازی مورد نظر را انتخاب نمایید:\n .', reply_markup=video_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))

    elif update.message.text== 'بازگشت' :
        bot.sendMessage(reply_markup=start_markup,chat_id=update.message.chat_id,text="لطفا یکی از گزینه های مورد نظر را انتخاب نمایید")
    elif update.message.text== 'لیگ آلمان' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text== 'لیگ برترایران' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text== 'لیگ اسپانیا' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text== 'لیگ فرانسه' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text == 'لیگ جزیره' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text== 'سری آ' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text=='روزنامه':
        bot.sendMessage(chat_id=update.message.chat_id,text="لطفا روزنامه مورد نظر را انتخاب نمایید.",reply_markup=getmag_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))


    elif update.message.text=='خبر ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('khabar',mags['خبر ورزشی'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text=='ایران ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('iran',mags['ایران ورزشی'].format(get_valid_date())),reply_markup=getmag_markup)

    elif update.message.text=='گل':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('gol',mags['گل'].format(get_valid_date())),reply_markup=getmag_markup)


    elif update.message.text == 'نود':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('navad',mags['نود'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text == 'ابرار ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('abrar',mags['ابرار ورزشی'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text == 'استقلال':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('estegh',mags['استقلال'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text == 'شوت':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('shoot',mags['شوت'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text == 'هدف':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('hadaf',mags['هدف'].format(get_valid_date())),reply_markup=getmag_markup)
    elif update.message.text == 'پیروزی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=get_photo('piroozi',mags['پیروزی'].format(get_valid_date())),reply_markup=getmag_markup)

    elif update.message.text == 'امتیاز بده 😁':
        bot.sendMessage(chat_id=update.message.chat_id, text="اگه پسند کردین بهم امتیاز بدین لطفا 👇🏻   ☺️ ",reply_markup=rate_inline_keyboard_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    elif update.message.text == 'ارتباط با ادمین':
        bot.sendMessage(chat_id=update.message.chat_id, text="روی دکمه زیر کلیک کنید",reply_markup=admin_inline_keyboard_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))


def chart(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_chart.get_chart(update.message.text) , reply_markup=getrow_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    except Exception as e :
        error_logger.error(e)


def news(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=tarafdari_scrapp.get_news(), parse_mode=ParseMode.HTML, reply_markup=start_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    except Exception as e :
        error_logger.error(e)


def button(bot, update,user_data):
    if user_data['intend'] == "live":
        query = update.callback_query
        if query.data=="back":
            bot.editMessageText(message_id=query.message.message_id,chat_id=query.message.chat_id,text='لطفا دسته مورد نظر را انتخاب نمایید:\n .', reply_markup=user_data['score_markup'])
        else:
            bot.editMessageText(message_id=query.message.message_id,chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML,text=get_score(user_data['lives'][int(query.data)]),reply_markup=back_to_list_markup)

    elif user_data['intend'] == "summary":
        query = update.callback_query
        response=get_url(user_data['videos'][int(query.data)]['href'])
        bot.editMessageText(message_id=query.message.message_id,chat_id=query.message.chat_id,
                            parse_mode=ParseMode.HTML,
                            text="<a href='{0}'> {1} </a>".format(response,user_data['videos'][int(query.data)]['title']))

    elif user_data['intend'] == "inner":
        query = update.callback_query
        if query.data == "end":
            bot.editMessageText(message_id=query.message.message_id, chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML, text="😊")
            bot.sendMessage(chat_id=query.message.chat_id,
                            parse_mode=ParseMode.HTML, text="لطفا انتخاب نمایید  ", reply_markup=getnews_markup)
        else:
            bot.editMessageText(message_id=query.message.message_id, chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML, text=tarafdari_scrapp.get_inner_news(query.data[1]),
                                reply_markup=get_news_keyboard(query.data))

    elif user_data['intend'] == "outer":
        query = update.callback_query
        if query.data == "end":
            bot.editMessageText(message_id=query.message.message_id, chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML, text="😊")
            bot.sendMessage(chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML, text="لطفا انتخاب نمایید ",reply_markup=getnews_markup)
        else:

            bot.editMessageText(message_id=query.message.message_id, chat_id=query.message.chat_id,
                                parse_mode=ParseMode.HTML, text=tarafdari_scrapp.get_outer_news(query.data[1]), reply_markup=get_news_keyboard(query.data))


def score(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML, text=get_score(),reply_markup=start_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    except Exception as e :
        error_logger.error(e)


def rate(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text="اگه پسند کردین بهم امتیاز بدین لطفا 👇🏻   ☺️ ",reply_markup=rate_inline_keyboard_markup)
        collec.insert_one(ast.literal_eval(str(update.message)))
    except Exception as e :
        error_logger.error(e)


def get_valid_date():
    e = jdatetime.datetime.now()
    if e.weekday()!=6:
        return str(e.date())
    return str(e.replace(year=e.year,month=e.month,day=e.day-1).date())


def error_callback(bot, update, error):

    try:
        raise error
    except Unauthorized as e:
        inf=e.message+"chat id :" + str(update.message.chat_id)
        error_logger.error(inf)
        # remove update.message.chat_id from conversation list
    except BadRequest as e:
        inf = e.message + "chat id :" + str(update.message.chat_id)
        error_logger.error(inf)
        # handle malformed requests - read more below!
    except TimedOut as e :
        inf = e.message + "chat id :" + str(update.message.chat_id)
        error_logger.error(inf)
        # handle slow connection problems
    except NetworkError as e:
        inf = e.message + "chat id :" + str(update.message.chat_id)
        error_logger.error(inf)
        # handle other connection problems
    except ChatMigrated as e:
        inf = e.message + "new chat id :" + str(e.new_chat_id)
        error_logger.error(inf)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError as e :
        inf = e.message
        error_logger.error(inf)
        # handle all other telegram related errors
#eztok: 318165040:AAEiSKoYbEJYnbH3Lputj0u4z487Ujl0z2c
#score_bot :  95539936:AAH-GnoFYItZ5mQHXkIqUxFYwG6EnUzC0k0
updater = Updater(token='95539936:AAH-GnoFYItZ5mQHXkIqUxFYwG6EnUzC0k0')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
chart_handler = CommandHandler('jadval', chart)
news_handler = CommandHandler('news', news)
score_handler = CommandHandler('score', score)
rate_handler = CommandHandler('rate', rate)

echo_handler= MessageHandler(Filters.text , echo,pass_user_data=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(button,pass_user_data=True))

dispatcher.add_handler(chart_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(score_handler)
dispatcher.add_handler(rate_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_error_handler(error_callback)
updater.start_polling()
