import random

x = 0
y = 300
x2 = 300
y2 = 0

speed_x = 3
speed_y = 3
speed_x_2 = 1
speed_y_2 = 1

bone = None
puppy = None

def setup():
    global bone, puppy, bonex, boney, puppyx, puppyy, grass
    size(1600,1200)
    bone = loadImage('bone.png')
    puppy = loadImage('puppy.png')
    bonex = 407/5
    boney = 613/5
    puppyx = 486/5
    puppyy = 514/5
    grass = loadImage('grass.png')
    grass.resize(1600,1200)
    

def draw():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass
    background(grass)
    image(bone, x, y,bonex,boney)
    image(puppy, x2, y2, puppyx, puppyy)
    x += speed_x * 3
    y += speed_y *3
    
    x2 += speed_x_2
    y2 += speed_y_2
    
    
    check_collision()
    find_center()
    find_direction()





def check_collision():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass
    #Edge Boundries
        
    if (x > 1600 - (bonex) or x < 0):
        speed_x *= -1
        if speed_x_2 >0:
            speed_x_2 += 1
        else:
            speed_x_2 -= 1
        if speed_y_2 > 0:
            speed_y_2 += 1
        else:
            speed_y_2 -= 1
            
            
 
    elif (y > 1200 - (boney) or y < 0):
        speed_y *= -1
        if speed_x_2 >0:
            speed_x_2 += 1
        else:
            speed_x_2 -= 1
        if speed_y_2 > 0:
            speed_y_2 += 1
        else:
            speed_y_2 -= 1
        
        
        

  
def find_direction():
    
    global bonex_center, boney_center,speed_y_2, speed_x_2,x2,y2,puppyy_center,puppyx_center
    
    if bonex_center < puppyx_center:
        if speed_x_2 > 0:
            speed_x_2 *= -1
        
        
    if bonex_center > puppyx_center:
        if speed_x_2 < 0:
            speed_x_2 *= -1
            
            
    if boney_center < puppyy_center:
        if speed_y_2 > 0:
            speed_y_2 *= -1 
    
    if boney_center > puppyy_center: 
        if speed_y_2 < 0:
            speed_y_2 *= -1
        
        
    
 
       
def find_center():
    global bonex, boney, x, y, bonex_center, boney_center, x2, y2, puppyx_center, puppyy_center, puppyx, puppyy
    
    bonex_center = x + bonex/2
    boney_center = y + boney/2
    puppyx_center = x2 + puppyx/2
    puppyy_center = y2 + puppyy/2
    
    
    print(bonex_center, boney_center)
    
