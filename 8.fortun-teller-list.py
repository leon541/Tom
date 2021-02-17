import random
fortune_list = []
fortune_list.append("no,no no")
fortune_list.append("yep")
fortune_list.append("maybe")
fortune_list.append("of corse  ")
fortune_list.append("alas,yes")
fortune_list.append("sure")
print("would you like me to tell you your fortune")
answer = input("yes or no: ")
while answer == "yes" or answer == "Yes":
    print("ask me a yes or no qeston . . .")
    qestion = input()
    #print(random.choice(fortune_list))
    # random.randint(3,9) returns a number between 3 (included) and 9 (included)

    # random.randrange(3,9) returns a number between 3 (included) and 9 (not included)
    choice = random.randrange(0, len(fortune_list))
    print(fortune_list[choice])
    print("do you want another fortune?")
    answer = input("yes or no")



