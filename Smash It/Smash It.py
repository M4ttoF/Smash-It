#Final Project
#By: Matthew Farias and Nicole Cesca
#This program was designed for the enjoymet of others. This battle game is based off super smash bros which includes,
#two characters Marth and Sonic. When pressing play the user has the option of three different stages to battle at.
#Each player starts off with low damage and when the get hit by their opponent it gradually increses to medium and them to high.
#If a player gets knocked of the screen, then they will respawn (come back to life).
#Each charcter can respawn a total of three times (4 Lives/Stocks). After that if the charcter gets knocked off the screen or their damage
#makes it to high their opponent will be the declarde winner of this match.
#This game was desiged to have fun battleling your friends as well as to determine the overall true Smash It champion.

from pygame import *

screen = display.set_mode((800,600))

# Background Pics
##########################################################################
# These are the images that will display to show the stage depending on which stage the user chooses
# Each stage has its own corresponding mask
backPic1 = image.load("Back Pics/Battlefield_new.png")
backPic1_trans = transform.smoothscale(backPic1, screen.get_size())
maskPic1 = image.load("Back Pics/Battlefield_Mask_Two.png")
maskPic1_trans = transform.smoothscale(maskPic1, screen.get_size())

backPic2 = image.load("Back Pics/FinalDestination.png")
overlay_for_backpic=image.load("Back Pics/final destination background.png")
overlay_for_backpic_trans=transform.smoothscale(overlay_for_backpic, screen.get_size())
maskPic2 = image.load("Back Pics/FinalDestinationMaskV2.png")


backPic3 = image.load("Back Pics/Best.png")
backPic3_trans = transform.smoothscale(backPic3, screen.get_size())
maskPic3 = image.load("Back Pics/Town and citygoodMask.png")
maskPic3_trans = transform.smoothscale(maskPic3, screen.get_size())


################################################################################

currentLevel = 0  #this is for the mask pics, for the current level selected 

##################################################################################

# Sonic logo that will appear on screen to represent which percent is his

soniclogo = image.load("Logos/SonicSymbol.png")
soniclogo = transform.scale(soniclogo,(150,150))

# Marth logo that will appear on screen to represent which percent is his
marthlogo = image.load("Logos/FireEmblemSymbol.png")
marthlogo = transform.scale(marthlogo,(150,150))

#Percentage level pics
highpic=image.load("Logos/High.png")
mediumpic=image.load("Logos/Medium.png")
lowpic=image.load("Logos/Low.png")

init()
mixer.init()
def moveMarth():
# This is the main function for marth and it keeps track of Marth's movements, frame
# his velocity for both X and Y and whether he gets hit or not
    global dFrame, p2dFrame, p2frame, p1hitDir, p2hitDir, move, frame, standright, marinair, newMove, marthWaittime, saveMove, p2move, p2newMove
    keys=key.get_pressed()

    if marth[X]>900 or marth[X]<-100 or marth[Y]<-100 or marth[Y]> 700:
        respawnMarth()

    marth[ONGROUND] = False
    if marth[VY]<10: # sets a maximum gravity for marth
        marth[VY] += 1         # add gravity to VY
#########################
#Marth moving from getting hit
    if marth[VX] < 0:
        marth[VX]+=1
        marthLeft(marth,-marth[VX])
    elif marth[VX] > 0:
        marth[VX]-=1
        marthRight(marth,marth[VX])

#########################

###########################

##########################
# Marth Gravity
    #This will move marth upwards if his VY is < 0  and will display a different sprite depending on which direction he is facing
    if marth[VY] < 0:
        marthUp(marth,-marth[VY])
        if marth[FACERIGHT] ==True:
            newMove=AIR_R # sets te move to be his Idle air depending on the direction he faces
        else:
            newMove=AIR_L


    #This will move marth down according to how high his VY is (The higher it is the faster he falls)    
    elif marth[VY] > 0:
        marthDown(marth,marth[VY])
        if marth[FACERIGHT] ==True:
            newMove=AIR_R
        else:
            newMove=AIR_L
#############################
# Marth VX
   #This is will move marth in a corresponding directiong to his VX
    # if his VX > 0 then he will move faster towards the right
    # if his VX < 0 then he will move faster towards the left
    # he will slow down as he moves and his VX will be constantly trying to return to 0
    if marth[VX]<0:
        marth[VX]+=1
        
    elif marth[VX]>0:
        marth[VX]-=1
#############################################
    #This will let marth do his moves as long as he is not currently in a move and
    #He is not vulnerable from his recovery move (After a character uses a recovery move
    # they are unable to do any moves until they hit the ground
    if marthWaittime==0 and marth[VULNERABLE]==False: #checks to see if marth is currently in an attack

########################
        # Resetting dFrame so that a hit will not register more than once
        dFrame=[-1]

        if marth[ONGROUND]==False:
        ############
        # Air moves
            if keys[K_h]:
                marthRecovery(marth)

            
            elif keys[K_s] and keys[K_g]:
                marthDair(marth)

            elif keys[K_w] and keys[K_g]:
                marthUPSmash(marth)

            elif keys[K_g]:
                marthFair(marth)
                
            elif keys[K_s] and marth[VY]< 20 and marth[VY]>=0:
                marth[VY]+=10 # this lets marth fall faster than normal so he can evade attacks in the air and manouver

            
            elif keys[K_SPACE] and marth[DOUBLEJUMP]==True and marth[VY]>-5:
                marth[VY]=-15
                marth[DOUBLEJUMP]=False
                if marth[FACERIGHT] ==True:
                    newMove=AIR_R
                else:
                    newMove=AIR_L

            elif keys[K_a]:
                marthLeft(marth,10)
                
            elif keys[K_d]:
                marthRight(marth,10)
            elif keys[K_s] and marth[VY]< 20 and marth[VY] >= -1:
                marth[VY]+=10 # this lets marth fall faster than normal so he can evade attacks in the air and manouver


        else:

            #######################
            # Ground Moves

            if keys[K_h]:
                marthRecovery(marth)
            
            elif keys[K_SPACE]:
                marth[VY]=-10
                if marth[FACERIGHT] ==True:
                    newMove=AIR_R
                else:
                    newMove=AIR_L

            elif keys[K_w] and keys[K_g]:
                marthUPSmash(marth)
                


            elif keys[K_g]:
                marthFSmash(marth)

            elif keys[K_v]:
                marthTaunt(marth)
            
            elif keys[K_a]:
                marthLeft(marth,10)
                
            elif keys[K_d]:
                marthRight(marth,10)



        

        #Standing/Idle animations    
            else:
                marthIdle(marth)
    else:
        #Resets newMove if he is currently in a move so that it compeletes the animation
        newMove=saveMove
        
        if newMove==STUN_L or newMove== STUN_R: #this allows marth to move side to side while he is stunned
            if keys[K_a]:
                marthLeft(marth,10)
                
            elif keys[K_d]:
                marthRight(marth,10)
            




    if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        frame = frame + 0.25 # adding 0.2 allows us to slow down the animation to 1/3 of regular speed
        if frame >= len(marpics[move]): #This sets the move to STUN after a recovery
            if marth[FACERIGHT]==True:
                newMove=STUN_R
                saveMove=STUN_R
            else:
                newMove=STUN_L
                saveMove=STUN_L
        if frame >= len(marpics[move]): # Resets the move back to the first frame when it is done completing the animation
            frame = 1
    elif newMove != -1:     # a move was selected
        move = newMove      # make that our current move
        frame = 1

    #################################################
        # Marth Damage
    # Tracks if player 2 is in a frame that does damage and checks if it collides with marth
    if int(p2frame) in p2dFrame and sonicArea.colliderect(marthArea):
        p1damage(marth)
    
