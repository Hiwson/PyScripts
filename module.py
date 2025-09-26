#file to be imported
def my_func(fname,lname,age):
	print("user is" + " " + fname + " " + lname + " " , age)
my_func("Giddy","Mwai",12)

#lists
students = ["David","Moses","Denn","Alfred"]
print(students)
print("The third item in mylist is" + " " + students[2])
print("the length of my list is",len(students))
#creating a list using list() constructor
ages = list((23,42,44,29,43,84))
print(ages)
#inserting an item into a list without replacing any item
students.insert(2,"Glen")
print(students)
#adding an item at the end of a list
ages.append(103)
print(ages)
#appending items to a list from another list
others = ["Jakwe","Elsa","Moses"]
others.extend(students)
print(others)