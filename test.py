from telegram import ParseMode
import logging
from keyboards_layout import getrow_markup,getmag_markup,start_markup,rate_inline_keyboard_markup
from telegram.ext import Updater,CommandHandler , MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,TimedOut, ChatMigrated, NetworkError)
from bot_logger import error_logger , info_logger
import get_chart ,get_news,get_score
from magdictionary import mags
import jdatetime
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR,filename='log/error.log')


def start(bot, update):
    update.message.reply_text("سلام من اسکور بات هستم؛ اگه حال نداری هر دقیقه سایتای سنگین و پر از تبلیغ ورزشیو چک کنی در خدمتم\n .",reply_markup=start_markup)
    info_logger.info(update.message)


def echo(bot, update):
    if update.message.text== 'جداول رده بندی' :
        bot.sendMessage(chat_id=update.message.chat_id, text="لطفا لیگ مورد نظر را انتخاب کنید",reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'rade bandi'))

    elif update.message.text=='آخرین خبر های ورزشی':
        bot.sendMessage(chat_id=update.message.chat_id,text=get_news.get_news(),parse_mode=ParseMode.HTML,reply_markup=start_markup)
        info_logger.info(str(update.message).replace(update.message.text,'news'))
   
    elif update.message.text== 'نتایج زنده' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_score.get_score(),reply_markup=start_markup)
        
        info_logger.info(str(update.message).replace(update.message.text ,'live score'))

    elif update.message.text== 'بازگشت' :
        bot.sendMessage(reply_markup=start_markup,chat_id=update.message.chat_id,text="لطفا یکی از گزینه های مورد نظر را انتخاب نمایید")
        info_logger.info(str(update.message).replace(update.message.text,'back used'))
    elif update.message.text== 'لیگ آلمان' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'bundesliga'))
    elif update.message.text== 'لیگ برترایران' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'iran leage'))
    elif update.message.text== 'لیگ اسپانیا' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'laliga'))
    elif update.message.text== 'لیگ فرانسه' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'france_leage'))
    elif update.message.text == 'لیگ جزیره' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(update.messag.replace(update.message.text,'premier leage'))
    elif update.message.text== 'سری آ' :
        bot.sendMessage(chat_id=update.message.chat_id,parse_mode=ParseMode.HTML,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
        info_logger.info(str(update.message).replace(update.message.text,'itly'))
    elif update.message.text=='روزنامه':
        bot.sendMessage(chat_id=update.message.chat_id,text="لطفا روزنامه مورد نظر را انتخاب نمایید.",reply_markup=getmag_markup)
        info_logger.info(str(update.message).replace(update.message.text,'magazine'))


    elif update.message.text=='خبر ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['خبر ورزشی'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text=='ایران ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['ایران ورزشی'].format(get_valid_date()),reply_markup=getmag_markup)

    elif update.message.text=='گل':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['گل'].format(get_valid_date()),reply_markup=getmag_markup)


    elif update.message.text == 'نود':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['نود'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text == 'ابرار ورزشی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['ابرار ورزشی'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text == 'استقلال':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['استقلال'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text == 'شوت':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['شوت'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text == 'هدف':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['هدف'].format(get_valid_date()),reply_markup=getmag_markup)
    elif update.message.text == 'پیروزی':
        bot.sendPhoto(chat_id=update.message.chat_id,photo=mags['پیروزی'].format(get_valid_date()),reply_markup=getmag_markup)

    elif update.message.text == 'امتیاز بده 😁':
        bot.sendMessage(chat_id=update.message.chat_id, text="اگه پسند کردین بهم امتیاز بدین لطفا 👇🏻   ☺️ ",reply_markup=rate_inline_keyboard_markup)
        info_logger.info(str(update.message).replace(update.message.text,'rate'))
    elif update.message.text == 'ارتباط با ادمین':
        bot.sendMessage(chat_id=update.message.chat_id, text="متاسفانه در حال حاضر ممکن نیست 😔😔\n ولی به زودی ممکن میشه 😊😊\n .",reply_markup=start_markup)
        info_logger.info(str(update.message).replace(update.message.text,'admin contact'))

def chart(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_chart.get_chart(update.message.text) , reply_markup=getrow_markup)
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def news(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id,text=get_news.get_news(),parse_mode=ParseMode.HTML,reply_markup=start_markup)
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def score(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_score.get_score(),reply_markup=start_markup)
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def rate(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text="اگه پسند کردین بهم امتیاز بدین لطفا 👇🏻   ☺️ ",reply_markup=rate_inline_keyboard_markup)
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def get_valid_date():
    e = jdatetime.datetime.now()
    if e.weekday()!=7:
        return str(e.date())

    return str(e.replace(year=e.year,month=e.month,day=e.day-1))


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

updater = Updater(token='95539936:AAH-GnoFYItZ5mQHXkIqUxFYwG6EnUzC0k0')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
chart_handler = CommandHandler('jadval', chart)
news_handler = CommandHandler('news', news)
score_handler = CommandHandler('score', score)
rate_handler = CommandHandler('rate', rate)

echo_handler= MessageHandler(Filters.text , echo)

dispatcher.add_handler(start_handler)

dispatcher.add_handler(chart_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(score_handler)
dispatcher.add_handler(rate_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_error_handler(error_callback)
updater.start_polling()