#################################################
        



#########################################################

def moveSonic():
# This is the main function for marth and it keeps track of sonic's movements, frame
# his velocity for both X and Y and whether he gets hit or not
    global p2frame, sonicWaittime, p2saveMove, p2move, p2newMove, p2dFrame, dFrame, p1hitDir, p2hitDir, frame
    keys=key.get_pressed()
############################
    #Respawing sonic
    if sonic[X]>900 or sonic[X]<-100 or sonic[Y]<-100 or sonic[Y]> 700:
        respawnSonic()
    #################################################
        #SONIC
    sonic[ONGROUND] = False
    if sonic[VY]<10: # sets a maximum gravity for sonic
        sonic[VY] += 1         # add gravity to VY
    

#########################
# Sonic VX
    if sonic[VX] < 0:
        sonic[VX]+=1
        sonicLeft(sonic,-sonic[VX])
    elif sonic[VX] > 0:
        sonic[VX]-=1
        sonicRight(sonic,sonic[VX])

############################
# Sonic Gravity
    if sonic[VY] < 0:
        sonicUp(sonic,-sonic[VY])
        if sonic[FACERIGHT] ==True:
            p2newMove=AIR_R # sets te move to be his Idle air depending on the direction he faces
        else:
            p2newMove=AIR_L
    elif sonic[VY] > 0:
        sonicDown(sonic,sonic[VY])
        if sonic[FACERIGHT] ==True:
            p2newMove=AIR_R
        else:
            p2newMove=AIR_L
        if keys[K_k] and sonic[ONGROUND]==False and sonic[VY]< 20:
            sonic[VY]+=10 # this lets sonic fall faster than normal so he can evade attacks in the air and manouver.
                   
            
    if sonicWaittime==0 and sonic[VULNERABLE]==False: #checks to see if sonic is currently in an attack
        

        if sonic[ONGROUND] == False:

            if keys[K_LEFTBRACKET]:
                sonicRecovery(sonic)
        
            elif keys[K_PERIOD] and sonic[DOUBLEJUMP]==True and sonic[VY]>-5:
                sonic[VY]=-15
                sonic[DOUBLEJUMP]=False
                if sonic[FACERIGHT] ==True:
                    p2newMove=AIR_R
                else:
                    p2newMove=AIR_L
                    
            elif keys[K_i] and keys[K_p]:
                sonicUPSmash(sonic)

            elif keys[K_k] and keys[K_p]:
                sonicDair(sonic)

            elif keys[K_p]:
                sonicFair(sonic)

            elif keys[K_j]:
                sonicLeft(sonic,10)
                
            elif keys[K_l]:
                sonicRight(sonic,10)



        else:
            if keys[K_LEFTBRACKET]:
                sonicRecovery(sonic)

            elif keys[K_n]:
                sonicTaunt(sonic)
                
            elif keys[K_PERIOD]:
                sonic[VY]=-10
                if sonic[FACERIGHT] ==True:
                    p2newMove=AIR_R
                else:
                    p2newMove=AIR_L

                    
            elif keys[K_i] and keys[K_p]:
                sonicUPSmash(sonic)
    
            elif keys[K_p]:
                sonicFSmash(sonic)

            
            
            elif keys[K_j]:
                sonicLeft(sonic,10)
                
            elif keys[K_l]:
                sonicRight(sonic,10)



    

        

        #Standing/Idle animations    
            else:
                sonicIdle(sonic)
    else:
        
        p2newMove=p2saveMove

        if p2newMove==STUN_L or p2newMove== STUN_R: #this allows marth to move side to side while he is stunned
            if keys[K_j]:
                sonicLeft(sonic,5)
                
            elif keys[K_l]:
                sonicRight(sonic,5)
        
        #####################
        #SONIC
    if p2move == p2newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        p2frame = p2frame + 0.6 # adding 0.2 allows us to slow down the animation to 1/3 of regular speed
        if p2frame >= len(sonicpics[p2move]): #This sets the move to STUN after a recovery
            if sonic[FACERIGHT]==True:
                p2newMove=STUN_R
                p2saveMove=STUN_R
            else:
                p2newMove=STUN_L
                p2saveMove=STUN_L        
        if p2frame >= len(sonicpics[p2move]):
            p2frame = 1
    elif p2newMove != -1:     # a move was selected
        p2move = p2newMove      # make that our current move
        p2frame = 1
#######################################
        # Sonic Damage
    if int(frame) in dFrame and marthArea.colliderect(sonicArea):
        p2damage(sonic)
    


#This function is the last resort of marth's moves and draws him standing still facing right or left depending on which way he was facing last
#marthIdle only works if there are no inputs for marth from the player
def marthIdle(marth):
    global newMove, marthArea, dFrame
    if marth[FACERIGHT]==True:
        newMove = IDLE_R
    else:
        newMove= IDLE_L
    #marthArea makes a rectangle that becomes marth's hitbox around his character we got this line from the Vinay and Anas example from the class folder
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
#This function moves marth to the right by using getPixel to check if there isnt a green pixel next to him on the mask

