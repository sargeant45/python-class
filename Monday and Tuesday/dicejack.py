import random

player_wins = 0
dealer_wins = 0
player_money = 1000

while True:

	dice_roll = 0
	player_score = 0
	dealer_score = 0
	
	print ("It's your turn to play Dice Blackjack")
	while True:
		dice_roll = random.randint(1, 6)
		player_score = player_score + dice_roll
		
		if player_score > 21:
			print("bust")
			dealer_wins = dealer_wins + 1
			break
		
		if player_score == 21:
			print("you win!")
			player_wins = player_wins + 1
			break
		
		print ("your score is: " + str(player_score) )
		
		print ("do you want to roll again?")
		roll_again = raw_input()
		
		if roll_again == "no":
			break
	
	
	# Program the Dealer (Computer Player)
	# Very similar to the Player, but no user input
	
	print ("It's the dealer's turn")
	while True:
		dice_roll = random.randint(1, 6)
		dealer_score = dealer_score + dice_roll
		
		if dealer_score > 21:
			print ("you win!")
		if dealer_score > 18:
			break
			
	if player_score <= 21 and dealer_score <= 21:
		if player_score > dealer_score:
			print ("you win!")
		if dealer_score > player_score:
			print ("you lose")
		if dealer_score == player_score:
			print ("tie")
	








