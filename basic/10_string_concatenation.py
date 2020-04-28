a = "hello"
b = "world"
c = a.upper() + " " + b.upper()
d = c + "!"
print(d)

e = d + " This {} my first type in {} when my age {} {}" #The format() method takes unlimited number of arguments, and are placed into the respective placeholders
f = "was"
g = 23
h = "python"

i = e.format(f,h,f,g)
print(i) 

p = "I want to pay {} dollars for {} pieces of the item {}"

price = 20.25
piece = 10
itemNo = 12

q = p.format(price,piece,itemNo)
print(q)

p = "I want to pay {0} dollars for {2} pieces of the item {1}" # we can define index number from format
q = p.format(price,piece,itemNo)
print(q)

