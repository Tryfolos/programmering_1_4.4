#################### Filip Hedman ####################

number_of_rows = int(input("How many rows do you want?"))
position = 1
startnumber = 1
multiplier = 1



for x in range(1, number_of_rows + 1):
	if number_of_rows >= x:
		while number_of_rows >= position:
			thing = startnumber * multiplier
			if thing >= 10:
				print(f"{thing}   ", end = "")
			if thing < 10:
				print(f"{thing}    ", end = "")
			multiplier += 1
			position += 1
		else:
			print("\n")
			startnumber += 1
			multiplier = 1
			position = 1




