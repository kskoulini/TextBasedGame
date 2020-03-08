import time
import random


"""INITIALIZATION OF REQUIRED VARIABLES"""
room=1
locked1=True
chest1=['golden sword','torch','bronze key']
inventory = list()
key1=True
complete=0
a=['yes','YES','Yes','Y','y']
b=['No','NO','no','N','n']

"""END OF INITIALIZATION"""



"""ALL REQUIRED FUNCTION DEFINITIONS"""
def game():
    global complete
    time.sleep(1)
    print('you enter a dark room and you can only find a gun on the floor')
    choice=input('do you take it? [Yes/No]: ').lower()
    if choice in a:
        print('you have taken the gun')
        time.sleep(1)
        gun = 1
    else:
        print('you did not take the gun')
        gun = 0
    print('as you proceed further in the room you see a  figure moving')
    choice=str(input('do u approach the object? [Y/N]: '))
    if choice in a:
            print('you approach the object.....')
            time.sleep(1)
            print('as you go closer you begin to find the object as a creepy human ')
            time.sleep(1)
            print('the human is a zombie...')
            choice=str(input('do u try to fight it?[Y/N]: '))

            if choice in ['y','yes','Y','YES']:
                    if gun==1:
                        print('you only have a gun to fight against it')
                        time.sleep(2)
                        print('-----------------')
                        print('you must shoot its head to kill the zombie')
                        print('if the zombie bites you more than 4 times,you will be infected and turn into a zombie')
                        print('------------------')
                        time.sleep(2)
                        user=(random.choice(b))
                        bite=0
                        choice=input("type 'shoot' to shoot at the zombie: ")
                        if 'shoot' in choice:
                            while 'shoot' in choice:
                                print('you shot at the',user,'of the zombie')
                                if user=='head':
                                    complete=1
                                    return complete
                                else:
                                    print('you missed it...zombie bites you')
                                    choice=input("Enter 'shoot' to try again or 'stop' to stop: ")
                                    user=(random.choice(b))
                                    bite=bite+1
                                    if bite==3:
                                        print("you havent done enough damage to the zombie. You've been bitten more than four time but have managed to escape")
                                        complete=-1
                                        return complete
                        else:
                            print('invalid input')
                                
                    else:
                        print('you dont have any weapon to fight it...and hence')
                        time.sleep(2)
            elif choice in b:
                print('you chose not to fight the zombie')
                time.sleep(1)
                print('as you turn away the zombie attacks you')
                complete=1
                return complete
            else:
                print('invalid input')
    else:
        print('you turn away from the object and try to go out but something wont let you....')
        time.sleep(2)
        print('the object u saw is a zombie....n since u chose not to fight it..')
        complete=True
        return complete
    
def invent():
    #Function to print the list of item in inventory
    #Can be used in any room
    global inventory
    if inventory:
        print("your inventory contains: ")
        for i in inventory:
            print (i)
    else:
        print("your inventory is empty")
        
def steps():#to obtain the no. of steps. 
    global n
    while True: 
       n = input("Enter the number of steps: ")
       if n.isdigit():
           n=int(n)
           break
       else:
           print("invalid input, please enter a number")
    
def step_forward():
    #function to step forward
    #can be used in any room 
    global x
    global y
    global n
    if angle==0 or abs(angle)==360:
        if y+n > 5:
            print("you will hit a wall, cannot take",n,"steps forward")
        else:
            y=y+n
            print("you have taken",n,"steps forward")
    elif abs(angle)==180:
        if y-n<-5:
            print("you will hit a wall, cannot take",n,"steps forward")
        else:
            y=y-n
            print("you have taken",n,"steps forward")
    elif angle==90 or angle==-270:
        if x+n>5:
            print("you will hit a wall, cannot take",n,"steps forward")
        else:
            x=x+n
            print("you have taken",n,"steps forward")
    else:
        if x-n<-5:
            print("you will hit a wall, cannot take",n,"steps forward")
        else:
            x=x-n
            print("you have taken",n,"steps forward")
    print("x=",x,"y=",y,'angle=',angle)
    
