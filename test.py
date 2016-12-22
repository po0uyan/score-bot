from telegram.ext import Updater,CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest,TimedOut, ChatMigrated, NetworkError)
from bot_logger import error_logger , info_logger
import get_chart ,get_news,get_score
start_message="\nسلام \n \n /score \n آخرين نتايج زنده مربوط به فوتبال \n\n  /news \n ارسال اخرين اخبار ورزشي \n\n /jadval  + عنوان لیگ مورد نظر \n دریافت جدول نتایج لیگ ها  \n\n  /ax  + عنوان مورد نظر   \n  ارسال تصوير مورد نظر \n\n/rozname \n روزنامه ورزشی \n\n /help\n كمك گرفتن از اسكور بات \n\n /rate \n امتیاز دهی به ربات \n."
help_message=" \n /score \n آخرين نتايج زنده مربوط به فوتبال \n\n  /news \n ارسال اخرين اخبار ورزشي \n\n/jadval  + عنوان لیگ مورد نظر \n دریافت جدول نتایج لیگ ها  \n\n  /ax + عنوان مورد نظر   \n  ارسال تصوير مورد نظر \n\n/rozname \n روزنامه ورزشی \n\n /help\n كمك گرفتن از اسكور بات \n\n اگه پسند کردین به من امتیاز بدین لطفا :-) \n https://telegram.me/storebot?start=pouyanbot \n."


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=start_message)
    info_logger.info(update.message)


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

updater = Updater(token='95539936:AAH-GnoFYItZ5mQHXkIqUxFYwG6EnUzC0k0')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
chart_handler = CommandHandler('jadval', chart)
news_handler = CommandHandler('news', news)
score_handler = CommandHandler('score', score)
help_handler = CommandHandler('help', help)


dispatcher.add_handler(start_handler)

dispatcher.add_handler(chart_handler)
dispatcher.add_handler(news_handler)
dispatcher.add_handler(score_handler)
dispatcher.add_handler(help_handler)


dispatcher.add_error_handler(error_callback)
updater.start_polling()
