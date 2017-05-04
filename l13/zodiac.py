class DayError(Exception):
	pass

class MonthError(Exception):
	pass


while True:
	try:
		date = input("Введите дату рождения в формате дд.мм.гг: ")
		day = int(date[:2])
		month = int(date[3:5])
		year = int(date[6:])
		# print(day, month, year)
		if day > 31 or day < 1:
			raise DayError
		if month > 12 or month < 1:
			raise MonthError
		if (day >= 21 and month == 5) or (day <= 20 and month == 6):
			print("Ты близнецы")

		break
	except ValueError:
		print("Введите дату в правильном формате")
	except DayError:
		print("Введите правильный день")
	except MonthError:
		print("Введите правильный месяц")
  