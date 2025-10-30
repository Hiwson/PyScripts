#Tuples are used to store multiple items just like list,set & dictionary
  #packing values into a tuple
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

#unpacking from a tuple
(no1,no2,no3,*no4) = students
print("Student No.1 is ",no1)
print("The rest are ",no4)  # an asterisk collectes the rest as a list

#looping through a tuple
t =0
print("The loop:")
while t < len(students):
   print(students[t])
   t += 1
#for loop can also be used to loop a tuple
"""for x in students:
       print(x)"""

#jioning tuples is done using + operator 