def step_backward():
   #Function to step backward
   #can be used in any room
   
   #while True: # loop to make if player enter a number
       #n = input("Enter the number of steps: ")
       #if n.isdigit():
           #n=int(n)
           #break
       #else:
           #print("invalid input, please enter a number")
   global n
   global x
   global y
   
   if angle==0:
       if y-n<-5:
           print("you will hit a wall wall, cannot take",n,"steps backward")
       else:
           y=y-n
           print("you have taken",n,"steps backward")
   elif angle==90 or angle == -270:
       if x-n<-5:
           print("you will hit a wall, cannot take",n,"steps forward")
       else:
           x=x-n
           print("you have taken",n,"steps forward")
   elif abs(angle)==180:
       if y+n>5:
           print("you will hit a wall,cannot take",n,"steps forward")
       else:
           y=y+n
           print("you have taken",n,"steps forward")
   else:
       if x+n>5:
           print("you will hit a wall, cannot take",n,"steps forward")
       else:
           x=x+n
           print("you have taken",n,"steps forward")
   print("x=",x,"y=",y,'angle=',angle)
        
def turn():
    #Function to turn left or right
    #can be used in any room
    global angle
    d = input("left or right? :").lower()
    if d =='left':
        angle=angle-90
        print("you have turned to the left")
    elif d =='right':
        angle=angle+90
        print("you have turned to the right")
    else:
        print("invalid input, please enter 'right' or 'left'")
    if abs(angle)==360:
        angle=0
    print("your angle is: ",angle)

"""END OF FUNCTION DEFINITIONS"""      


print("Welcome to our text-based adventure game in which you as a player will be allowed to move through rooms and access its objects as you please.",
      "The challenge that must be completed to win the game will be disclosed in-game. We will guide you through each phase of the game. Best of luck!! thank you for choosing our game")
input("Press enter to continue...")


#Rules of the game
print("-----------------------------")
print("following are the rules of the game:","\n\t1.At any point in the game the user may choose to 'turn'/'step forward'/'step backword' \nby typing in the same")
time.sleep(3)
print("\n\t2.The player will have to move around the room and walk to the various elements in the room to access them.")
time.sleep(3)
print("\n\t3.Once the player is close enough to access an element they will be provided with options to help the game proceed")
time.sleep(3)
print("\n\t4.The players current position will be described after each step. The player will be notified when they cannot step forward or backwards as they have hit a wall")
time.sleep(3)
print("\n\t5. The player cannot see what is behind him or her and hence will not be provided with a description of the same. They will have to turn around in order look behind them by entering 'turn'")
time.sleep(3)
print("\n\t6.You can enter 'look' at any point in the game to recieve a description of your current location")
time.sleep(3)
print("\n\t7.You can enter'end game' at any point in the game to exit.")
print("--------------------")




#Ask to start game
while True:
    play=input("Would you like to play this game? yes/no: ")
    if play.lower()=='yes':
        play=True
        break
    elif play.lower()=='no':
        play=False
        print("We will miss you <3 ")
        break
    else:
        print("invalid input, please enter 'yes' or 'no' ")
    
