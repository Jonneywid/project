import random
import time

#holds all of the impotant player stats and actions	
class Player:
	def __init__(self, name, health, strength, agility, stamina, intelligence, weapon):
		self.name = name
		self.health = health
		self.strength = strength
		self.agility = agility
		self.stamina = stamina
		self.intelligence = intelligence
		self.weapon = weapon
		
	#Should prob add a dodge
	player_actions = [
    "Attack",
    "Run",
    "Block"
    ]
	
	def pname(self):
		playername = self.name
		
		
	
	def stats(self):
		print('Name:', self.name)
		print('hth:', self.health)
		print('str:', self.strength)
		print('agi:', self.agility)
		print('stm:', {self.stamina})
		print('int:', self.intelligence)
		#print('weapon:', self.weapon)
		
	def increase_hth(self, amount):
		self.health += amount
		
	def increase_str(self, amount):
		self.strength += amount
		
	def increase_agi(self, amount):
		self.agility += amount
		
	def increase_stm(self, amount):
		self.stamina += amount
		
	def increase_int(self, amount):
		self.intelligence += amount
	
class Ememy:
	def __init__(self, health, strength, agility, weapon):
		self.health = health
		self.strength = strength
		self.agility = agility
		self.weapon = weapon
		self.stamina = 100

#Player weapon(How much damage will be done and stamina cost)
class Weapon:
	def __init__(self, name, wpdamage, stmcost):
		self.name = name
		self.wpdamage = wpdamage
		self.stmcost = stmcost
		
	def Weapondmg(self):
		Weapondmg = random.randint(self.damage, self.wpdamage + self.stregnth)
		
		
	#assuming each weapon will cost some stam to attack
	def staminacost(self):
		staminacost = self.stmcost
		
#This is for the attack option		
class Attack:
	def __init__(self, attacker, target):
		self.attacker = attacker
		self.target = target
	
	#hit chance based on agility
	def hit_chance(self):
		return 1 + (self.agility * 0.5)
	
	def playerdmg(self):
		Totaldmg = Weapondmg - self.estrength
		
	#def staminaend(self):
		#self.stamina - staminacost
	
	def execute(self):
		pass
		



#weapons
axe = Weapon('axe', 20, 15)
dagger = Weapon('dagger', 10, 5)





print("This dungeon could change your life")
#time.sleep(1.5)
print("Will you came out the dungeons with money and treasures beyond your wildest dreams")
#time.sleep(1.5)
print("Or die the same way you came in")
#time.sleep(1.5)
print("Take that as you will........")
#time.sleep(1.5)

playername = input("So what is your name: ")


#May change later but this is player inv	
Inv = []
player = Player(playername, 1, 1, 1, 100, 1, dagger)
ememy = Ememy(1, 1, 1, axe)




choice1 = int(input("""how would you describe your childhood:
	1. I like playground
	2. I like read
	3. I like both
	
	"""))

#add some commmet about said choice
if choice1 == 1:
	player.increase_str(5)
elif choice1 == 2:
	player.increase_int(3)
elif choice1 == 3:
	player.increase_str(3)
	player.increase_int(2)

player.stats()

#make a loop that tells who goes first in a battle based on agility
#Test fight
class Combat:
	def __init__(self, fighter1, fighter2):
		self.fighters = [fighter1, fighter2]
		self.gameover = False
		self.turn = 0

	def start(self):
		print("Duel starts.")
		if player.agility >= ememy.agility:
			print("You start")
			self.make_turn()
			
	def battle(self):
		playerchoice = int(input("""what is your move
					1. Attack
					2. Defend
					"""))
		if playerchoice == 1 and random.random() <= self.hit_chance:
			ememy.health - playerdmg
			print(ememy.health)
			
		else:
			print("you missed")
'''
	def make_turn(self):
		print("Turn {}".format(self.turn))
		if all(a.health > 0 for a in self.fighters):
			print("\n")
			self.turn += 1
			self.make_turn()	
		else:
			print("Duel finished in {} turns.".format(self.turn))
			print("\n")
'''
			
	
Combat(player, ememy).start()
	
'''
How I want a fight to go:


player.attack(dmg)


Whats your move?
1. attack
2. defend
3. run

I chose attack

"1"

you did 500000000 damage

ememy health 49500000000

ememy choses attack

ememy dealt 100000000000 dmg

you have 9500000000000000 health left

'''
	
	


