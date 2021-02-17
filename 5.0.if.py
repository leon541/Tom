driving_age = 16
your_age = int(input("whats your age:"))
if your_age>= driving_age:
    print("you can drive")
else:
    print("you cant drive")
    print("wait",driving_age - your_age,"years")
