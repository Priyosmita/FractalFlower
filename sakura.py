





import turtle
t=turtle.Turtle()
t.shape('turtle')
t.screen.bgcolor("black")
t.pensize(2)
t.color("#F4C2C2")
t.left(90)
t.speed(50)
def sakura(i):
    for i in range (300):
        t.circle(190-i,90)
        t.left(90)
        t.circle(190-i,90)
        t.left(18)
sakura(0)
#turtle.write("Flower")
turtle.done()
