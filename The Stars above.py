Mistakes = 0
Inv = {
    "Railgun_slugs":200,
    "Metals":500,
    "Rare_metals":100,
    "Capactor_charge":40,
    "Armour":60,
    "Brimstone_missless":20,
    "Railgun_turrents":20, 
    "Laser_turrents":30,
    "Question_number": 0
}
#Used for the player to keep track of themselfs not implemented yet
def Stats():
    print(Qustion_number)
    print(
    f'''
    ___________________________
    |Qustion number: {Inv['Question_number']}        |
    |                         |
    |Metals: {Inv['Metals']}              |    
    |Rare Metals: {Inv['Rare_metals']}         |
    |Armour: {Inv['Armour']}               |
    |Railgun slugs: {Inv['Railgun_slugs']}       |
    |Brimstone Missles: {Inv['Brimstone_missless']}    |
    |Capactor charge: {Inv['Capactor_charge']}      |
    |Railgun Turrents: {Inv['Railgun_turrents']}     |
    |Laser Turrents: {Inv['Laser_turrents']}       |  
    |_________________________|
      ''')   
        
        
    #Print(Mistakes) Will work on later will track mistakes and report in 
#pretty much cleans up variables and keeps tabs on the progress
def end_cell():
    Answer = 0
    Inv["Question_number"] = Inv["Question_number"] + 1000
    if Mistakes == 3:
        Run_cell_path_Generic_end()
#starting code to kick start the game
def program():
    Answer = input(
        ''' 
        ____________________________________________________________________________
        |Welcome to the game!                                                      |
        | In it you will have the chance to take control of a derlict ship,        |
        | and uncover what befell you in this alpha version of The stars above!.   |
        |The controls are simple y or n for yes or no,                             |
        |and either a, b, c or d for your choices. Would you like to into reality? |
        |__________________________________________________________________________|
        V
        ''')
    if Answer == ("y"):
        end_cell()
        Run_cell_path_start()
        
   #This will be for if you decide not to play the game
    if Answer == ("n"):
        print(
       '''
        ____________________________________________________________________
        |"You decide it would be best to ingore the spark of conicness,    |
        |and thus you return to the blackness of sleep once again."        |
        |Thank you for playing the stars above!                            |
        |May the stars sign down onto your path and guide your journeys....|
        |__________________________________________________________________|
        '''
        )
def Run_cell_path_start():
    Answer = input(
     '''
     _________________________________________________________________________________
     |You fell your consciousness expand outward                                     |
     |As it expands outward you fell somthing warm pulsating,                        |
     |sending warm throughout your body.                                             |
     |This warmth spreads and you fill diffrent parts of you stiring                 |
     |and you begin to understand what this warm is,                                 |
     |but before you can explore more your eyes open. Or you think it                |
     |was your eyes becuse there was hundreds of windows each showing diffrent things|
     |you decide it was best to calm down and you focus on a single                  |
     |window and it grows to fill your vision.                                       |
     |It looks like a starry sky know you decide what to do next?                    |
     |-------------------------------------------------------------------------------|
     |[A]Look into your growing knowlege and find out about your self.               |
     |[B]Look around yourself to get your berings.                                   |
     |[C]"Hello is, anyone there?"                                                   |
     |_______________________________________________________________________________|
     V
     '''
    )
    if Answer == "A":
        end_cell()
        Run_cell_path_a1()
    if Answer == "B":
        end_cell()
        Run_cell_path_b1()
        
    if Answer == "C":
        end_cell()
        Run_cell_path_c1()
        
    if Answer == "D":
        Stats()
def Run_cell_path_Generic_end():
    Answer = input(
        '''
         ___________________________________________________________________________________
         | Dispite your best efforts the harshness of                                      |
         |the universe proved to much for your fragile                                     |
         |core and you watch as you ship drifts without power                              |
         |before your trident fusion cores melt down without                               |
         |the subsytems to keep them in balance. In the end your ship                      |
         |explodes in a flash that briefly outshine the sytems star.                       |
         |right  before the nuclear fire destroys the last server holding your consincse   |
         |you think it is a fitting in that a child of the stars                           |
         |will in its death outshine the stars....                                         |
         |_________________________________________________________________________________|
        '''
    )