###############################
def marthRight(marth,vx):
    global newMove, marthArea, dFrame
    marth[FACERIGHT]=True
    if marth[ONGROUND]==True:
        newMove = RIGHT
    for i in range(vx):
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+20,marth[Y]+15) != GREEN:
            marth[X] += 1


    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)

#This function moves marth to the left by using getPixel to check if there isnt a green pixel next to him on the mask

############################
def marthLeft(marth,vx):
    global newMove, marthArea, dFrame
    marth[FACERIGHT]=False
    if marth[ONGROUND]==True:
        newMove = LEFT
    
    for i in range(vx):
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+2,marth[Y]+15) != GREEN:
            marth[X] -= 1

    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)

#########################################
#This function moves marth up by using getPixel to check if there isnt a green pixel above him on the mask
def marthUp(marth,vy):
    global marthArea, dFrame
    for i in range(vy):
        #Checks to see if the pixel above him is green
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+2) != GREEN:
            marth[Y] -= 1
        else:
            marth[VY] = 0

    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)

####################################
#This function moves marth down by using getPixel to check if there isnt a green pixel below him on the mask
def marthDown(marth,vy):
    global marthArea, dFrame
    for i in range(vy):
        #checks to see if the pixel under him is green
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+28) != GREEN:
            marth[Y] += 1
        else:
            marth[VY] = 0
            marth[ONGROUND] = True
            marth[DOUBLEJUMP]=True
            marth[VULNERABLE]= False

    
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)


###############################
# marthFSmash is his forward smash attack that will hit sonic upwards and to the direction where marth is facing
# It also sets the wait time to 12 frames (30 frames a second)

def marthFSmash(marth):
    global newMove, marthWaittime, saveMove, marthArea, p1hitDir, dFrame, damage
    if marth[FACERIGHT]==True:
        newMove = FS_R
        saveMove = FS_R
        p1hitDir="UR"
    else:
        newMove= FS_L
        saveMove= FS_L
        p1hitDir="UL"
    marthWaittime=12
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
    dFrame=[2]
    damage=14
    
#####################################
#marthUPSmash is his upward attack for both in the air on ground. If it hits it will make sonic go straight upwards

def marthUPSmash(marth):
    global newMove, marthWaittime, saveMove, marthArea, frame, p1hitDir, dFrame, damage
    if marth[FACERIGHT]==True:
        newMove = US_R
        saveMove = US_R
    else:
        newMove= US_L
        saveMove= US_L
    marthWaittime=12
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
    dFrame=[1]
    damage=10
    p1hitDir="UP"

#################################
#marthTaunt is just a taunt move that doesnt do any damage
# It is merely to mock the opponent and brag.
# This will play a short animation and sound file that the player can only exit by waiting for it to end or by getting hit

def marthTaunt(marth):
    global newmove, marthWaittime, saveMove, marthArea

    mTaunt = mixer.Sound("Taunts/Marth_Taunt2.ogg")
    mixer.Sound.play(mTaunt)
    if marth[FACERIGHT]==True:
        newMove=TAUNT_R
        saveMove=TAUNT_R
    else:
        newMove=TAUNT_L
        saveMove=TAUNT_L
    marthWaittime=36
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)

#################################
#This is marth's forward ariel attack
# It can only be used in the air and has 1 frame of damage
def marthFair(marth):
    global newMove, marthWaittime, saveMove, marthArea, p1hitDir, dFrame
    if marth[FACERIGHT]==True:
        newMove = FAIR_R
        saveMove = FAIR_R
        p1hitDir="RIGHT"
        marth[VX]=10
    else:
        newMove= FAIR_L
        saveMove= FAIR_L
        p1hitDir="LEFT"
        marthLeft(marth,10)
        marth[VX]=-20
    marthWaittime=13
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
    dFrame=[1]
#######################
#This is marth's downward ariel attack
#It can only be used in the air
    
def marthDair(marth):
    global newMove, marthWaittime, saveMove, marthArea, p1hitDir, dFrame, damage

    newMove= DAIR_R  #Marth's dair works in both directions so only one move is needed
    saveMove= DAIR_R
        
    marthWaittime=13
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
    dFrame=[2]
    damage=10
    p1hitDir="DOWN"

##################################
# This is marth's recovery move that shoots him upwards and to the direction he faces
# This is mainly used for going back on stage but can be used as an attack as well
def marthRecovery(marth):
    global newMove, marthWaittime, saveMove, marthArea, p1hitDir, dFrame, damage
    if marth[FACERIGHT]==True:
        newMove = RECOV_R
        saveMove = RECOV_R
        p1hitDir="UR"
        marth[VX]=15
    else:
        newMove = RECOV_L
        saveMove = RECOV_L
        p1hitDir="UL"
        marth[VX]=-15
    marth[VY]=-15
    damage=12
    dFrame = [1,2,3]
    marthWaittime=20
    moveW = marpics[move][int(frame)].get_size()[0]
    moveH = marpics[move][int(frame)].get_size()[1]
    marthArea=Rect(marth[X],marth[Y]-moveH,moveW,moveH)
    marth[VULNERABLE]=True

    

            
#This resets Marth's position on the stage and makes him face to the right
def respawnMarth():
    global marth
    marth[STOCKS]-=1

    if marth[STOCKS]>0:
        marth[X], marth[Y], marth[FACERIGHT], marth[VY], marth[DOUBLEJUMP], marth[PERCENT], marth[VX]=280,150,True,1,True,0, 0
##    else:
##        p2win()
        

#This creates a move for marth by taking the amount of sprites entered by the user and adds it to a 2D list
#We took this from one of Mr. McKenzie's examples
def makeMove(name,start,end):
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move


#This function is the last resort of sonic's moves and draws him standing still facing right or left depending on which way he was facing last
#sonicIdle only works if there are no inputs for sonic from the player
def sonicIdle(sonic):
    global p2newMove, sonicArea
    if sonic[FACERIGHT]==True:
        p2newMove = IDLE_R
    else:
        p2newMove= IDLE_L
    #sonicArea makes a rectangle that becomes sonic's hitbox around his character
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
#This function moves sonic to the right by using getPixel
def sonicRight(sonic,vx):
    global p2newMove, sonicArea
    sonic[FACERIGHT]=True
    if sonic[ONGROUND]==True:
        p2newMove = RIGHT
    for i in range(vx):
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+20,sonic[Y]+15) != GREEN:
            sonic[X] += 1
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)


