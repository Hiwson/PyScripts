#simple calculate program
name = input("What's your name friend? ")
print(f"Welcome {name}")
print("Have fun while performing your simple arithmetics....")
num1 = input("Enter your first integer: ")
operator = input("Enter the operand: ")
num2 = input("Enter your second integer: ")
print(f"{num1} {operator} {num2}")
match operator:
  case "+":
    print(float(num1) + float(num2))
  case "/":
    print(float(num1) / float(num2))
  case "×" | "*":
    print(float(num1) * float(num2))
  case "-":
    print(float(num1) - float(num2))
  case _:
    print("Enter basic operands!!")

