import telebot
from telebot import types

# keyboards = []

a = [[1, 2, 3], [4, 5, 6]]

keyboards = [1]

keyboards[0] = [["main"],
				["Создать задачу"], 
				["Поменять расписание"],
				["Я освободился!", "Я занят"]]


class replyKeyboard:
	def get(name):
		kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
		for keyboard in keyboards:
			if(keyboard[0] == name):
				for line_number in range(1, len(keyboard)):
					kb.row(*keyboard[line_number])
# main.row(*array)