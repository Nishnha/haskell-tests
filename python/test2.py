class Monster:
	agility = 20

	def __init__ (self, hp, defense):
		self.hp = hp
		self.defense = defense

	def say(self):
		print('Rawr')

class Slime(Monster):
	color = ""
	def __init__(self, hp, defense, color):
		super().__init__(hp, defense)
		self.color = color

	def glob(self):
		print("blub")

bob = Monster(30, 10)
ricky = Monster(10, 30)
slimy = Slime(5, 2, "red")

bob.say()
print(bob.hp, ricky.hp)
slimy.say()
#Monster.say(bob)
