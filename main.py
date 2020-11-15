#################### Filip Hedman ####################

antal_rader = int(input("Hur många rader vill du ha?"))
xposition = 0

#running = True


#while running == True:

for x in range(1, antal_rader):
	if antal_rader >= x:
		while antal_rader > xposition:
			xposition += 1
			print(f"{xposition}   ", end = "")
		else:
			print("\n")
			xposition = 0



