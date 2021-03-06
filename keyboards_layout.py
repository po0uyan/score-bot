from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
start_reply_keyboard = [['دریافت آخرین خلاصه بازی ها'],
                        ["آخرین خبر ها" , "جدول پخش tv"],
                        ["نتایج زنده", "جداول رده بندی "],
                        ["امتیاز بده 😁 ","ارتباط با ادمین"]]
getrow_reply_keyboard = [ ["بازگشت"],
                        ["لیگ جزیره","لیگ اسپانیا"],
                         [ "لیگ آلمان " , " سری آ  "],
                        ["لیگ فرانسه","لیگ برترایران"],
                        ]
getmag_reply_keyboard = [["بازگشت"],
                         ["خبر ورزشی","ایران ورزشی"],
                         [ "گل" , "نود"],
                        ["استقلال","پیروزی"],
                        ["شوت","هدف"],
                        ["ابرار ورزشی"]
                         ]
getnews_reply_keyboard=[["داخلی","خارجی"],
                        ["بازگشت"]
                        ]
getnews_markup=ReplyKeyboardMarkup(getnews_reply_keyboard, resize_keyboard=True,one_time_keyboard=True)
getmag_markup = ReplyKeyboardMarkup(getmag_reply_keyboard, resize_keyboard=True)
start_markup = ReplyKeyboardMarkup(start_reply_keyboard, resize_keyboard=True)
getrow_markup = ReplyKeyboardMarkup(getrow_reply_keyboard, resize_keyboard=True)
rate_keyboard=[[InlineKeyboardButton(text="برای امتیاز دهی اینجا کلیک کن ☺️ ☺️",url='https://telegram.me/storebot?start=pouyanbot')]]
rate_inline_keyboard_markup=InlineKeyboardMarkup(rate_keyboard)
admin_contact_keyboard=[[InlineKeyboardButton(text="برای ارتباط با ادمین اینجا کلیک کنید️",url='https://telegram.me/scorebotA')]]
admin_inline_keyboard_markup=InlineKeyboardMarkup(admin_contact_keyboard)
back_to_list_markup=InlineKeyboardMarkup([[InlineKeyboardButton('بازگشت به دسته ها 🔙',callback_data="back")]])


def get_video_keyboard(data):
    keyboard=[]
    for i, item in enumerate(data):
        keyboard.append([InlineKeyboardButton(item['title'], callback_data=str(i))])

    reply_markup = InlineKeyboardMarkup(keyboard)
    return  reply_markup


def get_score_keyboard(data):
    keyboard=[]
    for i, item in enumerate(data):
        keyboard.append([InlineKeyboardButton(item, callback_data=str(i))])

    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup


def get_news_keyboard(data):
    index=int(data[1])
    if data[0]=='p':
        if index > 0:
            return InlineKeyboardMarkup(
                [[InlineKeyboardButton("صفحه بعد ⬅️", callback_data="{0}{1}".format("n",index+1)),
                  InlineKeyboardButton("➡ صفحه قبل", callback_data="{0}{1}".format("p",index-1))]])
        else:
            return InlineKeyboardMarkup(
                [[InlineKeyboardButton("صفحه بعد ⬅️", callback_data="{0}{1}".format("n", index+1))]])
    else:
        if index < 4:
            return InlineKeyboardMarkup(
                [[InlineKeyboardButton("صفحه بعد ⬅️", callback_data="{0}{1}".format("n", index+1)),
                  InlineKeyboardButton("➡ صفحه قبل", callback_data="{0}{1}".format("p", index-1))]])

        else:

            return InlineKeyboardMarkup(
                [[InlineKeyboardButton("➡ صفحه قبل", callback_data="{0}{1}".format("p", index-1))],[InlineKeyboardButton("نمایش منو ⚽️", callback_data="end")]])
