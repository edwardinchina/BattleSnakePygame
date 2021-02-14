import pygame
import random
import color as c
from coordinate_functions import move, scale
## helper functions
#  These do simple math on tuples (x,y)


class Snake(object):
    head = (0,0)
    tail = [(0,1)]
    
    grow = False
    
    def __init__(self, p1, p2, color):
        self.head = p1
        self.tail = [p2]
        self.color = color

    def update(self,v,food):
        self.tail.insert(0,self.head) #old head become being of tail
        self.head = move(self.head,v) #new head is old head + v
        
        
        for rat in food:
            if(self.head == rat):
                food.remove(rat)
                self.grow = True
                print(len(self.tail))
        
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

screen_width = 1600
screen_height = 1200
screen = pygame.display.set_mode((screen_width,screen_height)) 



player = Snake((20,15),(21,15),c.red)

AI_Snakes = [Snake((30,15),(31,15),c.green),
             Snake((40,15),(41,15),c.blue),
             Snake((50,15),(51,15),c.yellow),
             Snake((60,15),(61,15),c.black),
             Snake((70,15),(71,15),c.white)]

food = []
squirrels = []

timer = 0

while(True):
    screen.fill(c.gray)
        
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # Window close button clicked?
        break                   #   ... leave game loop
    
    
    ## food
    if timer == 0:
        x = random.randint(0, screen_width/10)
        y = random.randint(0, screen_height/10)
        food.append((x,y))
        
        
        x = random.randint(0, screen_width/10)
        y = random.randint(0, screen_height/10)
        squirrels.append((x,y))
        
    
    for rat in food:
        ratBox = pygame.Rect(*scale(rat,10), 10, 10)
        pygame.draw.rect(screen, c.brown, ratBox)
    
    
    for s in squirrels:
        sBox = pygame.Rect(*scale(s,10), 10, 10)
        pygame.draw.rect(screen, c.white, sBox)
    
    v = random.choice([(-1, 0),(1, 0),(0, -1),(0, 1)])
    
    if len(player.tail) < 100:
        player.grow = True
    player.update(v,food)
    player.draw(screen)

    for ai in AI_Snakes:
        v = random.choice([(-1, 0),(1, 0),(0, -1),(0, 1)])
        if len(ai.tail) < 100:
            ai.grow = True
        ai.update(v,food)
        ai.draw(screen)
    
    pygame.display.flip()
    
    
    clock.tick(50)
    timer += 1
    timer %= 3
#end while
pygame.quit()