#This function moves sonic to the left by using getPixel
def sonicLeft(sonic,vx):
    global p2newMove, sonicArea
    sonic[FACERIGHT]=False
    if sonic[ONGROUND]==True:
        p2newMove = LEFT
    
    for i in range(vx):
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+2,sonic[Y]+15) != GREEN:
            sonic[X] -= 1
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)


#This function moves sonic up by using getPixel
def sonicUp(sonic,vy):
    global sonicArea
    for i in range(vy):
        #Checks to see if the pixel above him is green
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+2) != GREEN:
            sonic[Y] -= 1
        else:
            sonic[VY] = 0
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
###########################################################################################################################################################################
#This function moves sonic down by using getPixel
def sonicDown(sonic,vy):
    global sonicArea
    for i in range(vy):
        #checks to see if the pixel under him is green
        if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+28) != GREEN:
            sonic[Y] += 1
        else:
            sonic[VY] = 0
            sonic[ONGROUND] = True
            sonic[DOUBLEJUMP] = True
            sonic[VULNERABLE] = False
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)


def sonicFSmash(sonic):
    global p2newMove, sonicWaittime, p2saveMove, sonicArea, p2dFrame, p2hitDir, damageP2
    if sonic[FACERIGHT]==True:
        p2newMove = FS_R
        p2saveMove = FS_R
        p2hitDir="UR"
    else:
        p2newMove= FS_L
        p2saveMove= FS_L
        p2hitDir="UL"
    p2dFrame=[7,8,9,10]
    damageP2=20
    sonicWaittime=20
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)

def sonicUPSmash(sonic):
    global p2newMove, sonicWaittime, p2saveMove, sonicArea, damage, p2hitDir, p2dFrame, damageP2
    if sonic[FACERIGHT]==True:
        p2newMove = US_R
        p2saveMove = US_R
    else:
        p2newMove= US_L
        p2saveMove= US_L
    
    p2hitDir="UP"
    p2dFrame=[6,7,8]
    sonicWaittime=20
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
    damageP2=14



###############################CHANGED VARIABLES FOR MATTS PROGRAM#########################    

def sonicTaunt(sonic):
    global p2newmove, sonicWaittime, p2saveMove, sonicArea
##    pygame.mixer.music.load("Taunts/MarthTaunt.mp3")       # this is glitching6  #stuff matt included
##    pygame.mixer.music.play()
    sTaunt = mixer.Sound("Taunts/Sonic_Taunt.ogg")
    mixer.Sound.play(sTaunt)
    if sonic[FACERIGHT]==True:
        p2newMove=TAUNT_R
        p2saveMove=TAUNT_R
    else:
        p2newMove=TAUNT_L
        p2saveMove=TAUNT_L
    sonicWaittime=45
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)

def sonicFair(sonic):
    global p2newMove, sonicWaittime, p2saveMove, sonicArea, p2hitDir, p2dFrame, damageP2   #unsure what dFrame is and p2hitDir
    if sonic[FACERIGHT]==True:
        p2newMove = FAIR_R
        p2saveMove = FAIR_R
        p2hitDir="RIGHT"
        sonic[VX]+=10
    else:
        p2newMove= FAIR_L
        p2saveMove= FAIR_L
        p2hitDir="LEFT"
        sonic[VX]-=10
    damageP2=10
    sonicWaittime=15
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
    p2dFrame=[2,3,4,5]


