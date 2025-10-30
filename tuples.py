#Tuples are used to store multiple items just like list,set & dictionary
students = ("Joyce","Alice","Maina","Bob","Bob","Agnes","Omondi")
print(students)
#tuples are ordered and unchangeable and allow duplication

#accessing a specific item
print("First student is ",students[0]," and last is ",students[-1])
print("The tuple has ",len(students)," ","items")
print(students[3:]) #prints students from 3 to end
print(students[:4]) #prints students upto index 3
print(students[2:5]) #prints within a range

#it can contain different data types
tuple =("name",23,True)
print(tuple)