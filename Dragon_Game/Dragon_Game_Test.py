import os
import random
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Congradulations! You found the secret room!")

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see three caves. In one cave, the dragon is friendly
and will share his treasure with you. The next dragon
is greedy and hungry, and will eat you on sight. The final
dragon has no treasure and is quite scared of people, it will fly away
on sight.''')
print()

def chooseCave():
    cave = ''
    while cave !='1' and cave !='2' and cave !='3' and cave !='4':
        print('Which cave will you go into? (1, 2 or 3)')
        cave = os.environ['cave']

    return cave

def checkCave(chosenCave):
    if chosenCave == '4':
        chosenCave = '4'

    else:
        print('You approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps out in front of you! He opens his jaws and...')
        print()
        time.sleep(2)

    friendlyCave = random.randint(1, 3)
    unfriendlyCave = random.randint(1, 3)
    while unfriendlyCave == friendlyCave:
        unfriendlyCave = random.randint(1, 3)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        if chosenCave ==str(unfriendlyCave):
            print('Gobbles you down in one bite!')

        else:
            if chosenCave == '4':
                print('''You look up and see a hole in the ceiling,
you climb through it and find a whole room full of tresures!''')
                time.sleep(2)
                print()
                print('''As you are bagging what you found, you see somebody
approaching you, "My name is Mailliw" He says, "you have found the secrect room,
and for that you must be rewarded."''')
                time.sleep(2)
                print('''

You thought that the room was already stuffed with treasures,
but then more rain down from the ceiling!''')
                time.sleep(3)
                print(ascii_banner)
                time.sleep(4)
    
            else:
                print('Flies away!')
                print()
                displayIntro()
                caveNumber=chooseCave()
                checkCave(caveNumber)


playAgain = 'yes'
while playAgain =='yes' or playAgain =='y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?(yes or no)')
    playAgain = 'no'
