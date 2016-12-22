import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler , MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,TimedOut, ChatMigrated, NetworkError)
from bot_logger import error_logger , info_logger
import get_chart ,get_news,get_score
start_message="\nسلام \n \n /score \n آخرين نتايج زنده مربوط به فوتبال \n\n  /news \n ارسال اخرين اخبار ورزشي \n\n /jadval  + عنوان لیگ مورد نظر \n دریافت جدول نتایج لیگ ها  \n\n  /ax  + عنوان مورد نظر   \n  ارسال تصوير مورد نظر \n\n/rozname \n روزنامه ورزشی \n\n /help\n كمك گرفتن از اسكور بات \n\n /rate \n امتیاز دهی به ربات \n."
help_message=" \n /score \n آخرين نتايج زنده مربوط به فوتبال \n\n  /news \n ارسال اخرين اخبار ورزشي \n\n/jadval  + عنوان لیگ مورد نظر \n دریافت جدول نتایج لیگ ها  \n\n  /ax + عنوان مورد نظر   \n  ارسال تصوير مورد نظر \n\n/rozname \n روزنامه ورزشی \n\n /help\n كمك گرفتن از اسكور بات \n\n اگه پسند کردین به من امتیاز بدین لطفا :-) \n https://telegram.me/storebot?start=pouyanbot \n."
start_reply_keyboard = [["نتایج زنده", "جداول رده بندی "],
                        ["آخرین خبر های ورزشی"]]
start_markup = ReplyKeyboardMarkup(start_reply_keyboard, resize_keyboard=True)

getrow_reply_keyboard = [["لیگ جزیره ( premier league)","لیگ اسپانیا (la liga)", "لیگ آلمان (bundesliga)" ],
                        [" سری آ (italy) ","لیگ فرانسه (loshampione)","لیگ برتر (خلیج فارس)"],
                         ["بازگشت"]]
getrow_markup = ReplyKeyboardMarkup(getrow_reply_keyboard, resize_keyboard=True)


def start(bot, update):




    update.message.reply_text("سلام من اسکور بات هستم؛ اگه حال نداری هر دقیقه سایتای سنگین و پر از تبلیغ ورزشیو چک کنی در خدمتم",reply_markup=start_markup)
    # bot.sendMessage(chat_id=update.message.chat_id, text=start_message)
    info_logger.info(update.message)


def echo(bot, update):
    if update.message.text== 'جداول رده بندی' :

        bot.sendMessage(chat_id=update.message.chat_id, text="لطفا لیگ مورد نظر را انتخاب کنید",reply_markup=getrow_markup)
    elif update.message.text=='آخرین خبر های ورزشی':
        bot.sendMessage(chat_id=update.message.chat_id,text=get_news.get_news(),reply_markup=start_markup)
    elif update.message.text== 'نتایج زنده' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_score.get_score(),reply_markup=start_markup)
    elif update.message.text== 'بازگشت' :
        try :
            bot.sendMessage(reply_markup=start_markup,chat_id=update.message.chat_id,text="لطفا یکی از گزینه های مورد نظر را انتخاب نمایید")
        except Exception as e:
            print (e)
    elif update.message.text== 'لیگ آلمان (bundesliga)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
    elif update.message.text== 'لیگ برتر (خلیج فارس)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
    elif update.message.text== 'لیگ اسپانیا (la liga)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
    elif update.message.text== 'لیگ فرانسه (loshampione)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
    elif update.message.text== 'لیگ جزیره ( premier league)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)
    elif update.message.text== 'سری آ (italy)' :
        bot.sendMessage(chat_id=update.message.chat_id,text=get_chart.get_chart(update.message.text),reply_markup=getrow_markup)

def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message)
    info_logger.info(update.message)


def chart(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_chart.get_chart(update.message.text))
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def news(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_news.get_news())
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


def score(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_score.get_score())
        info_logger.info(update.message)
    except Exception as e :
        error_logger.error(e)


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

updater = Updater(token='318165040:AAEiSKoYbEJYnbH3Lputj0u4z487Ujl0z2c')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
chart_handler = CommandHandler('jadval', chart)
news_handler = CommandHandler('news', news)
score_handler = CommandHandler('score', score)
help_handler = CommandHandler('help', help)
echo_handler= MessageHandler(Filters.text , echo)

dispatcher.add_handler(start_handler)

dispatcher.add_handler(chart_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(score_handler)
dispatcher.add_handler(help_handler)

dispatcher.add_handler(echo_handler)
dispatcher.add_error_handler(error_callback)
updater.start_polling()
