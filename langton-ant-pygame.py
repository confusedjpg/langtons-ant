# Langton's ant visualised using Pygame
# The idea: an "ant" can walk in all 4 directions on a grid of squares:
# - if the ant is on a white (blank) square, it fills the square, turns 90° clockwise and goes forward once
# - if the ant is on a black (filled) square, it blanks the square, turns 90° counter-clockwise and goes forward once
# After around 11k steps, the ant will go infinitely in one direction, creating a "highway".
# In this simulation, the ant starts the highway but stops into a wall.

import pygame

WIDTH = HEIGHT = 500
SIZE = 5
RWIDTH, RHEIGHT = WIDTH // SIZE, HEIGHT // SIZE
# you can set any colors here, really, however i found out that setting it using words (i.e 'white') doesn't work
BLANK, FILLED = (0,0,0), (255,255,255)
SPEEDS = [0.1, 0.5, 0.75, 1, 2, 4, 8, 10, 20]
CURRENT_SPEED_ID = 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLANK)
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 20)

class Ant:
    def __init__(self):
        self.x = int(RWIDTH/2)
        self.y = int(RHEIGHT/2)
        self.dir = 0
        self.bumped_its_head_on_a_wall_stupid_ant_why_would_you_do_that = False
    
    def update(self):
        x, y = self.x, self.y
        
        if isColored(x, y):
            self.dir = (self.dir - 1) % 4
        else:
            self.dir = (self.dir + 1) % 4
        
        if self.dir == 0:
            self.y -= 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        else:
            self.x -= 1
        
        switchColor(x, y)

def convertTopLeft(x, y):
    return (x*SIZE, y*SIZE)

def switchColor(x, y):
    color = BLANK if isColored(x, y) else FILLED
    img = pygame.Surface((SIZE, SIZE))
    img.fill(color)
    rect = img.get_rect()
    rect.x, rect.y = convertTopLeft(x, y)
    screen.blit(img, rect)

def isColored(X, Y):
    X, Y = convertTopLeft(X, Y)
    for x in range(X, X+SIZE):
        for y in range(Y, Y+SIZE):
            try:
                if screen.get_at((x, y)) != FILLED:
                    return False
            except:
                ant.bumped_its_head_on_a_wall_stupid_ant_why_would_you_do_that = True
                return True
    return True

ant = Ant()
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, BLANK, pygame.Rect(0, 0, WIDTH, 100)) # erases previous top information
            if event.key == pygame.K_LEFT:
                CURRENT_SPEED_ID = (max(0, CURRENT_SPEED_ID-1))
            elif event.key == pygame.K_RIGHT:
                CURRENT_SPEED_ID = (min(CURRENT_SPEED_ID+1, len(SPEEDS)-1))

            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_s:
                pygame.image.save(screen, "langton-ant.png")

    if ant.bumped_its_head_on_a_wall_stupid_ant_why_would_you_do_that:
        end = font2.render("Just imagine that it goes that way forever.", True, FILLED, BLANK)
        endpos = img.get_rect(midleft=(int(WIDTH/2-font2.size("Just imagine that it goes that way forever.")[0]/2), HEIGHT-10))
        screen.blit(end, endpos)
    elif not paused:
        ant.update()
    
    info = ["ESC to exit", "SPACE to play/pause", "RIGHT/LEFT to go faster/slower", "S to save the current frame"]
    x = y = 10
    for txt in info:
        height = font2.get_height()
        img = font2.render(txt, True, FILLED, BLANK)
        imgpos = img.get_rect(topleft=(x, y))
        screen.blit(img, imgpos)
        y += (height+5)

    speed = font.render(f"x{SPEEDS[CURRENT_SPEED_ID]}", True, FILLED, BLANK)
    speedpos = speed.get_rect(topright=(WIDTH-10, 10))
    screen.blit(speed, speedpos)

    pygame.display.flip()
    clock.tick(60 * SPEEDS[CURRENT_SPEED_ID])
