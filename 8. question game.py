points = 0
correct_answer = 0

print("1.what is more expenceive a380 or an225 or one of the most expensive private yachts or a mansion")
print("a.a380")
print("b.an225")
print("c.yachts")
print("d.mansion")
answer = input("enter letter:")
if answer == "a" or answer == "A":
    print("correct")
    correct_answer += 1
    points += 2
else:
    print("no")
    points -= 1