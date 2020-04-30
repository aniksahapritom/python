tupleOne = ("apple", "charry", "mango")
print(tupleOne)
print(type(tupleOne))

x = list(tupleOne)

print(type(x))

x[1]="banana" # replace value in index one

print(x)

tupleOne = tuple(x)

print(tupleOne)

print(type(tupleOne))


# Different thing is that 

thistuple = ("apple",) # this is a tuple ##  Must be remember the comma (,)
print(type(thistuple))
thisString = ("apple")
print(type(thisString))


