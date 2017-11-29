# map.py
#
# simple map generator
#

import random
from time import sleep

def printMap():
	x = 100;
	y = 25;
	elements = ["~", "^", "t", "#"]
	
	# while(True): # FOREVER!!!
	for i in range(y):
		for i in range(x):
		
			# roll the dice!
			rando = random.randrange(0,100)
			
			if (75 > random.randrange(0,100)):
				print(" ", end="")
				continue
			
			if (25 <= rando <= 100):
				print(elements[0], end="") # ocean
			elif (10 <= rando <= 25):
				print(elements[1], end="") # mountain
			elif (5 <= rando <= 10):
				print(elements[2], end="") # tree
			elif (2 <= rando <= 5):
				print(elements[3], end="") # fortress
		print()
		# sleep(0.02)
		
def randoPrint():
	for i in range(100):
		rando = random.randrange(0,100)
		print(rando)
		

def main():
	printMap()
	# randoPrint() # test
	

main()
