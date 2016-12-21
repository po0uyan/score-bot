from telegram.ext import Updater,CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest,TimedOut, ChatMigrated, NetworkError)
from bot_logger import error_logger , info_logger
import get_chart

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="در حال حاضر قادر به پاسخگویی نمی باشیم")
    info_logger.info(update.message)

def chart(bot, update):
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text=get_chart.get_chart(update.message.text))
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

dispatcher.add_handler(start_handler)

dispatcher.add_handler(chart_handler)
dispatcher.add_error_handler(error_callback)
updater.start_polling()
