#################### Filip Hedman ####################

antal_rader = int(input("Hur många rader vill du ha?"))
rader = []
thing = 1

for x in range(1, 100):
	if antal_rader >= x:
		rader.append(x)

for x in rader:
	print(f"{rader}")