def sonicDair(sonic):
    global p2newMove, sonicWaittime, p2saveMove, sonicArea, p2hitDir, p2dFrame, damageP2

    if sonic[FACERIGHT]==True:
        p2newMove = DAIR_R
        p2saveMove = DAIR_R
        p2hitDir="RIGHT"
    else:
        p2newMove= DAIR_L
        p2saveMove= DAIR_L
        p2hitDir="LEFT"
        
    sonicWaittime=18
    moveW = sonicpics[p2move][int(p2frame)].get_size()[0]
    moveH = sonicpics[p2move][int(p2frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
    p2dFrame=[5,6,7]
    damageP2=10
    p2hitDir="DOWN"



def sonicRecovery(sonic):
    global p2newMove, sonicWaittime, p2saveMove, sonicArea, p2hitDir, p2dFrame, damageP2
    if sonic[FACERIGHT]==True:
        p2newMove = RECOV_L
        p2saveMove = RECOV_L
        p2hitDir="UR"

    else:
        p2newMove = RECOV_R
        p2saveMove = RECOV_R
        p2hitDir="UL"

    sonic[VY]=-15
    damageP2=12
    p2dFrame = [-1]
    sonicWaittime=20
    moveW = sonicpics[p2move][int(frame)].get_size()[0]
    moveH = sonicpics[p2move][int(frame)].get_size()[1]
    sonicArea=Rect(sonic[X],sonic[Y]-moveH,moveW,moveH)
    sonic[VULNERABLE]=True

#same as respawnMarth but for sonic
    
def respawnSonic():
    global sonic
    sonic[STOCKS]-=1

    if sonic[STOCKS]>0:
        sonic[X], sonic[Y], sonic[FACERIGHT], sonic[VY], sonic[DOUBLEJUMP], sonic[PERCENT], sonic[VX]=480,150,True,1,True,0, 0
##    else:
##        p2win()

#same as makeMove but for p2
def makep2Move(name,start,end):
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    p2move = []
    for i in range(start,end+1):
        p2move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return p2move

#This function sets marth the the STUN move and moves him accordingly to sonics attack move
def p1damage(marth):
    global newMove, p2hitDir, p2dFrame, damageP2
    marth[PERCENT]+=damageP2
    p2dFrame=[0]
    if marth[FACERIGHT]==True:
        newMove=STUN_R
        saveMove=STUN_R
    else:
        newMove=STUN_L
        saveMove=STUN_L
    marthWaittime=10
    if p2hitDir=="UR":
        for i in range(marth[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+20,marth[Y]+15) != GREEN:
                marth[VX] = marth[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+2) != GREEN:
                marth[VY] = -marth[PERCENT]//8

            else:
                marth[VY] = 0
    elif p2hitDir=="UL":
        for i in range(marth[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+2,marth[Y]+15) != GREEN:
                marth[VX] = -marth[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+2) != GREEN:
                marth[VY] = -marth[PERCENT]//8

            else:
                marth[VY] = 0
    elif p2hitDir=="UP":
        for i in range(marth[PERCENT]):
            marth[VY] = -marth[PERCENT]//5
    elif p2hitDir=="DOWN":
        for i in range(marth[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+28) != GREEN:
                marth[VY] += marth[PERCENT]//(7+i)
    elif p2hitDir=="LEFT":
         for i in range(marth[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+2,marth[Y]+15) != GREEN:
                marth[VX] = -marth[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+2) != GREEN:
                marth[VY] = -5
    elif p2hitDir=="RIGHT":
        for i in range(marth[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+20,marth[Y]+15) != GREEN:
                marth[VX] = marth[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],marth[X]+15,marth[Y]+2) != GREEN:
                marth[VY] = -5

        

# same as p1damage but for p2
def p2damage(sonic):
    global p2newMove, p1hitDir, damage, dFrame, sonicWaittime
    #dFrame is set back to -1 so that p2 cant get hit multiple times from 1 attack
    dFrame=[-1]
    sonicWaittime=15
    if sonic[FACERIGHT]==True:
        p2newMove=STUN_R
        p2saveMove=STUN_R
    else:
        p2newMove=STUN_L
        p2saveMove=STUN_L
    #sonic[INVIN]=True
    sonic[PERCENT]+=damage
    if p1hitDir=="UR":
        for i in range(sonic[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+20,sonic[Y]+15) != GREEN:
                sonic[VX] = sonic[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+2) != GREEN:
                sonic[VY] = -sonic[PERCENT]//8
##            elif getPixel(maskPic,sonic[X]+15,sonic[Y]+2) = GREEN and getPixel(maskPic,marth[X]+15,marth[Y]+28) != GREEN:
##                sonic[Y] += 1:
            else:
                sonic[VY] = 0
    elif p1hitDir=="UL":
        for i in range(sonic[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+2,sonic[Y]+15) != GREEN:
                sonic[VX] = -sonic[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+2) != GREEN:
                sonic[VY] = -sonic[PERCENT]//8
##            elif getPixel(maskPic,sonic[X]+15,sonic[Y]+2) = GREEN and getPixel(maskPic,marth[X]+15,marth[Y]+28) != GREEN:
##                sonic[Y] += 1:
            else:
                sonic[VY] = 0
    elif p1hitDir=="UP":
        for i in range(sonic[PERCENT]):
            sonic[VY] = -sonic[PERCENT]//5
    elif p1hitDir=="DOWN":
        for i in range(sonic[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+28) != GREEN:
                sonic[VY] = sonic[PERCENT]//(3)
    elif p1hitDir=="LEFT":
         for i in range(sonic[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+2,sonic[Y]+15) != GREEN:
                sonic[VX] = -sonic[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+2) != GREEN:
                sonic[VY] = -5
    elif p1hitDir=="RIGHT":
        for i in range(sonic[PERCENT]):
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+20,sonic[Y]+15) != GREEN:
                sonic[VX] = sonic[PERCENT]//5
            if getPixel([maskPic1_trans, maskPic2, maskPic3_trans][currentLevel],sonic[X]+15,sonic[Y]+2) != GREEN:
                sonic[VY] = -5
                
    #sonic[INVIN]=False
            



# This function tracks the pixel on the mask on the specific x and y specified and returns its RGB value
def getPixel(mask,x,y):
    if 0<= x < mask.get_width() and 0 <= y < mask.get_height():
        return mask.get_at((int(x),int(y)))[:3]
    else:
        return (-1,-1,-1)

# This function draws the damage level of both characters
def percent():
    if marth[PERCENT] <=50:
        screen.blit(lowpic, (200,450))
    elif marth[PERCENT] < 120 and marth[PERCENT] > 50:
        screen.blit(mediumpic, (200,450))
    elif marth[PERCENT] >= 120:
        screen.blit(highpic, (200,450))

    if sonic[PERCENT] <=50:
        screen.blit(lowpic, (400,450))
    elif sonic[PERCENT] < 120 and sonic[PERCENT] > 50:
        screen.blit(mediumpic, (400,450))
    elif sonic[PERCENT] >= 120:
        screen.blit(highpic, (400,450))

# this function draws all the images on screen and without it all the images lag
def drawScene():
    screen.fill((200,222,255))
    screen.blit(marthlogo, (200,400))
    screen.blit(soniclogo, (400,400))
    screen.blit(backPic, (0,0))
    percent()
    #Draws the picture based on the move given and the current frame
    pic = marpics[move][int(frame)]
    screen.blit(pic,(marth[X]-pic.get_width()//2,marth[Y]-pic.get_height()//2))

    #Draws the picture based on the p2move given and the current p2frame
    p2pic = sonicpics[p2move][int( p2frame)]
    screen.blit(p2pic,(sonic[X]-p2pic.get_width()//2,sonic[Y]-p2pic.get_height()//2))

    display.flip()
###################################################################################
#Draws all the images on screen for the first stage
def drawScene1():
    screen.fill((200,222,255))
    
    screen.blit(backPic1_trans, (0,0))
    screen.blit(marthlogo, (200,400))
    screen.blit(soniclogo, (400,400))
    percent()
    #Draws the picture based on the move given and the current frame
    pic = marpics[move][int(frame)]
    screen.blit(pic,(marth[X]-pic.get_width()//2,marth[Y]-pic.get_height()//2))

    #Draws the picture based on the p2move given and the current p2frame
    p2pic = sonicpics[p2move][int( p2frame)]
    screen.blit(p2pic,(sonic[X]-p2pic.get_width()//2,sonic[Y]-p2pic.get_height()//2))
         
    display.flip()

###########################
    #Draws all the images on screen for the second stage
def drawScene2():
    screen.fill((200,222,255))
    screen.blit(overlay_for_backpic_trans, (0,0))
    screen.blit(backPic2, (0,0))
    screen.blit(marthlogo, (200,400))
    screen.blit(soniclogo, (400,400))
    percent()
    #Draws the picture based on the move given and the current frame
    pic = marpics[move][int(frame)]
    screen.blit(pic,(marth[X]-pic.get_width()//2,marth[Y]-pic.get_height()//2))

    #Draws the picture based on the p2move given and the current p2frame
    p2pic = sonicpics[p2move][int( p2frame)]
    screen.blit(p2pic,(sonic[X]-p2pic.get_width()//2,sonic[Y]-p2pic.get_height()//2))
 
    display.flip()
#########################
    #Draws all the images on screen for the third stage
def drawScene3():
    screen.fill((200,222,255))
    screen.blit(backPic3_trans, (0,0))
    screen.blit(marthlogo, (200,400))
    screen.blit(soniclogo, (400,400))
    percent()
    #Draws the picture based on the move given and the current frame
    pic = marpics[move][int(frame)]
    screen.blit(pic,(marth[X]-pic.get_width()//2,marth[Y]-pic.get_height()//2))

    #Draws the picture based on the p2move given and the current p2frame
    p2pic = sonicpics[p2move][int( p2frame)]
    screen.blit(p2pic,(sonic[X]-p2pic.get_width()//2,sonic[Y]-p2pic.get_height()//2))
 
    display.flip()

#######################################################################################


#This resets all the values for sonic and marth
def reset():
    global marthWaittime, dFrame, p1hitDir, damage, sonicWaittime, p2dFrame, p2hitDir, damageP2, sonic, marth
    #This function resets marth and sonic to their default values to reset the game
    marth=[marthX,marthY,0,0,True,True,True,0,4,False]
    marthWaittime=0
    dFrame = [] #it is at -1 at the start because originally he has no damage frame and this changes when he attacks
    p1hitDir="NA"
    damage=0
    #Sonic's Aspects
    sonicX, sonicY = 500,200
    sonic=[sonicX,sonicY,0,0,True,False,True,0,4,False]
    sonicWaittime=0
    p2dFrame=[]
    p2hitDir="NA"
    damageP2=0

####################

    
#Marth's aspects
marthX, marthY = 300,200
X=0
Y=1
VY=2
VX=3
ONGROUND=4
FACERIGHT=5
DOUBLEJUMP=6
PERCENT=7
STOCKS=8
VULNERABLE=9
marth=[marthX,marthY,0,0,True,True,True,0,4,False]
marthWaittime=0
dFrame = [] 
p1hitDir="NA" # No hit direction as no moves were used yet
damage=0
#Sonic's Aspects
sonicX, sonicY = 500,200
sonic=[sonicX,sonicY,0,0,True,False,True,0,4,False]
sonicWaittime=0
p2dFrame=[]
p2hitDir="NA"
damageP2=0

# Making a variable for green for when we call getPixel
GREEN = (0,255,0)




LEFT = 0 # These are just the indicies of the moves
RIGHT = 1
IDLE_L = 2
IDLE_R = 3
AIR_L = 4
AIR_R = 5
FS_L = 6 #FS_L reps forward smash left and US_R reps up smash right, etc. 
FS_R = 7
US_L = 8
US_R = 9
TAUNT_L = 10
TAUNT_R = 11
FAIR_R = 12
FAIR_L = 13
DAIR_R = 14
DAIR_L = 15
RECOV_L = 16
RECOV_R = 17
STUN_R = 18
STUN_L = 19
newMove=IDLE_R # Sets the first move to him being idle facing the right


#All the pictures for Marth's moves are loaded into the  2D list marpics
marpics = []
marpics.append(makeMove("Mar_Run",1,7))      # LEFT
marpics.append(makeMove("Mar_Run",8,13))     # RIGHT
marpics.append(makeMove("Mar_Stand",1,8))    # Idle_L
marpics.append(makeMove("Mar_Stand",9,16))   # Idle_R
marpics.append(makeMove("Mar_Air",1,3))   # Air_L
marpics.append(makeMove("Mar_Air",4,6))   # Air_R
marpics.append(makeMove("Mar_Fsmash",0,3))   # Left Smash
marpics.append(makeMove("Mar_Fsmash",4,7))   # Right Smash
marpics.append(makeMove("Mar_Usmash",1,4))   # Left Up Smash
marpics.append(makeMove("Mar_Usmash",5,8))   # Right Up Smash
marpics.append(makeMove("Mar_Taunt",1,11))   # Left Taunt
marpics.append(makeMove("Mar_Taunt",12,22))  # Right Taunt
marpics.append(makeMove("Mar_Fair",1,5))   # Foward Air Right
marpics.append(makeMove("Mar_Fair",6,10))   # Forward Air Left
marpics.append(makeMove("Mar_Dair",1,4))   # Down air
marpics.append(makeMove("Mar_Dair",1,4))   # Down air
marpics.append(makeMove("Mar_Recov",1,7)) # Left Recovery
marpics.append(makeMove("Mar_Recov",8,14)) # Right Recovery
marpics.append(makeMove("Mar_Stun",1,2)) # Stun Frame Right
marpics.append(makeMove("Mar_Stun",3,4)) # Stun Frame Left
marpics.append



frame=0     # current frame within the move
move=0      # current move being performed


#All the pictures for Sonic's moves are loaded into the 2D list sonicpics
sonicpics = []
sonicpics.append(makep2Move("Sonic_Walk_Left",1,8))             # LEFT
sonicpics.append(makep2Move("Sonic_Walk",1,8))                  # RIGHT
sonicpics.append(makep2Move("Sonic_Idle_Left",1,12))            # Idle_L
sonicpics.append(makep2Move("Sonic_Idle_Right",1,12))           # Idle_R
sonicpics.append(makep2Move("Sonic_Jump_Left",1,14))            # Air_L
sonicpics.append(makep2Move("Sonic_Jump",1,14))                 # Jump_R
sonicpics.append(makep2Move("Sonic_ForwardSmash_Left",1,13))    # Left Smash
sonicpics.append(makep2Move("Sonic_ForwardSmash",1,13))         # Right Smash
sonicpics.append(makep2Move("Sonic_UpSmash_Left",2,12))         # Left Up Smash
sonicpics.append(makep2Move("Sonic_UpSmash",2,12))              # Right Up Smash
sonicpics.append(makep2Move("Sonic_Taunt_Left",1,10))           # Left Taunt
sonicpics.append(makep2Move("Sonic_Taunt",1,10))                # Right Taunt
sonicpics.append(makep2Move("Sonic_ForwardAireal", 1, 10))      #Sonic Forward Aireal Left
sonicpics.append(makep2Move("Sonic_ForwardAireal_Left", 1, 10)) #Sonic Forward Aireal Left
sonicpics.append(makep2Move("Sonic_DairLeft", 1, 8))#Sonic Downward Aireal Left
sonicpics.append(makep2Move("Sonic_Dair", 1, 8))     #Sonic Downward Aireal 
sonicpics.append(makep2Move("Sonic_Recovery", 1, 8))     #Sonic Recovery Left
sonicpics.append(makep2Move("Sonic_Recovery", 9, 16))     #Sonic Recovery Right
sonicpics.append(makep2Move("Sonic_Stun", 1, 2))     #Sonic Stun Left
sonicpics.append(makep2Move("Sonic_Stun", 3, 4))     #Sonic Stun Right



sonicpics.append

p2frame=0     # current p2frame within the move
p2move=0      # current move being performed

#This is for the frame rate
myClock= time.Clock()
running = True

#This is the function that is loaded for the first stage and calls drawscene1 for all the images
#The only things it does by itself is reduce the Waittime for both characters, load the music and
#checks to see if the game has ended. It exits if the player presses escape
def play1():
    global move, marthWaittime, sonicWaittime

    running = True
    mixer.music.load("Music/Dreamland.ogg")
    mixer.music.play(-1)
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        keys = key.get_pressed()
        if keys[27]:running = False
        
        if marthWaittime!=0:
            marthWaittime-=1


        if sonicWaittime!=0:
            sonicWaittime-=1
        moveMarth()
        moveSonic()
        drawScene1()

        if marth[STOCKS] < 1:
            running = False
            p2wins()
        elif sonic[STOCKS] < 1:
            running = False
            p1wins()

##        if sonicWaittime!=0:
##            sonicWaittime-=1

        myClock.tick(30)
        display.flip()
    return 'menu'
##############################
#This is the function that is loaded for the second stage and calls drawscene1 for all the images
#The only things it does by itself is reduce the Waittime for both characters, load the music and
#checks to see if the game has ended.
def play2():
    global move, marthWaittime, sonicWaittime

    mixer.music.load("Music/FD Music.ogg")
    mixer.music.play(-1)

    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        keys = key.get_pressed()
        if keys[27]:running = False
        if marthWaittime!=0:
            marthWaittime-=1

        if sonicWaittime!=0:
            sonicWaittime-=1
        moveMarth()
        moveSonic()
        drawScene2()

        if marth[STOCKS] < 1:
            running = False
            p2wins()
        elif sonic[STOCKS] < 1:
            running = False
            p1wins()
       

##        if sonicWaittime!=0:
##            sonicWaittime-=1 
        myClock.tick(30)
        display.flip()
    return 'menu'
##################
#This is the function that is loaded for the third stage and calls drawscene1 for all the images
#The only things it does by itself is reduce the Waittime for both characters, load the music and
#checks to see if the game has ended.
def play3():
    global move, marthWaittime, sonicWaittime

    mixer.music.load("Music/Green Greens.ogg")
    mixer.music.play(-1)

    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        keys = key.get_pressed()
        if keys[27]:running = False
        if marthWaittime!=0:
            marthWaittime-=1

        if sonicWaittime!=0:
            sonicWaittime-=1
        moveMarth()
        moveSonic()
        drawScene3()

        if marth[STOCKS] < 1:
            running = False
            p2wins()
        elif sonic[STOCKS] < 1:
            running = False
            p1wins()       

##        if sonicWaittime!=0:
##            sonicWaittime-=1 
        myClock.tick(30)
        display.flip()
    return 'menu'
    
frame=0     # current frame within the move
move=0      # current move being performed
        
myClock = time.Clock()
###############################################################################################

############################functions for when Marth or Sonic wins the match####################

#This is the function that runs if Marth wins
#It loads and blits the winning background for marth and plays marth's winning taunt
def p1wins():
    running = True
    p1wins_image = image.load("Back Pics/MarthWins.png")
    p1wins_image = transform.smoothscale(p1wins_image, screen.get_size())
    screen.blit(p1wins_image,(0,0))
    mixer.music.load("Taunts/Marth_Win.ogg")
    mixer.music.play()
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        

        display.flip()
    return "menu"

#######################
#This is the function that runs if Sonic wins
#It loads and blits the winning background for marth and plays Sonic's winning taunt
def p2wins():
    running = True
    p2wins_image = image.load("Back Pics/SonicWins.png")
    p2wins_image = transform.smoothscale(p2wins_image, screen.get_size())
    screen.blit(p2wins_image,(0,0))
    mixer.music.load("Taunts/Sonic_Win.ogg")
    mixer.music.play()
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        

        display.flip()
    return "menu"
    
###################################################################################


################################################################################################
white = (255,255,255)    #colour variables
red = (255,0,0)
yellow= (255,255,0)
purple= (128, 128, 255)
orange= (255, 128,0)
blue= (0,0,255)
################################################################################################

#creating rectangles for the buttons on the menu screeen 
####################################
playRect= Rect(174, 333, 200, 38)
instructionsRect= Rect(160, 377, 230, 45)
storyRect= Rect(174, 433, 195, 47)
creditsRect= Rect(167, 488, 215, 38)
####################################


        
myClock = time.Clock()


####################################Functions for menu page################################################################

#this is the function that loads and blits the instuction screen so that users can learn how to play the game
def instructions():
    running = True
    loadingscreen= image.load ("Back Pics/loading screen.png")
    loadingscreen= transform.smoothscale(loadingscreen, screen.get_size())
    screen.blit(loadingscreen, (0,0))
    display.flip()
    time.wait(4000)
    inst = image.load("Back Pics/instructions.png")
    inst = transform.smoothscale(inst, screen.get_size())
    screen.blit(inst,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"



#This function loads and blits the story image users can look at and read
def story():
    loadingscreen= image.load ("Back Pics/loading screen.png")
    loadingscreen= transform.smoothscale(loadingscreen, screen.get_size())
    screen.blit(loadingscreen, (0,0))
    display.flip()
    time.wait(4000)
    running = True
    story = image.load("Back Pics/Story_Com_sci.png")
    story = transform.smoothscale(story, screen.get_size())
    screen.blit(story,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"



#This function loads and blits the credit image users can read to see see who made this       
def credit():
    loadingscreen2= image.load ("Back Pics/loadingscreen2.png")
    loadingscreen2= transform.smoothscale(loadingscreen2, (800, 600))
    screen.blit(loadingscreen2, (0,0))
    display.flip()
    time.wait(4000)
    running = True
    cred = image.load("Back Pics/credits page.png")
    cred = transform.smoothscale(cred, screen.get_size())
    screen.blit(cred,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"


#This function loads and blits the stage selection screen for users to pick where they want to play
#After users pick a stage it redirects them to play1, play2 or play3
def background():
    global background1_selected_trans, background2_selected_trans, background3_selected_trans, currentLevel, sonic, marth
    running = True
    
    reset() # This will reset the characters back to their orignial values
    
    characterscreen= image.load ("Back Pics/MarthVsSonic.png")
    characterscreen= transform.smoothscale(characterscreen, screen.get_size())
    screen.blit(characterscreen, (0,0))
    display.flip()
    time.wait(4000)
    overlay = image.load ("Back Pics/destination_background2.png")
    overlay = transform.smoothscale(overlay, screen.get_size())
    screen.blit(overlay, (0,0))
    destination1= image.load("Back Pics/battlefield_small.png")
    destination1= transform.smoothscale(destination1, (200,150))
    screen.blit(destination1, (80,175))
    destination2= image.load("Back Pics/final destination background small.png")
    destination2= transform.smoothscale(destination2, (200,150))
    screen.blit(destination2, (520,175))
    destination3= image.load("Back Pics/town and city small.png")
    destination3= transform.smoothscale(destination3, (200,150))
    screen.blit(destination3, (300,375))
##############################################################################################################

    #Creating rectangles for the setting buttons on the play page 
    #############################################################
    background1Rect= Rect(80, 175, 200, 150)
    background2Rect= Rect(520, 175, 200, 150)
    background3Rect= Rect(300, 375, 200, 150)
    #############################################################


    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False



        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.blit(destination1, (80,175))
        screen.blit(destination2, (520,175))
        screen.blit(destination3, (300,375))

        if background1Rect.collidepoint(mpos):
            screen.blit(background1_selected_trans,(80,175))
            if mb[0]==1:
                currentLevel = 0
                return "play1"


        if background2Rect.collidepoint(mpos):
            screen.blit(background2_selected_trans,(520,175))
            if mb[0]==1:
                currentLevel = 1
                return "play2"

        if background3Rect.collidepoint(mpos):
            screen.blit(background3_selected_trans,(300,375))
            if mb[0]==1:
                currentLevel = 2
                return "play3"


        display.flip()
    return "menu"

#this is the function that loads and blits the images for the menu sceen as well as lets the user pick where they want to go (stage selection, credits, story or instructions)

def menu():
    global move, background1_selected_trans, background2_selected_trans, background3_selected_trans

    #Menu Music
    mixer.music.load("Music/Menu Music.ogg")
    mixer.music.play(-1)
    
    menupic = image.load("Back Pics/Smash It.png")
    #menupic_trans = transform.scale(menupic,(800,600))
    menupic_trans = transform.smoothscale(menupic, screen.get_size())

#######################################################################################################################
    

    #####################BUTTONS##########################################
    button1= image.load("Back Pics/Play_button.png")
    button2= image.load("Back Pics/Instructions_button.png")
    button3= image.load("Back Pics/Story_button.png")
    button4= image.load("Back Pics/Credits_button.png")

    button1_trans= transform.smoothscale(button1, (250,70))
    button2_trans= transform.smoothscale(button2, (250,70))
    button3_trans= transform.smoothscale(button3, (250,70))
    button4_trans= transform.smoothscale(button4, (250,70))

    button1_selected= image.load("Back Pics/Play_selected.png")
    button2_selected= image.load("Back Pics/Instructions_selected.png")
    button3_selected= image.load("Back Pics/Story_selected.png")
    button4_selected= image.load("Back Pics/Credits_selected.png")

    button1_selected_trans= transform.smoothscale(button1_selected, (284,70))
    button2_selected_trans= transform.smoothscale(button2_selected, (250,70))
    button3_selected_trans= transform.smoothscale(button3_selected, (282,70))
    button4_selected_trans= transform.smoothscale(button4_selected, (250,70))
    ###########################################################################
    
    ###########################################################################
    #destination options on the setting page
    #loading all selected images for this page
    background1_selected= image.load("Back Pics/battlefield_small_selected.png")
    background1_selected_trans= transform.smoothscale(background1_selected, (200,150))
    background2_selected= image.load("Back Pics/final destination background small selected.png")
    background2_selected_trans= transform.smoothscale(background2_selected, (200,150))
    background3_selected= image.load("Back Pics/town and city small selected.png")
    background3_selected_trans= transform.smoothscale(background3_selected, (200,150))
    ##################################################################################

    
    
    running=True
    while running:
        for e in event.get():
            if e.type==QUIT:
              return "exit"
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(menupic_trans,(0,0))


        #####################################    
        screen.blit(button1_trans,(150, 320))    #blitting on the buttons on the menu page
        screen.blit(button2_trans,(150,365))
        screen.blit(button3_trans,(150,430))
        screen.blit(button4_trans,(150,475))
        ####################################

###############################################################################################################
      
        if playRect.collidepoint(mpos):                     #recognizes when you mouse goes over the play button
            screen.blit(button1_selected_trans,(145,312))   #blits the selected image 
            if mb[0]== 1:                                   #recongizes when you click play button                            
                return "background"                         
               

        if instructionsRect.collidepoint(mpos):             
            screen.blit(button2_selected_trans,(145,362))
            if mb[0]==1:
                return "instructions"


        if storyRect.collidepoint(mpos):
            screen.blit(button3_selected_trans,(144,420))
            if mb[0]==1:
                return "story"


        if creditsRect.collidepoint(mpos):
            screen.blit(button4_selected_trans,(146,477))
            if mb[0]==1:
                return "credits"


            
        display.flip()
    return 'menu'

#############################################################################################################

screen = display.set_mode((800, 600))   #from Mr. McKenzie's menu example 
running = True
x,y = 0,0
OUTLINE = (150,50,30)
#This redirects the program to the function that will show which screen they are on
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "background":
        page= background()
    if page == "play1":
        page = play1()
    if page == "play2":
        page = play2()
    if page == "play3":
        page = play3()  
    if page == "instructions":
        page = instructions()    
    if page == "story":
        page = story()    
    if page == "credits":
        page = credit()

        


quit()
