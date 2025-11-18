		# Python functions
def hello():
   print("The function said Hello!")
hello()

  #using return keyword
def _sum():
    return 32 + 88
print("The sum is ",_sum())
 
  #empty functions
def empty_func():
    pass  #pass allows one to create a template to use later

  #function with parameter
def _myself(fname,lname): #placing parameters
     print("My name is " + fname +" "+ lname)
_myself("Njoka","Mokotho") #passing arguments
  #keyword arguments - here order doesn't matter
_myself(lname = "Onyighi",fname = "Njenje")

  # *args and **kwargs
def mates(*name):    #used when you're not sure of the no of arguments to pass
    print("One of my mates is " + name[3])
    print("My mates are ",name)
mates("Elifik","Dricks","Prim","Fadhil")
def _mystudy(**subjects):  #used when not sure of keyword argumwnts to pass
   print("Mostly I love",subjects["fav"])
   print("I study: ",subjects)
   print("The newest is: ",subjects["new"])
   print("This function is type ",type(subjects))
_mystudy(fav="DST & ALG",recent="Cyber sec",ongoing="OOP & SP",new="OP")
   #unpacking dictionary and list as arguments
