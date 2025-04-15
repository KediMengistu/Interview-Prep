x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc2():
  global y
  y = "fantastic"

myfunc2()

print("Python is " + y)

#global variables are those defined outside of functions.
#variables inside are local and can only be used or accessed from inside the functions scope.
#global keyword can be used to make local variables accessible from the outside.
#keep in mind that global and local variables can have the same name, however the local version will have it's own value and the global will have it's own value.