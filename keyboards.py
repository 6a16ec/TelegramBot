import telebot
from telebot import types

main = types.ReplyKeyboardMarkup(resize_keyboard = True)
main.row('Создать задачу')
main.row('Прочее')
