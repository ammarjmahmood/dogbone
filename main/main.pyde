x = 0
y = 300
x2 = 300
y2 = 0

speed_x = 2
speed_y = 2
speed_x_2 = 2
speed_y_2 = 2

bone = None
puppy = None

def setup():
    global bone, puppy
    size(800,600)
    bone = loadImage('bone.png')
    puppy = loadImage('puppy.png')

def draw():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy
    background('#000000')
    image(bone, x, y)
    image(puppy, x2, y2)
    x += speed_x
    y += speed_y
    x2 += speed_x_2
    y2 += speed_y_2
    
    
    if x2 > x and x2 < (x + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
        
    if x > x2 and x < (x2 + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
    
    if (x2 > 700 or x2 < 0):
        speed_x_2 *= -1
    elif (y2 > 555 or y2 < 0):
        speed_y_2 *= -1
        
    if (x > 700 or x < 0):
        speed_x *= -1
    elif (y > 555 or y < 0):
        speed_y *= -1
    
       
    
