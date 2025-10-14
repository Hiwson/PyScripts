#This is py strings
name = "Willy"
print(name)

#Multiline string
longTxt = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(longTxt)

#strings in py are arrays
print(len(name))
print("The 3rd letter in the name is - " + name[3])

#looping a string
for letter in name:
    print(letter)

#checking if a word is in a string
print("Lorem" in longTxt)
print("there" in longTxt)
print("there" not in longTxt)

#using slice syntax to return a range of charater in a text
txt = "susceptible is same as vulnerable"
print("range is - " + txt[11:22])

#modifying strings
	# 1. to upper and lower case
print(longTxt.upper())
	# 2. removing white space
wSpace = "        This text has some white space in it    "
print(wSpace)
nowSpace = wSpace.strip()
print(nowSpace)
	# 3. replacing a string
correct = nowSpace.replace("has","does not have")
print(correct)
	# 4. spliting words
salam = "Jambo, Kenya"
twoWords = salam.split(',')
print(twoWords)

# using the format() method - it makes it possible to concatinate int with str
quantity = 30
text = "I have {} items"
print(text.format(quantity))

intro = "My name is {} and am like {} yrs old"
age = 20
print(intro.format(name,age))
#you can use index on {} to specify what goes where
