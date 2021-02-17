import turtle
import time
turtle.screensize(800, 600, "green")
turtle.speed(1)
turtle.forward(300)

turtle.shape("turtle")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

pony = turtle.Turtle();

'''
pony.shape("turtle")
pony.forward(100)
pony.left(90)
pony.forward(100)
'''


turtle.color("red", "yellow")
turtle.speed(10)
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
time.sleep(1)

#turtle.done()