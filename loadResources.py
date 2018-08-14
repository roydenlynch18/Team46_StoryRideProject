## Story Ride Project
## "Insert Title Here"
## Purple Group - Team 46
## Resource Loading File

############################################################################################################
##                                                                                                        ##
##  File Overview:                                                                                        ##
##  This file is solely meant to do some inital data setup so that the main programming file with most    ##
##  of the game logic looks much cleaner. Here, I'm importing the images and sounds and assigning them a  ##
##  variable to be referred to in a dictionary and then can be used in the main program.                  ##
##                                                                                                        ##
############################################################################################################

## Import Statements
import pygame

## Initializing Pygame Mixer (To Load Sound Effects)
pygame.mixer.init()

## Defining Image Variables
textBubbleImage         = pygame.image.load("Resources/Images/textBubbleImage.png")
menuImage               = pygame.image.load("Resources/Images/menuImage.jpg")
habitatImage            = pygame.image.load("Resources/Images/habitatImage.png")
meteorImage             = pygame.image.load("Resources/Images/meteorImage.png")
investigateImage        = pygame.image.load("Resources/Images/investigateImage.png")
abductionImage          = pygame.image.load("Resources/Images/abductionImage.jpg")
cellImage               = pygame.image.load("Resources/Images/escapeImage.jpg")
escapeImage             = pygame.image.load("Resources/Images/escapeImage.jpg")
experimentsImage        = pygame.image.load("Resources/Images/experimentsImage.jpg")
hallwayImage            = pygame.image.load("Resources/Images/hallwayImage.jpg")
rightImage              = pygame.image.load("Resources/Images/rightImage.jpg")
straightImage           = pygame.image.load("Resources/Images/straightImage.jpg")
leftImage               = pygame.image.load("Resources/Images/leftImage.jpg")
guardImage              = pygame.image.load("Resources/Images/guardImage.jpg")
bossImage               = pygame.image.load("Resources/Images/bossImage.jpg")
notifyImage             = pygame.image.load("Resources/Images/notifyImage.jpg")
jobImage                = pygame.image.load("Resources/Images/jobImage.jpg")
trainingImage           = pygame.image.load("Resources/Images/notifyImage.jpg")
combatTrainingImage     = pygame.image.load("Resources/Images/combatTrainingImage.jpg")
pilotTrainingImage      = pygame.image.load("Resources/Images/pilotTrainingImage.jpg")
gotoSpaceImage          = pygame.image.load("Resources/Images/gotoSpaceImage.jpg")
approachingShipsImage   = pygame.image.load("Resources/Images/approachingShipsImage.jpg")
beingBoardedImage       = pygame.image.load("Resources/Images/beingBoardedImage.jpg")
fightImage              = pygame.image.load("Resources/Images/fightImage.jpg")
boardingMothershipImage = pygame.image.load("Resources/Images/boardingMothershipImage.jpg")
reportToNASAImage       = pygame.image.load("Resources/Images/approachingShipsImage.jpg")

## Defining Sound Variables
menuSound               = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
habitatSound            = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
meteorSound             = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
investigateSound        = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
abductionSound          = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
cellSound               = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
escapeSound             = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
experimentsSound        = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
hallwaySound            = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
rightSound              = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
straightSound           = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
leftSound               = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
guardSound              = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
bossSound               = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
notifySound             = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
jobSound                = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
trainingSound           = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
combatTrainingSound     = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
pilotTrainingSound      = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
gotoSpaceSound          = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
approachingShipsSound   = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
beingBoardedSound       = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
fightSound              = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
boardingMothershipSound = pygame.mixer.Sound("Resources/Sounds/someSound.wav")
reportToNASASound       = pygame.mixer.Sound("Resources/Sounds/someSound.wav")

## Creating a Dictionary To Connect Scenes with Resources
SCENES = [{"name":"menuScene",              "img":menuImage,                "sound":menuSound},
          {"name":"habitatScene",           "img":habitatImage,             "sound":menuSound},
          {"name":"meteorScene",            "img":meteorImage,              "sound":meteorSound},
          {"name":"investigateScene",       "img":investigateImage,         "sound":investigateSound},
          {"name":"abductionScene",         "img":abductionImage,           "sound":abductionSound},
          {"name":"cellScene",              "img":cellImage,                "sound":cellSound},
          {"name":"escapeScene",            "img":escapeImage,              "sound":escapeSound},
          {"name":"experimentsScene",       "img":experimentsImage,         "sound":experimentsSound},
          {"name":"hallwayScene",           "img":hallwayImage,             "sound":hallwaySound},
          {"name":"rightScene",             "img":rightImage,               "sound":rightSound},
          {"name":"straightScene",          "img":straightImage,            "sound":straightSound},
          {"name":"leftScene",              "img":leftImage,                "sound":leftSound},
          {"name":"guardScene",             "img":guardImage,               "sound":guardSound},
          {"name":"bossScene",              "img":bossImage,                "sound":bossSound},
          {"name":"notifyScene",            "img":notifyImage,              "sound":notifySound},
          {"name":"jobScene",               "img":jobImage,                 "sound":jobSound},
          {"name":"trainingScene",          "img":trainingImage,            "sound":trainingSound},
          {"name":"combatTrainingScene",    "img":combatTrainingImage,      "sound":combatTrainingSound},
          {"name":"pilotTrainingScene",     "img":pilotTrainingImage,       "sound":pilotTrainingSound},
          {"name":"gotoSpaceScene",         "img":gotoSpaceImage,           "sound":gotoSpaceSound},
          {"name":"approachingShipsScene",  "img":approachingShipsImage,    "sound":approachingShipsSound},
          {"name":"beingBoardedScene",      "img":beingBoardedImage,        "sound":beingBoardedSound},
          {"name":"fightScene",             "img":fightImage,               "sound":fightSound},
          {"name":"boardingMothershipScene","img":boardingMothershipImage,  "sound":boardingMothershipSound},
          {"name":"bossDirectionsScene",    "img":bossImage,                "sound":bossSound},
          {"name":"gameWinScene",           "img":menuImage,                "sound":bossSound},
          {"name":"gameLoseScene",          "img":menuImage,                "sound":bossSound}]
