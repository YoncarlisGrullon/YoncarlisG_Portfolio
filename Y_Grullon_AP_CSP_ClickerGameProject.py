##To randomly place each coin in the screen
import random


##The starting screen
sb = Rect(0,0,400,400, fill =gradient('dodgerBlue','deepskyBlue','royalBlue','royalBlue',start='top-right'))
sl =Label('Coin Game!', 200,100, fill=gradient('yellow','gold','gold'), size = 50)
button = Rect(140,180, 125,50, fill=gradient('lime','lawnGreen',start='top-right'))
play = Label('PLAY', 200,205,fill='black', size=30)
StartS = Group(sb,sl)
StartB = Group(button, play)
    
coins = Circle(200,200,25,fill=gradient('gold','yellow','gold',start='top-left'), visible=False)



coin_count = 0
BackGround = 0

def game_backGround():
    global coin_count, BackGround
    ##The background 
    BackGround = Rect(0,0,400,400, fill=gradient('lightBlue','paleTurquoise','lightBlue','lightCyan', start='left'))
    BackGround.misses = 0
    ##The counter for the number of coins you cicked
    coin_count = Label(0,200,55, font='grenze', size = 50)
    Label('Coins:',200,20, font='grenze', size = 50)
    #The coins model
    

#The mouse pointer
clicker = Circle(200,200,5,fill='red')

##This follows the users mouse
def onMouseMove(x,y):
    clicker.centerX = x
    clicker.centerY = y
    
    
##This the user earn misses and coins which is determined where they click
def onMousePress(x,y):
    global coin_count, BackGround
    if (clicker.hitsShape(StartB) ==True):
        StartS.visible = False
        StartB.visible = False
        coins.visible = True
        game_backGround()
    
        if (clicker.hitsShape(coins) == True):
            coin_count.value += 1
            print('Hit')
            coins.centerX = random.randint(0,370) 
            coins.centerY = random.randint(0,270)
        
        
        elif (clicker.hitsShape(coins) ==False):
            BackGround.misses +=1 
            print('Miss')
        
        else:
            
        
    
            print(BackGround.misses)
        
    
    
