x = 'hello'
x2 = "hello"
x3 = "Yo, it's me."
x4 = """"
Yolo
Dolo
Solo
Bolo
"""

print(x)
print(x2)
print(x3)
print(x4)

a = "Hello brother."
#prints e char.
print(a[1])

for z in a:
  print(z)
  
print(len(a))
print("bro" in a)

#slicing strings = extracting only part of string.
print(a[2:5]) #prints out characters indexed 2 through 4.
print(a[:5])  #prints out characters indexed 0 through 4. (start to value-1)
print(a[2:])  #prints out characters from value through the end.
print("negative index slicing:" + a[-3:-1]) #prints out characters backwards; -1 is the 0 index from right to left (must go from left to right so more negative to less negative).

#f strings require f at start of string and {} around non string variables.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#using modifiers to format the value of the placeholder in the {}, where we use : to indicate modifier usage.
#placeholders {} can contain variables, operations, functions and of course modifiers.
price = 59
txt2 = f"The price is {price:.2f} dollars"
print(txt2)

print(bool("hello")) #truthy value.
print(bool(14))      #truthy value.

#Notes:
#strings are specified using '' or "".
#can use quotes inside of other qoutes as long as internal and external differ.
#multi-line qoutes assigned to variables use three qoutes """...""".
#python does not have a char type, even in spite of string being arays of bytes representing unicode characters.
#use arrays to access these characters from the string.
#can loop through string via for-loop.
#len function returns it's length.
#in can be used to check if a string exists in another string.
#not in is the negation to check if the string does not exist in the other.
#there are many string methods.
#cannot combine string and number types without using fstrings or the format method.
#\ for escape characters.
#boolean is true or false.
#use bool function to evaluate any expresion or variable as being true or false.
#falsy values include the following: False, (), [], {}, "", 0, and None.
#another falsy value is an object created from class that has a __len__ function that returns 0 or False.
#python operators include:
"Arithmetic operators"
"Assignment operators"
"Comparison operators"
"Logical operators"
"Identity operators"      #new => is or is not (is returns ture if objects are same)
"Membership operators"    #new => in or not in (in returns trye is a sequence is in object)
"Bitwise operator"