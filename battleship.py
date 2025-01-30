# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Praytor
#               Ryan Santry
#               Timothy Tsai
#               Anson Thai
#               Griffin Ainsworth
# Section:      518
# Assignment:   Lab Topic 13
# Date:         16 December 2022

import turtle as t
import math as m





# Note from the Creators

# Ignore, any output or error that may be shown in the console. These were implemented for testing purposes





t.delay(0)
t.speed(0)
t.tracer(0, 0)
playerOneShipGrid = []
playerTwoShipGrid = []
playerOneShots = []
playerTwoShots = []
playerOneShotList = []
playerTwoShotList = []










########################################################################












def hull(x, y):
    ''' Center Hull Piece for Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x, y-5)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(0)
    t.forward(50)
    t.right(90)
    t.penup()
    t.forward(40)
    t.right(90)
    t.pendown()
    t.forward(50)
    t.end_fill()
    t.penup()
    t.setpos(x+25, y-25)
    t.pendown()
    t.dot(20, "#666666")

def hullRightEnd(x, y):
    ''' Right Hull Piece for Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x, y-5)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(0)
    t.forward(30)
    t.penup()
    t.setpos(x+29, y-45)
    t.setheading(180)
    t.pendown()
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+29, y-45)
    t.setheading(0)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.circle(20, 180)
    t.end_fill()
    t.penup()
    t.setpos(x+25, y-25)
    t.pendown()
    t.dot(20, "#666666")

def hullLeftEnd(x, y):
    ''' Left Hull Piece for Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x+50, y-5)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(180)
    t.forward(30)
    t.penup()
    t.setpos(x+20, y-45)
    t.setheading(00)
    t.pendown()
    t.forward(31)
    t.penup()
    t.end_fill()
    t.setpos(x+21, y-5)
    t.setheading(180)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.circle(20, 180)
    t.penup()
    t.end_fill()
    t.setpos(x+25, y-25)
    t.pendown()
    t.dot(20, "#666666")
    
def hullVert(x, y):
    ''' Center Hull Piece for Verical Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x+5, y)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(90)
    t.forward(50)
    t.right(90)
    t.penup()
    t.forward(40)
    t.right(90)
    t.pendown()
    t.forward(50)
    t.end_fill()
    t.penup()
    t.setpos(x+25, y+25)
    t.pendown()
    t.dot(20, "#666666")

