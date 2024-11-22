import random

Wins = 0
Fails = 0
win = True

print("Welcome to the Ladder game:")
a = input("Would you like to know how to play?: ")
if a.lower().strip() == "yes":
	print("\nYou are given a randomly generated number between 1 and 100 and tasked to put it into one of 10 slots. You will be asked to do this 10 times, and if you can get all ten numbers to be in increasing order, you win. Good luck and have fun\n")

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


def play_ladder_game():
	global Wins, Fails, order, win
	order = ["", "", "", "", "", "", "", "", "", ""]

	i = 0
	win = True
	while i < 10:
		print(f"\nYou have {10-i} turns left")
		while True:
			x = random.randint(1, 100)
			if x not in order:
				break
		print((x)," is your randomly generated number.")
		decided = False
		while decided == False:
			try:
				pick = int(input("Which slot would you like to put this in?: "))
				if pick < 1 or pick > 10:
					print("Please enter a valid slot within 1 to 10.")
					continue
				elif order[pick - 1] != "":
					print("This slot is already taken.")
					continue
				else:
					decided = True
			except ValueError:
				print("Please enter a valid slot of 1 to 10.")
		i += 1


		order[pick - 1] = x
		failcheck()
		print(order, "\n")
		if win == False:
			print("You have lost, Get use to it...")
			break


while True:
	play_ladder_game()
	if win == True:
		Wins += 1
		print("You won!")
		if Fails == 0:
			kd=Wins
		else:
			kd = Wins/Fails
		print(f"You have won {Wins} times and failed {Fails} times, WLR: {kd}\n")
	elif Fails > 0:
		kd = Wins/Fails
		print(f"Wins: {Wins}, Fails: {Fails}, WLR: {kd}\n")
	else:
		print(f"Wins: {Wins}, Fails: {Fails}, WLR: {Wins}\n")
	b = input("Would you like to play again?: ")
	if b != "yes":
		break
