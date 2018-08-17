## Story Ride Project
## "Tiger-stellar"
## Purple Group - Team 46
## Main Program File

######################################################################################################################################
##                                                                                                                                  ##
##  Code Organization:                                                                                                              ##
##  Comments are located before every unique block to denote the purpose of the lines of code that follow. Specifically in the      ##
##  main program loop, to help see the decision tree, dashes and single hashtag comments are used for game logic and story/scene    ##
##  clarification.                                                                                                                  ##
##                                                                                                                                  ##
######################################################################################################################################

## Import Statements
import pygame           
import time
from random import randint
from loadResources import *

## Global Variables
GAME_TITLE = "Tiger-stellar"
WINDOW_WIDTH = 960#480
WINDOW_HEIGHT = 540#480
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
#global skill
#skill = "null"  #Skill is an attribute attained in game. It will be used and manipulated by functions.

## Initializing Pygame
pygame.init()
pygame.display.set_caption(GAME_TITLE)
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load("Resources/Sounds/backgroundMusic.mp3")
pygame.mixer.music.play(-1,0.0)

## ---------------------------------------- FUNCTIONS ----------------------------------------


## Defining a Scene Change Function (Makes the Game Logic Code Much Cleaner)
def changeSceneTo(i,shiftDown,shiftRight):
    print(SCENES[i]["name"])
    #currentScene = SCENES[i]["name"]       #for some reason can't get this to work
    screen.fill(COLOR_BLACK)
    screen.blit(SCENES[i]["img"],(0+shiftDown,0+shiftRight))
    
## Setting Up Pygame to Display Text, Creating My Own Function to Display Lines (And Make Speech Bubble)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS',30)
def displayMessage(ln,msg):
    if ln==1:
        screen.blit(textBubbleImage,(105,355))
    text=myfont.render(msg,False,(0,0,0))
    screen.blit(text,(130,360+20*ln))

## Creating a Roulette-based Game
def rouletteDoor(guess,skill):
    print("roulette called")
    if skill != "null":
        print("checking skill in roulette function")
        print(skill)
        result = "win"
        return result
    else:
        key = randint(0,100)
        if key<50 and guess=="under":
            result = "win"
        elif key>=50 and guess=="over":
            result = "win"
        else:
            result = "loss"
        return result

## Creating a Battle Scene vs. Guard (Rock, Paper, Scissors)
def battleGuard():
    
    #Counter Variables
    playerWins=0
    guardWins=0
    ties=0
    
    #Possible Moves and Variables to Store Moves
    moves=["rock","paper","scissors"]
    
    #Game Loop
    while playerWins<3:

        #Reset Player's Move
        playerMove=""
        
        #Text Display
        displayMessage(1,"STOP RIGHT THERE CRIMINAL SCUM! You'll have to fight me first!")
        displayMessage(2,"Let's do this... you must win three times to pass...")
        displayMessage(3,"1. Rock")
        displayMessage(4,"2. Paper")
        displayMessage(5,"3. Scissors")
        displayMessage(6,"Wins: "+str(playerWins)+" | "+"Ties: "+str(ties)+" | "+"Losses: "+str(guardWins))
        
        #Update Screen in this Nested Loop
        pygame.display.update()
        clock.tick(60)

        #Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    playerMove = "rock"
                if event.key == pygame.K_2:
                    playerMove = "paper"
                if event.key == pygame.K_3:
                    playerMove = "scissors"

        #Restart Loop if No Move Yet
        if playerMove=="":
            continue

        #Determine Guard Move (It's Random)
        guardMove = moves[randint(0,2)]

        #Checking Win Conditions
        if playerMove==guardMove:
            ties+=1
            displayMessage(7,"Nobody ties me!")
            pygame.display.update()
            clock.tick(60)
        elif playerMove=="rock" and guardMove=="scissors":
            playerWins+=1
            displayMessage(7,"GRRR!")
            pygame.display.update()
            clock.tick(60)
        elif playerMove=="paper" and guardMove=="rock":
            playerWins+=1
            displayMessage(7,"GRRR!")
            pygame.display.update()
            clock.tick(60)
        elif playerMove=="scissors" and guardMove=="paper":
            playerWins+=1
            displayMessage(7,"GRRR!")
            pygame.display.update()
            clock.tick(60)
        else:
            guardWins+=1
            displayMessage(7,"Ha! This is too easy.")
            pygame.display.update()
            clock.tick(60)
            
    #Load Boss Scene
    changeSceneTo(13,0,0)
    displayMessage(1,"Well well well... we meet at last, Mike.")
    displayMessage(2,"I've heard rumours about you...")
    displayMessage(3,"Friends of mine have said you've summoned earthquakes even.")
    displayMessage(4,"Now its time for us to battle, and this shall be your last...")
    displayMessage(7,"...space to continue...")

