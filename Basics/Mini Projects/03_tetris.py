import pygame
import random

# making an array of colors for the blocks
colors =[
    (39, 207, 204), # greenish -blue
    (59, 194, 247), # blue
    (120, 60, 250), # purple
    (188, 54, 255), # pink
    (237, 36, 36 ), #red
    (245, 125, 12), #orange
    (255, 225, 28), #yellow
]

class Figure:
    x = 0
    y = 0

    figures = [
        [[1,5,9,13],[4,5,6,7]],
        [[4,5,9,10],[2,6,5,9]],
        [[6,7,9,10],[1,5,6,10]],
        [[1,2,5,9],[0,4,5,6],[1,5,9,8],[4,5,6,10]],
        [[1,2,6,10],[5,6,7,9],[2,6,10,11],[3,5,6,7]],
        [[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,19]],
        [[1,2,5,6]]
    ]

def __init__(self , x , y):
    self.x = x
    self.y = y
    self.type = random.randint(0,len(self.figures)-1)
    self.color = random.randint(1, len(colors)-1)
    self.rotation = 0

def image(self):
    return self.figures[self.type][self.rotation]

def rotate(self):
    self.rotation = (self.rotation +1) % len(self.figures(self.length))

class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self , height , width):
        self.height = height
        self.width = width
        self.feild = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.feild.append(new_line)

    def new_figure(self):
        self.figure = Figure(3,0)

    def intersections(self):
        


       









