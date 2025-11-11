import random
import math
	# getting user input
player = input("Whats your name lad??......\t")
do{
playerNo = input("Enter a number between 1-10:.....\t")
	# generating a random number
winningNo = random.random()
winningNo = math.floor(winningNo*10)
print(winningNo)
	# type conversion from string to integer
pick = int(playerNo)
	# conditioning to get the miss range
if pick < winningNo:
	print("Your number was lesser than winning number!!!!")
	print(f"Oooops!!! {player} lost mahn----try again")
elif pick > winningNo:
	diff = pick - winningNo
	print("Your number was greater than winning number!!!!")
	print(f"Oooops!!! {player} lost mahn----missed by ",diff)
else:
	print(f"{player} You won bruv!!!")
}
while(pick != winningNo);
