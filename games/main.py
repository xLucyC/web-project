import time
import random
from random import randint
from pygame import mixer
from pygame.locals import *
from pygame import mixer

#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('./Media/Spacegame.mp3')
#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

PlayerFuel = 0  # sets player fuel
Wordcount = 0  # keeps count of secret words found


def LoseFuel(fuel_amount):  # takes fuel amount from total
    global PlayerFuel
    PlayerFuel -= fuel_amount


def AddFuel(fuel_amount):  # adds fuel amount to total fuel
    global PlayerFuel
    PlayerFuel += fuel_amount


def ResetFuel():
    global PlayerFuel
    PlayerFuel -= PlayerFuel


def FuelCheck():
    global PlayerFuel
    if PlayerFuel <= 0:
        EndGame()  # checks there is fuel left and ends the game if there isn't.


def NewGame():
    print("Please Choose '1' for Easy, '2' for Medium and '3' for Hard then press 'Enter'\n")
    NewGameInput = input("")
    if NewGameInput == "1":
        NewGameEasy()
    elif NewGameInput == "2":
        NewGameMedium()
    elif NewGameInput == "3":
        NewGameHard()
    else:
        print("Please enter a choice before pressing 'Enter'.")
        NewLoadGame()


def LoadGame():
    global PlayerFuel
    print("Type '1' for Easy, '2' for Medium and '3' for Hard.")
    EsMeHa = input("")
    if EsMeHa == "1":
        PlayerFuel += 60
    elif EsMeHa == "2":
        PlayerFuel += 50
    elif EsMeHa == "3":
        PlayerFuel += 40
    else:
        Login()
    time.sleep(1)
    LoadGameInput = input("Please enter a Checkpoint between '1-8', and press 'Enter'.\n")
    if LoadGameInput == "1":
        Choice3and4()
    elif LoadGameInput == "2":
        Choice5and6()
    elif LoadGameInput == "3":
        Choice07()
    elif LoadGameInput == "4":
        Choice8and9and10()
    elif LoadGameInput == "5":
        Choice011()
    elif LoadGameInput == "6":
        Choice12and15and16()
    elif LoadGameInput == "7":
        Choice13and18and19()
    elif LoadGameInput == "8":
        Choice017()
    elif LoadGameInput == "9":
        BonusGame()
    else:
        print("Please enter a choice before pressing 'Enter'.")
        NewLoadGame()


def NewLoadGame():
    NewLoadGameInput = input("Type '1' for New Game or '2' to Load Game, and press 'Enter'.\n")
    if NewLoadGameInput == "1":
        NewGame()
    elif NewLoadGameInput == "2":
        LoadGame()
    else:
        print("Please enter a choice before pressing 'Enter'.")
        Login()


def EndGame():
    global Wordcount
    global PlayerFuel
    ResetFuel()
    print("You Have Ran out of Fuel.")
    print("Thanks for playing, Do you want to play again?")
    print("Press '1' to play again or '2' to end game.")
    PlayAgain = input()
    if PlayAgain == "1":
        NewGame()
    elif PlayAgain == "2":
        exit("Come back soon.")
    else:
        NewLoadGame()


def NewGameEasy():
    global PlayerFuel
    PlayerFuel += 60
    Intro()


def NewGameMedium():
    global PlayerFuel
    PlayerFuel += 50
    Intro()


def NewGameHard():
    global PlayerFuel
    PlayerFuel += 40
    Intro()


def AddSecret(secret):
    global Wordcount
    Wordcount += secret


def SecretCheck():
    global Wordcount
    if Wordcount < 5:
        print(f"You Have Found {Wordcount} Secret Words.")
        time.sleep(3)
        EndGame()
    elif Wordcount >= 5:
        print("Congratulations, You found all the secrets.")
    time.sleep(2)
    print(r"""⠀⠀⠀⠀⠀⠀⠀⢠⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣤⣤⣤⣤⣤⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣤⣤⣤⣤⣄⣤
⠸⣯⠉⣩⣍⣉⣭⣉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣍⣍⣉⣭⠉⠉⣿
⠀⣿⠀⢹⡏⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠉⣹⠀⢸⡏
⠀⢹⡇⢸⣇⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⣿⠀⣾⠓
⠀⠈⣿⠀⣿⡀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⣸⡇⢰⡟⠀
⠀⠀⠸⣧⠘⣷⡀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⢠⡟⢠⡿⠀⠀
⠀⠀⠀⠹⣧⡸⢷⡄⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⣰⡟⢠⡿⠁⠀⠀
⠀⠀⠀⠀⠘⢷⡌⠻⣦⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⢀⣼⠋⣴⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣦⡘⢷⣌⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣏⣴⠟⣡⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣍⠻⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⣡⡾⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣮⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣯⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣤⣄⣀⠀⠀⠀⠀⢀⣀⣤⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⡇⠀⣿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣼⣧⣤⣿⣦⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣿⣥⣤⣤⣤⣤⣤⣤⣤⣤⣤⣽⣧⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣿⣋⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣹⣷⣀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀Secrets⠀⠀Found⠀  ⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀5/5⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢙⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀""")
    time.sleep(2)
    print("You can now play the Bonus Game or you can play later,\n just enter '9' when loading game.")
    print("Play the bonus game now.")
    print("Choice 1. Yes, of Course.")
    print("Choice 2. Sorry, i'm too busy.")
    BonusChoice = input("")
    if BonusChoice == "1":
        BonusGame()
    else:
        EndGame()


def PreLogin():
    Login()


def Login():
    username = input("Please enter username or 'guest' and press 'Enter'. \n")
    time.sleep(1)
    if username.lower() == "guest":
        pass
    else:
        create_new_user = input(
            "Username doesn't exist. Would you like to create a new user?: \n""Type '1' for Yes and '2' for No.\n")
        if create_new_user.lower() == "1":
            password = new = input("Please enter a password for the new user. \n")
            users_file = open("users.txt", "a")
            users_file.write(f"{username},{password}\n")
            users_file.close()
            print("User created successfully!")
        else:
            print("Username doesn't exist")
            PreLogin()
        password = input("Please enter password and press 'Enter' \n")
        time.sleep(1)
        if password == "Pass1" or password == "guest" or password == new:
            print("Login successful")
        else:
            print("Incorrect password")
            PreLogin()
        time.sleep(1)
    print("Logging in...")
    time.sleep(2)
    print("Loading...")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(5)
    NewLoadGame()


# mini-game roll
def roll_dice():
    return random.randint(1, 2)  # can change odds as needed


def is_valid_number(number):
    return number.isdigit() and 1 <= int(number) <= 2  # can change odds as needed


def Ship():
    print(r"""                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                             SSt  `------'`""")


def RollSuccess():
    Ship()
    global PlayerFuel
    print("the Dice Roll Game ")  # change to fit story we don't need to use dice
    while True:
        target_number = input("Pick a number between 1 or 2: ")  # can change odds as needed
        if not is_valid_number(target_number):
            print("Invalid number. Please try again.")
            continue
        target_number = int(target_number)
        break

    while True:
        play_again = input("Press Enter to roll the dice or 'Q' to quit: ")
        if play_again.lower() == 'q':
            print("Thanks for playing!")
            Choice13and18and19()
            break

        dice_roll = roll_dice()
        print("You rolled a", dice_roll)
        if dice_roll == target_number:
            AddFuel(20)
            print("+20 Fuel")
            print("You found a Secret Word 'Asteroid'.")
            AddSecret(1)
            Choice13and18and19()
            break
        else:
            LoseFuel(20)
            print("-20 Fuel")
            if PlayerFuel <= 20:
                PlayerFuel -= 20
                print("doomed")
                FuelCheck()
                EndGame()
            else:
                print("You leave the asteroid belt and head towards a moon in the distance.")
                Choice13and18and19()


# mini game trivia

class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


# questions
questions = [
    Question(
        "What is the largest planet in our solar system?",
        ["Mars", "Jupiter", "Saturn", "Neptune"],
        2
    ),
    Question(
        "What is the closest star to Earth?",
        ["Alpha Centauri", "Betelgeuse", "Sun", "Proxima Centauri"],
        3
    ),
    Question(
        "Which planet is known as the 'Red Planet'?",
        ["Mars", "Venus", "Mercury", "Jupiter"],
        1
    ),
    Question(
        "What is the name of the largest moon of Saturn?",
        ["Europa", "Titan", "Ganymede", "Miranda"],
        2
    ),
    Question(
        "Who was the first person to walk on the moon?",
        ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"],
        2
    )
]


# questions 2,3,1,2,2

def get_user_answer():
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if 1 <= user_answer <= 4:
                return user_answer
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def QuizPicture():
    print(r"""                    dS$$S$S$S$S$S$S$$Sb                    
                   :$$S^S$S$S$S$S$S^S$$;                   
                   SSP   `^$S$S$^'   TSS                   
                   $$       `"'       $$                   
                  _SS ,-           -  SS_                  
                 :-.|  _    - .-   _  |.-;                 
                 :\(; ' "-._.'._.-" ` |)/;                 
                  \`|  , o       o .  |'/                  
                   ":     -'   `-     ;"                   
                     ;.              :                     
                     : `    ._.    ' ;                     
                   .sSb   ._____.   dSs.                   
                _.d8dSSb.   ._.   .SSbT8b._                
            _.oOPd88SSSS T.     .P SSSS888OOo.             
        _.mMMOOPd888SSSSb TSqqqSP dSSSS88OMOOOMm._         
     .oOMMMOMOOM8O8OSSSSSb TSSSP dSSSSS8OOMMOOMMOOOo._     
   .OOMMOOOMMOOMOOOO  "^SSSTSSP dSSS^"OOOOMMOOMMMOOMMMb.   
  dOOOMMMOMMOOOMOOOO      "^SSSS^"   :OOO8MMMOOMMOOMMOMMb  
 :MMMOOMMOMMOOMMO8OS         `P      8O8OPdMMOOMMOMMOMMMM; 
 MMMMOOMMMMMOOMbTO8S;               :8888MMMMMOMMOMMOMMMMM 
 OMMMMOOMMMMOOOMMOOOS        S     :O8OPdMOMMMOMOMMOOMMMMO 
:OMMMMOOMMOMMOOMbTObTb.     :S;   .PdOPdMOOMMMMMOMMOMMMMMO;
MOOMMMMOMMOMMOOMMMOObTSSg._.SSS._.PdOPdMOOMMMMOMMMMOMMMMOOM
MMOMMMMOMMMOMMOOMMbT8bTSSSSSSSSSPd8OPdOOOMMMMOOMMMMOMMMOOMM
MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM""")  # r"""""" interprets the string as RAW data.


