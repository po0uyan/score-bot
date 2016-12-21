from telegram.ext import Updater,CommandHandler
import logging
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="سلام عباس آقا")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

# create a file handler
    handler = logging.FileHandler('log/loginfo.log')
    handler.setLevel(logging.INFO)

# create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

# add the handlers to the logger
    logger.addHandler(handler)
    logger.propagate = False

    logger.info(update.message)
updater = Updater(token='318165040:AAEiSKoYbEJYnbH3Lputj0u4z487Ujl0z2c')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
