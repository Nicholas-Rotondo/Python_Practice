import random

def winner(AI, player):
	if (AI == player):
		return 0
	elif (AI == "rock" and player == "scissors"
		  or AI == "scissors" and player == "paper"
		  or AI == "paper" and player == "rock"):
		return -1
	else:
		return 1

def rps():
	player = raw_input("Rock, paper, or scissors: ").lower()
	options = ["rock", "paper", "scissors"]
	AI = random.choice(options)
	result = winner(AI, player)
	if (result == -1):
		print("\nYou: " + player + "\nOpponent: " + AI + "\n\nYou lost!")
	elif (result == 1):
		print("\nYou: " + player + "\nOpponent: " + AI + "\n\nYou won!")
	else:
		print("\nYou: " + player + "\nOpponent: " + AI + "\n\nDraw, try again!")
		rps()

rps()
