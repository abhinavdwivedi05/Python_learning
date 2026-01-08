listm=['apple','cake','dairymilk']
x=listm[0]

print(type(x))
print(x)
print(len(listm))

numlist= [1,2,3,4,6,7,8,9]


print("\n Iterating in a list ")
if 2 in numlist:
    print("present\n\n")
for x in range(len(listm)):
    print(listm[x])

print("\n Appending of list only the element that have a ")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

print("\n Sorting of list ")
numlist.sort()
print(numlist)

print("\n Sorting of list with conditions")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print("\n reversing of list")
listm.reverse()
print(listm)

print("\n copying of list")
newlistm= listm.copy()
print(newlistm)

print("\n joining of list")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
