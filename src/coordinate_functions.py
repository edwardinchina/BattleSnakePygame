## helper functions
#  These do simple math on tuples (x,y)

# move point p by velocity v
def move(p,v):
    return tuple(map(lambda x,y: x+y,p,v))

# scale grid to screen.
# this is useful to make a 10x10 grid big enough to see
def scale(p,s):
    return tuple(map(lambda x: x*s,p))

## TESTING

# move
result = move((10,10),(5,5))
print(result)
assert(result == (15,15))

p = (3,5)
v = (1,0)
result = move(p, v)
print(result)
assert(result == (4,5))

# scale
print(scale((10,10), 10))

p = (3,5)
s = (100)

print(scale(p, s))