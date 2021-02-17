import turtle

cow = turtle.Turtle()
cow.speed(1)
cow.color("blue")
for x in range(1,101): # 0, 1, 2, 3
    cow.circle(x)
    cow.left(360/x)

turtle.done()