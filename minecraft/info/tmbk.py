def representTBMK(value):
	response = value
	if value >= 1000000000000:
		response = str(round(value / 1000000000000, 1)) + " Trillion"
	elif value >= 1000000000:
		response = str(round(value / 1000000000, 1)) + " Billion"
	elif value >= 1000000:
		response = str(round(value / 1000000)) + " Million"
	elif value >= 1000:
		response = str(round(value / 1000, 1)) + " Thousand"

	return response