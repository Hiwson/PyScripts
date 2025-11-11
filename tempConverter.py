	# A simple temperature converter
print("Temperature conversion console")
print("Convert °c to °F and vice versa")
print("Options:\n1.°c to °F\n2.°F to °c\n")

opt = int(input("Please input you option.....\t"))

while (opt > 2 or opt == 0):
   print("\ninvalid option")
   print("Options:\n1.°c to °F\n2.°F to °c")
   opt = int(input("Please input you option....."))
else:
   fig = float(input("Input you figure to convert....\t"))

import math
if opt == 1:
   ans = math.floor((fig - 32) * (5/9))
   print(f"{fig}°c = ",ans,"°F")
else:
   ans = math.floor(fig * (9/5) +32)
   print(f"{fig}°F = ",ans,"°c")

print("\n\t\t-----Made by Willy----")
