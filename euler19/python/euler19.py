

def leapyear(n):
	if n % 4 == 0:
		if n % 400 == 0:
			return True
		elif n % 100 == 0:
			return False
	return True

def february(year):
	if leapyear:
		return 29
	else:
		return 28

def dayssince(day, month, year):
	"""returns days between 1 jan 1900 and day (int), month (int), year(int, >=1900)"""
	# assert year >= 1900
	# assert month > 0
	# assert month < 13
	# assert day > 0
	# assert day < 32
	days = 0
	months = {1 : 31, 2 : february(year), 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
	for y in range(1899, year-1):
		if leapyear:
			days += 366
		else:
			days += 365
	for m in range(1, month):
		days += months[m]
	return days + day


def weekday(n):
	week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	return week[n%7]

if __name__ == '__main__':

	Sundays = 0
	for year in range(1901, 2001):
		# months = {1 : 31, 2 : february(year), 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
		for month in range(1, 13):
			# for day in range(1, months[month]+1):
				# print day, month, year, weekday(dayssince(day, month, year))
			if weekday(dayssince(1, month, year)) == "Sunday":
				Sundays += 1
				# print Sundays, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	print Sundays


