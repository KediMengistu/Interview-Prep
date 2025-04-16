#random module used to create a random valued variable.
import random

#use type to see the type of the variable.
x = 5
print(type(x))

a = 1     #int
b = 2.8   #float
c = 1j    #complex

#convert these values to the correspoding types.
a2 = float(b) #float to float.
b2 = int(a) #int to float.
c2 = int(a) #int to complex.

#getting random value between 1 and 9 (inclusive, exclusive).
print(random.randrange(1, 10))

d = int(4.5)
f = float(8)
g = str(3)

print(d)
print(f)
print(g)

#Notes:
#different kinds of data types include...
" text type         = str"
" numeric types     = int, float, complex"
" sequence types    = list, tuple, range"
" mapping types     = dict"
" set types         = set, frozenset"
" boolean type      = bool"
" binary types      = bytes, bytearray, memoryview"
" none types        = none type"

#the data type is either set at declariation time implicitly or explicitly.
#use casting functions to cast values