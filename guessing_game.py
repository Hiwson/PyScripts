import random
import math

player = input("Whats your name lad??......")
playerNo = input("Enter a number between 1-10:.....")
winningNo = random.random()
winningNo = math.floor(winningNo*10)
print(winningNo)

pick = int(playerNo)
if pick < winningNo:
	print("Your number was lesser than winning number!!!!")
	print(f"Oooops!!! {player} lost mahn----try again")
elif pick > winningNo:
	diff = pick - winningNo
	print("Your number was greater than winning number!!!!")
	print(f"Oooops!!! {player} lost mahn----missed by ",diff)
else:
	print(f"{player} You won bruv!!!")

