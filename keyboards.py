import telebot
from telebot import types

# keyboards = []

a = [[1, 2, 3], [4, 5, 6]]

keyboards = [1]

keyboards[0] = [["main"],
				["Создать задачу"], 
				["Поменять расписание"],
				["Я освободился!", "Я занят"]]


class workKeyboard:
	def get(name):
		print(name)
		kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
		for keyboard in keyboards:
			if(keyboard[0][0] == name):
				for line_number in range(1, len(keyboard)):
					kb.row(*keyboard[line_number])
		return kb

# keyboard = types.InlineKeyboardMarkup()
#     callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
#     keyboard.add(callback_button)
#     bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


class messageKeyboard:
	def get(name):
		kb = types.InlineKeyboardMarkup()
		for keyboard in keyboards:
			if(keyboard[0][0] == name):
				for line_number in range(1, len(keyboard)):
					buttons = []
					for button in keyboard[line_number]:
						buttons.append(types.InlineKeyboardButton(text = button, callback_data = button))
						kb.add(*buttons)

		kb.add(types.ReplyKeyboardRemove())
		return kb


# main.row(*array)