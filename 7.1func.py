def tom_say(something):
    print("tom say:",something)

def berty_say(something):
    print("berty say:",something)

tom_say("hi")
berty_say("hi")
tom_say("ok")
berty_say("ok")
berty_say("hi")
tom_say("ok")
tom_say("bye")
berty_say("bye")


# * * * (num)
def printStars (num):
    for x in range(num):
        print("*", end="")

# *
# * *
# * * * (num)
def printFlag(num):
    for x in range(1,num + 1):
        printStars(x)
        print("")


print("")
f = int(input("input flag size:"))
printFlag(f)

print("")
n = int(input("how many stars do you need:"))
printStars(n)