def hullTopEnd(x, y):
    ''' Top Hull Piece for Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x+5, y)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(90)
    t.forward(30)
    t.penup()
    t.setpos(x+45, y+29)
    t.setheading(270)
    t.pendown()
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+45, y+29)
    t.setheading(90)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.circle(20, 180)
    t.end_fill()
    t.penup()
    t.setpos(x+25, y+25)
    t.pendown()
    t.dot(20, "#666666")
    
def hullBottomEnd(x, y):
    ''' Bottom Hull Piece for Ship "Pieces" '''
    t.speed(0)
    t.penup()
    t.setpos(x+5, y+50)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setheading(270)
    t.forward(30)
    t.penup()
    t.setpos(x+45, y+21)
    t.setheading(90)
    t.pendown()
    t.forward(31)
    t.penup()
    t.end_fill()
    t.setpos(x+5, y+21)
    t.setheading(270)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.circle(20, 180)
    t.penup()
    t.end_fill()
    t.setpos(x+25, y+25)
    t.pendown()
    t.dot(20, "#666666")

def boatSprite(x, y):
    '''Aesthetic ships at the bottom of the Game Window'''
    t.width(5)
    t.color("#111111")
    t.penup()
    t.setpos(x+140, y+15)
    t.setheading(155)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setpos(x+85, y+5)
    t.setheading(155)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setpos(x+340, y+15)
    t.setheading(25)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setpos(x+395, y-10)
    t.setheading(25)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setpos(x+160, y+35)
    t.setheading(170)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.circle(30, 105)
    t.penup()
    t.setpos(x+165, y-20)
    t.end_fill()
    t.penup()
    t.setpos(x+255, y+40)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(24)
    t.right(120)
    t.forward(45)
    t.end_fill()
    t.penup()
    t.setpos(x+255, y+10)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+320, y+10)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(24)
    t.right(90)
    t.forward(28)
    t.right(60)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+380, y-20)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(24)
    t.right(90)
    t.forward(28)
    t.right(60)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+100, y-3)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(24)
    t.left(90)
    t.forward(28)
    t.left(60)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.setpos(x+240, y+10)
    t.setheading(0)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(125)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(135)
    t.end_fill()
    t.penup()
    t.setpos(x+165, y+40)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.forward(20)
    t.right(45)
    t.forward(20)
    t.right(45)
    t.forward(45)
    t.right(90)
    t.forward(35)
    t.end_fill()
    t.penup()
    t.setpos(x+165, y-20)
    t.setheading(90)
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.pendown()
    t.forward(60)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(60)
    t.end_fill()
    t.penup()
    t.fillcolor("#9B9B9B")
    t.begin_fill()
    t.setpos(x, y)
    t.setheading(0)
    t.pendown()
    t.forward(150)
    t.right(45)
    t.forward(24)
    t.left(45)
    t.forward(275)
    t.right(135)
    t.forward(50)
    t.right(45)
    t.forward(425-50*m.sqrt(2))
    t.right(45)
    t.forward(74)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    
def carrierHor(x, y):
    '''Horizontal Carrier Sprite'''
    t.penup()
    hullLeftEnd(x, y)
    hull(x+50, y)
    hull(x+100, y)
    hull(x+150, y)
    hull(x+200, y)
    hullRightEnd(x+250, y)

def battleshipHor(x, y):
    '''Horizontal Battleship Sprite'''
    t.penup()
    hullLeftEnd(x, y)
    hull(x+50, y)
    hull(x+100, y)
    hull(x+150, y)
    hullRightEnd(x+200, y)

def cruiserHor(x, y):
    '''Horizontal Cruiser Sprite'''
    t.penup()
    hullLeftEnd(x, y)
    hull(x+50, y)
    hull(x+100, y)
    hullRightEnd(x+150, y)

def submarineHor(x, y):
    '''Horizontal Submarine Sprite'''
    t.penup()
    hullLeftEnd(x, y)
    hull(x+50, y)
    hullRightEnd(x+100, y)

def destroyerHor(x, y):
    '''Horizontal Destroyer Sprite'''
    t.penup()
    hullLeftEnd(x,y)
    hullRightEnd(x+50, y)
    
    
    
def carrierVert(x, y):
    '''Vertical Carrier Sprite'''
    t.penup()
    hullTopEnd(x, y)
    hullVert(x, y-50)
    hullVert(x, y-100)
    hullVert(x, y-150)
    hullVert(x, y-200)
    hullBottomEnd(x, y-250)

def battleshipVert(x, y):
    '''Vertical Battleship Sprite'''
    t.penup()
    hullTopEnd(x, y)
    hullVert(x, y-50)
    hullVert(x, y-100)
    hullVert(x, y-150)
    hullBottomEnd(x, y-200)

def cruiserVert(x, y):
    '''Vertical Cruiser Sprite'''
    t.penup()
    hullTopEnd(x, y)
    hullVert(x, y-50)
    hullVert(x, y-100)
    hullBottomEnd(x, y-150)

def submarineVert(x, y):
    '''Vertical Submarine Sprite'''
    t.penup()
    hullTopEnd(x, y)
    hullVert(x, y-50)
    hullBottomEnd(x, y-100)

def destroyerVert(x, y):
    '''Vertical Destroyer Sprite'''
    t.penup()
    hullTopEnd(x,y)
    hullBottomEnd(x, y-50)
    
carrierCount = 1
battleshipCount = 1
cruiserCount = 1
submarineCount = 2
destroyerCount = 2

isHome = False
isInstructions = False
isPlayerOneAttackPage = False
isPlayerOneSelectionI = False
isPlayerOneSelectionII = False
isPlayerOneShipSelectionI = False
isPlayerOneShipsPlaced = False
isPlayerTwoAttackPage = False
isPlayerTwoSelectionI = False
isPlayerTwoSelectionII = False
isPlayerTwoShipSelectionI = False
isPlayerTwoShipSelectionII = False
isPlayerTwoShipsPlaced = False
isWinner = False









######################################################################










def winnerOnePage():
    '''Player One is the Winner'''
    global isWinner
    isWinner = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player One----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    t.setpos(0, -150)
    t.write("------You Won The Game------", move = False, align = "center", font = ("Copperplate Gothic Light", 40, "bold"))
    
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(10)
        t.color("#BD8205")
        t.setheading(0)
        t.fillcolor("#8F6B22")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()











#######################################################################












def winnerTwoPage():
    '''Player Two is the Winner'''
    global isWinner
    isWinner = True
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player Two----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    t.setpos(0, -150)
    t.write("------You Won The Game------", move = False, align = "center", font = ("Copperplate Gothic Light", 40, "bold"))
    
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(10)
        t.color("#991313")
        t.setheading(0)
        t.fillcolor("#D22C2C")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()










######################################################################











dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}


class Grid:
    def __init__(self, name):
        self.name = name
        self.board = [[' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      ['A', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['B', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['C', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['D', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['E', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['F', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['G', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['H', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['I', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                      ['J', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
        self.ships = []
        self.total_ship_count = 25

    def display(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()

    def add_ships(self, ship):
        self.ships.append(ship)

    def subtract_count(self):
        self.total_ship_count -= 1

    def ship_count(self):
        return self.total_ship_count


def validSpot(player, column, row):
    if column > 11 or column < 1 or row > 11 or row < 1 \
            or player.board[row][column] != '~' or player.board[row][column] == '0':
        return False
    return True


def validShot(column, row):
    if 12 > column > 0 and 12 > row > 0:
        return True
    return 1 / 0


def hit_ship(opp_player, grid1, column, row):
    if opp_player.board[row][column] == '0':
        if grid1.board[row][column] == '~':
            opp_player.subtract_count()
            return True
    return False


def winner_winner(player):
    if player.ship_count() == 0:
        if player == player1:
            winnerTwoPage()
        elif player == player2:
            winnerOnePage()
        return True
    return False


class ShipV:
    sunk = False
    def __init__(self, column, row, player, length):
        self.column = column
        self.row = row
        self.player = player
        self.length = length

        place = False
        for i in range(self.length):
            if not (validSpot(self.player, self.column, self.row + i)):
                place = False
                t.penup()
                t.setpos(25, -250)
                t.color("#F2422A")
                t.write("Invalid Placement", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
                t.color("#DBDBDB")
                t.penup()
                t.setpos(-725, 287)
                t.width(3)
                t.color("#072645")
                t.setheading(0)
                t.fillcolor("#072645")
                t.begin_fill()
                t.pendown()
                t.forward(25)
                t.right(90)
                t.forward(500)
                t.right(90)
                t.forward(25)
                t.right(90)
                t.forward(500)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                t.setpos(-675, -253)
                t.width(3)
                t.color("#072645")
                t.setheading(0)
                t.fillcolor("#072645")
                t.begin_fill()
                t.pendown()
                t.forward(600)
                t.right(90)
                t.forward(35)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.forward(35)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                break
            else:
                place = True
        if place:
            global coord
            global orrientation
            global ship_length
            global playerOneShipGrid
                        
            global carrierCount
            global battleshipCount
            global cruiserCount
            global submarineCount
            global destroyerCount

            
            if self.length == 6 and carrierCount > 0:
                carrierVert(-650 + 50*(self.column - 1), 300-50*(self.row))
                carrierCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row + j][self.column] = '0'
            elif self.length == 5 and battleshipCount > 0:
                battleshipVert(-650 + 50*(self.column - 1), 300-50*(self.row))
                battleshipCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row + j][self.column] = '0'
            elif self.length == 4 and cruiserCount > 0:
                cruiserVert(-650 + 50*(self.column - 1), 300-50*(self.row))
                cruiserCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row + j][self.column] = '0'
            elif self.length == 3 and submarineCount > 0:
                submarineVert(-650 + 50*(self.column - 1), 300-50*(self.row))
                submarineCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row + j][self.column] = '0'
            elif self.length == 2 and destroyerCount > 0:
                destroyerVert(-650 + 50*(self.column - 1), 300-50*(self.row))
                destroyerCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row + j][self.column] = '0'
            print("Confirm")
            
            t.penup()
            t.setpos(550, 250)
            t.width(3)
            t.color("#223343")
            t.setheading(0)
            t.fillcolor("#223343")
            t.begin_fill()
            t.pendown()
            t.forward(100)
            t.right(90)
            t.forward(550)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(550)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(575, 185)
            t.write(f"{carrierCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, 85)
            t.write(f"{battleshipCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -15)
            t.write(f"{cruiserCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -115)
            t.write(f"{submarineCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -215)
            t.write(f"{destroyerCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            
            t.penup()
            t.setpos(-675, -253)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(600)
            t.right(90)
            t.forward(35)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(35)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(-725, 287)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(25)
            t.right(90)
            t.forward(500)
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(500)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(215, 212)
            t.width(3)
            t.color("#223343")
            t.setheading(0)
            t.fillcolor("#223343")
            t.begin_fill()
            t.pendown()
            t.forward(25)
            t.right(90)
            t.forward(425)
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(425)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(250, -260)
            t.width(5)
            t.color("#111111")
            t.setheading(0)
            t.fillcolor("#2B2B2B")
            t.begin_fill()
            t.pendown()
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.right(90)
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            t.setpos(337, -310)
            t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
            
            t.penup()
            t.setpos(475, -260)
            t.width(5)
            t.color("#111111")
            t.setheading(0)
            t.fillcolor("#2B2B2B")
            t.begin_fill()
            t.pendown()
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.right(90)
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            t.setpos(562, -310)
            t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
            
            t.penup()
            t.setpos(-130, -230)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(300)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(300)
            t.right(90)
            t.forward(30)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            global checkConfirm
            checkConfirm = True
        else:
            a = 1 / 0


class ShipH:
    sunk = False
    position = []
    def __init__(self, column, row, player, length):
        self.column = column
        self.row = row
        self.player = player
        self.length = length
        place = False
        for i in range(self.length):
            if not (validSpot(self.player, self.column + i, self.row)):
                place = False
                t.penup()
                t.setpos(25, -250)
                t.color("#F2422A")
                t.write("Invalid Placement", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
                t.color("#DBDBDB")
                t.penup()
                t.setpos(-725, 287)
                t.width(3)
                t.color("#072645")
                t.setheading(0)
                t.fillcolor("#072645")
                t.begin_fill()
                t.pendown()
                t.forward(25)
                t.right(90)
                t.forward(500)
                t.right(90)
                t.forward(25)
                t.right(90)
                t.forward(500)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                t.setpos(-675, -253)
                t.width(3)
                t.color("#072645")
                t.setheading(0)
                t.fillcolor("#072645")
                t.begin_fill()
                t.pendown()
                t.forward(600)
                t.right(90)
                t.forward(35)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.forward(35)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                
                break
            else:
                place = True
        if place:
            global coord
            global orrientation
            global ship_length
            global playerOneShipGrid
            
            global carrierCount
            global battleshipCount
            global cruiserCount
            global submarineCount
            global destroyerCount
            if self.length == 6 and carrierCount > 0:
                carrierHor(-650 + 50*(self.column - 1), 300-50*(self.row - 1))
                carrierCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row][self.column + j] = '0'
            elif self.length == 5 and battleshipCount > 0:
                battleshipHor(-650 + 50*(self.column - 1), 300-50*(self.row - 1))
                battleshipCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row][self.column + j] = '0'
            elif self.length == 4 and cruiserCount > 0:
                cruiserHor(-650 + 50*(self.column - 1), 300-50*(self.row - 1))
                cruiserCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row][self.column + j] = '0'
            elif self.length == 3 and submarineCount > 0:
                submarineHor(-650 + 50*(self.column - 1), 300-50*(self.row - 1))
                submarineCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row][self.column + j] = '0'
            elif self.length == 2 and destroyerCount > 0:
                destroyerHor(-650 + 50*(self.column - 1), 300-50*(self.row - 1))
                destroyerCount -= 1
                if self.player == player1:
                    playerOneShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                else:
                    playerTwoShipGrid.append([coord[1], dic[coord[0]], orientation, ship_length])
                for j in range(self.length):
                    self.player.board[self.row][self.column + j] = '0'
            print("Confirm")
            
            t.penup()
            t.setpos(550, 250)
            t.width(3)
            t.color("#223343")
            t.setheading(0)
            t.fillcolor("#223343")
            t.begin_fill()
            t.pendown()
            t.forward(100)
            t.right(90)
            t.forward(550)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(550)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(575, 185)
            t.write(f"{carrierCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, 85)
            t.write(f"{battleshipCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -15)
            t.write(f"{cruiserCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -115)
            t.write(f"{submarineCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            t.setpos(575, -215)
            t.write(f"{destroyerCount} left", move = False, align = "left", font = ("Georgia", 22, "normal"))
            
            t.penup()
            t.setpos(-675, -253)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(600)
            t.right(90)
            t.forward(35)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(35)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(-725, 287)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(25)
            t.right(90)
            t.forward(500)
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(500)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(215, 212)
            t.width(3)
            t.color("#223343")
            t.setheading(0)
            t.fillcolor("#223343")
            t.begin_fill()
            t.pendown()
            t.forward(25)
            t.right(90)
            t.forward(425)
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(425)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            t.penup()
            t.setpos(250, -260)
            t.width(5)
            t.color("#111111")
            t.setheading(0)
            t.fillcolor("#2B2B2B")
            t.begin_fill()
            t.pendown()
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.right(90)
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            t.setpos(337, -310)
            t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
            
            t.penup()
            t.setpos(475, -260)
            t.width(5)
            t.color("#111111")
            t.setheading(0)
            t.fillcolor("#2B2B2B")
            t.begin_fill()
            t.pendown()
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.right(90)
            t.forward(175)
            t.right(90)
            t.forward(75)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            t.setpos(562, -310)
            t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
            
            t.penup()
            t.setpos(-130, -230)
            t.width(3)
            t.color("#072645")
            t.setheading(0)
            t.fillcolor("#072645")
            t.begin_fill()
            t.pendown()
            t.forward(300)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(300)
            t.right(90)
            t.forward(30)
            t.end_fill()
            t.width(0)
            t.color("#DBDBDB")
            t.penup()
            
            global checkConfirm
            checkConfirm = True
        else:
            a = 1 / 0


player1 = Grid('p1')
player2 = Grid('p2')











player1_shots = Grid('p1_shots')
player2_shots = Grid('p2_shots')
game_over = False
turns = 0

def playerOneShootI():
    global turns
    global game_over
    global coord
    global dic
    global player1
    global player1_shots
    global player2
    global player2_shots
    global playerOneShots
    global playerOneShotList
    try:
        if isPlayerOneAttackPage == True:
            shot = [coord[1], dic[coord[0]]]
            if validShot(shot[0], shot[1]):
                if hit_ship(player2, player1_shots, shot[0], shot[1]):
                    player2.board[shot[1]][shot[0]] = 'X'
                    print('\nThat was a hit!')
                    player1_shots.board[shot[1]][shot[0]] = 'X'
                    player1_shots.display()
                    print('Your Board\n')
                    player1.display()
                    game_over = winner_winner(player2)
                    playerOneShots.append([shot[0], shot[1], "H"])
                    playerOneShotList.append([coord[0], coord[1], "Hit"])
    
                else:
                    player1_shots.board[shot[1]][shot[0]] = 'O'
                    player1_shots.display()
                    print('You missed!\n')
                    player1.display()
                    playerOneShots.append([shot[0], shot[1], "M"])
                    playerOneShotList.append([coord[0], coord[1], "Miss"])
    except:
        playerOneAttackPageI()
        print("ERROR")
        
def playerTwoShootI():
    global turns
    global game_over
    global coord
    global dic
    global player1
    global player1_shots
    global player2
    global player2_shots
    global playerTwoShots
    global playerTwoShotList
    try:
        if isPlayerTwoAttackPage == True:
            shot = [coord[1], dic[coord[0]]]
            if validShot(shot[0], shot[1]):
                if hit_ship(player1, player2_shots, shot[0], shot[1]):
                    player1.board[shot[1]][shot[0]] = 'X'
                    print('\nThat was a hit!')
                    player2_shots.board[shot[1]][shot[0]] = 'X'
                    player2_shots.display()
                    print('Your Board\n')
                    player2.display()
                    game_over = winner_winner(player1)
                    playerTwoShots.append([shot[0], shot[1], "H"])
                    playerTwoShotList.append([coord[0], coord[1], "Hit"])
    
                else:
                    player2_shots.board[shot[1]][shot[0]] = 'O'
                    player2_shots.display()
                    print('You missed!\n')
                    player2.display()
                    playerTwoShots.append([shot[0], shot[1], "M"])
                    playerTwoShotList.append([coord[0], coord[1], "Miss"])
    except:
        playerTwoAttackPageI()
        print("ERROR")
    # try:
    #     if turns % 2 == 1:
    #         shot = input('Player 2 take a shot: ').split(' ')
    #         shot[0], shot[1] = int(dic[shot[0]]), int(shot[1])
    #         if validShot(shot[0], shot[1]):
    #             if hit_ship(player1, player2_shots, shot[0], shot[1]):
    #                 player1.board[shot[0]][shot[1]] = 'X'
    #                 print('\nThat was a hit!')
    #                 player2_shots.board[shot[0]][shot[1]] = 'X'
    #                 player2_shots.display()
    #                 print('Your Board\n')
    #                 player2.display()
    #                 game_over = winner_winner(player1)

    #             else:
    #                 player2_shots.board[shot[0]][shot[1]] = 'O'
    #                 player2_shots.display()
    #                 print('You missed!\n')
    #                 player2.display()

    # except:
    #     print('Invalid Shot, Try Again')
    #     turns -= 1
    turns += 1













#########################################################################









def instructions():
    '''General Instructions Page'''
    # Actual Instructions
    
    global isInstructions
    isInstructions = True
    global isHome
    isHome = False
    
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    tSize = 12
    t.setpos(0, 370)
    t.write("Battleship Instructions", move = False, align = "center", font = ("Georgia", 50, "bold"))
    t.setpos(0, 367)
    t.write("__________________________________", move = False, align = "center", font = ("Georgia", 50, "bold"))
    t.setpos(-700, 330)
    t.write("- Each player will be given a fleet of 5 different ships to place on the grid:", move = False, align = "left", font = ("Georgia", tSize, "underline"))
    t.setpos(-700, 300)
    t.write("          1 Carrier (Size of 6), 1 Battleships (Size of 5), 1 Cruiser (Size of 4)", move = False, align = "left", font = ("Georgia", 10, "italic"))
    t.setpos(-700, 270)
    t.write("          2 Submarines (Size of 3), and 2 Destroyers (Size of 2)", move = False, align = "left", font = ("Georgia", 10, "italic"))
    t.setpos(-700, 240)
    t.write("- Both players must secretly place each ship on the board without knowing the positions of the opponent's ships", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 210)
    t.write("- The ships must be placed in accordance with the Rules outlined below", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 180)
    t.write("        - Each player will be prompted to input a position, direction, and type when inputing their ship locations", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 150)
    t.write("        - Ships will be placed either vertically or horizontally", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 120)
    t.write("       - Do not place a ship so that any part of it is overlapping the edge of the board or another ship", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 90)
    t.write("               - If this occurs, you will need to fill in the information again", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 60)
    t.write("        - Position of ships cannot be changed after it has been input", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 30)
    t.write("- You and your opponent will alternate turns, calling one shot per turn to try to hit each other's ships", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, 0)
    t.write("- Calling your shot:", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -30)
    t.write("        - You will be propted to enter the 'coordinate' position of where you would like to shoot    Ex. D4", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -60)
    t.write("        - The program will then tell you whether or not you hit a ship once it's your turn again", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -90)
    t.write("                - A Red peg indicates a hit, and a White peg indicates a miss", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -120)
    t.write("        - After a hit or miss, your turn is over, and play will then transition to Player 2", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -150)
    t.write("- The total amount of 'ship pegs' left to hit in order to win will be displayed below the player name", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    t.setpos(-700, -180)
    t.write("- If you are the first player to sink all of your opponent's ships, you will win the game", move = False, align = "left", font = ("Georgia", tSize, "normal"))
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Battleship Sprite
    
    boatSprite(-550, -285)
    
    # Ship Chart
    
    t.penup()
    t.fillcolor("#223343")
    t.begin_fill()
    t.setpos(200, 330)
    t.pendown()
    t.setheading(0)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.penup()
    t.end_fill()
    t.setpos(450, 290)
    t.setheading(0)
    t.write("Ship Classes", move = False, align = "center", font = ("Georgia", 25, "normal"))
    t.setpos(450, 285)
    t.write("________________", move = False, align = "center", font = ("Georgia", 25, "normal"))
    
    
    def carrierEx():
        t.penup()
        t.setpos(250, 228)
        t.write("--- Carrier ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 225)
        hull(300, 225)
        hull(350, 225)
        hull(400, 225)
        hull(450, 225)
        hullRightEnd(500, 225)
    
    def battleshipEx():
        t.penup()
        t.setpos(250, 128)
        t.write("--- Battleship ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 125)
        hull(300, 125)
        hull(350, 125)
        hull(400, 125)
        hullRightEnd(450, 125)
    
    def cruiserEx():
        t.penup()
        t.setpos(250, 28)
        t.write("--- Cruiser ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 25)
        hull(300, 25)
        hull(350, 25)
        hullRightEnd(400, 25)
    
    def submarineEx():
        t.penup()
        t.setpos(250, -72)
        t.write("--- Submarine ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-75)
        hull(300, -75)
        hullRightEnd(350, -75)
    
    def destroyerEx():
        t.penup()
        t.setpos(250, -172)
        t.write("--- Destroyer ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-175)
        hullRightEnd(300, -175)
    
    def shipList():
        carrierEx()
        battleshipEx()
        cruiserEx()
        submarineEx()
        destroyerEx()
    
    shipList()
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
        
    
    # Back Button Graphic
    
    t.penup()
    t.setpos(450, -280)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(350)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(150)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(625, -380)
    t.write("Back Home", move = False, align = "center", font = ("Copperplate Gothic Light", 35, "bold"))






#####################################################################










def playerOneSelectionI():
    '''Intermediate Page between Home and Ship selection for Player One'''
    
    global isHome
    isHome = False
    global isPlayerOneSelectionI
    isPlayerOneSelectionI = True
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player One----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    t.setpos(0, -140)
    t.write("---Continue To Place Your Ships---", move = False, align = "center", font = ("Copperplate Gothic Light", 30, "bold"))
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#083563")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()



    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    









#####################################################################













def homeScreen():
    '''Home Page / Starting Screen'''
    
    global isInstructions
    isInstructions = False
    global isHome
    isHome = True
    global isPlayerOneSelectionI
    isPlayerOneSelectionI = False
    global isPlayerOneShipSelectionI
    isPlayerOneShipSelectionI = False
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Title
    
    t.penup()
    t.setpos(0, 175)
    t.write("Battleship", move = False, align = "center", font = ("Copperplate Gothic Light", 150, "bold"))
    t.setpos(0, 170)
    t.write("__________________", move = False, align = "center", font = ("Copperplate Gothic Light", 100, "bold"))
    t.setpos(0, 110)
    t.write("The Naval Combat Game", move = False, align = "center", font = ("Copperplate Gothic Light", 40, "normal"))
    t.setpos(0, -430)
    t.write("Created for ENGR 102 by Griffin Ainsworth, Timothy Tsai, Anson Thai, Ryan Santry, and Landon Praytor", move = False, align = "center", font = ("Copperplate Gothic Light", 10, "normal"))
    
    # Boat Sprites
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    # Button Graphics
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#083563")
        t.begin_fill()
        t.pendown()
        t.forward(400)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(400)
        t.right(90)
        t.forward(200)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-500, 50)
    buttonSprite(100, 50)
    t.setpos(-300, -75)
    t.write("Play Game", move = False, align = "center", font = ("Copperplate Gothic Light", 35, "bold"))
    t.setpos(300, -75)
    t.write("Instructions", move = False, align = "center", font = ("Copperplate Gothic Light", 35, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    
    
    
    
    
    
    
    
    
    

################################################################################











def playerOneShipSelectionI():
    '''Ship selection for Player One'''
    
    global isPlayerOneSelectionI
    isPlayerOneSelectionI = False
    global isPlayerOneShipSelectionI
    isPlayerOneShipSelectionI = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 350)
    t.write("----------Player One----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 360)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Ship List
    
    t.penup()
    t.fillcolor("#223343")
    t.begin_fill()
    t.setpos(200, 330)
    t.pendown()
    t.setheading(0)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.penup()
    t.end_fill()
    t.setpos(450, 290)
    t.setheading(0)
    t.write("Ship Classes", move = False, align = "center", font = ("Georgia", 25, "normal"))
    t.setpos(450, 285)
    t.write("________________", move = False, align = "center", font = ("Georgia", 25, "normal"))
    
    
    def carrierEx():
        t.penup()
        t.setpos(250, 228)
        t.write("--- Carrier ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 225)
        hull(300, 225)
        hull(350, 225)
        hull(400, 225)
        hull(450, 225)
        hullRightEnd(500, 225)
        t.penup()
        t.setpos(575, 185)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def battleshipEx():
        t.penup()
        t.setpos(250, 128)
        t.write("--- Battleship ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 125)
        hull(300, 125)
        hull(350, 125)
        hull(400, 125)
        hullRightEnd(450, 125)
        t.penup()
        t.setpos(575, 85)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def cruiserEx():
        t.penup()
        t.setpos(250, 28)
        t.write("--- Cruiser ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 25)
        hull(300, 25)
        hull(350, 25)
        hullRightEnd(400, 25)
        t.penup()
        t.setpos(575, -15)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def submarineEx():
        t.penup()
        t.setpos(250, -72)
        t.write("--- Submarine ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-75)
        hull(300, -75)
        hullRightEnd(350, -75)
        t.penup()
        t.setpos(575, -115)
        t.write("2 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def destroyerEx():
        t.penup()
        t.setpos(250, -172)
        t.write("--- Destroyer ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-175)
        hullRightEnd(300, -175)
        t.penup()
        t.setpos(575, -215)
        t.write("2 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def shipList():
        carrierEx()
        battleshipEx()
        cruiserEx()
        submarineEx()
        destroyerEx()
    
    shipList()
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    # Boat Sprites
    
    boatSprite(-450, -365)
    
    # Ship Board
    
    def playerOneShipBoardI():
        
        t.width(3)
        t.penup()
        t.setpos(-650, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(-675 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(-675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(-625 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
    playerOneShipBoardI()
    
    # Additional Button Sprites
    
    t.penup()
    t.setpos(250, -260)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(337, -310)
    t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
    
    t.penup()
    t.setpos(475, -260)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(562, -310)
    t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
    
    t.penup()
    t.setpos(-68, -140)
    t.width(5)
    t.color("#898989")
    t.setheading(0)
    t.fillcolor("#595959")
    t.begin_fill()
    t.pendown()
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(19, -194)
    t.write("Confirm", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
    
    
    # Additional Instructions
    
    t.penup()
    t.setpos(25, 250)
    t.write("Instructions", move = False, align = "center", font = ("Georgia", 18, "bold"))
    t.setpos(25, 245)
    t.write("________________", move = False, align = "center", font = ("Georgia", 16, "normal"))
    t.setpos(25, 225)
    t.write("- Select a ship by clicking on", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 205)
    t.write("the respective ship model", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 175)
    t.write("- Select either Vertical or Horizontal", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 145)
    t.write("- Select coordinates for your ship by", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 125)
    t.write("clicking on the respective number or", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 105)
    t.write("letter in its respective column or row", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 75)
    t.write("- Click 'Confirm' to confirm your selection", move = False, align = "center", font = ("Georgia", 13, "normal"))
    
    t.setpos(25, 20)
    t.write("'Vertical' will place your ship starting at your", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, 0)
    t.write("marked coordinates, and place the rest of the ship", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -20)
    t.write("moving downwards, towards row J", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -50)
    t.write("'Horizontal' will place your ship starting at your", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -70)
    t.write("marked coordinates, and place the rest of the ship", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -90)
    t.write("moving rightwards, towards column 10", move = False, align = "center", font = ("Georgia", 10, "italic"))
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 360)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    
    t.penup()
    t.setpos(650, 425)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(738, 372)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))













##############################################################################












def playerOneSelectionII():
    '''Intermediate Page between Player Two and attack selection for Player One'''
    
    global isPlayerTwoShipSelectionI
    isPlayerTwoShipSelectionI = False
    global isPlayerTwoAttackPage
    isPlayerTwoAttackPage = False
    global isPlayerOneSelectionII
    isPlayerOneSelectionII = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player One----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#083563")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    










#####################################################################













def playerTwoSelectionI():
    '''Intermediate Page between Ship selection for Player One and Ship selection for Player Two'''
    
    global isPlayerOneShipSelectionI
    isPlayerOneShipSelectionI = False
    global isPlayerTwoSelectionI
    isPlayerTwoSelectionI = True
    
    global carrierCount
    global battleshipCount
    global cruiserCount
    global submarineCount
    global destroyerCount
    
    carrierCount = 1
    battleshipCount = 1
    cruiserCount = 1
    submarineCount = 2
    destroyerCount = 2
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player Two----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    t.setpos(0, -140)
    t.write("---Continue To Place Your Ships---", move = False, align = "center", font = ("Copperplate Gothic Light", 30, "bold"))
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#083563")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    












#####################################################################













def playerTwoSelectionII():
    '''Intermediate Page between Player One and Attack selection for Player Two'''
    
    global isPlayerOneAttackPage
    isPlayerOneAttackPage = False
    global isPlayerTwoSelectionII
    isPlayerTwoSelectionII = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 280)
    t.write("----------Player Two----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    boatSprite(-550, -285)
    boatSprite(200, -330)
    
    def buttonSprite(x, y):
        t.penup()
        t.setpos(x, y)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#083563")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(250)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
    
    buttonSprite(-250, 210)
    t.setpos(0, 50)
    t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 55, "bold"))
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 340)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 300)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 380)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()











#####################################################################













def playerTwoShipSelectionI():
    '''Ship selection for Player Two'''
    
    global isPlayerTwoSelectionI
    isPlayerTwoSelectionI = False
    global isPlayerTwoShipSelectionI
    isPlayerTwoShipSelectionI = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 350)
    t.write("----------Player Two----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 360)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Ship List
    
    t.penup()
    t.fillcolor("#223343")
    t.begin_fill()
    t.setpos(200, 330)
    t.pendown()
    t.setheading(0)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(700)
    t.penup()
    t.end_fill()
    t.setpos(450, 290)
    t.setheading(0)
    t.write("Ship Classes", move = False, align = "center", font = ("Georgia", 25, "normal"))
    t.setpos(450, 285)
    t.write("________________", move = False, align = "center", font = ("Georgia", 25, "normal"))
    
    
    def carrierEx():
        t.penup()
        t.setpos(250, 228)
        t.write("--- Carrier ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 225)
        hull(300, 225)
        hull(350, 225)
        hull(400, 225)
        hull(450, 225)
        hullRightEnd(500, 225)
        t.penup()
        t.setpos(575, 185)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def battleshipEx():
        t.penup()
        t.setpos(250, 128)
        t.write("--- Battleship ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 125)
        hull(300, 125)
        hull(350, 125)
        hull(400, 125)
        hullRightEnd(450, 125)
        t.penup()
        t.setpos(575, 85)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def cruiserEx():
        t.penup()
        t.setpos(250, 28)
        t.write("--- Cruiser ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250, 25)
        hull(300, 25)
        hull(350, 25)
        hullRightEnd(400, 25)
        t.penup()
        t.setpos(575, -15)
        t.write("1 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def submarineEx():
        t.penup()
        t.setpos(250, -72)
        t.write("--- Submarine ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-75)
        hull(300, -75)
        hullRightEnd(350, -75)
        t.penup()
        t.setpos(575, -115)
        t.write("2 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def destroyerEx():
        t.penup()
        t.setpos(250, -172)
        t.write("--- Destroyer ---", move = False, align = "left", font = ("Georgia", 18, "normal"))
        hullLeftEnd(250,-175)
        hullRightEnd(300, -175)
        t.penup()
        t.setpos(575, -215)
        t.write("2 left", move = False, align = "left", font = ("Georgia", 22, "normal"))
    
    def shipList():
        carrierEx()
        battleshipEx()
        cruiserEx()
        submarineEx()
        destroyerEx()
    
    shipList()
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    # Boat Sprites
    
    boatSprite(-450, -365)
    
    # Ship Board
    
    def playerOneShipBoardI():
        
        t.width(3)
        t.penup()
        t.setpos(-650, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(-675 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(-675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(-625 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
    playerOneShipBoardI()
    
    # Additional Button Sprites
    
    t.penup()
    t.setpos(250, -260)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(337, -310)
    t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
    
    t.penup()
    t.setpos(475, -260)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(562, -310)
    t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
    
    t.penup()
    t.setpos(-68, -140)
    t.width(5)
    t.color("#898989")
    t.setheading(0)
    t.fillcolor("#595959")
    t.begin_fill()
    t.pendown()
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(19, -194)
    t.write("Confirm", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
    
    
    # Additional Instructions
    
    t.penup()
    t.setpos(25, 250)
    t.write("Instructions", move = False, align = "center", font = ("Georgia", 18, "bold"))
    t.setpos(25, 245)
    t.write("________________", move = False, align = "center", font = ("Georgia", 16, "normal"))
    t.setpos(25, 225)
    t.write("- Select a ship by clicking on", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 205)
    t.write("the respective ship model", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 175)
    t.write("- Select either Vertical or Horizontal", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 145)
    t.write("- Select coordinates for your ship by", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 125)
    t.write("clicking on the respective number or", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 105)
    t.write("letter in its respective column or row", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(25, 75)
    t.write("- Click 'Confirm' to confirm your selection", move = False, align = "center", font = ("Georgia", 13, "normal"))
    
    t.setpos(25, 20)
    t.write("'Vertical' will place your ship starting at your", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, 0)
    t.write("marked coordinates, and place the rest of the ship", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -20)
    t.write("moving downwards, towards row J", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -50)
    t.write("'Horizontal' will place your ship starting at your", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -70)
    t.write("marked coordinates, and place the rest of the ship", move = False, align = "center", font = ("Georgia", 10, "italic"))
    t.setpos(25, -90)
    t.write("moving rightwards, towards column 10", move = False, align = "center", font = ("Georgia", 10, "italic"))
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 360)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()

    
    
    t.penup()
    t.setpos(650, 425)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(738, 372)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
    
    













##############################################################################















def playerOneAttackPageI():
    '''Attack Page for Player One'''
    
    global isPlayerOneSelectionII
    isPlayerOneSelectionII = False
    global isPlayerOneAttackPage
    isPlayerOneAttackPage = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 350)
    t.write("----------Player One----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    # Boat Sprites
    
    boatSprite(-450, -365)
    
    
    
    # Ship Board
    
    def playerOneAttackBoardI():
        
        t.width(3)
        t.penup()
        t.setpos(-650, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(-675 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(-675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(-625 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
    playerOneAttackBoardI()
    
    def playerOneShipBoardII():
        
        t.width(3)
        t.penup()
        t.setpos(150, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(125 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(175 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
                
        #playerOneShipGrid

        
        for i in range(len(playerOneShipGrid)):
            
            if playerOneShipGrid[i][2] == "h":
                if playerOneShipGrid[i][3] == 6:
                    carrierHor(150 + 50*(playerOneShipGrid[i][0] - 1), 300-50*(playerOneShipGrid[i][1] - 1))
                    
                elif playerOneShipGrid[i][3] == 5:
                    battleshipHor(150 + 50*(playerOneShipGrid[i][0] - 1), 300-50*(playerOneShipGrid[i][1] - 1))
                    
                elif playerOneShipGrid[i][3] == 4:
                    cruiserHor(150 + 50*(playerOneShipGrid[i][0] - 1), 300-50*(playerOneShipGrid[i][1] - 1))
                    
                elif playerOneShipGrid[i][3] == 3:
                    submarineHor(150 + 50*(playerOneShipGrid[i][0] - 1), 300-50*(playerOneShipGrid[i][1] - 1))
                    
                elif playerOneShipGrid[i][3] == 2:
                    destroyerHor(150 + 50*(playerOneShipGrid[i][0] - 1), 300-50*(playerOneShipGrid[i][1] - 1))
            else:
                if playerOneShipGrid[i][2]:
                    if playerOneShipGrid[i][3] == 6:
                        carrierVert(150 + 50*(playerOneShipGrid[i][0] - 1), 250-50*(playerOneShipGrid[i][1] - 1))
                        
                    elif playerOneShipGrid[i][3] == 5:
                        battleshipVert(150 + 50*(playerOneShipGrid[i][0] - 1), 250-50*(playerOneShipGrid[i][1] - 1))
                        
                    elif playerOneShipGrid[i][3] == 4:
                        cruiserVert(150 + 50*(playerOneShipGrid[i][0] - 1), 250-50*(playerOneShipGrid[i][1] - 1))
                        
                    elif playerOneShipGrid[i][3] == 3:
                        submarineVert(150 + 50*(playerOneShipGrid[i][0] - 1), 250-50*(playerOneShipGrid[i][1] - 1))
                        
                    elif playerOneShipGrid[i][3] == 2:
                        destroyerVert(150 + 50*(playerOneShipGrid[i][0] - 1), 250-50*(playerOneShipGrid[i][1] - 1))
                        
        global playerOneShots
        global playerTwoShots
                        
        for i in range(len(playerTwoShots)):
            if playerTwoShots[i][2] == "H":
                t.penup()
                t.setpos(100 + 50*(playerTwoShots[i][0]) + 25, 300 - 50*(playerTwoShots[i][1]) + 25)
                t.dot(15, "#CE2F21")
            elif playerTwoShots[i][2] == "M":
                t.penup()
                t.setpos(100 + 50*(playerTwoShots[i][0]) + 25, 300 - 50*(playerTwoShots[i][1]) + 25)
                t.dot(15, "#EFEFEF")
                
        playerOneHits = 0
        for i in range(len(playerOneShots)):
            if playerOneShots[i][2] == "H":
                t.penup()
                t.setpos(-700 + 50*(playerOneShots[i][0]) + 25, 300 - 50*(playerOneShots[i][1]) + 25)
                t.dot(15, "#CE2F21")
                playerOneHits += 1
            elif playerOneShots[i][2] == "M":
                t.penup()
                t.setpos(-700 + 50*(playerOneShots[i][0]) + 25, 300 - 50*(playerOneShots[i][1]) + 25)
                t.dot(15, "#EFEFEF")
                
        playerOneHitsRemaining = 25 - playerOneHits
        t.penup()
        t.setpos(0, 300)
        t.color("#BD8205")
        t.write(f"{playerOneHitsRemaining} / 25 left", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
        t.color("#DBDBDB")
                
                
    playerOneShipBoardII()
    
    t.penup()
    t.setpos(-88, -140)
    t.width(5)
    t.color("#898989")
    t.setheading(0)
    t.fillcolor("#595959")
    t.begin_fill()
    t.pendown()
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(0, -194)
    t.write("Confirm", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))


    t.penup()
    t.setpos(0, 250)
    t.write("Instructions", move = False, align = "center", font = ("Georgia", 18, "bold"))
    t.setpos(0, 245)
    t.write("________________", move = False, align = "center", font = ("Georgia", 16, "normal"))
    t.setpos(0, 225)
    t.write("- Select a point to shoot at", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 205)
    t.write("by selecting the corresponding", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 185)
    t.write("letter and number on the left", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 165)
    t.write("board (without your ships)", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 135)
    t.write("- Then finish your turn by", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 115)
    t.write("clicking continue to shoot", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 75)
    t.write("- The right board shows your ships", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 55)
    t.write("and your opponents shots", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 25)
    t.write("- The left board shows your shots", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 5)
    t.write("at your opponents ships", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, -25)
    t.write("- Red dots denote a hit", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, -55)
    t.write("- White dots denote a miss", move = False, align = "center", font = ("Georgia", 13, "normal"))
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 360)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.fillcolor("#303030")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 360)
    t.setheading(0)
    t.fillcolor("#E2C800")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.width(8)
    t.color("#BD8205")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(650, 425)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(738, 372)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))














################################################################################












def playerTwoAttackPageI():
    '''Attack Page for Player Two'''
    
    global isPlayerTwoSelectionII
    isPlayerTwoSelectionII = False
    global isPlayerTwoAttackPage
    isPlayerTwoAttackPage = True
    
    t.delay(0)
    t.clear()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.Screen().bgcolor("#072645")
    t.color("#DBDBDB")
    t.setpos(0, 350)
    t.write("----------Player Two----------", move = False, align = "center", font = ("Copperplate Gothic Light", 50, "bold"))
    
    # Water Feature
    
    t.penup()
    t.setpos(-1000, -300)
    t.fillcolor("#135A7F")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.setpos(1000, -600)
    t.setheading(180)
    t.pendown()
    t.forward(2000)
    t.penup()
    t.end_fill()
    for i in range(-60,60):
        t.goto(-50 - i*4,-330 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-80,95):
        t.goto(-500 - i*3.5,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    for i in range(-70,100):
        t.goto(450 - i*4.25,-390 - 15*m.sin((i/100)*2*m.pi))
        t.pendown()
    t.penup()
    
    # Oversize Border
    
    t.color("#111111")
    t.penup()
    t.setpos(-1900, -500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    
    t.penup()
    
    t.setpos(1900, 500)
    t.fillcolor("#111111")
    t.begin_fill()
    t.setheading(180)
    t.pendown()
    t.forward(2800)
    t.left(90)
    t.forward(1500)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(4000)
    t.right(90)
    t.forward(90)
    t.end_fill()
    t.color("#DBDBDB")
    t.penup()
    
    # Boat Sprites
    
    boatSprite(-450, -365)
    
    
    
    # Ship Board
    
    def playerTwoAttackBoardI():
        
        t.width(3)
        t.penup()
        t.setpos(-650, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(-675 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(-675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(-625 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
    playerTwoAttackBoardI()
    
    def playerTwoShipBoardII():
        
        t.width(3)
        t.penup()
        t.setpos(150, 300)
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(1)
        for i in range(4):
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(500)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        for i in range(4):
            t.left(90)
            t.forward(500)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500)
            t.left(90)
            t.forward(50)
        t.left(90)
        t.forward(500)
        t.width(0)
        t.penup()
        
        
        xAxis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for i in xAxis:
            t.penup()
            t.setpos(125 + 50*(int(i)), -250)
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
        
        yAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        count = 0
        for i in yAxis:
            t.penup()
            t.setpos(675, 250 - 50*(count))
            t.write(i, move = False, align = "center", font = ("Copperplate Gothic Light", 30, "normal"))
            count += 1
        
        for i in range(10):
            for j in range(10):
                t.penup()
                t.setpos(175 + 50*j, 275 - 50*(i))
                t.pendown()
                t.dot(10, "#666666")
                t.penup()
                
        #playerTwoShipGrid

        
        for i in range(len(playerTwoShipGrid)):
            
            if playerTwoShipGrid[i][2] == "h":
                if playerTwoShipGrid[i][3] == 6:
                    carrierHor(150 + 50*(playerTwoShipGrid[i][0] - 1), 300-50*(playerTwoShipGrid[i][1] - 1))
                    
                elif playerTwoShipGrid[i][3] == 5:
                    battleshipHor(150 + 50*(playerTwoShipGrid[i][0] - 1), 300-50*(playerTwoShipGrid[i][1] - 1))
                    
                elif playerTwoShipGrid[i][3] == 4:
                    cruiserHor(150 + 50*(playerTwoShipGrid[i][0] - 1), 300-50*(playerTwoShipGrid[i][1] - 1))
                    
                elif playerTwoShipGrid[i][3] == 3:
                    submarineHor(150 + 50*(playerTwoShipGrid[i][0] - 1), 300-50*(playerTwoShipGrid[i][1] - 1))
                    
                elif playerTwoShipGrid[i][3] == 2:
                    destroyerHor(150 + 50*(playerTwoShipGrid[i][0] - 1), 300-50*(playerTwoShipGrid[i][1] - 1))
            else:
                if playerTwoShipGrid[i][2]:
                    if playerTwoShipGrid[i][3] == 6:
                        carrierVert(150 + 50*(playerTwoShipGrid[i][0] - 1), 250-50*(playerTwoShipGrid[i][1] - 1))
                        
                    elif playerTwoShipGrid[i][3] == 5:
                        battleshipVert(150 + 50*(playerTwoShipGrid[i][0] - 1), 250-50*(playerTwoShipGrid[i][1] - 1))
                        
                    elif playerTwoShipGrid[i][3] == 4:
                        cruiserVert(150 + 50*(playerTwoShipGrid[i][0] - 1), 250-50*(playerTwoShipGrid[i][1] - 1))
                        
                    elif playerTwoShipGrid[i][3] == 3:
                        submarineVert(150 + 50*(playerTwoShipGrid[i][0] - 1), 250-50*(playerTwoShipGrid[i][1] - 1))
                        
                    elif playerTwoShipGrid[i][3] == 2:
                        destroyerVert(150 + 50*(playerTwoShipGrid[i][0] - 1), 250-50*(playerTwoShipGrid[i][1] - 1))
                        
                        
        global playerOneShots
        global playerTwoShots
                        
        for i in range(len(playerOneShots)):
            if playerOneShots[i][2] == "H":
                t.penup()
                t.setpos(100 + 50*(playerOneShots[i][0]) + 25, 300 - 50*(playerOneShots[i][1]) + 25)
                t.dot(15, "#CE2F21")
            elif playerOneShots[i][2] == "M":
                t.penup()
                t.setpos(100 + 50*(playerOneShots[i][0]) + 25, 300 - 50*(playerOneShots[i][1]) + 25)
                t.dot(15, "#EFEFEF")
                
        playerTwoHits = 0
        for i in range(len(playerTwoShots)):
            if playerTwoShots[i][2] == "H":
                t.penup()
                t.setpos(-700 + 50*(playerTwoShots[i][0]) + 25, 300 - 50*(playerTwoShots[i][1]) + 25)
                t.dot(15, "#CE2F21")
                playerTwoHits += 1
            elif playerTwoShots[i][2] == "M":
                t.penup()
                t.setpos(-700 + 50*(playerTwoShots[i][0]) + 25, 300 - 50*(playerTwoShots[i][1]) + 25)
                t.dot(15, "#EFEFEF")
                        
        
        playerTwoHitsRemaining = 25 - playerTwoHits
        t.penup()
        t.setpos(0, 300)
        t.color("#991313")
        t.write(f"{playerTwoHitsRemaining} / 25 left", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
        t.color("#DBDBDB")
                
                
                
    playerTwoShipBoardII()
    
    t.penup()
    t.setpos(-88, -140)
    t.width(5)
    t.color("#898989")
    t.setheading(0)
    t.fillcolor("#595959")
    t.begin_fill()
    t.pendown()
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(176)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(0, -194)
    t.write("Confirm", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
    
    t.penup()
    t.setpos(0, 250)
    t.write("Instructions", move = False, align = "center", font = ("Georgia", 18, "bold"))
    t.setpos(0, 245)
    t.write("________________", move = False, align = "center", font = ("Georgia", 16, "normal"))
    t.setpos(0, 225)
    t.write("- Select a point to shoot at", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 205)
    t.write("by selecting the corresponding", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 185)
    t.write("letter and number on the left", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 165)
    t.write("board (without your ships)", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 135)
    t.write("- Then finish your turn by", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 115)
    t.write("clicking continue to shoot", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 75)
    t.write("- The right board shows your ships", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 55)
    t.write("and your opponents shots", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 25)
    t.write("- The left board shows your shots", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, 5)
    t.write("at your opponents ships", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, -25)
    t.write("- Red dots denote a hit", move = False, align = "center", font = ("Georgia", 13, "normal"))
    t.setpos(0, -55)
    t.write("- White dots denote a miss", move = False, align = "center", font = ("Georgia", 13, "normal"))
    
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 360)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(-625, 360)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(-625, 440)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.fillcolor("#FF6700")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 400)
    t.setheading(0)
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    t.penup()
    t.setpos(375, 360)
    t.setheading(0)
    t.fillcolor("#000000")
    t.begin_fill()
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    
    t.penup()
    t.setpos(375, 440)
    t.setheading(0)
    t.width(8)
    t.color("#991313")
    t.pendown()
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(120)
    t.color("#DBDBDB")
    t.width(0)
    t.penup()
    
    
    t.penup()
    t.setpos(650, 425)
    t.width(5)
    t.color("#111111")
    t.setheading(0)
    t.fillcolor("#2B2B2B")
    t.begin_fill()
    t.pendown()
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.width(0)
    t.color("#DBDBDB")
    t.penup()
    t.setpos(738, 372)
    t.write("Exit Game", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))















################################################################################













numCord = False
letCord = False
isPlayerOneShipsPlaced = False
isPlayerTwoShipsPlaced = False
coord = ["", ""]


# Button Functionality
    
def insButton(x,y):
    if x < 500 and x > 100 and y < 50 and y > -150 and isHome == True:
        instructions()
t.onscreenclick(insButton, 1, add=False)
    

def backButton(x,y):
    if x < 800 and x > 450 and y < -280 and y > -420 and isInstructions == True:
        homeScreen()
t.onscreenclick(backButton, 1, add=True)


def playerOneSelectionButtonI(x,y):
    if x < 250 and x > -250 and y < 210 and y > -40 and isPlayerOneSelectionI == True:
        playerOneShipSelectionI()
t.onscreenclick(playerOneSelectionButtonI, 1, add=True)


def playButton(x,y):
    if x < -100 and x > -500 and y < 50 and y > -150 and isHome == True:
        playerOneSelectionI()
t.onscreenclick(playButton, 1, add=True)


isShipClass = False

def playerOneShipButtonCarrier(x,y):
    if x < 550 and x > 250 and y < 225 and y > 175 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Carrier")
        global isShipClass
        isShipClass = True
        global ship_length
        ship_length = 6
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#223343")
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonCarrier, 1, add=True)


def playerOneShipButtonBattleship(x,y):
    if x < 500 and x > 250 and y < 125 and y > 75 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Battleship")
        global isShipClass
        isShipClass = True
        global ship_length
        ship_length = 5
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#223343")
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(215, 112)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonBattleship, 1, add=True)


def playerOneShipButtonCruiser(x,y):
    if x < 450 and x > 250 and y < 25 and y > -25 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Cruiser")
        global isShipClass
        isShipClass = True
        global ship_length
        ship_length = 4
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#223343")
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(215, 12)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonCruiser, 1, add=True)


def playerOneShipButtonSubmarine(x,y):
    if x < 400 and x > 250 and y < -75 and y > -125 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Submarine")
        global isShipClass
        isShipClass = True
        global ship_length
        ship_length = 3
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#223343")
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(215, -88)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonSubmarine, 1, add=True)


def playerOneShipButtonDestroyer(x,y):
    if x < 350 and x > 250 and y < -175 and y > -225 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Destroyer")
        global isShipClass
        isShipClass = True
        global ship_length
        ship_length = 2
        
        t.penup()
        t.setpos(215, 212)
        t.width(3)
        t.color("#223343")
        t.setheading(0)
        t.fillcolor("#223343")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(425)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(215, -188)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonDestroyer, 1, add=True)


def playerOneShipButtonVertical(x,y):
    if x < 425 and x > 250 and y < -260 and y > -335 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Vertical")
        global isHor
        isHor = False
        global isVert
        isVert = True
        global orientation
        orientation = "v"
        
        t.penup()
        t.setpos(250, -260)
        t.width(5)
        t.color("#898989")
        t.setheading(0)
        t.fillcolor("#595959")
        t.begin_fill()
        t.pendown()
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.right(90)
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        t.setpos(337, -310)
        t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
        
        t.penup()
        t.setpos(475, -260)
        t.width(5)
        t.color("#111111")
        t.setheading(0)
        t.fillcolor("#2B2B2B")
        t.begin_fill()
        t.pendown()
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.right(90)
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        t.setpos(562, -310)
        t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
t.onscreenclick(playerOneShipButtonVertical, 1, add=True)

def playerOneShipButtonHorizontal(x,y):
    if x < 650 and x > 475 and y < -260 and y > -335 and (isPlayerOneShipSelectionI == True or isPlayerTwoShipSelectionI == True):
        print("Horizontal")
        global isHor
        isHor = True
        global isVert
        isVert = False
        global orientation
        orientation = "h"
        
        t.penup()
        t.setpos(250, -260)
        t.width(5)
        t.color("#111111") 
        t.setheading(0)
        t.fillcolor("#2B2B2B")
        t.begin_fill()
        t.pendown()
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.right(90)
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        t.setpos(337, -310)
        t.write("Vertical", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
        
        t.penup()
        t.setpos(475, -260)
        t.width(5)
        t.color("#898989")
        t.setheading(0)
        t.fillcolor("#595959")
        t.begin_fill()
        t.pendown()
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.right(90)
        t.forward(175)
        t.right(90)
        t.forward(75)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        t.setpos(562, -310)
        t.write("Horizontal", move = False, align = "center", font = ("Copperplate Gothic Light", 18, "bold"))
t.onscreenclick(playerOneShipButtonHorizontal, 1, add=True)



# Number and Letter Buttons



def playerOneShipButtonA(x,y):
    if x < -650 and x > -700 and y < 300 and y > 250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("A")
        global letCord
        letCord = True
        global coord
        coord[0] = "A"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonA, 1, add=True)


def playerOneShipButtonB(x,y):
    if x < -650 and x > -700 and y < 250 and y > 200 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("B")
        global letCord
        letCord = True
        global coord
        coord[0] = "B"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 237)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonB, 1, add=True)


def playerOneShipButtonC(x,y):
    if x < -650 and x > -700 and y < 200 and y > 150 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("C")
        global letCord
        letCord = True
        global coord
        coord[0] = "C"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 187)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonC, 1, add=True)


def playerOneShipButtonD(x,y):
    if x < -650 and x > -700 and y < 150 and y > 100 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("D")
        global letCord
        letCord = True
        global coord
        coord[0] = "D"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 137)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonD, 1, add=True)


def playerOneShipButtonE(x,y):
    if x < -650 and x > -700 and y < 100 and y > 50 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("E")
        global letCord
        letCord = True
        global coord
        coord[0] = "E"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 87)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonE, 1, add=True)


def playerOneShipButtonF(x,y):
    if x < -650 and x > -700 and y < 50 and y > 0 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("F")
        global letCord
        letCord = True
        global coord
        coord[0] = "F"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, 37)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonF, 1, add=True)


def playerOneShipButtonG(x,y):
    if x < -650 and x > -700 and y < 0 and y > -50 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("G")
        global letCord
        letCord = True
        global coord
        coord[0] = "G"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, -13)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonG, 1, add=True)


def playerOneShipButtonH(x,y):
    if x < -650 and x > -700 and y < -50 and y > -100 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("H")
        global letCord
        letCord = True
        global coord
        coord[0] = "H"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, -63)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonH, 1, add=True)


def playerOneShipButtonI(x,y):
    if x < -650 and x > -700 and y < -100 and y > -150 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("I")
        global letCord
        letCord = True
        global coord
        coord[0] = "I"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, -113)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonI, 1, add=True)


def playerOneShipButtonJ(x,y):
    if x < -650 and x > -700 and y < -150 and y > -200 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("J")
        global letCord
        letCord = True
        global coord
        coord[0] = "J"
        
        t.penup()
        t.setpos(-725, 287)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(500)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-725, -163)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButtonJ, 1, add=True)


# # # # # # # # # # # # # # # # # # # # # # # # # #


def playerOneShipButton1(x,y):
    if x < -600 and x > -650 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("1")
        global numCord
        numCord = True
        global coord
        coord[1] = 1
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-638, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton1, 1, add=True)


def playerOneShipButton2(x,y):
    if x < -550 and x > -600 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("2")
        global numCord
        numCord = True
        global coord
        coord[1] = 2
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-588, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton2, 1, add=True)


def playerOneShipButton3(x,y):
    if x < -500 and x > -550 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("3")
        global numCord
        numCord = True
        global coord
        coord[1] = 3
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-538, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton3, 1, add=True)


def playerOneShipButton4(x,y):
    if x < -450 and x > -500 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("4")
        global numCord
        numCord = True
        global coord
        coord[1] = 4
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-488, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton4, 1, add=True)


def playerOneShipButton5(x,y):
    if x < -400 and x > -450 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("5")
        global numCord
        numCord = True
        global coord
        coord[1] = 5
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-438, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton5, 1, add=True)


def playerOneShipButton6(x,y):
    if x < -350 and x > -400 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("6")
        global numCord
        numCord = True
        global coord
        coord[1] = 6
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-388, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton6, 1, add=True)


def playerOneShipButton7(x,y):
    if x < -300 and x > -350 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("7")
        global numCord
        numCord = True
        global coord
        coord[1] = 7
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-338, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton7, 1, add=True)


def playerOneShipButton8(x,y):
    if x < -250 and x > -300 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("8")
        global numCord
        numCord = True
        global coord
        coord[1] = 8
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-288, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton8, 1, add=True)


def playerOneShipButton9(x,y):
    if x < -200 and x > -250 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("9")
        global numCord
        numCord = True
        global coord
        coord[1] = 9
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-238, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton9, 1, add=True)


def playerOneShipButton10(x,y):
    if x < -150 and x > -200 and y < -200 and y > -250 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        print("10")
        global numCord
        numCord = True
        global coord
        coord[1] = 10
        
        t.penup()
        t.setpos(-675, -253)
        t.width(3)
        t.color("#072645")
        t.setheading(0)
        t.fillcolor("#072645")
        t.begin_fill()
        t.pendown()
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.right(90)
        t.forward(600)
        t.right(90)
        t.forward(35)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
        
        t.penup()
        t.setpos(-188, -253)
        t.width(3)
        t.color("#A17A16")
        t.setheading(0)
        t.fillcolor("#CE9B1C")
        t.begin_fill()
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.end_fill()
        t.width(0)
        t.color("#DBDBDB")
        t.penup()
t.onscreenclick(playerOneShipButton10, 1, add=True)

def confirmReset():
    global numCord
    numCord = False
    global letCord
    letCord = False
    global isVert
    isVert = False
    global isHor
    isHor = False
    global isShipClass
    isShipClass = False
    global checkConfirm
    checkConfirm = False
    

def playerOneShipButtonConfirm(x,y):
    if x < 108 and x > -68 and y < -140 and y > -215 and isPlayerOneShipSelectionI == True:
        if numCord and letCord and (isVert or isHor) and isShipClass:
            while True:
                global coord
                try:
                    if orientation == 'h':
                        temp = ShipH(coord[1], dic[coord[0]], player1, ship_length)
                    else:
                        temp = ShipV(coord[1], dic[coord[0]], player1, ship_length)
                except ZeroDivisionError or IndexError:
                    print('Try Again')
                    t.penup()
                    t.setpos(-725, 287)
                    t.width(3)
                    t.color("#072645")
                    t.setheading(0)
                    t.fillcolor("#072645")
                    t.begin_fill()
                    t.pendown()
                    t.forward(25)
                    t.right(90)
                    t.forward(500)
                    t.right(90)
                    t.forward(25)
                    t.right(90)
                    t.forward(500)
                    t.end_fill()
                    t.width(0)
                    t.color("#DBDBDB")
                    t.penup()
                    t.setpos(-675, -253)
                    t.width(3)
                    t.color("#072645")
                    t.setheading(0)
                    t.fillcolor("#072645")
                    t.begin_fill()
                    t.pendown()
                    t.forward(600)
                    t.right(90)
                    t.forward(35)
                    t.right(90)
                    t.forward(600)
                    t.right(90)
                    t.forward(35)
                    t.end_fill()
                    t.width(0)
                    t.color("#DBDBDB")
                    t.penup()
                    break
                player1.display()
                break
            global carrierCount
            global battleshipCount
            global cruiserCount
            global submarineCount
            global destroyerCount
            if carrierCount == 0 and battleshipCount == 0 and cruiserCount == 0 and submarineCount == 0 and destroyerCount == 0:
                t.penup()
                t.setpos(-68, -235)
                t.width(5)
                t.color("#C94040")
                t.setheading(0)
                t.fillcolor("#AA2626")
                t.begin_fill()
                t.pendown()
                t.forward(176)
                t.right(90)
                t.forward(75)
                t.right(90)
                t.forward(176)
                t.right(90)
                t.forward(75)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                t.setpos(19, -289)
                t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
                global isPlayerOneShipsPlaced
                isPlayerOneShipsPlaced = True
        global checkConfirm
        if checkConfirm:
            confirmReset()
        
t.onscreenclick(playerOneShipButtonConfirm, 1, add=True)

def playerOneShipButtonContinue(x,y):
    if x < 108 and x > -68 and y < -235 and y > -310 and isPlayerOneShipSelectionI == True and isPlayerOneShipsPlaced == True:
        playerTwoSelectionI()
        isPlayerOneShipsPlaced == False
        global numCord
        global letCord
        numCord = False
        letCord = False
            
t.onscreenclick(playerOneShipButtonContinue, 1, add=True)



def playerTwoSelectionButtonII(x,y):
    if x < 250 and x > -250 and y < 210 and y > -40 and isPlayerTwoSelectionI == True:
        playerTwoShipSelectionI()
t.onscreenclick(playerTwoSelectionButtonII, 1, add=True)




def playerTwoShipButtonConfirm(x,y):
    if x < 108 and x > -68 and y < -140 and y > -215 and isPlayerTwoShipSelectionI == True:
        if numCord and letCord and (isVert or isHor) and isShipClass:
            while True:
                global coord
                try:
                    if orientation == 'h':
                        temp = ShipH(coord[1], dic[coord[0]], player2, ship_length)
                    else:
                        temp = ShipV(coord[1], dic[coord[0]], player2, ship_length)
                except ZeroDivisionError or IndexError:
                    print('Try Again')
                    t.penup()
                    t.setpos(-725, 287)
                    t.width(3)
                    t.color("#072645")
                    t.setheading(0)
                    t.fillcolor("#072645")
                    t.begin_fill()
                    t.pendown()
                    t.forward(25)
                    t.right(90)
                    t.forward(500)
                    t.right(90)
                    t.forward(25)
                    t.right(90)
                    t.forward(500)
                    t.end_fill()
                    t.width(0)
                    t.color("#DBDBDB")
                    t.penup()
                    t.setpos(-675, -253)
                    t.width(3)
                    t.color("#072645")
                    t.setheading(0)
                    t.fillcolor("#072645")
                    t.begin_fill()
                    t.pendown()
                    t.forward(600)
                    t.right(90)
                    t.forward(35)
                    t.right(90)
                    t.forward(600)
                    t.right(90)
                    t.forward(35)
                    t.end_fill()
                    t.width(0)
                    t.color("#DBDBDB")
                    t.penup()
                    break
                player2.display()
                break
            global carrierCount
            global battleshipCount
            global cruiserCount
            global submarineCount
            global destroyerCount
            if carrierCount == 0 and battleshipCount == 0 and cruiserCount == 0 and submarineCount == 0 and destroyerCount == 0:
                t.penup()
                t.setpos(-68, -235)
                t.width(5)
                t.color("#C94040")
                t.setheading(0)
                t.fillcolor("#AA2626")
                t.begin_fill()
                t.pendown()
                t.forward(176)
                t.right(90)
                t.forward(75)
                t.right(90)
                t.forward(176)
                t.right(90)
                t.forward(75)
                t.end_fill()
                t.width(0)
                t.color("#DBDBDB")
                t.penup()
                t.setpos(19, -289)
                t.write("Continue", move = False, align = "center", font = ("Copperplate Gothic Light", 20, "bold"))
                global isPlayerTwoShipsPlaced
                isPlayerTwoShipsPlaced = True
        global checkConfirm
        if checkConfirm:
            confirmReset()
t.onscreenclick(playerTwoShipButtonConfirm, 1, add=True)



def playerTwoShipButtonContinue(x,y):
    if x < 108 and x > -68 and y < -235 and y > -310 and isPlayerTwoShipSelectionI == True and isPlayerTwoShipsPlaced == True:
        playerOneSelectionII()
        isPlayerTwoShipsPlaced == False
        global numCord
        global letCord
        numCord = False
        letCord = False
            
t.onscreenclick(playerTwoShipButtonContinue, 1, add=True)



def playerOneSelectionAttackButtonI(x,y):
    if x < 250 and x > -250 and y < 210 and y > -40 and isPlayerOneSelectionII == True:
        playerOneAttackPageI()
        global numCord
        global letCord
        numCord = False
        letCord = False
t.onscreenclick(playerOneSelectionAttackButtonI, 1, add=True)


def playerOneAttackButtonConfirm(x,y):
    if x < 88 and x > -88 and y < -140 and y > -215 and isPlayerOneAttackPage == True:
        if numCord and letCord:
            playerOneShootI()
            global isWinner
            if isWinner:
                return()
            else:
                playerTwoSelectionII()
t.onscreenclick(playerOneAttackButtonConfirm, 1, add=True)



def playerTwoSelectionAttackButtonI(x,y):
    if x < 250 and x > -250 and y < 210 and y > -40 and isPlayerTwoSelectionII == True:
        playerTwoAttackPageI()
        global numCord
        global letCord
        numCord = False
        letCord = False
t.onscreenclick(playerTwoSelectionAttackButtonI, 1, add=True)


def playerTwoAttackButtonConfirm(x,y):
    if x < 88 and x > -88 and y < -140 and y > -215 and isPlayerTwoAttackPage == True:
        if numCord and letCord:
            playerTwoShootI()
            global isWinner
            if isWinner:
                return()
            else:
                playerOneSelectionII()
t.onscreenclick(playerTwoAttackButtonConfirm, 1, add=True)



def exitButton(x, y):
    if x > 650 and x < 825 and y < 425 and y > 350 and (isPlayerOneShipSelectionI or isPlayerOneAttackPage or isPlayerTwoShipSelectionI or isPlayerTwoAttackPage):
        global playerOneShotList
        global playerTwoShotList
        firedShots = open("fired_shots.txt", "w")
        for i in range(len(playerOneShotList)):
            firedShots.write(f"Player One:  Shot #{i+1} - {playerOneShotList[i][0]}{playerOneShotList[i][1]} - {playerOneShotList[i][2]}")
            firedShots.write("\n")
        firedShots.write("\n\n\n")
        for i in range(len(playerTwoShotList)):
            firedShots.write(f"Player Two:  Shot #{i+1} - {playerTwoShotList[i][0]}{playerTwoShotList[i][1]} - {playerTwoShotList[i][2]}")
            firedShots.write("\n")
        firedShots.close()
        
        t.bye()
    elif x < 250 and x > -250 and y < 210 and y > -40 and isWinner == True:
        firedShots = open("fired_shots.txt", "w")
        for i in range(len(playerOneShotList)):
            firedShots.write(f"Player One:  Shot #{i+1} - {playerOneShotList[i][0]}{playerOneShotList[i][1]} - {playerOneShotList[i][2]}")
            firedShots.write("\n")
        firedShots.write("\n\n\n")
        for i in range(len(playerTwoShotList)):
            firedShots.write(f"Player Two:  Shot #{i+1} - {playerTwoShotList[i][0]}{playerTwoShotList[i][1]} - {playerTwoShotList[i][2]}")
            firedShots.write("\n")
        firedShots.close()
        
        t.bye()
t.onscreenclick(exitButton, 1, add=True)



homeScreen()



t.update()

t.done()