def run_quiz(question):
    global PlayerFuel
    QuizPicture()
    time.sleep(2)
    score = 0
    for i, question in enumerate(question[:5]):  # add more question if needed
        print(f"Question {i + 1}:")
        question.display_question()
        user_answer = get_user_answer()
        if question.check_answer(user_answer):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print()

    print(f"You scored {score}!")
    if score >= 4:
        AddFuel(20)
        AddSecret(1)
        print("+20 fuel")
        print("Secret word = 'Mars'.")
        FuelCheck()
        if PlayerFuel > 15:
            Home()
        elif PlayerFuel <= 15:
            Safe()
        elif PlayerFuel <= 0:
            Stranded()
    else:
        LoseFuel(-20)
        print("-20 fuel")
        FuelCheck()
        print(f"Your Remaining Fuel is {PlayerFuel}")
        if PlayerFuel > 15:
            Home()
        elif PlayerFuel <= 15:
            Safe()
        elif PlayerFuel <= 0:
            Stranded()


# math trivia
Loop = True
lives = 3


def TriviaCheck():
    global PlayerFuel
    if PlayerFuel > 15:
        Home()
    elif PlayerFuel <= 15:
        Safe()
    elif PlayerFuel <= 0:
        Stranded()


def MathTrivia():
    global PlayerFuel
    global lives
    print(r"""    .-....-.
             /        \
            /_        _\
           // \      / \\
           |\__\    /__/|
            \    ||    /
             \        /
              \  __  /  \  /          ________________________________
               '.__.'    \/          /                                 \
                |  |     /\         |        "What is 5*100"             |
                |  |    O  O        |         "What is 5*100"!           |
                ----    //         O \_________________________________/
               (    )  //        O
              (\\     //       o
             (  \\    )      o
             (   \\   )   /\
   ___[\______/^^^^^^^\__/) o-)__
  |\__[=======______//________)__\
  \|_______________//____________|
      |||      || //||     |||
      |||      || @.||     |||
       ||      \/  .\/      ||
                  . .
                 '.'.`""")
    time.sleep(2)
    print("In order to pass you must answer the questions, fail a question lose a life.")
    lives = 3  # Global lives count

    print("you have 3 lives")
    while lives > 0:  # Keeps the game going so long as there are lives left
        print("What is 5 * 500?")
        ans = int(input(""))
        if ans == 2500:
            print("Correct!")
        else:
            print("Incorrect!")
            lives -= 1  # Removes a life from the global count
            print("You have two {} lives remaining".format(lives))

        print("What is 65 - 27?")
        ans = int(input(""))
        if ans == 38:
            print("Correct!")
        else:
            print("Incorrect!")
            lives -= 1
            print("You have {} lives remaining.".format(lives))

        print("What is 60 * 60?")
        ans = int(input(""))
        if ans == 3600:
            print("Correct!")
        else:
            print("Incorrect")
            lives -= 1

        print("what is 500/5?")
        ans = int(input(""))
        if ans == 100:
            print("Correct!")
        else:
            print("Incorrect!")
            print("You have {} lives remaining.".format(lives))

        if lives == 0:
            print("GAME OVER")  # Ends game when out of lives
            EndGame()
        if lives == 3:
            print("Congratulations!, you have played a perfect game, please collect your fuel")
            print("The Secret Word is 'Galaxy'.")  # Conditional message based on lives remaining
            AddSecret(1)
            AddFuel(20)
            lives -= 3
            TriviaCheck()
        else:
            LoseFuel(20)
            if lives == 2:
                lives -= 1
            elif lives == 1:
                lives -= 1
            TriviaCheck()
            print("Congratulations you have passed the test, please collect your fuel.")


# casino game

Chips = int(100)


def CasinoSign():
    print(r"""                                88                          
                                ""                          

 ,adPPYba, ,adPPYYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYba,   
a8"     "" ""     `Y8 I8[    "" 88 88P'   `"8a a8"     "8a  
8b         ,adPPPPP88  `"Y8ba,  88 88       88 8b       d8  
"8a,   ,aa 88,    ,88 aa    ]8I 88 88       88 "8a,   ,a8"  
 `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"' 88 88       88  `"YbbdP"'   """)


def CasinoGame():
    global PlayerFuel
    global Chips
    CasinoSign()
    time.sleep(2)
    play = input("Do you want to play a game of High/Low? Y or N?\n")
    while play.lower() == "y":
        number = randint(1, 10)
        guess = input("Guess H for high or L for low.\n")
        if guess.lower() == "h":
            if number > 5:
                print("You guessed correctly! The number was", number)
                Chips = Chips + 10
                print("You have", Chips, "Chips.")
                play = input("Play again? Y or N?\n")
                if Chips < 1:
                    print("You have run out of Chips, time to go to the ATM.")
                    print("Your Chips has been reset.")
                    Chips = int(100)

            if number < 6:
                print("You guessed wrong! The number was", number)
                Chips = Chips - 10
                print("You have", Chips, "Chips.")
                play = input("Play again? Y or N?\n")
                if Chips < 1:
                    print("You have run out of Chips, time to go to the ATM")
                    print("Your Chips has been reset.")
                    Chips = int(100)

        if guess.lower() == "l":
            if number < 6:
                print("You guessed correctly! The number was", number)
                Chips = Chips - 10
                print("You have", Chips, "Chips.")
                play = input("Play again? Y or N?\n")
                if Chips < 1:
                    print("You have run out of Chips, time to go to the ATM.")
                    print("Your Chips has been reset.")
                    Chips = int(100)

            if number > 5:
                print("You guessed wrong! The number was", number)
                Chips = Chips - 10
                print("You have", Chips, "Chips.")
                play = input("Play again? Y or N\n?")
                if Chips < 1:
                    print("You have run out of Chips, time to go to the ATM")
                    print("Your Chips has been reset.")
                    Chips = int(100)

    print("Okay, the game is over.")
    print("You finished with", Chips, "Chips.")
    if Chips > 100:
        AddFuel(20)
        AddSecret(1)
        print("+20 Fuel")
        print("You found the Secret Word: 'Universe'.")
        time.sleep(2)
    elif Chips == 100:
        AddFuel(10)
        print("+10 Fuel")
        time.sleep(2)
    elif Chips < 100:
        LoseFuel(20)
        print("-20 Fuel")
        time.sleep(2)
    Choice7()


# Bonus Game
symbols = ["@", "#", "*"]


def BonusGame():
    CasinoSign()
    time.sleep(2)
    while True:
        tokens = 100
        print("Welcome to Space Slots.")
        while tokens > 0:
            print("You have", tokens, "tokens.")
            try:
                bet = int(input("Bet amount: "))
            except:
                print("Please enter a whole number of tokens")
                continue
            if bet > tokens:
                print("Not enough tokens.")
            else:
                tokens -= bet
                sq_one = random.choice(symbols)
                sq_two = random.choice(symbols)
                sq_three = random.choice(symbols)

                print()

                print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
                print("--------------")

                print("|", sq_one, "|", sq_two, "|", sq_three, "|")
                print("--------------")

                print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
                print()

                if sq_one == sq_two == sq_three:
                    amount_won = bet * 2
                    print("You won", amount_won, "tokens.")
                    tokens += amount_won
                else:
                    print("You lost this time.")
        print("You are out of tokens.")
        time.sleep(1)
        print("Thank you for playing.")
        time.sleep(1)
        print()
        EndGame()


def Intro():
    global Wordcount
    if Wordcount >= 5:
        SecretCheck()
    print(r"""████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████▒▒██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▓▓▓▓██████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████▒▒████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████▓▓▓▓▓▓████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████░░██████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""")
    time.sleep(3)
    print(
        "Whilst travelling many light years across the empty black vastness of deep space our astronaut was suddenly "
        "awoken from their Hyper Sleep Pod by the sound of the ion drives slowing.")
    time.sleep(2)
    print(
        "Noticing through the nearest viewport that celestial objects were coming into view within a massive "
        "unfamiliar galaxy the ship had entered,\n our astronaut quickly saw they were in a very strange place indeed.")
    time.sleep(2)
    print(
        "Whirling black-holes and many planets of all different colors and sizes could be seen as the ship seemed to "
        "be pulled towards them uncontrollably by a mysterious force.")
    time.sleep(2)
    print(
        "Noticing the ships low fuel levels our astronaut quickly made their way down to the air-lock, put on a Space "
        "Suit and exited onto the external walkway,\n Before arriving at the giant docking area.")
    time.sleep(2)
    print(
        "Walking intrepidly further towards the edge our astronaut realised that obtaining ship supplies was of "
        "supreme importance if they ever wanted to return safely back to Earth!")
    time.sleep(2)
    print("The adventure begins...")
    time.sleep(3)
    Choice1and2()


def Choice1():
    global PlayerFuel
    LoseFuel(5)
    FuelCheck()
    print(r"""                .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __""")
    time.sleep(2)
    print("Landed on small planet!")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice3and4()


