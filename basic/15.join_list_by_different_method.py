#One way
listOne = ["a", "b", "c"]
listtwo = [1, 2, 3]

listthree = listOne + listtwo
print(listthree)

# two way
list4 = ["a", "b"]
list5 = [1, 2, 3]

for x in list5:
    list4.append(x)
print(list4)

# thrid way
list6 = ["apple", "banana", "blackberry"]
list7 = [1, 2, 3, 4, 5]

list6.extend(list7)
print(list6)