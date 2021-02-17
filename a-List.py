def printList(list):
    print("----")
    for i in list:
        print(i)
    print("----")



foods = ["apple","banana","pie","pear"]
print(foods[2])

print("----")
for x in foods:
    print(x)
print("--append apple--")

foods.append("apple")

for x in foods:
    print(x)
print("--remove pie--")
foods.remove("pie")

for i in foods:
    print(i)
print("----")

print("len: ", len(foods))

foods.insert(0, "dragonfruit")
printList(foods)

foods.reverse()
printList(foods)

print("apple index:" , foods.index("apple"))
print("pear index:" , foods.index("pear"))

print("----")

foods.clear()
print(foods)

