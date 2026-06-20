from random import *

rowlen = 5

table = []
row1 = [randint(1,5)]
c = 0
while len(row1) < rowlen:
    row1.append(randint(1 if row1[c]<1 else row1[c]-1,5 if row1[c] + 1 > 5 else row1[c] +1))
    c += 1
table.append(row1)
for i in range(rowlen-1):
    c = 0
    row = []
    prevrow = table[len(table)-1]
    while len(row) < rowlen:
        row.append(randint(1 if prevrow[c]-1 < 1 else prevrow[c]-1,5 if prevrow[c] + 1 > 5 else prevrow[c] +1))
        c += 1
    table.append(row)


for i in table:
    print(i)

import turtle
colors = {5:"#000000",4:"#222222", 3:"#444444", 2:"#666666",1:"#888888",0:"#aaaaaa"}




my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
my_turtle.speed(10)

my_turtle.color("#000000")
for row in table:
    for i in row:
        my_turtle.fillcolor(colors[i])
        my_turtle.begin_fill()
        for _ in range(4):
            my_turtle.forward(20)  # Move forward 100 pixels
            my_turtle.right(90)     # Turn 90 degrees clockwise
        my_turtle.end_fill()
        my_turtle.forward(20)
    my_turtle.backward(20*rowlen)
    my_turtle.right(90)
    my_turtle.forward(20)
    my_turtle.left(90)
screen.exitonclick()
