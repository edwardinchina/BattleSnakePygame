import pygame
import random

## helper functions
#  These do simple math on tuples (x,y)

# move point p by velocity v
def move(p,v):
    return tuple(map(lambda x,y: x+y,p,v))

# scale grid to screen.
# this is useful to make a 10x10 grid big enough to see
def scale(p,s):
    return tuple(map(lambda x: x*s,p))


class Snake(object):
    head = (0,0)
    tail = [(0,1)]
    
    grow = False
    
    def __init__(self, p1, p2, color):
        self.head = p1
        self.tail = [p2]
        self.color = color

    def update(self,v):
        self.tail.insert(0,self.head) #old head become being of tail
        self.head = move(self.head,v) #new head is old head + v
        
        if(not self.grow):
            self.tail.pop() #removes last part of tail
        else:
            self.grow = False
        
    def draw(self,screen):
        
        x,y = scale(self.head,10)
        
        headBox = pygame.Rect(x, y, 10, 10)
        
        pygame.draw.rect(screen, self.color, headBox)
        
        for t in self.tail:
            tBox = pygame.Rect(*scale(t,10), 10, 10)
            pygame.draw.rect(screen, self.color, tBox)
             
      
pygame.init() 
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600,1200)) 

# Initialing Color 
red = (255,0,0) 
green = (0,255,0) 
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
gray = (150,150,150)


player = Snake((20,15),(21,15),red)

AI_Snakes = [Snake((30,15),(31,15),green),
             Snake((40,15),(41,15),blue),
             Snake((50,15),(51,15),yellow),
             Snake((60,15),(61,15),black),
             Snake((70,15),(71,15),white)]
  
while(True):
    screen.fill(gray)
        
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # Window close button clicked?
        break                   #   ... leave game loop
    
    
    v = random.choice([(-1, 0),(1, 0),(0, -1),(0, 1)])
    
    if len(player.tail) < 100:
        player.grow = True
    player.update(v)
    player.draw(screen)

    for ai in AI_Snakes:
        v = random.choice([(-1, 0),(1, 0),(0, -1),(0, 1)])
        if len(ai.tail) < 100:
            ai.grow = True
        ai.update(v)
        ai.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(50)
#end while
pygame.quit()