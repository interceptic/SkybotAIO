def representTBMK(value):
	response = value
	if value >= 1000000000000:
		response = str(round(value / 1000000000000, 1)) + "T"
	elif value >= 1000000000:
		response = str(round(value / 1000000000, 1)) + "B"
	elif value >= 1000000:
		response = str(round(value / 1000000)) + "M"
	elif value >= 1000:
		response = str(round(value / 1000, 1)) + "K"

	return response