def getSum(num):
    sum = 0
    for x in range(1, num+1):
        sum = sum + x
    return sum
print("sum to 10: ", getSum(10))  # 55
print("sum to 100: ", getSum(100))  # 5050


def isodd(num):
    if num % 2 == 1:
        return True
    return False
for x in range (1, 16):
    if isodd(x):
        print( x , " is even ")
    else:
        print( x, " is odd")
# <-- to do
def is_even(num):
    if num % 2 == 1:
        return False
    return True

for x in range (1, 16):
    if is_even(x):
        print( x , " is even ")
    else:
        print( x, " is odd")

# to do -->

# to do 2
def is_prime(num):
    for x in range (2, num):
        if num % x == 0:
            return False
    return True

for x in range (1, 21):
    if is_prime(x):
        print( x , " is a prime number ")
    else:
        print( x, " is not prime")

#to do
# 1 : 1
# 2 : 4
# 4 : 4 * 4
def get_square(num):
    return num * num

for x in range (1, 11):
   print( x , "square is ",get_square(x))


print( "-----------------------------------")


def get_bigger( n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


print(" the bigger of 2 , 3 is ", get_bigger(2, 3))

print( "-----------------------------------")

def get_biggest( n1, n2, n3):
    if n1 > n2 and n1> n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(" the biggest of 2 , 3 , 4 is ", get_biggest(2, 3 , 4))




