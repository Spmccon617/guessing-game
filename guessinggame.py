from random import randint

while True:
	number = randint(1,100)
	guessNumber = input("What is the number?")

	if guessNumber is number:
		print("Good job!")
		break
	else:
		print(number)
		print("Better luck next time")
		break
