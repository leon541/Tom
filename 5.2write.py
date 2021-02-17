import turtle
hi = turtle.Turtle();
hi.shape("turtle")

your_age = int(input("enter your age:"))
if your_age>=10 and your_age<=15:
    hi.write("your age is bewtwn 10 and 15")
    hi.backward(20)

turtle.done()