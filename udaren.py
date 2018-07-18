import requests, time

# vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
# consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

consonants = "бвгджзклмнпрстфхцчшщ"
vowels = "аеёиоуыэюя"


while 1:
	try:
		# word = "челОвек"
		word = input("Введите слово: ")

		word = word.lower()
		link = "http://accentonline.ru/" + word[0] + "/" + word

		request = requests.get(link)
		html = request.text

		important = html[html.find('<meta name="description"'):]
		important = important[:important.find('">')]

		# print(link, important)


		for char in important:
			if(char >= "0" and char <= "9"): main_syllable = int(char)

		syllable_number = 0
		for i in range(len(word)):
			char = word[i]

			if(vowels.find(char) != -1):
				syllable_number += 1
				if(syllable_number == main_syllable):
					word = list(word)
					word[i] = word[i].upper()
					word = "".join(word)

		print("Ударение: ", word)
	except:
		print("error")


