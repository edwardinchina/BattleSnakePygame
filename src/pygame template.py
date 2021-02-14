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
        #scale
        x,y = scale(self.head,world_scale)
        
        headBox = pygame.Rect(x, y, world_scale, world_scale)
        
        
        pygame.draw.rect(screen, self.color, headBox)
        
        for t in self.tail:
            tBox = pygame.Rect(*scale(t,world_scale), world_scale, world_scale)
            pygame.draw.rect(screen, self.color, tBox)


class Player(Snake):
    def update(self,food):
        keys = pygame.key.get_pressed()
        x = 0
        y = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x = 1

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x = -1
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y = 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y = -1

        super().update((x,y),food)


## Set Up Global Variables
pygame.init() 
clock = pygame.time.Clock()


world_scale = 15
world_width = 50
world_height = 30

screen_width =  world_width * world_scale
screen_height = world_height * world_scale
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
        x = random.randint(0, world_width)
        y = random.randint(0, world_height)
        food.append((x,y))
        
        
        x = random.randint(0, world_width)
        y = random.randint(0, world_height)
        squirrels.append((x,y))
        
    
    for rat in food:
        ratBox = pygame.Rect(*scale(rat,world_scale), world_scale, world_scale)
        pygame.draw.rect(screen, brown, ratBox)
    
    
    for s in squirrels:
        sBox = pygame.Rect(*scale(s,world_scale), world_scale, world_scale)
        pygame.draw.rect(screen, white, sBox)
    
    if len(player.tail) < 100:
        player.grow = True
    player.update(food)   #don't pass v to player, player has controls
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