from telegram import ReplyKeyboardMarkup , InlineKeyboardButton, InlineKeyboardMarkup
start_reply_keyboard = [["نتایج زنده", "جداول رده بندی "],
                        ["آخرین خبر های ورزشی","روزنامه"]]
getrow_reply_keyboard = [["لیگ جزیره","لیگ اسپانیا"],
                         [ "لیگ آلمان " , " سری آ  "],
                        ["لیگ فرانسه","لیگ برترایران"],
                         ["بازگشت"]]
getmag_reply_keyboard = [["خبر ورزشی","ایران ورزشی"],
                         [ "گل" , "نود"],
                        ["استقلال","پیروزی"],
                        ["شوت","هدف"],
                        ["ابرار ورزشی"],
                         ["بازگشت"]]
getmag_markup = ReplyKeyboardMarkup(getmag_reply_keyboard, resize_keyboard=True)
start_markup = ReplyKeyboardMarkup(start_reply_keyboard, resize_keyboard=True)
getrow_markup = ReplyKeyboardMarkup(getrow_reply_keyboard, resize_keyboard=True)
