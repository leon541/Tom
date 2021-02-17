import random
game_over = False
time = 0
while not game_over:
    random_number = random.randint(0,10000)
    #print(random_number)
    stop = False
    while not stop:
        guess_number = int(input("guess a random number bewtwn 0 - 10000:"))
        if guess_number > random_number:
            print("the number is too big")
        elif guess_number < random_number:
                print("the number is too small ")
        elif guess_number == random_number:
            print("right")
            stop = True
            time = time + 1 # time++
        if time == 2:
            print("you win")
            game_over = True