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
    global bone, puppy, bonex, boney, puppyx, puppyy, grass
    size(800,600)
    bone = loadImage('bone.png')
    puppy = loadImage('puppy.png')
    bonex = 407/5
    boney = 613/5
    puppyx = 486/5
    puppyy = 514/5
    grass = loadImage('grass.png')
    grass.resize(800,600)
    

def draw():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass
    background(grass)
    image(bone, x, y,bonex,boney)
    image(puppy, x2, y2, puppyx, puppyy)
    x += speed_x * 3
    y += speed_y * 3
    x2 += speed_x_2
    y2 += speed_y_2
    
    
    if x2 > x and x2 < (x + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
        
    if x > x2 and x < (x2 + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
    
    check_collision()
    find_center()


def check_collision():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass
    #Edge Boundries
        
    if (x > 800 - (bonex) or x < 0):
        speed_x *= -1
        speed_x_2 += 3
        speed_y_2 += 3
        
        find_center()
    elif (y > 600 - (boney) or y < 0):
        speed_y *= -1
        speed_x_2 += 3
        speed_y_2 += 3
        
    if (x2 > (800 - puppyx) or x2 < 0):
        speed_x_2 *= -1
    elif (y2 > (600 - puppyy) or y2 < 0):
        speed_y_2 *= -1
        
  
        
 
       
def find_center():
    global bonex, boney, x, y, bonex2, boney2
    
    bonex2 = x + bonex/2
    boney2 = y + boney/2
    print(bonex2, boney2)
    
