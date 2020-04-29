listOne =["apple", "charry", "orange", "banana"]

listOne.append("mango") #upadte this same list by the add a item in the end of the list

print(listOne)

listOne.insert(2,"blackberry") #update the list by insert one item  in the index of the number
print(listOne)

listOne.remove("charry") #remove any specified item from the list 
print(listOne)

listOne.pop()  #The pop() method removes the specified index, (or the last item if index is not specified):
print(listOne)

listOne.pop(2) #the pop() function output will be romoved orange from the list
print(listOne)

copylist= listOne.copy()
print("this is the copylist")
print(copylist)

del listOne[0] #delete one element from the index one form the list 
print(listOne)

listOne.clear() # clear all list element or item
print(listOne)



print(copylist)

del copylist

print(copylist) #delete this list