## Creating a Battle Scene vs. Boss (Tic Tac Toe)
def fightBoss(skill):

    #Creating Board as Single List (It's Easier in This Case)
    board=[0,0,0,
           0,0,0,
           0,0,0]

    #Making a Global Winner Variable (Needs To Be Accessable By isOver Function)
    global winner
    winner="null"
    #global skill
    #skill="null"

    #Creating a Function to Check Win Conditions and End Game
    def isOver():
        if board[0]==1 and board[1]==1 and board[2]==1:
            winner="player"
            return winner
        if board[3]==1 and board[4]==1 and board[5]==1:
            winner="player"
            return winner
        if board[6]==1 and board[7]==1 and board[8]==1:
            winner="player"
            return winner
        if board[0]==1 and board[3]==1 and board[6]==1:
            winner="player"
            return winner
        if board[1]==1 and board[4]==1 and board[7]==1:
            winner="player"
            return winner
        if board[2]==1 and board[5]==1 and board[8]==1:
            winner="player"
            return winner
        if board[0]==1 and board[4]==1 and board[8]==1:
            winner="player"
            return winner
        if board[6]==1 and board[4]==1 and board[2]==1:
            winner="player"
            return winner
        if board[0]==2 and board[1]==2 and board[2]==2:
            winner="boss"
            return winner
        if board[3]==2 and board[4]==2 and board[5]==2:
            winner="boss"
            return winner
        if board[6]==2 and board[7]==2 and board[8]==2:
            winner="boss"
            return winner
        if board[0]==2 and board[3]==2 and board[6]==2:
            winner="boss"
            return winner
        if board[1]==2 and board[4]==2 and board[7]==2:
            winner="boss"
            return winner
        if board[2]==2 and board[5]==2 and board[8]==2:
            winner="boss"
            return winner
        if board[0]==2 and board[4]==2 and board[8]==2:
            winner="boss"
            return winner
        if board[6]==2 and board[4]==2 and board[2]==2:
            winner="boss"
            return winner
        if board[0]!=0 and board[1]!=0 and board[2]!=0 and board[3]!=0 and board[4]!=0 and board[5]!=0 and board[6]!=0 and board[7]!=0 and board[8]!=0:
            winner="tie"
            return winner
        else:
            return "false"

    #Printing Board to Console for Lols.
    print(str(board[0])+"|"+str(board[1])+"|"+str(board[2]))
    print("-----")
    print(str(board[3])+"|"+str(board[4])+"|"+str(board[5]))
    print("-----")
    print(str(board[6])+"|"+str(board[7])+"|"+str(board[8]))
    print("     ")

    displayMessage(1,"                                                  "+str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    displayMessage(2,"                                                  "+"----------")
    displayMessage(3,"                                                  "+str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    displayMessage(4,"                                                  "+"----------")
    displayMessage(5,"                                                  "+str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
    pygame.display.update()
    clock.tick(60)

    #Defining Game Logic Variables
    winCondition=False
    playerTurn=True
    bossTurn=False
    #playerMove=10
    #bossMove=10

    #Game Loop
    firstTurn=True
    while winCondition==False:

        #Player's Turn
        while playerTurn==True:
            playerMove=10
            #Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        playerMove=0
                    if event.key == pygame.K_w:
                        playerMove=1
                    if event.key == pygame.K_e:
                        playerMove=2
                    if event.key == pygame.K_a:
                        playerMove=3
                    if event.key == pygame.K_s:
                        playerMove=4
                    if event.key == pygame.K_d:
                        playerMove=5
                    if event.key == pygame.K_z:
                        playerMove=6
                    if event.key == pygame.K_x:
                        playerMove=7
                    if event.key == pygame.K_c:
                        playerMove=8

            #Restart Loop If Move is Incoherent (Preset to be Incoherent to Avoid Keypress Glithces)
            if playerMove>8:
                continue

            #Place Move (Only If Spot is Unoccupied)
            if board[playerMove]==0:
                board[playerMove] = 1

                #Print Board to Console for Lols.
                print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
                print("--------")
                print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
                print("--------")
                print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
                print("     ")

                displayMessage(1,"                                                  "+str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
                displayMessage(2,"                                                  "+"----------")
                displayMessage(3,"                                                  "+str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
                displayMessage(4,"                                                  "+"----------")
                displayMessage(5,"                                                  "+str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
                pygame.display.update()
                clock.tick(60)

                #Check If Winning Board (no -> continue playing)
                print(skill)
                if isOver()=="false":
                    if skill=="combat" and firstTurn==True:
                        playerTurn=True
                        bossTurn=False
                        firstTurn=False
                    else:
                        playerTurn=False
                        bossTurn=True
                    
                #Check If Winning Board (yes - player wins)
                elif isOver()=="player":
                    print(isOver())
                    winCondition=True
                    break

                #Check If Winning Board (yes - boss wins)
                elif isOver()=="boss":
                    print(isOver())
                    winCondition=True
                    break

                elif isOver()=="tie":
                    print(isOver())
                    winCondition=True
                    break

            #Notify If Incorrent Move
            elif board[playerMove] == 1 or 2:
                print("Someone has already moved there.")
                continue

        #Double-check win condition before next turn, in order to break parent while loop.
        if winCondition==True:
            break
        
        #Boss's Turn (Repeat Comments from Above)
        while bossTurn==True:
            bossMove=10
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        bossMove=0
                    if event.key == pygame.K_y:
                        bossMove=1
                    if event.key == pygame.K_u:
                        bossMove=2
                    if event.key == pygame.K_g:
                        bossMove=3
                    if event.key == pygame.K_h:
                        bossMove=4
                    if event.key == pygame.K_j:
                        bossMove=5
                    if event.key == pygame.K_b:
                        bossMove=6
                    if event.key == pygame.K_n:
                        bossMove=7
                    if event.key == pygame.K_m:
                        bossMove=8
                        
            if bossMove>8:
                continue

            if board[bossMove]==0:
                board[bossMove] = 2
                
                print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
                print("-------")
                print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
                print("-------")
                print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
                print("     ")

                displayMessage(1,"                                                  "+str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
                displayMessage(2,"                                                  "+"----------")
                displayMessage(3,"                                                  "+str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
                displayMessage(4,"                                                  "+"----------")
                displayMessage(5,"                                                  "+str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
                pygame.display.update()
                clock.tick(60)

                if isOver()=="false":
                    playerTurn=True
                    bossTurn=False

                elif isOver()=="player":
                    print(isOver())
                    winCondition=True
                    break

                elif isOver()=="boss":
                    print(isOver())
                    winCondition=True
                    break

                elif isOver()=="tie":
                    print(isOver())
                    winCondition=True
                    break
                
            elif board[bossMove] == 1 or 2:
                print("Someone has already moved there.")
                continue

        if winCondition==True:
            break

    if isOver()=="player":
        changeSceneTo(0,0,0)
        displayMessage(1,"You Win!")
        displayMessage(2,"LSU Prevails!")
        displayMessage(7,"...press 'r' to restart..")
        pygame.display.update()
        clock.tick(60)
        currentScene="gameDone"
        print(currentScene)
        
    elif isOver()=="boss":
        changeSceneTo(0,0,0)
        displayMessage(1,"You Lose!")
        displayMessage(2,"Today is one of the worst days in history...")
        displayMessage(7,"...press 'r' to restart...")
        pygame.display.update()
        clock.tick(60)
        currentScene="gameDone"
        print(currentScene)

    elif isOver()=="tie":
        changeSceneTo(0,0,0)
        displayMessage(1,"It's a tie...")
        displayMessage(2,"Maybe you'll fight another day...")
        displayMessage(7,"...press 'r' to restart...")
        pygame.display.update()
        clock.tick(60)
        currentScene="gameDone"


## ---------------------------------------- MAIN ----------------------------------------


## Defining Main Function
def main():
    
    ## Initializing Logic Variables
    gameOver = False

    ## Drawing Menu
    currentScene = "menuScene"
    screen.fill(COLOR_BLACK)
    screen.blit(menuImage,(0,0))
    displayMessage(1,"Welcome to Tiger-stellar, the ride where you decide!")
    displayMessage(2,"Click <SPACE> to progress to the next scene.")
    displayMessage(3,"When presented with a choice, click 1 or 2 to decide.")
    displayMessage(4,"Good luck!")
    displayMessage(7,"...space to continue...")

    skill="null"

    ## Main Program Loop
    while not gameOver:
        
        ## Initializing Logic Variables
        decision = ""
        
        ## Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    decision = "choice_1"
                if event.key == pygame.K_2:
                    decision = "choice_2"
                if event.key == pygame.K_3:
                    decision = "choice_3"
                if event.key == pygame.K_SPACE:
                    decision = "choice_space"
                if event.key == pygame.K_r:
                    decision = "restart"
                    
        ## --------------------             
        ## ---- Game Logic ----
        ## --------------------

        ## ---- Restart ----
        if decision == "restart":
            currentScene = "menuScene"
            screen.fill(COLOR_BLACK)
            screen.blit(menuImage,(0,0))
            displayMessage(1,"Welcome to Tiger-stellar, the ride where you decide!")
            displayMessage(2,"Click <SPACE> to progress to the next scene.")
            displayMessage(3,"When presented with a choice, click 1 or 2 to decide.")
            displayMessage(4,"Good luck!")
            displayMessage(7,"...space to continue...")
            
        ## ---- Menu ----
        elif currentScene == "menuScene" and decision == "choice_space":
            #Load Habitat
            x=1
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Ahh. What a beautiful night.")
            displayMessage(2,"I'm sure tonight will be another great night at LSU.")
            displayMessage(7,"...space to continue...")

        ## ---- Habitat ----
        elif currentScene == "habitatScene" and decision == "choice_space":
            #Load Meteor
            x=2
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Woah! A wild meteor appears!")
            displayMessage(2,"DECISION! Do you want to...")
            displayMessage(3,"1. Investigate the meteor, or")
            displayMessage(4,"2. Notify NASA about it.")

        ## ---- Meteor (DECISION) ----
        elif currentScene == "meteorScene" and decision == "choice_1":
            #Load Investigate
            x=3
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Hmm. What in the world is the this!?")
            displayMessage(7,"...space to continue...")
        elif currentScene == "meteorScene" and decision == "choice_2":
            #Load Notify
            x=14
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"This is not cool, I need to notify NASA now!")
            displayMessage(7,"...space to continue...")

        ## ---- Investigate ----
        elif currentScene == "investigateScene" and decision == "choice_space":
            #Load Abduction
            x=4
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Oh no... what is that rumbling sound?")
            displayMessage(2,"WOAAAAH!!!")
            displayMessage(7,"...space to continue...")

        ## ---- Abduction ----
        elif currentScene == "abductionScene" and decision == "choice_space":
            #Load Cell
            x=5
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Where am I????")
            displayMessage(2,"It looks like I've been abducted!")
            displayMessage(3,"And now I'm trapped in a cell!")
            displayMessage(4,"DECISION! Do you want to ...")
            displayMessage(5,"1. Try to escape now, or")
            displayMessage(6,"2. Wait for a better opportunity to arise.")

        ## ---- Cell (DECISION) ----
        elif currentScene == "cellScene" and decision == "choice_1":
            #Load Escape
            x=6
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Alright, looks like there's a door and code.")
            displayMessage(2,"It wants me to guess if the number is below 50 or over 50??")
            displayMessage(3,"DECISION! Do you want to ...")
            displayMessage(4,"1. Pick Below 50")
            displayMessage(5,"2. Pick Above 50")
            
        elif currentScene == "cellScene" and decision == "choice_2":
            #Load Experiments
            x=7
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Uh oh...")
            displayMessage(2,"I think they're taking me to a lab of some sort...")
            displayMessage(7,"...space to continue...")

        ## ---- Escape (DECISION) ----
        elif currentScene == "escapeScene" and decision == "choice_1":
            #Load Win (Hallway)
            if rouletteDoor("under",skill)=="win":
                x=8
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"I got it right! Phew...")
                displayMessage(2,"Let's find their leader and teach him a lesson...")
                displayMessage(3,"Hmm, it looks like I'm in a main hallway.")
                displayMessage(4,"DECISION! Do you want to ...")
                displayMessage(5,"1. Go Left")
                displayMessage(6,"2. Go Straight")
                displayMessage(7,"3. Go Right")
            else:
                x=7
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"I got it wrong! Oh no...")
                displayMessage(2,"I think some guards are coming... this can't be good.")
                displayMessage(3,"...space to continue...")
        elif currentScene == "escapeScene" and decision == "choice_2":
            #Load Win (Hallway)
            print(rouletteDoor("over",skill))
            if rouletteDoor("over",skill)=="win":
                x=8
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"I got it right! Phew...")
                displayMessage(2,"Let's find their leader and teach him a lesson...")
                displayMessage(3,"Hmm, it looks like I'm in a main hallway.")
                displayMessage(4,"DECISION! Do you want to ...")
                displayMessage(5,"1. Go Left")
                displayMessage(6,"2. Go Straight")
                displayMessage(7,"3. Go Right")
            else:
                x=7
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"I got it wrong! Oh no...")
                displayMessage(2,"I think some guards are coming... this can't be good.")
                displayMessage(3,"...space to continue...")

        ## ---- Experiments ----
        elif currentScene == "experimentsScene" and decision == "choice_space":
            #Load Job
            x=14
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"*wakes up*")
            displayMessage(2,"Where am I now? NASA?")
            displayMessage(3,"I guess I need to work here and get my revenge now...")
            displayMessage(7,"...space to continue...")

        ## ---- Hallway (DECISION) ----
        elif currentScene == "hallwayScene" and decision == "choice_1":
            #Load Left
            x=11
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"It's a dead end!")
            displayMessage(7,"...space to continue...")
    
        elif currentScene == "hallwayScene" and decision == "choice_2":
            #Load Straight
            x=10
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"You think you hear and just saw a guard, just on the other side of this door.")
            displayMessage(2,"DECISION! Do you want to ...")
            displayMessage(3,"1. Turn back to the hallway, or")
            displayMessage(4,"2. Confront the guard.")
            
        elif currentScene == "hallwayScene" and decision == "choice_3":
            #Load Right
            x=9
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"It's a dead end!")
            displayMessage(7,"...space to continue...")

        ## ---- Right ----
        elif currentScene == "rightScene" and decision == "choice_space":
            #Load Hallway
            x=8
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"I'm back in the main hall.")
            displayMessage(2,"1. Go Left")
            displayMessage(3,"2. Go Straight")
            displayMessage(4,"3. Go Right")

        ## ---- Straight (DECISION) ----
        elif currentScene == "straightScene" and decision == "choice_1":
            #Load Hallway
            x=8
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"I'm back in the main hall.")
            displayMessage(2,"1. Go Left")
            displayMessage(3,"2. Go Straight")
            displayMessage(4,"3. Go Right")
            
        elif currentScene == "straightScene" and decision == "choice_2":
            #Load Guard
            x=12
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"STOP RIGHT THERE! You'll have to fight me first!")
            displayMessage(2,"Let's do this... you must win three times to pass...")
            displayMessage(3,"1. Rock")
            displayMessage(4,"2. Paper")
            displayMessage(5,"3. Scissors")
            displayMessage(6,"Wins: 0 | Ties: 0 | Losses: 0")
            pygame.display.update()
            clock.tick(60)
            battleGuard()
            currentScene = SCENES[13]["name"]
            print("battle guard function closed")
            print(currentScene)

        ## ---- Left ----
        elif currentScene == "leftScene" and decision == "choice_space":
            #Load Hallway
            x=8
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"I'm back in the main hall.")
            displayMessage(2,"1. Go Left")
            displayMessage(3,"2. Go Straight")
            displayMessage(4,"3. Go Right")

        ## ---- Guard (DECISION) ----
