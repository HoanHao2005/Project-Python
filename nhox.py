import turtle
from turtle import *
wn=Screen()
wn.bgcolor('black')
t=turtle.Turtle()
t.pencolor('white')
def curve():
    for _ in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()
def write(message,pos):
        x,y=pos
        t.penup()
        t.goto(x,y)
        t.color('white')
        style=('Stencil Std',18,'italic')
        t.write(message,font=style)

write('I',(-65,95))
write('L',(-50,95))
write('U',(-35,95))
write('V',(-20,95))
write('W',(5,95))
write('I',(30,95))
write('B',(36,95))
write('U',(50,95))

wn.mainloop()