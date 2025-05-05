import random


PlayButton = Group(Rect(150,200,100,35,fill='ForestGreen'),Label('PLAY', 200,217, size= 30, font='arial'))
app.background = gradient('White','skyBlue','lightSkyBlue','skyBlue','skyBlue','lawnGreen','limeGreen', start='top')
ScreenName = Label('Snake?!', 200,150,size=50, rotateAngle=- 10)
snakeStart = Group(Rect(70,350,20,5), Circle(100,355,2, fill='red'))

clicker = Circle(200,200, 1, fill='yellow')

def onMouseMove(x,y):
    clicker.centerX =x
    clicker.centerY = y

def onMousePress(x,y):
    if (clicker.hitsShape(PlayButton) == True):
        PlayButton.visible = False
        ScreenName.visible = False
        snakeStart.visible = False
        clicker.visible = False
        
        
        app.background = gradient('lawnGreen','limeGreen','lawnGreen','limeGreen','lime', 'green' ,start = 'top-left')
        snake.visible = True
        apple.visible = True
        Eat.visible = True
        e.visiible = True
    



## The head of the snake, used group to add on extra shapes 
snake = Group(Rect(20,200,25,25, visible = False))




##The shape for the apple
apple = Circle(200,200,10, fill='red', visible = False)
##The label 'apples eaten'
Eat = Label('Apples Eaten:', 200,20,size = 30, font='arial', visible = False)
##The number label which will be changed every time the snake hits the apple
e = Label(0,320,20, size=30, font='orbitron',visible = False)


hits = True
eaten = 0

def onStep():
    global hits, eaten
    ##make it so the snake will always move to the right
    snake.centerX+=1
    ##It will reset the snake back when it hits 400 in the Y axis
    if snake.centerY>400:
        snake.centerY = 0
    ##It will reset the snake back when it hits 400 in the X axis    
    elif snake.centerX > 400:
        snake.centerX = 0
    
    ##If the snake hits the apple and hits equals true then adds 1 to the e label and apple visisble == False 
    if (snake.hitsShape(apple)==True) and hits == True:
        eaten +=1
        e.value = eaten
        hits = False
        apple.visible = False
        ##This another rectangle to the snake everytime it hits the apple
        snake.add(Rect(snake.centerX-35, snake.centerY-12, 25,25))
        apple.centerX = random.randint(50,300)
        apple.centerY = random.randint(50,300)
        apple.visible = True
        hits = True
        

        
        
        print('Hit!')
        
        


def onKeyPress(key):
    global Key_Press
    if key == 'w':
        snake.centerY-=10
    elif key=='a':
        snake.centerX-=10
    elif key=='s':
        snake.centerY+=10
    elif key=='d':
        snake.centerX+=10
        
        
        
