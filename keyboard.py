from telebot import types

def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Дай таблицу")
    btn2 = types.KeyboardButton("Добавить")
    btn3 = types.KeyboardButton("Удалить")
    markup.add(btn1, btn2, btn3)
    return markup

def kb_yn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    return markup