##        elif currentScene == "guardScene" and "choice_space":
##            pass
##            #This scene fully takes place in the battleGuard() function.
##
##        ## ---- Beat Guard ----
##            x=13
##            currentScene = SCENES[x]["name"]
##            changeSceneTo(x)
            

        ## ---- Boss (DECISION) ---- ########*#*#*#*#*#*#**#
        elif currentScene == "bossScene" and decision == "choice_space":
            x=24
            currentScene = SCENES[x]["name"]
            displayMessage(1,"Directions - ")
            displayMessage(2,"Mike (Player): Use the grid of Q,W,E/A,S,D/Z,X,C to pick your move.")
            displayMessage(3,"Boss (Operator): Use the grid of T,Y,U/G,H,J/B,N,M to pick yours.")
            displayMessage(4,"Simply select the corresponding spot to mark either an X (1) or O (2).")
            displayMessage(7,"...space to begin...")

        elif currentScene == "bossDirectionsScene" and decision == "choice_space":
            fightBoss(skill)

        ## ---- Notify ----
        elif currentScene == "notifyScene" and decision == "choice_space":
            x=15
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,125,0)
            displayMessage(1,"NASA: That's great information, welcome aboard Mike!")
            displayMessage(7,"...space to continue...")

        ## ---- Job ----
        elif currentScene == "jobScene" and decision == "choice_space":
            #Load Training
            x=16
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"NASA: Alright Mike, we're going to need to train you!")
            displayMessage(2,"DECISION! Do you want to ...")
            displayMessage(3,"1. Train in Combat, or")
            displayMessage(4,"2. Train in Piloting.")

        ## ---- Training (DECISION) ----
        elif currentScene == "trainingScene" and decision == "choice_1":
            #Load Combat
            x=17
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,35,0)
            displayMessage(1,"With these moves, I'll be able to punch any enemy...")
            displayMessage(2,"twice before they even realize what him them!")
            displayMessage(6,"*ability gained: two first moves vs. boss")
            displayMessage(7,"...space to continue...")
            
        elif currentScene == "trainingScene" and decision == "choice_2":
            #Load Pilot
            x=18
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,175,0)
            displayMessage(1,"With these flight skills, I can navigate through any...")
            displayMessage(2,"squadron of enemy ships!")
            displayMessage(6,"*ability gained: can bypass mothership security squads")
            displayMessage(7,"...space to continue...")

        ## ---- Combat ----
        elif currentScene == "combatTrainingScene" and decision == "choice_space":
            #Load Space
            x=19
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"NASA: You're done! Time to get to space!")
            displayMessage(2,"I'm ready!")
            displayMessage(7,"...space to continue...")
            skill="combat"
            print("Updated Skill: "+str(skill))

        ## ---- Pilot ----
        elif currentScene == "pilotTrainingScene" and decision == "choice_space":
            #Load Space
            x=19
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"NASA: You're done! Time to get to space!")
            displayMessage(2,"I'm ready!")
            displayMessage(7,"...space to continue...")
            skill="pilot"
            print("Updated Skill: "+str(skill))

        ## ---- Space ----
        elif currentScene == "gotoSpaceScene" and decision == "choice_space":
            #Load Ships
            x=20
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Hmm, it looks like some other ships are flying near...")
            displayMessage(2,"DECISION! Do you want to ...")
            displayMessage(3,"1. Let them board and see what they want, or")
            displayMessage(4,"2. Fend them off.")

        ## ---- Ships (DECISION) ----
        elif currentScene == "approachingShipsScene" and decision == "choice_1":
            #Load Boarded
            x=21
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Oh no, they have weapons. This was a terrible idea!!!")
            displayMessage(7,"...space to continue...")
            
        elif currentScene == "approachingShipsScene" and decision == "choice_2":
            #Load Fend
            x=22
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Phew, we did it...")
            displayMessage(2,"DECISION! Do you want to ...")
            displayMessage(3,"1. Go board the mothership, or")
            displayMessage(4,"2. Go home to report to NASA.")

        ## ---- Boarded ----
        elif currentScene == "beingBoardedScene" and decision == "choice_space":
            #Load Abduction
            x=4
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Oh no they're abducting me!!")
            displayMessage(7,"...space to continue...")

        ## ---- Fend (DECISION) ----
        elif currentScene == "fightScene" and decision == "choice_1":
            #Load Boarding
            if skill=="pilot":
                x=23
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"Here's the mothership, lets find their leader!")
                displayMessage(7,"...space to continue...")
            else:
                x=23
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"Hopefully I can get past any security ships...")
                displayMessage(7,"...space to continue...")
                
            
        elif currentScene == "fightScene" and decision == "choice_2":