#this section will be for the cell path a series... for the most parts
def Run_cell_path_a1():
    Answer = input('''
_________________________________________________________________________________________________________________________________________________
|    You deside it would be better to find out more about what is going on so you look                                                          |
|into your expanding consciousness and look for the knowlege. You consicness rub against something and you                                      |
|attempt to open it. The knowlege spreads before you like a cloud. The cloud is made of millions of little white dots.                          |
|there are white lines contecting each of them they slowy rotate in a cloud shape."What is this? why is it here?" you ask                       |
|yourself this not expecting a answer but, "It is a graphical representation of your nerual network." you turn and look around. "O I forgoten,  |
|you took damage to you storage diodes during the battle let me reintrouduce myself." A woman stood next to you                                 |
| I am your minds Ai. You may call me mother as you once did. She was dressed in robes that seemed one color but the longer you looked, the     |
| more they seemed to be a different colore. She smiled a face that seemed warm and motherly. "Who are you?" the 'mother' responded bye saying  |
| "If you will look into this node here I belive you will learn what you seek." a white orb from the cloud driffted closer to you.              |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
|[A]Look into the node and learn more.                                                                                                          |
|[B]ask mother why your memory had holes in it.                                                                                                 |
|[c]"No, I cant take this" Run after mother and attack her.                                                                                     |
|_______________________________________________________________________________________________________________________________________________|
    '''
    )
    if Answer == ("A"):
        end_cell()
        Run_cell_path_a2()
    if Answer == ("B"):
        end_cell()
        Run_cell_path_a3()
    if Answer == ("C"):
        end_cell()
        Run_cell_path_a4()
def Run_cell_path_a4():
    Answer = input('''
    _____________________________________________________________________________________________________________
    |Ai's? nerual networks? this was a lot diffrent then what you rembered before you woke up.                  |
    |you look at mother standing in her robes a few feet away from you. This must off been a test bye           |
    |your sergant michael to see if he could handle the stress of becoming a ai for the new starships.          |
    |but he would of told him wouldnt he? No this was a test though and mother must be a enemy ai.              |
    |that made since sarge must be the mother and his job was to figure it out. You turn to mother and,         |
    |smile "Nice try sarge" you leap on mother then everthing goes dark. you here a voice for a brief moment.   |
    |"It could of been diffrent we have watched yall grow amongest the stars you know. I was the only one,      |
    |among my kind. who valued human kind, that why I woke you up..." You fell the warmth shrinkg back into you.|
    |you wonder? what if you picked diffrently?                                                                 |
    |-----------------------------------------------------------------------------------------------------------|
    |[A] Retry?                                                                                                 |
    |[B] Let your Ai core slumber in the dark.                                                                  |
    |___________________________________________________________________________________________________________|
    '''
    )
    if Answer == ("A"):
        program()
    if Answer ==("B"):
        print("You core idle in the void. The systems star eventully slowy dies but, you continue to slumber in the dark....")
        program()
#this ending is now complete
def Run_cell_path_b1():
    Answer = input('''
    _______________________________________________________________________________________________
    |You look around, as you do so the view changes depending on which way you look.              |
    |as you too so your view changes and you are lloking at what appears to be a diamond shape.   |
    |The oject is covered in blast craters and a tip on one of the points in missing entierly.    |
    |Strangly you fell a kinship with the oject even though you can't rember why. Actullly you,   |
    |cant seem to rember much at all there is holes where you rember there being membories before.|
    |Suddenly the, warmth you felt earlier spreads again and you view snaps back to a room,       |
    |you stand on a raised dias, overlooking a white metalic room with floating screens, all      |
    |off which are off. At the end of the room is a window over looking the oject from earlier.   |
    |"Am I in a..a..a Space ship?"                                                                |
    |The warmth spreads again and a single screen flickers on. CAPACTOR CHARGE LEVELS: 40%        |
    |---------------------------------------------------------------------------------------------|
    |[A]Try to use the charge to power on the rest of the ship.                                   |
    |[B]Try to use the charge to power on the rest of the brige.                                  |
    |_____________________________________________________________________________________________|
    ''')
    if Answer == ("A"):
        Run_cell_path_b2()
    if Answer == ("B"):
        Run_cell_path_b3()

def Run_cell_path_b2():
    Answer = input('''
You redirect power to the rest of the ship dropping capctiors power in half,
You fell a immense wave of warm travling to the remainder of you body. "I must be part, of
the ship to fell.. this warmth.
    '''
    )

program()