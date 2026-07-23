from random import *

# def create(rowlen):
#     table = []
#     row1 = [randint(1,5)]
#     c = 0
#     while len(row1) < rowlen:
#         row1.append(randint(1 if row1[c]==1 else row1[c]-2,5 if row1[c] + 2 > 5 else row1[c] +2))
#         c += 1
#     table.append(row1)
#     for i in range(rowlen-1):
#         c = 0
#         row = []
#         prevrow = table[len(table)-1]
#         while len(row) < rowlen:
#             row.append(randint(1 if prevrow[c]-2 < 1 else prevrow[c]-2,5 if prevrow[c] + 2 > 5 else prevrow[c] +2))
#             c += 1
#         table.append(row)


#     for i in table:
#         print(i)
#     return table





def island(rowlen,isize):
    map = []
    for i in range(rowlen):
        row = []
        for j in range(rowlen):
            row.append(0)
        map.append(row)
    seedx = randint(int(rowlen/2)-1,int(rowlen/2))
    seedy = randint(int(rowlen/2)-1,int(rowlen/2))
    seedx -= int(isize/2) if seedx - int(isize/2) > 0 else 0
    seedy -= int(isize/2) if seedy - int(isize/2) > 0 else 0
    x = seedx
    y = seedy
    # for i in range(isize):
    #     for i in range(isize):
    #         map[seedy][x] = 5
    #         x+=1
    #     x = seedx
    #     y+=1
    x = seedx
    y = seedy
    height = 5
    change = 1
    map[seedy][seedx] = 5
    for i in range(2):
        height -= 1
        change += 1
        x-=1
        map[y][x] = height
        y+=1 
        map[y][x] = height
        x+=1
        map[y][x] = height
        x+=1
        map[y][x] = height
        y-=1
        map[y][x] = height
        y-=1
        map[y][x] = height
        x-=1 
        map[y][x] = height
        x-=1 
        map[y][x] = height
        x = seedx
        y = seedy
    # x = seedx
    # for i in range(int(isize/2)):
    #     x += 1
    #     map[seedy][x] = 5

    # x = seedx
    # for i in range(int(isize/2)):
    #     x -= 1
    #     map[seedy][x] = 5

    # y = seedy
    # for i in range(int(isize/2)):
    #     y += 1
    #     map[y][seedx] = 5
    
    # y = seedy
    # for i in range(int(isize/2)):
    #     y -= 1
    #     map[y][seedx] = 5

    for i in map:
         print(i)
    return map




import turtle
colors = {5:"#104500",4:"#0F8005", 3:"#02BC2A", 2:"#F7FDAE",1:"#6DBDCD",0:"#111063"}




my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
my_turtle.speed(0)
screen.tracer(0)
my_turtle.penup()

my_turtle.color("#000000")
def print_table(table,rowlen):
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
rowlen = int(input("Table Size: "))
size = int(input("Island Size: "))
print_table(island(rowlen,size),rowlen)











































# import matplotlib.pyplot as plt
# from perlin_noise import PerlinNoise
# from random import *

# def create(size,resolution):
#     noise = PerlinNoise(octaves=size, seed=randint(1,100))
#     noise_grid = []
#     for i in range(resolution):
#         row = []
#         for j in range(resolution):
#             noise_value = noise([i / resolution, j / resolution])
#             row.append(noise_value)
#         noise_grid.append(row)
#     return noise_grid 

# def show(map):
#     plt.imshow(map, cmap='terrain')
#     plt.axis('off')
#     plt.show()
# show(create(int(input("Size: ")),int(input("Resolution: "))))
