print("Hello, World!")

#no {} to denote code block.
if 5 > 2:
  print("Five is greater than two!")

#use this to comment code.
x = 5
y = "Hello world"
print(x)
print(y)

a = 4
a = "hello"
print(a)

b = str(3) #'3'
c = int(3) # 3
d = float(3) #3.0

print(type(b))
print(type(c))
print(type(d))

f, g, h = "hello", "good morning", "adios" #multi value, multi variable assignment.
print(f)
print(g)
print(h)

r = t = y = 50 #assign multiple variables to a single value.
print(r)
print(t)
print(y)

#unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Notes:
#python can be simply run directly from the terminal via python or py command.
#indentation in python is equivalent to {} in Java and C.
#the indentation can be any number of spaces spcified but all code in the same code block must follow the same indentation principle.
#variables are created when you assign a value to it.
#there is no multi-line comments in python.
#a work around this is to use multi-line string which if not assinged to a variable, python will ignore.

#variables do not need to be declared with any specific type.
#casting is used to specify type of variable in python.
#get type of variable via the type function.
#string varibles can be declared via single or double qoutes.
#variable names are case sensitive.
#can unpack values from a collection variable to be stored in other variables.
#print can be used to ouput values of variables to the screen.