# adventure2.py

class Character:

	def __init__(self):
		self.name = " "
		self.inventory = []
	# limit the inventory

class Weapon:

	def __init__(self, name, attack):
		self.name = name
		self.attack = attack
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.__str__()
		
w1 = Weapon("sword", 10)

player1 = Character()
player1.inventory.append(w1)
print (player1.inventory)