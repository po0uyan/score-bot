from telegram.ext import Updater,CommandHandler
import logging
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="سلام عباس آقا")

    formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logging.basicConfig(format=formatter,filename='log/loginfo.log',level=logging.INFO)
    logging.info(update.message)
    print (update.message.message_id)
updater = Updater(token='318165040:AAEiSKoYbEJYnbH3Lputj0u4z487Ujl0z2c')
dispatcher = updater.dispatcher
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
