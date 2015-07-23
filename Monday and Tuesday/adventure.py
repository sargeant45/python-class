map = [ "forest", "forest", "house" ]

map2d = [ ["forest", "forest", "house"],
		  ["hills", "forest", "walls"],
		  ["desert", "gate", "walls"] ]
x = 0
y = 0
player_hp = 20

key_x = random.randint(0, 2)
key_y = random.randint(0, 2)
has_key = False

while True:
	print ("What would you like to do? ")
	user_input = raw_input()
	
	if user_input == "south":
		y = y + 1
		if y > 2:
			y = 2
		
	if user_input == "north":
		y = y -1
		if y < 0:
			y = 0
		
	print ("You are in the " + map2d[y][x])
	
	if map2d[y][x] == "forest":
		print ("you see several tall trees")
	
	if x == key_x and y == key_y:
		print ("You see a key")
		has_key = True
	
	if map2d[y][x] == "desert":
		print ("You've encountered a giant scorpion, and it's attacking you!")
		scorpion_hp = 10;
		print ("What would you like to do?")
		fight_input = raw_input()
		if fight_input == "attack" or fight_input == "fight":
			print ("you hit the scorpion")
			scorpion_hp = scorpion_hp - random.randint(1, 4)
			print ("the scorpion is angry and hits you back!")
			player_hp = player_hp - random.randit(1, 6)
		if fight_input == "run" or fight_input == "run away":
			print ("you run away")
			y = y - 1