#Game code    
while play: #Main loop
    
    
    if room == 1:  #Room 1 into
        x = 0
        y = 0
        angle = 0
        print("\nyou are in a small, dank, dimly lit room whose only source of illumination is a small candle." )
        print("You are facing an emtpy wall infront of which is placed a table with the candle on top, 5 steps ahead of you.\n You can make out the silhouette of a door 5 steps to your right and a chest 5 steps to your left.\n you cannot see what is behind you")
       
        while room==1:  #room1 loop
            
            #choice outputs
            choice=input("what will you do? :").lower()
            if 'look' in choice:
                if angle==0 or abs(angle)==360:
                    print("You are facing an emtpy an empty wall infront of which is placed a table with the candle on top. You are",5-y,"steps away from the empty wall.","\n There is a door",5-x,"steps to your right and a chest",5+x,"steps to your left.\n you cannot see what is behind you")
                elif angle==90 or angle==-270:
                    print("You are facing a door. The door is",5-x,"steps away from you. There is wall covered in photoframes",5+y,"steps to your right and an empty wall infront of which is a table and a candle on top,",5-y,"steps to your left. You cannot see what is behind you")
                elif abs(angle)==180:
                    if y==-5:
                        print("you stand infront of the photoframed covered wall. You realise each frame holds not only a picture but a memory of love. You do not know these people or this love of theirs means nothing to you, yet it warms your heart")
                    print("You are facing the wall covered in photoframes but you're too far away to make out what they hold. you are",5+y,"steps away from the wall. There is a door",5-x,"to your left. There is a chest",5+x,"steps to your right. You cannot see what is behind you")
                else:
                    print("you are facing a chest. The chest is",5+x,"steps away from you. There is an empty wall with a table holding a candle infront of it",5-y,"steps to you right and a photoframe covered wall",5+y,"steps to your left. you cannot see what is behind you")
            elif 'turn' in choice:
                turn()
            elif 'forward' in choice or 'front' in choice:
                steps()
                step_forward()
            elif 'back' in choice:
                steps()
                step_backward()
            elif choice=='\n':
                pass
            elif 'exit'in choice or 'end' in choice:
                room=-1
                print("you have exited the game")
                break
            elif 'inventory' in choice:
                invent()
            else:
                print("Invalid input")
                
            ##Element access loops##
            
            #chest access loop
            while (angle==-90 or angle==270) and x==-5 and y==0: 
                choice=input("You can now access the chest infront of you, what will you do? ").lower()
                #output for basic inputs
                if 'forward' in choice or 'front' in choice:
                    steps()
                    step_forward()
                elif 'back' in choice:
                    steps()
                    step_backward()
                    if x>-5:
                        print("you have stepped away from the chest and cannot access it")
                elif 'turn' in choice:
                    turn()
                    if angle!=-90 and angle!=270:
                        print("you have turned away from the chest and cannot access it")
                elif 'exit' in choice or 'end' in choice:
                    room=-1
                    break
                elif 'inventory' in choice:
                    invent()
                    
                #output for chest access     
                if locked1:
                    if 'open' in choice:
                        print("The chest is locked")
                else:
                    
                    if 'open' in choice:
                        print("you have opened the chest using the small key. Awesome!")
                        if chest1:
                            print("Inside the chest you find",chest1)
                        else:
                            print("The chest is empty")
                    if 'take':
                        if 'sword' in choice:
                            if 'golden sword' in chest1:
                                chest1.remove('golden sword')
                                inventory.append('golden sword')
                                print("the golden sword has been added to inventory")
                                print("you can look at the items in the inventory by typing 'inventory'")
                            else:
                                print("you have already taken the sword")
                        elif 'torch' in choice:
                            if 'torch' in chest1:
                                chest1.remove('torch')
                                inventory.append('torch')
                                print("the torch has been added to inventory")
                            else:
                                print("already taken torch")
                        elif 'key' in choice:
                            if 'bronze key' in chest1:
                                chest1.remove('bronze key')
                                inventory.append('bronze key')
                                print("Bronze key has been added to inventory")
                            else:
                                print("already taken bronze key")
                        elif 'look' in choice:
                            print("You are standing infront of a large wooden chest. The chest does not seem to have anything special to it")
                        elif 'close' in choice:
                            print("The chest is now closed")
                    else:
                        print("invalid input")
            
            #room 2 Door acess loop
            while (angle==90 or angle==-270) and x==5 and y==0: 
                choice=input("You are facing the door, what would you like to do?").lower()
                #Output for basic inputs
                if 'back'in choice:
                    steps()
                    step_backward()
                    if x<5:
                        print("You have stepped away from the door and cannot access it")
                elif 'forward' in choice or 'front' in choice:
                    steps()
                    step_forward()
                elif 'turn' in choice:
                    turn()
                    if angle!=90 and angle!=-270:
                        print("you have turned away from the door and cannot access it")
                elif 'inventory' in choice:
                    invent()
                elif 'look' in choice:
                    print("you are standing infront of a wooden door. The door has a borze handle")
                elif 'open' in choice:
                    room=2
                    print("you open the door and step out of the room")
                    break
                elif 'exit' in choice or 'end' in choice:
                    room=-1
                    print("you have exited the game")
            
            #Candle access loop
            while angle==0 and y==5 and x==0:
                print("\nYou are standing infront of the table with candle atop. ")
                choice=input("What will you do? :").lower()
                if 'look' in choice:
                    print("\n In the dim illuminiscence of the candle you find an evelope placed on the table")
                    print("\n Hint: in order to take an item please type 'take <item name>'...\nyou can take the envolope by entering 'take envolope\n")
                elif 'back' in choice:
                    steps()
                    step_backward()
                    if y<5:
                        print("you have stepped away from the table and cannot access it")
                elif 'forward' in choice or 'front' in choice:
                    steps()
                    step_forward()
                elif 'exit' in choice or 'end' in choice:
                    room=-1
                    break
                elif 'turn' in choice:
                    turn()
                elif 'inventory' in choice:
                    invent()
                elif ('take' in choice or 'open' in choice or 'read' in choice) and 'envolope' in choice:
                    print("Inside the envolope is a letter that reads.....\n---you have been trapped here and the only way for you to get out is by outwitting your kidnapper and moving through each room---")
                    if key1:
                        print("you find a key inside")
                elif 'take' in choice and 'key' in choice:
                    if key1:
                        key1=False
                        locked1 = False
                        inventory.append("small key")
                        print("Small key has been added to your inventory")
                    else:
                        print("small key already taken")
                else:
                    print("Invalid input")
            
    if room==2:
        x=0
        y=0
        angle=0
        torch=False
        door1='locked'
        print("you have successfully crossed the first room\ncongratulations\n")
        time.sleep(2)
        print("You find yourself in another small rool, in order to proceed you must find the key that unlocks the door to the next room\nbut that is not going tobe so easy as you have many hurdles\n")
        time.sleep(2)
        print("hope you remember all the rules of the game\n ......................ALL THE BEST")
        while room==2:  
            while not torch:
                
                choice=input("what are you going to do? :")
                if 'look' in choice:
                    print("you are currently standing in the middle of the dark room, there is no source of light in the room so you cant see anything in the room")
                    print("hint: first make sure to get a source of light, remember that you have an inventory")
                    #print("you cant see anything")
                if 'step forward' in choice:
                    steps()
                    if ((angle==0 or angle==360) and y==3 and x==0) or ((angle==-90 or angle == 270) and y==4 and x==-2) or ((angle==90 or angle==270) and y==4 and x==2):
                        if y+n>3:
                            print("you cant take more than 3 steps here as you have hit something")
                    else:
                        step_forward()
                if 'step backward' in choice:
                    steps()
                    step_backward()
                if 'turn' in choice:
                    turn()
                if 'inventory' in choice:
                   invent()
                   print("to take something from the inventory enter 'take <item name>'")
                if 'take' in choice:
                    if choice[5:] in inventory:
                        print("you have taken the",choice[5:])
                        if 'torch' in choice:
                            torch=True
                            print("you take the torch and turn it on, you are now able to look around the room")
                    else:
                        print("you dont have that in your inventory")
            while torch and room==2:
                choice = input('what do you want to do?').lower()
                if 'look' in choice:
                    if angle==0 or abs(angle)==360:
                        print("You are standing in the most beautiful room you have ever seen,\ninfront of you is a round beautifully carved wooden table",3-y,"steps ahead of you with a few things on it")
                        print(5-x<"steps to your right is a well suspecious looking sofa and a paint of the monalisa on the wall behind it")
                        print(5+x,"steps to your left is an another door which is larger than the one in front of you , an odd clock hanging on the wall and a chair beside it")
                        print("you cant see what is behind you\n")
                    if angle==90 or abs(angle)==270:
                        print("you are facing a suspecious well furnished sofa with a painting on the wall behind it, it is",5-x,"ahead of you")
                        print(3-y,'steps to your left is a beatuiful round table and a door 2 steps beyond it')
                        print(5+y,'steps to your right there is the door from which you entered the room')                        
                        print("you cant see what is behind you\n")
                    if abs(angle)==180:
                        print("You are facing the door you just walked through, it is",5+y,"steps ahead of you")
                        print(5-x,'steps to your left is a suspecious looking well furnished sofa with a painting on the wall behind it')
                        print(5+x,"steps to your right is the largest door in the room, there is an odd clock hanging on the wall next to it and a chiar beside it")
                        print("you cant see what is behind you\n")
                    if angle==270 or abs(angle)==90:
                        print(5+x,"steps in front of you is the largest door in the room, an odd clock hanging on the wall a chair beside it")
                        print(5+y,"steps to your left is the door your just step through")
                        print(3-y,"steps to your right a beautiful round table")
                        print('you cant see what is behind you')
                            
                elif 'forward' in choice:
                    steps()
                    if (angle==0 or angle == 360) and x==0 and y==0 and y+n>3:
                        print("you cant take",n,"as there is a table in front of you")
                    elif (angle==90 or angle==-270) and x==-2 and y==4 and x+n>5:
                        print('you could only take three steps as there is a table in front of you')
                    elif (angle==-90 or angle==270) and x==2 and y==4 and x-n>5:
                        print('you cannot take',n,' as there is a table in front of you')
                    else:
                        step_forward()
                                
                elif 'backward' in choice:
                    if (angle==0 or angle == 360) and x==0 and y==5:
                        n=2
                        print("you have crossed the table")
                    elif (angle==90 or angle==-270) and x==2 and y==4:
                        n=2
                        print("you have crossed the table")
                    elif (angle==-90 or angle==270) and x==-2 and y==4:
                        n=2
                        print("you have crossed the table")
                    else:
                        steps()
                    step_backward()
                    
                elif 'turn' in choice:
                    turn()
                    
                else:
                    print("invalid input ....enter stepforward or stepbackward or turn")
                
                ##Element access loops##            
                #wall-clock/wardrobe accessing loop    
                while (angle==270 or angle ==-90) and x==-5 and y==0:
                    print("You face are standing in front a large door and to its right there is a wall clock which is not working and reads 9'O'CLOCK and there is wooden chair right below the clock but you dont miss the fact that the on the chair WHITE paint is splilled")
                    choice=input("do want to open the door? yes/no/step forward/step backward/turn: ").lower()
                    if 'yes' in choice:
                        print("you have opened the door which leads to the wardrobe .....all you see in the robe is that it has only 3 colours of dresses arranged in a neat order like RED BLACK and WHITE")
                    elif 'no' in choice:
                        print("you didnt open the door you might miss some important details")
                    elif 'forward' in choice:
                        steps()
                        step_forward()
                    elif 'backward' in choice:
                        steps()
                        step_backward
                    elif 'turn' in choice:
                        turn()
                    else:
                        print("invalid input ...enter yes/no/step forward/step backward/turn")
                        #else:
                            #print("you are still",5-n," steps far....you cant assess the things before you")
                                                             
                                
                #Table accessing loop
                while ((angle==0 or angle==360) and y==3 and x == 0) or ((angle==90 or angle==-270) and y==4 and x==-2) or ((angle==-90 or angle==270) and y==4 and x==2):
                    choice = input('do you want to examine the table or go towards the door?input(examine table)or (cross)/step forward/step backward/turn: ').lower()
                    if 'examine' in choice:
                        print('there is a envelope on the table that reads............................................please look around the room to find numbers to corresponding colours')
                        choice=input("there is also a vase on the table, input 'yes' to examnine else 'no': ").lower()
                        if 'yes' in choice:
                            print('the vase is in pure BLACK colour with ONLY 3 flowers in it')
                        else:
                            print('you didnt examine the vase you mght miss some details')
                    elif 'cross' in choice:
                            n=2
                            step_forward()
                            if angle==0 or angle==360:
                                print('you have taken the remaining steps towards the door')
                    elif 'forward' in choice:
                        n=2
                        step_forward()
                    elif'backward' in choice:
                        steps()
                        step_backward()
                    else:
                        print("Invalid input")
                        
                #room 3 Door accessing loop    
                while (angle==0 or angle == 360) and y == 5 and x==0:
                    choice = input("you are facing the door, do you want to open the  door and step through? yes/no/step forward/step backward: ").lower()
                    if 'yes' in choice:
                        if door1=='locked':
                            print('the door is locked you cant open it and the door seems to have digital lock if you enter the 3 digits you can cross the room')
                            choice=input('do you want try to open the door:')
                            if 'yes' in choice:
                                for i in range(0,3):                                
                                    if i == 2:
                                        print("You have only one chance left, the game will end if you loose.\nEnter carefully else 'quit' to start over")
                                        print('you have only',3-i,'chances let')
                                    choice=input("Enter a 3 digit number (in digits) or 'quit' to stop: ")
                                    if choice=='039':
                                        print("CONGRATULATIONS!!! the door is unlocked")
                                        door1='unlocked'
                                        break
                                    elif 'quit' in choice:
                                        print('you couldnt open the door .....search for the clues to open it')
                                        break
                                    else:
                                        print("invalid input")
                                        if i==2:
                                            room=-1
                                            print("***GAME OVER***")
                                                
                        else:
                            room = 3
                            print("***you move into the next room***")
                        if room!=2:
                            break
                    elif 'no' in choice:
                        print("you didnt open the door")
                        break
                    elif 'step forward' in choice:
                        steps()
                        step_forward()
                    elif 'step backward' in choice:
                        n=2
                        print("you have crossed the table")
                        steps()
                        step_backward()
                    elif 'turn' in choice:
                        turn()
                    else:
                        print("invalid input....enter yes/no/turn/step forward/step backward")
                        
                #Sofa/painting accessing loop
                if (angle==90 or angle==270) and x==5 and y==0:
                    print("in front you there is a well furnished sofa but the dominating thing is BLOOD STAINED (PURE RED) clothes on it")
                    while (angle==90 or angle==270) and x==5 and y==0:
                        print("You see a painting of the monalisa on the wall ...")
                        choice = input("do you want to examine the painting? yes/no.....step forward/step backward/turn: ").lower()
                        if 'yes' in choice:
                            print("the painting looks exactly as the DAVinci's painting but you see that the frame is decorated with only one number i.e 0")
                        elif 'no' in choice:
                            print("you didnt examine the painting you mights miss some important details")
                        elif 'step forward' in choice:
                            steps()
                            step_forward()
                        elif 'step backward' in choice:
                            steps()
                            step_backward()
                        elif 'turn' in choice:
                            turn()
                        elif 'look' in choice:
                            print("in front you there is a well furnished sofa but the dominating thing is BLOOD STAINED (PURE RED) clothes on it")
                            print("there is a monalisa painting on the wall ...")
                        else:
                            print("invalid input...enter yes/no/step forward/step backward")
                                
                #room 1 door access loop
                while abs(angle)==180 and x==0 and y==-5:
                    print("there is a door in front of you which leads you to the previous room")
                    choice=input("do you want to open the door and step through? yes/no/step forward/step backward/turn: ").lower()
                    if 'yes' in choice:
                        print('***You have exited the room and have entered the previous room***')
                        room=1
                        break
                    elif 'no' in choice:
                        print('you are still in the current room ...please do examine the things')
                    elif 'turn' in choice:
                        turn()
                    elif 'forward' in choice:
                        step_forward()
                    elif 'backward' in choice:
                        step_backward()
                    else:
                        print('invalid input ...enter yes/no/turn/step forward/step backward')
                        

    if room==3:
        print('-------------')
        print('welcome to the world of zombies')
        print('-------------')
        a=['y','yes','Y','YES']
        b=['left leg','right leg','left hand','right hand','chest','thigh','stomach','shoulder','head']
        alive=True
        x=0
        y=0
        angle=0
        while alive and room==3:
            if complete==0:
                complete=game()
            if complete==-1:
                while True:
                    choice=input("Sorry you have lost the game, woud you like to try again? yes/no: ").lower()
                    if choice in a:
                        print("you get another chance")
                        complete=0
                        break
                    elif choice in b:
                        print("GAME OVER")
                        room=-1
                        break
                    else:
                        print("invalid input, please enter yes/no")
            if complete==1 and room==3:
                print("You have managed successfully imapale the zombie but it slowly regaining strength")
                print("You need a stronger weapon to attack it")
                print("hint:check your inventory for something to use")
                while complete==1 and room==3:
                    choice=input("what would you like to do?").lower()
                    if 'turn' in choice:
                        turn()
                    elif 'forward' in choice:
                        steps()
                        step_forward()
                        if y==4 and abs(x)<=2:
                            print("you are too close too the zombie, step back else you might get bitten")
                        if y==5 and abs(x)<=2:
                            print("you got too close to the zombie, it bites you and you could not break free")
                            print("you've been infected! GAME OVER")
                            complete=-1
                    elif 'backward' in choice:
                        steps()
                        step_backward()
                    elif 'look' in choice:
                        print("you are staring at the mangled body of a zombie, it seems to be slowly regaining strength")
                    elif 'inventory' in choice:
                        invent()
                    elif 'take' in choice:
                        if 'torch' in choice:
                            print("you are already using the torch, it is helping you locate the zombie")
                        elif 'sword' in choice:
                            print("you take the golden sword in place of the gun")
                            choice=input("would you like the attack the zombie? yes/no: ").lower()
                            if choice in a:
                                print("you use the golden sword to attack the zombie and are able to successfully save yourself!!!")
                                complete=3
                            elif choice in b:
                                print("you do not use the sword to attack the zombie, before you know you it attains full strength and jumps at you")
                                print("you are too impaled to continue and collapse, you've been infected")
                                print("GAME OVER")
                                room=-1
                        
                            else:
                                print("invalid input, please enter 'yes' or 'no' next time")
                    else:
                        print("invalid input, pleas enter step forward/step backward/turn/inventory next time")
            if complete==3 and room==3:
                print("you are able to successfully open the door using the bronze key and escape!!")
                print("congratulations!!! you won the game!!!")
                print("GAME OVER")
                room=-1
                        
        if room==-1:
            print("room -1, thank you for playing")
            break
        
    
print("Bye!")
     
     
     
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
