# i = 1
# while i < 6:
#   print(i)
#   if i==3:
#     # break
#     pass
#   i+=1

index = 0
while index < 10:
  if index == 4:
    index+=1
    continue
  print(index)
  index+=1

# x = "string"
# for i in x:
#   print(i)

print("########################################################################")
for x in range(6): #loops from 0 to 5
  print(x)
print("########################################################################")
for x in range(2, 6): #loops from 2 to 5
  print(x)
print("########################################################################")
for x in range(2, 6, 2): #loops from 2 to 5 in steps of 2
  print(x)

thisList = ["apple", "bananana", "cherry"]
print(thisList)
print(len(thisList))
print(thisList[0])
print(thisList[-1])   #reverse indexing
print(thisList[1:2])  #range indexing to return a sub-list essentially (inclusive to exclusive).
print(thisList[:2])   #start to end index supplied - can do the reverse to do start index specified to end of array (inclusive to exclusive).
print(thisList[-3:-1])

thislist2 = ["apple", "banana", "cherry"]
for i in range(len(thislist2)):
  print(thislist2[i])

#Notes:
#break used to break out of loop.
#loops are really used as iterators over collections in python.
#range creates a set of value from 0 to the input(exclusive) and increments by 1 until input is reached.
#range(6) => 0, 1, 2, 3, 4, 5.
#python does not have a built in array data type.
#use lists as arrays in python.
#can check if element is in list using the in keyword.
#use insert(index, value) to insert element into array at the specified index value.
#insert, append, extend, remove, pop, del (keyword), clear.
#there are a series of other list related functions that refer to sorting, copying, joining lists, etc - https://www.w3schools.com/python/python_lists_methods.asp
#essentially use lists as your array.
