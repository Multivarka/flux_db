import telebot
from key import key
from database import add, get, get_deleted, delete
from keyboard import keyboard, kb_yn
from test import Test
import time


bot = telebot.TeleBot(key)
res = []
# delete_num = 0
object_delete = Test()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "1", reply_markup=keyboard())

@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    if "таблицу" in text.lower():
        bot.send_message(message.chat.id, get(), reply_markup=keyboard())
    elif "добавить" in text.lower():
        msg = bot.send_message(message.chat.id, "Напиши контакт")
        bot.register_next_step_handler(msg, wait_contact)
    elif "удалить" in text.lower():
        msg = bot.send_message(message.chat.id, get_deleted())
        bot.register_next_step_handler(msg, wait_delete)
    else:
        bot.send_message(message.chat.id, "Непон", reply_markup=keyboard())

    print(f"Сообщение: {text}")

def wait_contact(message):
    print(f"Сообщение: {message.text}")
    res.clear()
    res.append(message.text)
    msg = bot.send_message(message.chat.id, "Напиши сумму")
    bot.register_next_step_handler(msg, wait_sum)

def wait_sum(message):
    print(f"Сообщение: {message.text}")
    res.append(int(message.text))
    msg = bot.send_message(message.chat.id, "Напиши описание заказа")
    bot.register_next_step_handler(msg, warn)

def warn(message):
    print(f"Сообщение: {message.text}")
    res.append(message.text)
    msg = bot.send_message(message.chat.id, f"Будет записано -> {res[0]}: ({res[1]}, [{res[2]}])?", reply_markup=kb_yn())
    bot.register_next_step_handler(msg, result)

def result(message):
    print(f"Сообщение: {message.text}")
    if message.text.lower() == "да":
        add((res[0], res[1], res[2]))
        bot.send_message(message.chat.id, "Сделано", reply_markup=keyboard())
    else:
        res.clear()
        bot.send_message(message.chat.id, "Отменено", reply_markup=keyboard())

def wait_delete(message):
    print(f"Сообщение: {message.text}")
    try:
        object_delete.set_delete_num(int(message.text))
        msg = bot.send_message(message.chat.id, f"Вы уверены что хотите удалить {object_delete.get_delete_num()} элемент?", reply_markup=kb_yn())
        bot.register_next_step_handler(msg, warn_delete)
    except:
        bot.send_message(message.chat.id, "Я вас не понял", reply_markup=keyboard())



def warn_delete(message):
    print(f"Сообщение: {message.text}")
    if message.text.lower() == "да":
        delete(object_delete.get_delete_num())
        bot.send_message(message.chat.id, "Удалено", reply_markup=keyboard())
    else:
        res.clear()
        bot.send_message(message.chat.id, "Отменено", reply_markup=keyboard())


print("Бот запущен")
try:
    bot.polling(none_stop=True, interval=0)
except:
    time.sleep(10)