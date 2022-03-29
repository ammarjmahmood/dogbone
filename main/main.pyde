import random

speed_x = 3
speed_y = 3
speed_x_2 = 1
speed_y_2 = 1

bone = None
puppy = None

add_library('minim')

def setup():
    global bone, puppy, bonex, boney, puppyx, puppyy, grass, x, y, x2, y2, game_over
    size(1600,1200)
    game_over = False
    



    bone = loadImage('bone.png')
    puppy = loadImage('puppy.png')
    bonex = 407/5
    boney = 613/5
    puppyx = 486/5
    puppyy = 514/5
    grass = loadImage('grass.png')
    grass.resize(1600,1200)
    # make these random intregers between screen so it makes it spawn randmoly on the screen
    x = random.randint(0, 1600 - bonex) #0 #between 0 and 1600
    y = random.randint(0, 1200 - boney) #300 #between 0 and 1200
    x2 = random.randint(0, 1600 - puppyx) #300 #between 0 and 1600
    y2 = random.randint(0, 1200 - puppyy) #0 #between 0 and 1200
    #add music 
    minim = Minim(this)
    sound = minim.loadFile("calm.mp3")
    sound.loop()

def draw():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass, x, y, x2, y2, game_over
    
    if game_over == False:
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
        check_end()
    else:
        background(grass)
        textSize(52)
        textAlign(CENTER)
        text("DOG HAS CAUGHT BONE!!!!", 700, 500)
        



def check_collision():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass, x, y, x2, y2
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
        
        
        
def check_end():
    #check if two things are touching and if so change game over 
    global game_over 
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, bone, puppy, bonex, boney, puppyx, puppyy, grass, x, y, x2, y2
    
    # if bonex_center == puppyx_center and boney_center == puppyy_center:
    #     game_over = True
        
        
    # if (bonex_center - 2) == (puppyx_center - 2) or (bonex_center + 2) == (puppyx_center + 2) and (boney_center - 2) == (puppyy_center - 2) or (boney_center + 2) == (puppyy_center + 2):
    #     game_over = True
    
    if (x-30) < (x2-30) + (bonex - 30) and (x - 30) + (puppyx - 30) > (x2 - 30) and (y - 30) < (y2 - 30) + (boney - 30) and (boney - 30) + (y - 30) > (y2 - 30):
        game_over = True
    
def find_direction():
    
    global bonex_center, boney_center,speed_y_2, speed_x_2,x2,y2,puppyy_center,puppyx_center, x, y, x2, y2
    
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
    global bonex, boney, x, y, bonex_center, boney_center, x2, y2, puppyx_center, puppyy_center, puppyx, puppyy, x, y, x2, y2
    
    bonex_center = x + bonex/2
    boney_center = y + boney/2
    puppyx_center = x2 + puppyx/2
    puppyy_center = y2 + puppyy/2
    
    
    print(bonex_center, boney_center)
    
