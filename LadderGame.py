import random

#Starting default values
Wins = 0
Fails = 0
win = True

#Introdution to game
print("Welcome to the Ladder game:")
a = input("Would you like to know how to play?: ")
if a.lower().strip() == "yes" or a.lower().strip() =="y":
	print("\nYou are given a randomly generated number between 1 and a max number, chosen via the difficulty selected. You are tasked to place all numbers into one of 10 slots. You win if you get all the numbers in ascending order (left to right). Good luck and have fun\n")

#function for checking if player failed the game
def failcheck():
	global Wins, Fails, order, win
	check = []
	for j in order:
		if j != "":
			check.append(j)
	if len(check) > 1:
		for k in range(0,len(check)-1):
			if check[k] > check[k+1]:
				win = False
				Fails +=1

#function that starts game
def play_ladder_game():
	global Wins, Fails, order, win
	#clears array for the randomly generated numbers
	order = [""] * 10
	# Difficulty selection
	while True:
		diff = input(
            "What difficulty would you like to play?:\n"
			"   Baby        (1-11)\n"
            "   Easy        (1-13)\n"
            "   Medium      (1-15)\n"
            "   Hard        (1-20)\n"
			"   Tricky      (1-30)\n"
            "   Impossible  (1-100)\n"
        ).lower().strip()
		if diff == "baby":
			MaxNum=11
			break
		if diff == "easy":
			MaxNum = 13
			break
		elif diff == "medium":
			MaxNum = 15
			break
		elif diff == "hard":
			MaxNum = 20
			break
		elif diff == "tricky":
			MaxNum = 30
			break
		elif diff == "impossible":
			MaxNum = 100
			break
		else:
			print("Please enter a valid difficulty.\n")

	#logic for randomly generated numbers
	i = 0
	win = True
	while i < 10:
		print(f"\nYou have {10-i} turns left")
		while True:
			x = random.randint(1,MaxNum)
			if x not in order:
				break
		print((x)," is your randomly generated number.")
		decided = False
		#loop for valid selection of slot in array
		while decided == False:
			try:
				pick = int(input("Which slot would you like to put this in?: "))
				if pick < 1 or pick > 10:
					print("\nPlease enter a valid slot within 1 to 10.")
					continue
				elif order[pick - 1] != "":
					print("\nThis slot is already taken.")
					continue
				else:
					decided = True
			except ValueError:
				print("\nPlease enter a valid slot of 1 to 10.")
		i += 1

		order[pick - 1] = x
		failcheck()
		print(order, "\n")
		#checks if player lost
		if win == False:
			print("You have lost, Get use to it...")
			break

#initial function that calls upon game functions and returns results at end of game
while True:
	play_ladder_game()
	if win == True:
		Wins += 1
		print("You won!")
		if Fails == 0:
			kd=Wins
		else:
			kd = Wins/Fails
		print(f"You have won {Wins} times and failed {Fails} times, Your Win/Loss Ratio is: {kd}\n")
	elif Fails > 0:
		kd = Wins/Fails
		print(f"Wins: {Wins}, Fails: {Fails}, WLR: {kd}\n")
	else:
		print(f"Wins: {Wins}, Fails: {Fails}, WLR: {Wins}\n")
	Replay = input("Would you like to play again?: ")
	if Replay.lower().strip() != "yes" and Replay.lower().strip() != "y":
		break
