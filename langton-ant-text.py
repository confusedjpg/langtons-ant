import os
from random import randint
from time import sleep

def drawGrid(grid: list):
    os.system("cls || clear")
    for line in grid:
        print(*line)

# if set the size to 2 it basically creates a loading icon
# there you go, another feature
def langton(size=20):
    white, black = ' ', '#'
    grid = [[white for i in range(size)] for i in range(size)]
    ant = '+'
    x = y = int(size/2)
    direction = 0
    step = 1
    while True:
        currentSquare = grid[y][x]
        grid[y][x] = ant
        drawGrid(grid)
        if currentSquare == white:
            currentSquare = black
            direction = (direction+1) % 4
        else:
            currentSquare = white
            direction = (direction-1) % 4
        
        grid[y][x] = currentSquare

        if direction == 0:
            ant = '^'
            y = (y-1) % size
        elif direction ==  1:
            ant = '>'
            x = (x+1) % size
        elif direction == 2:
            ant = 'v'
            y = (y+1) % size
        elif direction == 3:
            ant = '<'
            x = (x-1) % size

        sleep(0.1)
        step += 1

langton()
