from cmu_graphics import *
app.stepPerSecond = 90
player = Rect(200,200,30,50,fill='crimson',border='black')
playercharge = Rect(200,200,30,25,fill='crimson',border='black')
ground = Group(Line(50,370,350,370,opacity=60),Rect(0,370,400,8000,fill=None),Rect(325, 175,40,5),Rect(100,300,40,7))
walls1 = Group(Line(50,50,50,300)) 
walls2 = Group(Line(350,200,350,300))
player.visible = True
player.centerY = 344
playercharge.visible = False
player.dy = 0
player.gravity = 0.6
app.jump = 0
app.jumpmax = 15
app.air_force = 0
app.charge = False
app.sidespeed = 3
app.walk = 3
player.dx = 0
# def levelLoader(level):
#    with open(level) as file:
#        for line in file:
#            print(line.rstrip())




def onKeyHold(keys):
    if player.hitsShape(ground) == True:
        if (('space' in keys) == False):
            if ('d' in keys):
                    player.centerX += app.walk
            if ('a' in keys):
                    player.centerX -= app.walk
    if player.hitsShape(ground) == True:
        if ('space' in keys):
                app.jump += -0.6             
                playercharge.visible = True
                player.visible = False
        if (app.jump <= -app.jumpmax):
            app.jump = -app.jumpmax
    if ('space' in keys):
        app.charge = True
    else:
        app.charge = False
    if player.hitsShape(ground) == True and app.charge == True:
        if('d' in keys):
            app.air_force = app.sidespeed
        if('a' in keys):
            app.air_force = -app.sidespeed   
    
def onKeyPress(keys):
       if keys == 'space':
        app.air_force = 0

def onKeyRelease(keys):
    if player.hitsShape(ground) == True:
        if (keys == 'space'):
            player.dy = app.jump
            playercharge.visible = False
            player.visible = True
            app.jump = 0
    if (keys == 'space'):  
        app.charge = False
    



def onStep():
#stuff above 
    if player.hitsShape(ground) == False:
        player.centerX += app.air_force
    playercharge.centerX = player.centerX 
    playercharge.centerY = player.centerY+12.5
    player.centerY += player.dy
    if player.hitsShape(ground) != True:
        player.dy += player.gravity

    for platform in ground.children:
        if player.hitsShape(platform) and player.bottom < platform.top + (player.dy):
            player.bottom = platform.top
            player.dy = 0
        if player.hitsShape(platform) and player.bottom > platform.top + (player.dy+9):
            player.top = platform.bottom
            player.dy = 2
    for side in walls1.children:
        if player.hitsShape(side) and player.left < side.right + (player.dx):
            player.left = side.right
            app.air_force = -app.air_force
    for side in walls2.children:
        if player.hitsShape(side) and player.right > side.left + (player.dx):
            player.right = side.left
            app.air_force = -app.air_force
    


cmu_graphics.run()