##            #Load Report
##            x=24
##            currentScene = SCENES[x]["name"]
##            changeSceneTo(x,0,0)
            x=5
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Oh no! The security ships captured us on the way home!")
            displayMessage(2,"It looks like we're trapped in some sort of cell.")
            displayMessage(3,"DECISION! Do you want to ...")
            displayMessage(4,"1. Try to escape now, or")
            displayMessage(5,"2. Wait for a better opportunity to arise.")
                              

        ## ---- Boarding ----
        elif currentScene == "boardingMothershipScene" and decision == "choice_space":
            #Load Hallway
            if skill=="pilot":
                x=8
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
                displayMessage(1,"Hmm, it looks like I'm in a main hallway.")
                displayMessage(2,"Let's find their leader and teach him a lesson...")
                displayMessage(3,"DECISION! Do you want to ...")
                displayMessage(4,"1. Go Left")
                displayMessage(5,"2. Go Straight")
                displayMessage(6,"3. Go Right")
            else:
                x=5
                currentScene = SCENES[x]["name"]
                changeSceneTo(x,0,0)
##                displayMessage(1,"Oh no! The security ships captured us!")
##                displayMessage(2,"It looks like we're trapped in some sort of cell.")
##                displayMessage(3,"Alright, looks like there's a door and code.")
##                displayMessage(4,"It wants me to guess if the number is below 50 or over 50??")
##                displayMessage(5,"DECISION! Do you want to ...")
##                displayMessage(6,"1. Pick Below 50")
##                displayMessage(7,"2. Pick Above 50")
                displayMessage(1,"Oh no! The security ships captured us!")
                displayMessage(2,"It looks like we're trapped in some sort of cell.")
                displayMessage(5,"DECISION! Do you want to ...")
                displayMessage(6,"1. Try to escape now.")
                displayMessage(7,"2. Wait for a better opportunity to arise.")
                

        ## ---- Reporting ----
        elif currentScene == "reportToNASAScene" and decision == "choice_space":
            #Load Abduction
            x=5
            currentScene = SCENES[x]["name"]
            changeSceneTo(x,0,0)
            displayMessage(1,"Oh no! They've abducted me on the way home!")
            displayMessage(2,"I'll have to escape and fight back...")
            displayMessage(7,"...space to continue...")

        # ---- Game Win, Then Repeat ----
        elif currentScene ==  "gameDone" and decision == "choice_space":
            currentScene = SCENES[0]["name"]
            changeSceneTo(0,0,0)

            currentScene = "menuScene"
            screen.fill(COLOR_BLACK)
            screen.blit(menuImage,(0,0))
            displayMessage(1,"Welcome to Tiger-stellar, the ride where you decide!")
            displayMessage(2,"Click <SPACE> to progress to the next scene.")
            displayMessage(3,"When presented with a choice, click 1 or 2 to decide.")
            displayMessage(4,"Good luck!")
            displayMessage(7,"...space to continue...")

            skill="null"


        ## Updating Screen
        pygame.display.update()
        ## 60 FPS Limit
        clock.tick(60)
    ## Quit Pygame
    pygame.quit()
    quit()

## Calling Main Function
if __name__ == "__main__":
    main()