def Choice2():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print("You head towards the asteroid belt\n")
    time.sleep(3)
    print(r"""▒▒▒▒▒▒████▓▓▒▒▓▓██▓▓██▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓██████████▓▓
██▒▒▒▒██▓▓██████████▓▓▓▓▓▓██▓▓▓▓▒▒▒▒██▓▓▓▓▓▓▓▓██████████▓▓▓▓████▓▓
▓▓██▓▓██████████▓▓██▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓████████████████▓▓▒▒▓▓████
██████████████▓▓▓▓██████▓▓████████████████████████████▓▓▓▓▒▒░░▓▓██
████▓▓▓▓██████▓▓▓▓████████▓▓▓▓██▓▓████▓▓▒▒▒▒▒▒▓▓██████████▓▓▓▓▓▓██
██▓▓▒▒▓▓██▓▓▒▒▒▒██████▓▓▒▒▓▓██████████▒▒▒▒▒▒  ░░▒▒████▓▓██████████
██▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓██████▒▒██████▓▓████▓▓▒▒▒▒░░░░▒▒▒▒████████▓▓████
██▓▓▒▒▓▓████▓▓▓▓████████████▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▒▒▒▒██▓▓██▓▓▓▓████
▓▓██████████▓▓██▓▓▒▒▒▒▓▓████░░▒▒░░██▓▓██████▓▓▓▓▒▒██████████▒▒██▓▓
▓▓██▓▓▓▓▓▓████▓▓██░░▒▒▓▓▓▓██▓▓▒▒░░  ▓▓██████▓▓████████▓▓▓▓▒▒▓▓████
██▓▓██████░░▒▒████▓▓▒▒████▓▓████████▓▓██████▓▓████▓▓░░▓▓████▓▓██▓▓
████▓▓██░░░░░░▒▒████████▓▓▓▓████▓▓████████▓▓████▒▒▓▓██▓▓████▓▓██▓▓
▓▓████▓▓░░░░  ▒▒██████▓▓██▓▓████████████▓▓▒▒████████████████████▓▓
▓▓████████▒▒░░██▓▓██████████████████▓▓░░▒▒██▓▓████████████████████
██▓▓▓▓████████▓▓██████▒▒░░▒▒████████▒▒░░  ░░▓▓██▓▓██▒▒▓▓████████▓▓
██▓▓░░██▓▓██▓▓██████▓▓░░░░░░▒▒██████░░░░    ████████░░▒▒████▓▓████
██░░  ██▓▓██▓▓██████▓▓    ░░▒▒▓▓▓▓▓▓░░▒▒░░▒▒▓▓██████▓▓░░▒▒▓▓██████
▓▓████████▓▓▓▓▓▓▓▓▓▓██▒▒░░▒▒██████▓▓░░  ████▓▓▓▓▓▓██▓▓▒▒▒▒▓▓████▓▓
██████████▒▒▒▒▓▓██████▓▓██████████  ░░▒▒██████▒▒▒▒████▓▓░░▓▓██████
██████████████▓▓▓▓████▓▓██████▒▒▓▓██░░████████████████▓▓▓▓▒▒██████
██████▓▓██████████▓▓████████████████████████▓▓████████████████████
██▓▓████████████▓▓██▓▓██▓▓▒▒░░▓▓██▓▓██████████▒▒▒▒▓▓████▓▓██▒▒▓▓██
██████████████████████▒▒░░▒▒▓▓██████▓▓▓▓▓▓▓▓░░░░  ░░██▓▓████▓▓▒▒▒▒
▒▒▓▓██▓▓████▒▒████▓▓██████████▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░▒▒▓▓██████████
██▓▓██████▒▒▒▒▒▒████████████▒▒    ██▓▓▓▓▓▓▓▓▒▒░░░░▒▒████▓▓▓▓██████
████████████░░░░▒▒▒▒████████░░    ██▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓
██████████▓▓▓▓  ░░██████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓██████
▓▓▓▓████████▓▓▓▓░░▓▓████▓▓▓▓▓▓▓▓██▓▓▓▓░░▓▓████▓▓▓▓▓▓▓▓▓▓████▓▓██▓▓
████████████▓▓██▓▓██████▓▓██▓▓▓▓▓▓██░░  ░░██▓▓▓▓▓▓▓▓████▓▓████████
████████▓▓██████████▓▓▓▓██░░░░██▓▓██░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████████
▓▓██▓▓▒▒████▓▓████▓▓▓▓▓▓▓▓▒▒▒▒████████▒▒██▓▓██▓▓▓▓▓▓▓▓▓▓██  ▓▓████
██▓▓░░▒▒██████████████▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓████▓▓▒▒██▓▓
▓▓▒▒░░████████▓▓▒▒██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓████████▓▓▓▓██""")
    time.sleep(3)
    print("You weave and dodge past asteroids as you investigate the belt.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice5and6()


def Choice3():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print(r"""           .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\        ./ //  /  \/   .
  .                    \\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
                        ________________________
____________------------                        -------------_________""")
    time.sleep(2)
    print(
        "You decide to see if there's any people on the small planet. After walking a while you see a Space Casino,"
        "\n You also see what looks like a Shuttle Station with small crafts arriving and leaving the planet.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice07()


def Choice4():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r"""⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠇⡠⠊⠉⠙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠀⠌⢠⣤⣤⠀⠈⠳⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣅⠀⢯⣿⡿⢀⢀⠀⠈⢵⣖⠒⠒⠠⢄⡀⠀⠀
⠀⠱⡀⠀⠀⠀⣿⣿⡷⠀⡡⠛⡄⠀⠀⠈⢱⠀⠀
⠀⠀⠹⣎⠀⠀⠉⠉⢁⣼⣠⠊⢹⡄⠤⡀⠀⡇⠀
⠀⠀⠀⠈⢳⣄⠀⡠⢂⠸⡌⠙⣎⠀⠀⠈⢢⡅⠀
⠀⠀⠀⠀⠀⡝⡙⠒⠿⣤⠟⢲⢾⠿⡢⣄⠀⠁⠀
⠀⠀⠀⠀⠀⢇⠇⠀⠀⢨⡀⠀⠳⣕⠰⣌⢢⠀⠀
⠀⠀⠀⠀⠀⠈⠺⠤⢀⣀⣙⣦⡀⠀⠙⠢⢄⣣⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁""")
    time.sleep(2)
    print(
        "After landing on the small planet you receive an alert on your 'comms' device that your ship is under attack "
        "by aliens so you head back to your ship.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice8and9and10()


def Choice5():
    global PlayerFuel
    LoseFuel(5)
    FuelCheck()
    print(r"""                                                                                        

            ░░                                                                  ░░      


      ░░                                ░░  ██                                          
  ░░                                        ██                              ░░░░        
                                            ██                                          
                                          ▓▓▓▓▓▓                                        
                                        ▓▓▓▓▓▓▓▓▓▓                                      
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▓▓▓▓▒▒▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ░░░░▒▒░░░░░░░░                                    
                                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                    
                                      ▓▓▒▒▒▒▓▓▒▒▒▒▓▓                                    
                                      ▓▓▒▒▒▒██▒▒▒▒▓▓                                    
                                    ████▓▓▓▓▓▓██▓▓▓▓██      ░░                          
                                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                
                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                              
                                ▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              
        ░░                      ▓▓▓▓▓▓░░████████████░░████                        ░░    
                                ▓▓    ▓▓░░░░░░▓▓░░░░    ▓▓                              




                        ▒▒                ▒▒    ▒▒          ▒▒    ▒▒                    
""")
    time.sleep(3)
    print(
        "After landing on the asteroid you receive an alert on your 'comms' device that your ship is under attack by "
        "aliens so you head back to your ship to investigate.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice8and9and10()


def Choice6():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print(r"""
             @@@
               @@@   \         /  *
                __@**__\_/0\_/______*
                   %%  \_\v/_/  @
                                 @*
                              \   |% *
                         @@  *  \ ||\
                        @@@@     /~ \| *
                           @@@@  \_ /|
                              @@/*||/
                              /  @@*%
                                 %|

                                           @@@
                                          @@@@@
                                             @@@@
                            @@@      *   **     @@@
                              @@@ %  *  /~/^\~\  @@@
                                 *#~~~~~/~\0/~\~~~*@*~
                                    * /  *    %**%
                                              ##**

                                @@@@@@@@@    @@@@@    @@@@
                              @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@
                                @@@@@@@@@@@   @@@@@@   @@@@@@@
                                    @@@@@@@       @@@@@     @@@
                                         @@@@@        @@@@@    @@
                                           @@@@@@@      @@@@@   @@@
                                              @@@@@ `' { @{@)(` @@
                                          '`  '`@#@\ |**@%'~`*/ % ' '
                                       \_**__<^ #\_*|||%//\**^>~#\=`-|/\~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    time.sleep(3)
    print("You see a crashed Ship in the distance.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice011()


def Choice7():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r"""⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣧⡀⠤⠤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀⣦⣤⣤⣄⣈⡉⠉⠛⠛⠷⢶⠄⢠⣴⣦⡀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠉⠉⠛⠛⠷⣦⣀⠀⠀⢻⣿⣿⣿⡀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡆⠀⠀⠈⠉⠘⡇⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⢀⠀⢀⣀⣠⣤⡴⠾⠋⠀⠀⠀⢀⣠⡾⠃⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⠶⠶⠶⠀⠿⠃⠘⠉⠉⠀⠀⢀⣀⣤⣴⠾⠛⠉⠀⠀⠀⠀⠀
⠀⣿⣿⣟⣉⣀⣀⣀⣀⣠⣤⣤⣤⣴⡶⠶⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    time.sleep(3)
    print("You leave the small planet")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice12and15and16()


def Choice8():
    global PlayerFuel
    LoseFuel(5)
    FuelCheck()
    print(r"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⠻⠟⠻⠟⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⡠⢀⠌⡉⡉⢞⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠁⣀⣀⠐⠒⠂⠆⣀⣀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢛⢉⡉⡉⢛⣛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⡛⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⡼⠐⡌⢲⠛⠠⠠⠒⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⢀⠐⣠⠷⠛⠉⠉⠙⠲⣄⠀⡄⠈⠻⠆⠀⡘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⠍⣀⢹⢤⣃⠹⣧⢢⣂⢙⠷⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⡡⢈⣬⠵⣂⣧⠷⣩⢻⣷⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡅⠸⠘⣠⠛⢀⡼⢶⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⠛⣛⣛⠻⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠐⣠⡞⠁⠀⠀⠀⠀⠀⣀⣟⣀⡀⢁⡤⢤⣆⠑⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠁⠜⣠⣫⢴⢺⡵⢥⣕⡯⢾⠦⢱⠳⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⣟⣿⣽⣽⣯⣽⣧⣙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⢂⣴⠟⣶⣟⣏⣛⣳⡧⢫⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢻⡜⠠⣼⡿⣽⣿⣿⢡⣿⣿⣿⣿⣿⠿⢿⢟⣯⠞⣏⡇⢄⣱⣭⢁⠊⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇⠀⡈⢀⡏⠀⠀⠀⣰⡶⠿⠏⠉⠉⠉⢹⡏⢀⣰⢿⡆⠰⠆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠎⡰⣸⠡⢶⣏⢿⣸⠯⣎⣰⠟⠚⡀⠠⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⠏⡉⣰⡎⡸⣉⠿⣷⣬⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⢈⢱⣿⣶⣸⣉⡹⣶⠹⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠈⠳⠏⢿⠿⢛⣴⣿⣿⣿⣿⣿⢱⣺⢠⠏⡈⠿⠰⠪⢀⠾⢻⢚⢙⢀⢀⡙⢿⠿⣿⡻⣟⣻
⣿⣿⣿⣿⣿⣿⡏⠀⢐⠀⣼⣇⠀⣠⠞⢁⡄⠒⠂⡉⡉⡉⠙⢿⣋⣁⡼⠃⠀⡅⢂⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡇⢰⣵⠱⢛⣷⢾⢿⢞⣋⢗⠐⣨⣾⠇⡨⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⡟⢡⠦⣛⣱⣣⣼⡅⢦⢑⠻⢿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣰⢋⣾⣓⢎⡷⡹⢷⣹⣯⣿⡽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣼⡽⠌⠉⢫⢓⢤⠰⠺⡸⢜⢁⢏⠋⣼⡫⠅⠃⠘⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡁⠐⡊⢠⠀⣨⠟⢁⡴⠁⡀⠒⠂⠂⣀⡰⢦⡀⢨⠡⠀⠐⢂⠐⡁⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢠⠘⠊⣆⠟⣢⣋⡫⠛⠁⣐⣴⠟⣡⠆⠊⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢏⠼⣩⡾⣫⢗⣽⡿⣣⠜⣾⣿⢂⢹⣿⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢺⣧⠺⢧⢯⡮⣕⢯⣝⣿⡿⢧⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢫⡊⢀⣌⡣⣚⡺⢛⠣⠠⡀⢉⢮⢺⢘⡸⢸⢸⣿⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠐⡆⠀⠁⠀⢀⡞⠀⠂⠂⠢⠄⡂⢸⣆⢀⡟⠀⢀⡶⠶⢤⡀⠑⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⢶⣲⠈⣌⢀⣀⠀⠀⠈⢼⢐⠒⠐⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡿⣺⣵⣿⣼⣷⡿⣏⠷⣭⡪⠿⢋⠳⢘⣿⣿⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣧⣞⣷⣿⡾⣿⣿⡹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢰⢈⢏⣡⡆⣢⢀⠠⠚⠐⠙⠩⢽⣰⣸⠐⣯⢸⢣⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡅⠀⢳⡀⠀⠀⣈⣤⠶⠒⠲⣆⢀⣡⡀⠉⡉⠀⡀⢾⡀⢀⢠⡇⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⠶⠤⢭⠭⠭⠥⠾⣘⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣷⢵⡶⢾⣙⢮⠳⣩⡑⣂⡆⡰⠢⡱⢈⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡔⢹⣹⣆⢻⣽⢮⢫⠰⣀⣈⠜⠂⣸⢸⣿⢸⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣗⡀⠠⢈⠁⣰⠏⠀⠀⠐⠀⠈⣿⠀⢸⠀⣀⣤⣄⠈⠓⠖⠉⣀⠂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣻⣮⠝⠇⡽⣾⢿⡉⢨⡷⢽⣫⢰⠣⢹⣹⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⡑⡈⣞⣟⡷⢸⣹⢧⠃⠑⣊⢼⣿⠘⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⠀⠨⠀⢻⡀⠀⠀⠀⢀⣴⠏⠛⢧⡞⠁⢀⠈⢷⠀⠐⡀⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⡔⠹⠾⢟⠿⠣⠔⠒⠴⠠⠉⢀⣽⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣾⡱⡹⢹⢽⣵⣬⠤⣋⢐⡸⠋⣀⣽⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⢠⠀⠙⠲⠶⠖⠋⠁⠄⡀⠸⣇⠀⠀⣠⡟⠀⠂⣁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣛⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣻⣿⣯⣬⣐⡶⣾⣿⢿⠶⣚⣬⣴⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣼⣤⣄⣐⣑⢂⣒⣠⣴⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠐⠒⠄⣀⠁⠉⠄⠡⠄⠈⢙⠛⠁⢀⢤⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⠈⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣻⢿⡿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠽⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣈⢉⡁⣁⢉⡁⣤⣴⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣛⡛⡛⠘⠀⠡⠩⠿⠝⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢿⠃⠘⣴⡘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡄⢐⠀⢀⡀⠄⠺⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢱⠘⠘⠋⡈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣷⡒⢀⣴⣶⡶⢉⡥⢂⠌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠔⢠⣴⣄⣨⣔⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢫⠅⠺⢒⢈⢀⠑⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠐⠀⡀⠎⢻⢟⠣⡄⢂⢛⢴⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣧⣴⣾⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣐⢺⢀⢀⣛⣂⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⡅⢰⡌⢣⢌⣓⢌⠅⠊⢨⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣬⢊⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣧⡉⠭⣾⠳⠚⠉⠈⠐⠂⣀⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡿⣹⣎⣳⠹⠾⣟⢿⣻⣯⣿⣿⣿⣿⣮⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣏⣻⠬⢧⣭⡝⡾⣍⣿⢻⣿⣿⣚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢣⡙⢰⡤⠖⢣⢡⡒⠎⡚⠛⢾⢻⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⢟⣛⢛⣛⣛⣛⠛⡻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠫⢋⠥⠂⠊⠀⣞⢱⠀⣄⠔⡀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⠎⢂⡨⢡⣰⢚⡵⣎⢶⡪⣝⢺⡎⠀⢹⣷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢡⡾⠝⡈⠅⢈⢀⡉⢉⡛⣷⡚⡑⠬⠻⢿⠿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡌⠙⡨⠐⢁⣀⣔⢹⣈⢀⠢⢪⢏⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣻⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⡙⢘⠮⢡⡎⣖⣫⢚⡜⢮⡱⠍⡚⣠⠀⠀⠸⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢿⡋⠔⠈⣉⠽⢯⠽⢏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⡴⢠⠆⠁⣀⠔⢈⠁⠆⠑⠀⠉⠡⠠⠘⠸⠀⠐⠈⠀⠤⠄⠄⢄⠠⠪⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⠿⡄⠀⡰⠋⣁⣑⡕⠠⠌⠐⡨⢨⠀⡇⠈⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⡿⡿⢿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡷⡆⠽⢠⢧⡹⣜⣢⢫⡜⣎⠱⣼⢣⡏⢠⢰⢸⢸⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⢀⠌⠠⣱⠴⠨⠲⢹⠀⠢⢻⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠘⠠⠀⢄⠂⠄⠀⠀⠐⢐⢨⢀⡐⠠⣐⠐⡀⠦⢰⡰⣶⣿⣿⣿⣷⣶⣤⡠⡄⢰⢹⣿⣿⣿⣿⣿⣿⠿⡄⣛⢀⠎⡛⣸⠘⠅⢁⠼⡈⢁⢤⡆⠀⠸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⠓⡉⠩⢉⢋⡙⢛⠊⣉⠲⣶⣶⣶⣦⣴⣀⡞⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣷⢃⢂⢮⡲⡹⢆⡞⣒⠞⣬⢘⣴⠈⠀⢼⠀⢸⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠇⠀⠀⠘⡡⠐⢀⢠⢞⠄⠀⠀⠹⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢋⢀⠁⠀⠀⠀⢀⢀⣐⢼⣀⢆⡸⡄⢆⢑⠅⠸⢑⠰⢸⠃⢿⣿⣿⣿⣿⣿⣿⣿⡇⢐⠘⣿⣿⣿⣿⣿⣿⣿⡇⢾⡐⠠⣸⢁⠂⡀⡁⣺⠑⡌⢈⡁⢉⡘⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⠀⠀⠰⢁⠁⣈⠱⢇⡰⢨⣅⠹⣿⣿⣿⣿⡏⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣷⠈⣷⢇⠿⣎⢱⣉⢾⣉⢸⢊⡔⢰⠨⠐⢁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣯⢀⠀⠈⢠⠋⠠⢱⢢⢠⠀⠂⠀⢠⠐⢸⣿⣿⣿⣿⣿⣿⣿⠿⡛⢯⢩⠀⢠⠀⢀⠘⢠⠀⠠⠃⣠⢲⡏⡮⠧⠴⣌⠳⣘⠈⠕⢀⢅⢊⡦⠈⢼⢸⣿⣿⣿⣿⣿⣿⣿⠃⠾⢀⣿⣿⣿⣿⣿⣿⣷⣯⣖⣥⡄⢉⠊⠰⠵⠲⠀⣰⢺⡠⡡⢊⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢛⣩⡴⡈⠥⢞⣶⠆⠩⠤⠧⠶⠿⣷⡜⠸⢸⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣣⣝⠾⣜⣳⡾⡻⠕⠛⠩⢴⣛⠴⠊⠀⠨⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠐⠀⢀⠘⠬⠢⣱⠈⠠⠀⠀⡈⢀⣿⣿⣿⣿⣿⣿⣿⣿⢟⠉⢀⠤⢐⣴⣶⣷⣟⢸⢠⢀⠦⣱⡟⢖⠔⠣⢘⢚⢡⠐⠲⡰⡴⣡⠋⠐⡀⢸⣻⣿⣿⣿⣿⠿⡟⢅⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⢾⣽⣊⢚⢙⣃⠦⣩⠴⠑⣁⢔⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣱⣶⣿⣿⡟⡧⠁⡎⠉⠠⠈⠩⠁⠛⢉⣈⣤⠝⢠⢘⣥⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⠿⣶⠓⠚⠀⠂⠋⠘⠉⢀⣀⢤⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⠀⢠⢲⡠⠀⢉⡘⠠⠔⠰⢠⡾⣽⣿⣿⣿⣿⣿⣿⣿⢰⢋⢐⣥⣾⡿⣿⣽⣿⣿⡄⠈⡈⠙⠓⠱⠐⠲⠣⡅⠎⠲⠘⢈⢰⠈⣘⠈⠘⠱⠘⠸⠿⠋⠡⠒⢐⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣬⣰⣒⠒⠤⠤⠶⠶⣚⣩⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣰⣿⣿⣿⣿⣿⣽⢧⢉⡉⠈⢀⡉⣀⡠⠈⠙⢡⣼⠖⠈⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣟⣿⣻⣟⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣭⠷⠫⠛⠻⠻⠻⠿⣿⣿
⣫⡉⣿⣿⣿⣿⣿⣷⣆⣨⣘⣃⠃⢠⣭⢈⡼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠸⢸⢿⣷⣿⣿⣿⣿⣿⣧⠰⢤⠓⡙⠙⠻⠮⢱⣘⣐⠉⢊⠥⠴⠉⠁⠐⠀⠐⣐⣀⣤⣤⣦⣽⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠗⡘⠻⡿⠿⠿⠿⠿⡿⠲⣼⡀⠬⠍⠐⠈⠉⠄⢰⠼⡋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡉⢻⣿⣿⣿⣿⣏⢊⡑⡋⠨⠩⠉⠙⠈⢲⢸⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣽⣽⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡔⠀⢈⠙⠛⠻⠛⠿⠿⠿⠎⡙⢚⡂⣠⠰⠺⠊⠈⠀⢐⡉⠑⢀⠀⢀⠀⠴⠡⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣷⣷⣿⣿⣿⣿⣦⡐⠊⠙⠛⠛⣛⢩⠬⠄⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣋⢿⣿⣿⣿⣿⣿⢋⡼⢗⣎⢿⣿⣿⣿⣯⠐⠾⠬⠼⠵⢥⠼⢓⠘⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠬⢀⠈⠨⢤⣤⣡⠠⡄⡀⠀⡐⢐⡀⠀⣀⣐⣀⠠⠴⣋⠄⠯⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣷⣲⣶⣶⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⣙⣾⣿⣿⡿⢏⣺⠈⢀⢱⢼⡸⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣋⣡⣒⣚⣸⣽⣥⣶⣦⣀⣀⠒⠞⠲⠒⠶⢌⣓⣨⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣎⣉⠶⡚⠫⠤⠂⢠⠸⠚⠾⢮⢘⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣳⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢉⢹⣿⣿⣿⣷⢌⢈⣹⠢⢡⡀⠐⠩⢁⣛⣩⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⠘⡑⠰⡦⠉⠁⢐⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⣛⣋⣙⣛⣛⡛⠻⠦⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⠢⢣⡗⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣵⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣋⣴⠿⠛⠭⢸⢲⢰⢖⠃⠈⠉⠘⢷⢀⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⡷⣘⢿⣿⡿⠟⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠽⢃⣉⣬⣁⣭⣭⣴⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣜⢄⠎⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢔⢁⠜⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⠞⠛⠑⡶⠻⠟⢍⣒⣳⣡⠅⢀⢲⡇⠠⡸⢸⣌⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⠁⠲⣰⢶⢫⡬⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠶⢙⡼⣞⠻⠍⢛⣀⣥⠶⣒⡮⡻⣟⣽⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠟⠛⠙⢉⣙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣏⠩⠩⠭⠭⠑⠙⠐⠂⡂⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⡔⠴⢩⡾⠐⠄⢐⡲⠶⢖⣮⣈⠈⢺⣮⢬⠀⠘⢌⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣧⢠⡸⢀⠈⠐⣿⣿⣿⣿⣿⣿⣿⣿⠏⠴⠉⣠⣟⢳⣬⠶⢞⠛⠕⠞⡈⣨⢹⣆⠞⣹⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⢍⠛⠻⠿⣟⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⣩⠤⠀⠁⢠⡈⠉⣿⣶⣤⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣮⢠⡬⠂⠐⠀⠙⢠⡁⠌⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣠⡾⠢⠠⠄⢀⡀⣀⠁⢉⠉⣁⢈⠈⢀⣣⢌⢘⢖⠤⡜⣼⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⢡⢀⣉⣀⣀⣉⢻⣿⣿⣿⣿⣿⡹⢩⣹⣿⠇⣁⡢⠂⡆⠤⠠⣰⣿⠺⣫⠘⡘⢻⡃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⢀⡠⠋⡁⣂⣼⢧⡁⠒⣬⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠏⣴⠋⠀⠀⣤⣸⢕⠂⠀⣴⢮⣙⢷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣼⣿⣿⣿⣿⣿⡾⣟⣿⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣐⣱⠤⢲⣺⢀⣰⣾⣶⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⡟⣀⠀⠀⠀⠀⠀⠤⠦⠥⠮⠤⠦⠂⢒⢨⢹⢦⢙⠰⠁⢿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣨⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡓⠃⢱⡚⠉⣁⡬⢳⢈⢠⠲⣺⠝⢸⠈⡐⣂⣂⠆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⢀⡞⣠⡞⢏⡹⠒⠋⡄⡃⠙⢹⣩⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠰⡇⢰⣤⡄⠉⠑⡡⠞⣶⣉⢶⠌⢁⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣋⢲⣱⣸⣤⣿⢻⡜⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣨⣶⣿⣿⣀⢻⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⡈⠉⠻⢲⣢⣠⢀⣀⢀⠀⠀⠀⠤⠤⠄⠿⢧⢻⡜⡼⣤⢸⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣏⢢⠰⣽⡞⢯⠙⢡⠺⠞⠽⡑⠹⠀⢠⢯⡾⣽⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠐⠀⠈⢳⣯⠜⣡⢳⠈⡑⢠⠃⢰⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠈⣛⠈⠉⠴⢀⠘⡓⢞⣩⢟⢈⢰⢟⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⠯⢦⡿⣏⡷⣿⢿⣾⢻⡝⡷⠿⠾⠹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⢸⣶⡀⣌⠩⠀⠐⠀⣀⠒⠐⢈⢠⢂⢤⡐⠙⢸⡇⢿⠺⠘⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡆⠙⡀⢹⢖⢵⠄⠨⠉⠠⠠⢚⢀⢬⢫⣿⢟⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠄⠀⠄⠹⡙⠓⡉⢄⡃⠂⣼⢋⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣦⣷⠋⣈⣁⣵⣊⢲⢛⡱⠀⣠⠔⣛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿⢦⢂⡿⣱⣏⣞⡥⡏⠄⣩⣜⠊⠉⠽⠟⣈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣣⢫⣇⣨⣭⠤⣠⣄⣀⠈⠔⠁⡂⠔⠖⡒⣻⠦⢹⢸⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣄⢫⣚⣂⡙⠻⢜⣴⣰⠘⠇⢫⢉⢩⣓⡘⢃⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠄⠠⢅⡩⠔⠡⢠⠟⢈⢄⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣆⢛⣉⣙⢘⣂⣭⠔⠐⣑⣠⠾⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⡎⣾⢱⢷⡎⣿⢱⡎⣯⡻⣳⠎⢔⢮⢟⢣⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⠠⠹⣗⣒⣐⣉⠭⡥⣬⣬⣔⣨⡈⠩⠂⠖⠚⡼⢊⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣘⠀⠚⠙⢙⣘⣹⢩⠭⠡⢌⠬⠴⠲⢫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣷⣆⠀⠀⠺⣀⠈⠀⡁⡠⣱⡿⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣭⣛⠿⡷⣶⠿⡟⣯⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣟⣮⡜⣫⢞⢾⣡⢷⠽⢿⠞⢐⣲⢈⢮⣾⢃⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡮⣐⡠⠭⢙⢛⣒⣲⡒⢒⣚⣚⣛⣛⣭⠴⢫⣴⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣶⣌⠡⣉⣉⣙⣚⣘⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣿⡇⣦⡔⢿⢻⡽⢾⣫⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣷⣻⢙⠪⢷⡿⢬⣕⡁⣮⣿⠇⢠⢸⢟⣾⣿⢸⣿⣿⣿⣿⣯⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣶⣥⡲⠮⠭⠌⠚⢘⣈⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣣⣽⣷⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⢨⣜⢸⣮⠺⠌⢥⣼⡟⢱⣼⣜⢨⡾⢯⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⣮⣍⠙⠰⢈⣟⠝⣴⣿⢉⣔⣯⣿⢹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣠⡀⣌⢩⣜⠯⠷⠾⣙⣨⣴⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣷⣤⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⠰⣄⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
    time.sleep(3)
    print("You manage to escape the escape the attack somehow and flee towards a collection of planets.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice12and15and16()


def Choice9():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r"""	
+------------------------------------------------------------------------+
|                                                                        |
|  +------------------------------------------------------------------+  |
|  |                                                                  |  |
|  |                     Error                                        |  |
|  |                     Error                                        |  |
|  |                     Error                                        |  |
|  |                     Crashed                                      |  |
|  |                     Restarting                                   |  |
|  |                     Error..                                      |  |
|  |                                                                  |  |
|  |                                                                  |  |
|  |                                                                  |  |
|  +------------------------------------------------------------------+  |
|        f0    f1    f2    f3    f4    f5    f6    f7    f8    f9        |
+------------------------------------------------------------------------+
|                                                                        |
|  [f0]  [f1]  [f2]  [f3]  [f4]  [f5]  [f6]  [f7]  [f8]  [f9]   [On/Off] |
|                                                                        |
|     [Q]  [W]  [E]  [R]  [T]  [Y]  [U]  [I]  [O]  [P]   [<] [^] [v] [^] |
|                                                                        |
|     [Q]  [W]  [E]  [R]  [T]  [Y]  [U]  [I]  [O]  [P]   [7] [8] [9] [/] |
|                                                                        |
|       [A]  [S]  [D]  [F]  [G]  [H]  [J]  [K]  [L]      [4] [5] [6] [*] |
|                                                                        |
|  [CTRL]  [Z]  [X]  [C]  [V]  [B]  [N]  [M]  [ ENTER ]  [1] [2] [3] [-] |
|                                                                        |
|  [SHIFT]  [ALT]   [    space    ]   [,]  [.]  [SHIFT]  [0] [.] [=] [+] |
|                                                                        |
+------------------------------------------------------------------------+
""")
    time.sleep(3)
    print(
        "When you arrive back to your ship all the alien creatures have already gone, but you see there is damage "
        "to the computers.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice17()


def Choice10():
    global PlayerFuel
    LoseFuel(5)
    FuelCheck()
    print(r"""         ___---___                    
      .--         --.      
    ./   ()      .-. \.
   /   o    .   (   )  \
  / .            '-'    \         
 | ()    .  O         .  |      
|                         |      
|    o           ()       |
|       .--.          O   |            
 | .   |    |            |
  \    `.__.'    o   .  /    
   \                   /                   
    `\  o    ()      /'                
      `--___   ___--'
            ---""")
    print("You Land on the small moon")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice13and18and19()


def Choice11():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print("You board your Ship and go to small moon in the distance.")
    time.sleep(3)
    print(r"""██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████
██████▓▓▓▓░░          ░░▒▒▓▓▓▓▓▓██████████████████
██████░░  ░░  ░░░░░░░░      ▒▒▓▓▓▓██████████▒▒░░██
████░░  ░░▒▒▒▒░░░░▒▒▒▒░░░░    ▒▒▓▓▓▓██████████▓▓██
▓▓░░▒▒░░░░░░▓▓▒▒▒▒░░▒▒▒▒░░░░░░  ▒▒▓▓▓▓████████▓▓██
▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░  ▒▒▓▓▓▓██████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░▒▒░░░░  ▓▓▓▓██████████
██████████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░▓▓▓▓████████
████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░  ▒▒░░  ▓▓▓▓████████
████████████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓████████
██████████████▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒░░░░▓▓████████
██████████████▓▓▓▓▒▒▒▒▓▓▓▓░░░░▒▒▒▒▒▒░░  ▓▓████████
████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
████████████████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓██████
██████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓████████
████████████████████████▓▓██▓▓▓▓▓▓▒▒░░▓▓██████████
████████████████████████████▓▓▓▓▒▒  ░░▓▓██████████
████████████████████████████▓▓▓▓░░░░▓▓▓▓██████████
██████████████████████████████▒▒▒▒░░▓▓████████████
████████████████████████████▓▓▓▓░░████████████████
████████████████████████▓▓▓▓▓▓▒▒██▓▓██████████████""")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice13and18and19()


def Choice12():
    global PlayerFuel
    LoseFuel(0)
    FuelCheck()
    print(r"""	
    +------------------------------------------------------------------------+
    |                                                                        |
    |  +------------------------------------------------------------------+  |
    |  |                                                                  |  |
    |  |                     Error                                        |  |
    |  |                     Error                                        |  |
    |  |                     Error                                        |  |
    |  |                     Crashed                                      |  |
    |  |                     Restarting                                   |  |
    |  |                     Error..                                      |  |
    |  |                                                                  |  |
    |  |                                                                  |  |
    |  |                                                                  |  |
    |  +------------------------------------------------------------------+  |
    |        f0    f1    f2    f3    f4    f5    f6    f7    f8    f9        |
    +------------------------------------------------------------------------+
    |                                                                        |
    |  [f0]  [f1]  [f2]  [f3]  [f4]  [f5]  [f6]  [f7]  [f8]  [f9]   [On/Off] |
    |                                                                        |
    |     [Q]  [W]  [E]  [R]  [T]  [Y]  [U]  [I]  [O]  [P]   [<] [^] [v] [^] |
    |                                                                        |
    |     [Q]  [W]  [E]  [R]  [T]  [Y]  [U]  [I]  [O]  [P]   [7] [8] [9] [/] |
    |                                                                        |
    |       [A]  [S]  [D]  [F]  [G]  [H]  [J]  [K]  [L]      [4] [5] [6] [*] |
    |                                                                        |
    |  [CTRL]  [Z]  [X]  [C]  [V]  [B]  [N]  [M]  [ ENTER ]  [1] [2] [3] [-] |
    |                                                                        |
    |  [SHIFT]  [ALT]   [    space    ]   [,]  [.]  [SHIFT]  [0] [.] [=] [+] |
    |                                                                        |
    +------------------------------------------------------------------------+
    """)
    time.sleep(3)
    print("You board the Shuttle to a Worm Hole,\n but along the way the shuttles guidance computers fail!")
    time.sleep(5)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice017()


def Choice13():
    global PlayerFuel
    LoseFuel(0)
    FuelCheck()
    print(r"""                       .,,uod8B8bou,,.
                  ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
             ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
             !...:!TVBBBRPFT||||||||||!!^^""'   ||||
             !.......:!?|||||!!^^""'            ||||
             !.........||||                     ||||
             !.........|||| error               ||||
             !.........||||  error              ||||
             !.........||||   error             ||||
             !.........||||           error     ||||
             !.........||||            error    ||||
             `.........||||             error  ,||||
              .;.......||||               _.-!!|||||
       .,uodWBBBBb.....||||       _.-!!|||||||||!:'
    !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb.... 
    !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
    !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
    !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.  
    !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
    `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
      `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
        `........::::::::::::::::;iof688888888888888888888b.     `
          `......:::::::::;iof688888888888888888888888888888b.
            `....:::;iof688888888888888888888888888888888899fT!  
              `..::!8888888888888888888888888888888899fT|!^"'   
                `' !!988888888888888888888888899fT|!^"' 
                    `!!8888888888888888899fT|!^"'
                      `!988888888899fT|!^"'
                        `!9899fT|!^"'
                          `!^"'
    """)
    time.sleep(3)
    print("You Head back to ship to check computers.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Choice17()


def Choice15():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print(r"""██████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████████████████
████████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░▒▒▒▒▒▒▓▓████████████████████████
████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒██████████████████████
██████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒████████████████████
████████████████████▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓██████████████████
████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▓▓██████████████
██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓████████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░  ░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▓▓██████████
██████████▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒██████████
████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓██████
████████▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
████▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒▒▒░░▒▒░░▒▒░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒██
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░░░  ░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒  ░░░░░░░░░░▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
██▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒
██▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒░░▒▒░░  ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒
██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒
██▓▓▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒██
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒██
████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░  ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓████
████████▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
██████████▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒░░░░▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████
████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████
██████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
██████████████████▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████
████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████
████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████████████
██████████████████████████▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▓▓▒▒▓▓████████████████████████
██████████████████████████████▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████████████████████████
████████████████████████████████████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓████████████████████████████████
""")
    time.sleep(3)
    print("You board the Ship and you land on another planet where there's fuel supplies for your ship")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    DistantPlanet()


def Choice16():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r"""
 .      .   . .   .  +   .    .         
                   .       .      
 .     *
  .       *           . . 
.               :.       +   . 
.  .   .  + .
     __ __________________
    / +.         .   *    "-_
   /   .  Y  .               \
  /   : \ | / ;    +   .      \
 /  +  '-___-'   .   .    + .  \
/_______________________________\
     ____| |________________.J' #L
    /.+  J L   .   .     . +..    \
   /    / ! \     +   .            L
  /   :'  x  ':         :     .    F
 / .   '-___-'  +..  .     *      /
/______________________________-="
        .    * . . .  .     .
. .     .      .
           .      .   .        ! /
      *             .        - O -
          .     .          . / |
               .  .. +  .
.   .  *   .      +..  .          *""")
    time.sleep(3)
    print("You board the Ship")
    time.sleep(2)
    print("You fire up the ships engines and head into a close by worm-hole in hope you find a way back to Earth!")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Wormhole()


def Choice17():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r""" ________________________________         
      /                                "-_          
     /      .  |  .                       \          
    /      : \ | / :                       \         
   /        '-___-'                         \      
  /_________________________________________ \      
       _______| |________________________--""-L 
      /       F J                              \ 
     /       F   J                              L
    /      :'     ':                            F
   /        '-___-'                            / 
  /_________________________________________--"  """)
    time.sleep(3)
    print("You fire up the ships engines and head into a close by worm-hole,\n in hope you find a way back to Earth!")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Wormhole()


def Choice18():
    global PlayerFuel
    LoseFuel(15)
    FuelCheck()
    print(r"""    .+++++.
   | ~~~~~ |
   ) '*_*' (
   (  ._.  )
    '.._..'    
  _,/\   /\,_
 /    ':'    \
""")
    time.sleep(3)
    print("You make your way towards the Merchant in the background.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    time.sleep(3)
    Merchant()


def Choice19():
    global PlayerFuel
    LoseFuel(10)
    FuelCheck()
    print(r"""                                       ,:
                                                 ,' |
                                                /   :
                                             --'   /
                                             \/ />/
                                             / 
   /_/      __
            \ \_____
         ###[==_____>
            /_/
""")
    time.sleep(3)
    print("You Travel towards the wormhole hastily.")
    time.sleep(3)
    print(f"Your Remaining Fuel is {PlayerFuel}")
    Wormhole()


def Choice1and2():
    print(r'" .              +   .                .   . .     .  .' "\n"
          r"                   .                    .       .     *" "\n"
          r"  .       *                        . . . .  .   .  + ." "\n"
          r'            "You Are Here"            .   .  +  . . .' "\n"
          r".                 |             .  .   .    .    . ." "\n"
          r"                  |           .     .     . +.    +  ." "\n"
          r"                 \|/            .       .   . ." "\n"
          r"        . .       V          .    * . . .  .  +   ." "\n"
          r"           +      .           .   .      +" "\n"
          r"                            .       . +  .+. ." "\n"
          r"  .                      .     . + .  . .     .      ." "\n"
          r"           .      .    .     . .   . . .        ! /" "\n"
          r"      *             .    . .  +    .  .       - O -" "\n"
          r"          .     .    .  +   . .  *  .       . / |" "\n"
          r"               . + .  .  .  .. +  ." "\n"
          r".      .  .  .  *   .  *  . +..  .            *" "\n"
          r" .      .   . .   .   .   . .  +   .    .            +"
          "")
    time.sleep(3)
    print(f"Your Starting Fuel is {PlayerFuel}.")
    print("Choose a path to take.")
    print("1. Travel to small planet.", "-5 Fuel.")
    print("2. Head out to Asteroid belt.", "-10 Fuel.")
    time.sleep(3)
    Choice1and2Input = input("")
    if Choice1and2Input == "1":
        Choice1()
    elif Choice1and2Input == "2":
        Choice2()
    else:
        print("Please enter an input.")
    Intro()


def Choice3and4():
    print("")
    time.sleep(1)
    print("Would you like to?")
    print("Choice 1. Look for people?", "-10 Fuel.")
    print("Choice 2. Head back to the Ship.", "-15 Fuel")
    Choice3and4Input = input("")
    if Choice3and4Input == "1":
        Choice3()
    elif Choice3and4Input == "2":
        Choice4()
    else:
        print("Please enter an input.")
    Choice1()


def Choice5and6():
    print("You begin searching, looking for anything that could be used for supplies.")
    time.sleep(1)
    print("Do you want to?")
    time.sleep(2)
    print("Choice 1. Land on an asteroid and take a closer inspection.", "-5 Fuel")
    time.sleep(2)
    print("Choice 2. Keep Searching along the asteroid belt.", "-10 Fuel")
    Choice5and6Input = input("")
    if Choice5and6Input == "1":
        Choice5()
    elif Choice5and6Input == "2":
        Choice6()
    else:
        print("Please enter an input.")
    Choice2()


def Choice07():
    print("")
    time.sleep(1)
    print("Where do you want to go?")
    print("1. Space Casino?", "0 Fuel")
    print("2. Shuttle Station?", "-15 Fuel")
    GambleCheck = input("")
    if GambleCheck == "1":
        CasinoGame()
    elif GambleCheck == "2":
        Choice12and15and16()
    else:
        print("Please enter an input.")
    Choice3()


def Choice8and9and10():
    print(r"""                                         )  (  (    (
                                         (  )  () @@  )  (( (
                                     (      (  )( @@  (  )) ) (
                                   (    (  ( ()( /---\   (()( (
     _______                            )  ) )(@ !O O! )@@  ( ) ) )
    <   ____)                      ) (  ( )( ()@ \ o / (@@@@@ ( ()( )
 /--|  |(  o|                     (  )  ) ((@@(@@ !o! @@@@(@@@@@)() (
|   >   \___|                      ) ( @)@@)@ /---\-/---\ )@@@@@()( )
|  /---------+                    (@@@@)@@@( // /-----\ \\ @@@)@@@@@(  .
| |    \ =========______/|@@@@@@@@@@@@@(@@@ // @ /---\ @ \\ @(@@@(@@@ .  .
|  \   \\=========------\|@@@@@@@@@@@@@@@@@ O @@@ /-\ @@@ O @@(@@)@@ @   .
|   \   \----+--\-)))           @@@@@@@@@@ !! @@@@ % @@@@ !! @@)@@@ .. .
|   |\______|_)))/             .    @@@@@@ !! @@ /---\ @@ !! @@(@@@ @ . .
 \__==========           *        .    @@ /MM  /\O   O/\  MM\ @@@@@@@. .
    |   |-\   \          (       .      @ !!!  !! \-/ !!  !!! @@@@@ .
    |   |  \   \          )   -cfbd-   .  @@@@ !!     !!  .(. @.  .. .
    |   |   \   \        (    /   .(  . \)). ( |O  )( O! @@@@ . )      .
    |   |   /   /         ) (      )).  ((  .) !! ((( !! @@ (. ((. .   .
    |   |  /   /   ()  ))   ))   .( ( ( ) ). ( !!  )( !! ) ((   ))  ..
    |   |_<   /   ( ) ( (  ) )   (( )  )).) ((/ |  (  | \(  )) ((. ).
____<_____\\__\__(___)_))_((_(____))__(_(___.oooO_____Oooo.(_(_)_)((_""")
    time.sleep(2)
    print(
        "You succeed in fending off the attack with some weapons you accidentally found whilst hiding inside a closet.")
    time.sleep(3)
    print("After recovering from the struggle, what would you like to do?")
    time.sleep(1)
    print("Choice 1. Head towards the space between a collection of planets.", "-5 Fuel")
    time.sleep(1)
    print("Choice 2. Remain on your current course, and brave the upcoming storm.", "-15 Fuel")
    time.sleep(1)
    print("Choice 3. Head to the small moon on the other side and investigate.", "-5 Fuel")
    Choice8and9and10Input = input("")
    if Choice8and9and10Input == "1":
        Choice8()
    elif Choice8and9and10Input == "2":
        Choice9()
    elif Choice8and9and10Input == "3":
        Choice10()
    else:
        print("Please enter an input.")
    Choice4()


def Choice011():
    print("After landing on a small asteroid you see an abandoned ship that may be useful to you.")
    time.sleep(1)
    print("Do you want to attempt to salvage the ship.")
    print("1. Yes?", "0 Fuel")
    print("2. No?", "-10 Fuel")
    GambleCheck = input("")
    if GambleCheck == "1":
        RollSuccess()
    elif GambleCheck == "2":
        Choice13and18and19()
    else:
        print("Please enter an input.")
    Choice011()


def Choice12and15and16():
    print("You finish exploring the small planet.")
    time.sleep(1)
    print("Do you want to?")
    time.sleep(1)
    print("Choice 1. Return to the Ship.", "0 Fuel")
    print("Choice 2. Leave to explore the distant planet.", "-10 Fuel")
    print("Choice 3. Leave to investigate the Wormhole.", "-15 Fuel")
    Choice12and15and16Input = input("")
    if Choice12and15and16Input == "1":
        Choice12()
    elif Choice12and15and16Input == "2":
        Choice15()
    elif Choice12and15and16Input == "3":
        Choice16()
    else:
        print("Please enter an input.")
    Choice11()


def Choice13and18and19():
    print(
        "On arrival at the small moon you recieve an alert that your ships computers have failed, You also see a "
        "wandering merchant that may be useful and a wormhole has appeared in the distance.")
    time.sleep(3)
    print("Do you want to?")
    print("Choice 1. Head back to ship to check computers.", "0 Fuel")
    print("Choice 2. Speak to merchant.", "-15 Fuel")
    print("Choice 3. Go and investigate the wormhole.", "-10 Fuel")
    time.sleep(1)
    Choice13and18and19Input = input("")
    if Choice13and18and19Input == "1":
        Choice13()
    elif Choice13and18and19Input == "2":
        Choice18()
    elif Choice13and18and19Input == "3":
        Choice19()
    else:
        print("Please enter an input.")
    Choice10()


def Choice017():
    print(
        "You spend a few days repairing the computers on your Ship, You eventually get everything working again and "
        "take a day to rest")
    time.sleep(3)
    print(
        "Whilst resting you start being pulled towards a wormhole. You rush to take your seat and try to escape.")  # taken to wormhole
    Wormhole()


def DistantPlanet():
    global PlayerFuel
    FuelCheck()
    print(r"""██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████▓▓▓▓▒▒▓▓████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████▓▓▓▓▓▓▒▒▓▓██████████████████████▓▓██████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒████████████████▒▒░░░░  ░░░░▓▓████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▒▒▒▒██████████████░░      ░░    ░░▓▓██████████████████████████████████████████████████████████████████████████████▓▓▒▒
████████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓████████████░░    ░░      ░░  ░░██████████████████████████████████████████████████████████████████████████████░░░░
██████████████████████████████████████████████████████▓▓▓▓▓▓▓▓██████████████░░    ░░  ░░░░      ▒▒██████████████████████████████████████████████████████████████████████████████▓▓
██████████████████████████████████████████████████████████████████████████▓▓          ░░        ░░████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████▒▒    ░░          ░░  ░░████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████                    ▒▒████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████░░░░              ░░▓▓████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████░░            ░░▒▒██████████████████████████████████████████████████████████████████████████████████
████████████▓▓▓▓████████████████████████████████████████████████████████████████░░    ░░░░░░▒▒████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████▓▓██▓▓████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████▓▓▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████▓▓▓▓██████████████████████████████████████████████████████░░██████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████▓▓██████████████████████████████████████████████████████████████████
██████████████████▓▓▓▓██████████████████░░██████████████████████████████████████████████████████████████████▓▓▓▓████▓▓▒▒▒▒████████████████████████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▒▒▓▓████████████████████████████████████████████████████████████████████████████████████████▓▓▓▓▒▒▓▓████████████████████████████████████████████████████████
██████████████████▓▓▓▓▓▓▓▓████████████████████████████████████████████████████████████████████████████████████████▒▒▓▓▒▒▓▓████████████████████████████████████████████████████████
██▓▓▒▒██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████████████████████████████████████████████████████████████████████████▓▓▓▓▓▓████████████████████████████████████████████████████████
██▒▒▒▒▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████████████████████████████████████████████████████████████████████████▓▓██████████████████████████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████▓▓██▓▓████████████▓▓██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████▓▓▓▓▓▓██████████▓▓▓▓▓▓████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
""")
    time.sleep(5)
    print("As you land on the planet a figure emerges from the tall grass ahead. The figure starts shouting in what "
          "appeared to be gibberish, you realised it was very familiar.")
    time.sleep(2)
    MathTrivia()


def Wormhole():
    global PlayerFuel
    FuelCheck()
    print(r"""██████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████▓▓██████████
████████████▓▓████████████████████████████████████████████████████████████████████████████████████████████
████████████▓▓▓▓██████████████████████████████████████████████████████████████████████████████████████████
████████████▓▓██████████████████████████████▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████████████████████████
████████████████████████████████████████▓▓▒▒░░▓▓▓▓██████▓▓▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████
████████████████████████████████▓▓██████▓▓░░  ░░▓▓████▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓████████████████████
██████████████████████████████▓▓████████▓▓░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████
████████████████████████████▓▓▒▒▓▓██████▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓██████████████
████████████████████████████████▓▓██████▓▓▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒░░▒▒░░░░░░  ░░░░▒▒▒▒░░▒▒▓▓▒▒▓▓▓▓▓▓██████████
██████████████████████████████████████████▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░░░      ░░░░░░▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓████████
████████████████████████████████████████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░          ░░  ░░▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓██████
██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒░░▒▒        ░░  ░░░░▒▒▓▓▒▒▓▓░░▓▓▓▓▓▓████
██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒  ░░░░░░▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓██
██████████████████████████████████████▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒░░░░▒▒░░░░░░▒▒░░░░▒▒▓▓▓▓░░▒▒▓▓▓▓▓▓▓▓
████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓
██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓
██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░▓▓██
██████████████████▓▓▓▓▒▒▒▒██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒░░▒▒▓▓
████████████████████████▓▓░░██████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒██
░░▒▒▓▓████████▓▓▓▓▓▓▓▓▓▓██▒▒▓▓██████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓████████████████▓▓████████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░░░    ░░▒▒▒▒▓▓▓▓██████████████████████████▓▓▓▓▓▓▓▓▓▓  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████
▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▓▓██████████████▓▓████████████▓▓▓▓▓▓▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████
▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓██████████████████████████████████▓▓██████▓▓████▓▓▓▓██████▓▓████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░▒▒▓▓██▓▓████████████████████████████████████████████████████▓▓████
▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░  ▒▒██████████████████████████████████████████▓▓████████████████
▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒████████████████████████████████████████████████████████
██▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░  ▒▒██████████████▓▓████████████████████████████████████
████▓▓████████████████▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░  ░░▓▓████████████████████████████████████████████████""")
    time.sleep(5)
    print("You arrive at the Edge of the Wormhole, It look alot bigger up close.")
    if PlayerFuel <= 15:
        Safe()
    elif PlayerFuel <= 0:
        Stranded()
    else:
        Stranded()


def Merchant():
    global PlayerFuel
    FuelCheck()
    print(r"""      .#####.
       |_____|
      (\#/ \#/)
       |  U  |
       \  _  /
        \___/
    .---'   `---.
   /  #########  \
  /  |####|####|  \
 /  /\ ####### /\  \
(  \  \  ###  /  /  )
 \  \  \_###_/  /  /
  \  \ |\   /| /  /
   'uuu| \_/ |uuu'
       |  |  |
       |  |  |
       |  |  |
       |  |  |
  dp   |  |  |
       )  |  (
     .oooO Oooo.""")
    time.sleep(3)
    print("You approach the Merchant and you start to greet him, he quickly interrupts you.")
    run_quiz(questions)


def Home():
    print(r"""        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.""")
    time.sleep(2)
    print(r"""
          *                 *                  *              *
                                                      *             *
                        *            *                             ___
  *               *                                          |     | |
        *              _________##                 *        / \    | |
                      @\\\\\\\\\##    *     |              |--o|===|-|
  *                  @@@\\\\\\\\##\       \|/|/            |---|   |L|
                    @@ @@\\\\\\\\\\\    \|\\|//|/     *   /     \  |.|
             *     @@@@@@@\\\\\\\\\\\    \|\|/|/         |  U    | |C|
                  @@@@@@@@@----------|    \\|//          |  .    |=| |
       __         @@ @@@ @@__________|     \|/           |  K    | | |
  ____|_@|_       @@@@@@@@@__________|     \|/           |_______| |_|
=|__ _____ |=     @@@@ .@@@__________|      |             |@| |@|  | |
____0_____0__\|/__@@@@__@@@__________|_\|/__|___\|/__\|/___________|_|_
""")
    time.sleep(3)
    print(
        "with supplies running low you manage to make it home and are greeted by your friends and family who cant "
        "wait to hear all about you adventures in the cosmos,\n you are happy in the knowledge you have survived the "
        "worst the universe has to throw at you…")
    time.sleep(3)
    SecretCheck()


def Safe():
    print(r"""██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████
██████▓▓▓▓░░          ░░▒▒▓▓▓▓▓▓██████████████████
██████░░  ░░  ░░░░░░░░      ▒▒▓▓▓▓██████████▒▒░░██
████░░  ░░▒▒▒▒░░░░▒▒▒▒░░░░    ▒▒▓▓▓▓██████████▓▓██
▓▓░░▒▒░░░░░░▓▓▒▒▒▒░░▒▒▒▒░░░░░░  ▒▒▓▓▓▓████████▓▓██
▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░  ▒▒▓▓▓▓██████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░▒▒░░░░  ▓▓▓▓██████████
██████████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░▓▓▓▓████████
████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░  ▒▒░░  ▓▓▓▓████████
████████████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓████████
██████████████▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒░░░░▓▓████████
██████████████▓▓▓▓▒▒▒▒▓▓▓▓░░░░▒▒▒▒▒▒░░  ▓▓████████
████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
████████████████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ▓▓▓▓██████
████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓██████
██████████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓████████
████████████████████████▓▓██▓▓▓▓▓▓▒▒░░▓▓██████████
████████████████████████████▓▓▓▓▒▒  ░░▓▓██████████
████████████████████████████▓▓▓▓░░░░▓▓▓▓██████████
██████████████████████████████▒▒▒▒░░▓▓████████████
████████████████████████████▓▓▓▓░░████████████████
████████████████████████▓▓▓▓▓▓▒▒██▓▓██████████████""")
    time.sleep(2)
    print(
        "you crash on to a uninhabited planet similar to earth there lots of resources and the climate is nice,"
        " But even though you are safe, you miss your loved ones and can only dream of sleeping in your own bed…")
    time.sleep(2)
    print("You found the Secret Word 'Home'.")
    AddSecret(1)
    EndGame()


def Stranded():
    print(r"""████████████████████████████████████████████████████████████████████████████▓▓▓▓▓▓████████████
██████████████████████████████████████████████▓▓██████████████████████████████▓▓██▓▓████▓▓▓▓██
██████████████████▓▓██░░████████████████████████████████████████████████▓▓▓▓▓▓▓▓████▓▓████████
████████████▓▓██▓▓████████████████████████████████████████████████████▓▓██████▓▓▓▓▓▓▓▓▓▓██████
██████████████████████████████████▓▓██████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓████
██████████████████████████████████████▓▓████████████████████████████▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
██████████████████████████████████████████████▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████
████████████████████████████████████████████████████████▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓████████
████████████████████████████▓▓██████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████
██████████████████████████████████████████████▓▓▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████▓▓
██████████████████████████████████████████▓▓▓▓▒▒▒▒░░░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████
██████████████████████████████████████▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒░░▒▒▒▒▓▓▓▓▓▓████████████████
██████████████████████████████████▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓████████████████████
██████████████████████▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██████████████████████
████████████████████████▓▓██▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓██████████████████████████
████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████████████████▒▒██
████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓████████████████████████████████
██████████████████▓▓▒▒░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████████████████▓▓████████████
████▓▓████████████▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████████████████████████████████████████
██████████████▓▓▓▓░░░░░░▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████████████████████████████████████████████
██████████▓▓▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████████████████████████████████████▓▓██████▓▓
██████████▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████████▓▓████████████████████████▓▓████████▓▓██████
▓▓████████▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓██████████████▓▓▒▒▓▓████▒▒████████████▓▓████████████████
████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▓▓████▓▓██████████████████▓▓▒▒██▓▓██████████████████████████████▓▓
██████████▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓██████████████████████████████████████████████████████████████████
██████▓▓████▓▓▓▓▓▓▓▓▓▓████▓▓██████████████████████████████████████████████████████████████████
▓▓██▓▓██▓▓▓▓██▓▓▓▓▓▓██████████████████████████████████████████████████████████████▓▓██████▓▓██
▒▒████████▓▓▒▒▒▒▓▓████████████████████████████████████████████▓▓████████████████████████▓▓████
████████▓▓░░▒▒▓▓██████████████████████████████████████████████████████████████████████████████
██████▒▒▓▓▓▓▓▓████████▓▓████████████████████▓▓████████████████████████████████████████████▓▓██
██████████▓▓██████████▓▓██████████████████████████████████████████████████████████████████████""")
    time.sleep(5)
    print(
        "The worm-hole leads you deeper into the unknown depths of space, with no fuel and no guidance computers you "
        "are stranded in deep space... forever...")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(". or are you???")
    time.sleep(2)
    EndGame()


print(r"""------------    ------    ----            ------    ------------ ------------ --------  ------------        --------   ----------   ---      --- ------------ ------------ ------------ ---      --- 
************   ********   ****           ********   ************ ************ ********  ************       **********  ************  ***    ***  ************ ************ ************  ***    ***  
----          ----------  ----          ----------  ---          ------------   ----    ---               ----    ---- --        --   ---  ---   ----         ----         ----           ---  ---   
****  ****** ****    **** ****         ****    **** ***              ****       ****    ***               ***      *** **        **    ******    ************ ************ ************    ******    
----  ------ ------------ ----         ------------ ---              ----       ----    ---               ---      --- --        --     ----     ------------ ------------ ------------     ----     
****    **** ************ ************ ************ ***              ****       ****    ***               ****    **** **        **     ****            *****        ***** ****             ****     
------------ ----    ---- ------------ ----    ---- ------------     ----     --------  ------------       ----------  ------------     ----     ------------ ------------ ------------     ----     
************ ****    **** ************ ****    **** ************     ****     ********  ************        ********   **********       ****     ************ ************ ************     ****     """)
time.sleep(2)
print(r"""   ------         ------------ ------------ ---      --- ------------ - -----------     ------    ------------ ------------ ----------   
  ********        ************ ************  ***    ***  ************   ***********    ********   ************ ************ ************ 
 ----------       ------------ ----           ---  ---   ------------   ----       -  ----------  ----         ----         --        -- 
****    ****          ****     ************    ******        ****       ***********  ****    **** ************ ************ **        ** 
------------          ----     ------------    ------        ----       -----------  ------------ ------------ ------------ --        -- 
************          ****     ****           ***  ***       ****       ****       * ************        ***** ****         **        ** 
----    ----          ----     ------------  ---    ---      ----       -----------  ----    ---- ------------ ------------ ------------ 
****    ****          ****     ************ ***      ***     ****       ***********  ****    **** ************ ************ **********   
                                                                                                                                         """)
time.sleep(2)
print(r"""------------ -----------     ------    ------------ ------------      ------------ ----    ---- -----------  ---    ---  --------  ---    ---     ------    ----         
************ ************   ********   ************ ************      ************ ****    **** ***********  ***    ***  ********  ***    ***    ********   ****         
----         ---      ---  ----------  ---          ----              ----         ----    ---- ----    ---  ---    ---    ----    ---    ---   ----------  ----         
************ ************ ****    **** ***          ************      ************ ****    **** *********    ***    ***    ****    ***    ***  ****    **** ****         
------------ -----------  ------------ ---          ------------      ------------ ----    ---- ---------    ---    ---    ----    ---    ---  ------------ ----         
       ***** ****         ************ ***          ****                     ***** ************ ****  ****    ********     ****     ********   ************ ************ 
------------ ----         ----    ---- ------------ ------------      ------------ ------------ ----   ----    ------    --------    ------    ----    ---- ------------ 
************ ****         ****    **** ************ ************      ************ ************ ****    ****    ****     ********     ****     ****    **** ************ 
""")
time.sleep(2)
print(r"""-----------  -----------  ------------ 
***********  ************ ************ 
----    ---  ---      --- ----         
*********    ************ ****  ****** 
---------    -----------  ----  ------ 
****  ****   ****         ****    **** 
----   ----  ----         ------------ 
****    **** ****         ************ """)
time.sleep(5)
print(r"""██████▓▓██████▓▓▓▓██████████▓▓██████████████████████████
▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓██████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██▓▓████████████████
▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▓▓▓▓▓▓██████▒▒████████
████▓▓▓▓▓▓████▓▓████████████████▒▒▒▒▓▓▓▓████████████████
██████████████████▓▓████████████▓▓▓▓▒▒▓▓▓▓▓▓▒▒██████▓▓██
██▓▓██████████▒▒████▓▓████████████████▓▓▓▓▒▒▓▓▓▓████▓▓██
▓▓▒▒▓▓████▓▓▓▓████▓▓████████▒▒████████▓▓▒▒▒▒▓▓████▓▓▓▓██
▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████▓▓▒▒▓▓▓▓██▓▓▓▓▓▓
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓██████████████▓▓▒▒████▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓██████████▓▓▒▒▓▓██▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░░░░░▒▒██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▒▒▒▒▒▒░░░░▒▒▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓
▓▓▓▓▓▓▓▓██████▓▓▒▒░░░░      ░░░░▒▒▒▒▓▓██████▓▓▓▓▓▓▓▓▓▓▒▒
▓▓▓▓▓▓██████▓▓▓▓▒▒░░░░      ░░░░▒▒▒▒██▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓
▓▓▓▓████████▓▓▒▒▒▒░░░░      ░░▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓
▓▓▓▓██████████▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓██▓▓████▓▓▓▓▓▓
▓▓▓▓██████████▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓██▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▓██████▓▓████▓▓▒▒░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████
▓▓▓▓████████▓▓████▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓████████
▓▓▓▓▓▓████████████████▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓████████████
▓▓▓▓▓▓██████████████████████████████▓▓██████████████████
██▓▓▓▓▓▓██▓▓████████████████████████████████████████████
▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████▓▓████████
████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████████████████▓▓▓▓▓▓▓▓██████
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓██████▓▓▓▓▓▓▓▓▓▓████
▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓██████████
▓▓██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓██▓▓▒▒██████▓▓
██▓▓▓▓██████████████████▓▓▓▓▓▓████▓▓██████████▓▓████████
████████████▓▓████▓▓████████▓▓▒▒▓▓▓▓▓▓██████████████████
▓▓██████████████████▓▓██████████████████████████████████""")  # Prints ascii wormhole

Login()

