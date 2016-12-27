from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
start_reply_keyboard = [["نتایج زنده", "جداول رده بندی "],
                        ["آخرین خبر های ورزشی","روزنامه"],
                        ["امتیاز بده 😁 ","ارتباط با ادمین"]]
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
rate_keyboard=[[InlineKeyboardButton(text="برای امتیاز دهی اینجا کلیک کن ☺️ ☺️",url='https://telegram.me/storebot?start=pouyanbot')]]
rate_inline_keyboard_markup=InlineKeyboardMarkup(rate_keyboard)