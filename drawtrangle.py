from turtle import *

colors = ["red","blue","green","yellow","black"]
def drawtrangle(x=0,y=0,colorindex=0):
    home()
    goto(x,y)
    pencolor(colors[colorindex])
    pendown()
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    penup()

for i in range(10):
    drawtrangle(i*20,i*20,i % 5)

done()
