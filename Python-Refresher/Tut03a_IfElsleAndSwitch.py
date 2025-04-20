x = int(99)
if x > 5:
  print(f"x is greater than 5. x: {x}\n")
elif x == 5:
  print(f"x is equal to 5. x: {x}\n")
else:
  print(f"x is less than to 5. x: {x}\n")

x = 5
if(x == 5): print(f"x is equal to 5. x: {x}")

a = 4
b = 7
#printing A in the case that a > b and otherwise printing B.
print("A") if a > b else print("B")

value = 99
match (value):
  case 1:
    print(f"value case 1 is matched: value is {value}\n")
  case 2:
    print(f"value case 2 is matched: value is {value}\n")
  case 3:
    print(f"value case 3 is matched: value is {value}\n")
  case 4 | 5 | 6 | 7 | 8| 9 | 10:
    print(f"value case 4, 5, 6, 7, 8, 9 or 10 is matched: value is {value}\n")
  case _:
    print(f"value case 3 is matched: value is {value}\n")

#Notes:
#if...elif...else
#if you have only one if can execute on one line (the condiition and the code block to execute occur on the same line).
#can do the same for the if-else branching where you have the entire structure on one line.
#can further this by adding another if-else construct on the same line as another.
#logical operators are and, or, not.
#use pass in empty if in case there is nothing to execute - prevents empty if error.
#can add if statements to case statements.