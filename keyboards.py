import telebot
from telebot import types

main = types.InlineKeyboardMarkup(resize_keyboard = True)
main.row('Создать задачу')
main.row('Прочее')
