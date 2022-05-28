#                      [TITLE]
# This is a work in progress, text adventure/rpg 
# 
# Version 1:
# - Working on intro
#

import time



print('Hello and welcome to your new adventure!')


# Personality Quiz similar to pmd, start with 
#  basic general questions then do research on 
#  some actual psychology later.
# for version 1: let's assume user input is nice, 
#  but look into error handling later.
#  also only 2 types exist happy and sad

print('Now before we begin I must ask you a few questions.')
print('Ready?')

happy_score = 0
sad_score = 0
print('Question 1: Are you happy? ')
a1 = input()
if a1 == 'yes':
    happy_score += 1    
else:
    sad_score += 1

print('Question 2: Are you a half glass empty person? ')
a2 = input()
if a2 == 'no':
    happy_score += 1    
else:
    sad_score += 1


print('Question 3: Would you sacrifice your career for your family? ')
a3 = input()
if a3 == 'yes':
    happy_score += 1    
else:
    sad_score += 1


print('Question 4: Do you need to be in the company of others to feel happy?')
a4 = input()
if a4 == 'no':
    happy_score += 1    
else:
    sad_score += 1


print('Question 5: Are you sad? ')
a5 = input()
if a5 == 'no':
    happy_score += 1    
else:
    sad_score += 1


print('Question 6: Are you an optimist? ')
a6 = input()
if a6 == 'yes':
    happy_score += 1    
else:
    sad_score += 1


print('Question 7: Do you enjoy yourself? ')
a7 = input()
if a7 == 'yes':
    happy_score += 1    
else:
    sad_score += 1


print('Question 8: Do you let others help you if you need the help? ')
a8 = input()
if a8 == 'yes':
    happy_score += 1    
else:
    sad_score += 1


print('Bonus Question: How much wood could a wood chuck, chuck?')
bq = input()
if bq == 'raccoon':
    print('Congrats, you know whats up')
else:
    print('Ha Ha Ha ')


time.sleep(0.3)

difficulty = ''

if happy_score > sad_score:
    print('Congrats, you appear to be happy! You know how to appreciate life and enjoy it.')
    difficulty = 'easy'


elif sad_score > happy_score:
    print('It seems like life has got you down, but dont give up! ')
    difficulty = 'hard'


else:
    print('hmm... I cant get a read on you...')
    print('Choose: hard or easy')
    difficulty = input()

# checkpoint 06/27/2020

# Later task: Write function that prints out these options
# door (Unlocked): x x x   (Closed) x x x    (open) x x x   
#                  x u x            x c x           x o x
#                  x u x            x c x           x o x
#                  x u x            x c x           x o x
#
# 
# 
# 
#

# Write function door, with a member function for opening and closing doors/ remembering door states

def door(state):
    if state == 'o':
        print('x x x')
        print('x o x')
        print('x o x')
        print('x o x')
    elif state == 'u':
        print('x x x')
        print('x u x')
        print('x u x')
        print('x u x')
    elif state == 'c':
        print('x x x')
        print('x c x')
        print('x c x')
        print('x c x')
    else:
        print('error')


door('u')
print('You walk up to a door, do you open it?')

if input() == 'o':
    door('o')



def item_box(state):
    if state == 'o':
        print('x x x')
        print('x o x')
        print('x x x')      
    elif state == 'u':
        print('x x x')
        print('x u x')
        print('x x x')
    elif state == 'c':
        print('x x x')
        print('x c x')
        print('x x x')
    else:
        print('error')



print('Quick theres a zombie coming and an weapon box in front of you, open the weapon box?')

if input() == 'o':
    item_box('o')


if difficulty == 'easy':
    print('You found an old Shotgun w/ 8 rounds! nice!')

else:
    print('There is an old handgun w/ 5 rounds')

# hmmm, here I see I need to make some charcter classes so I can keep track of inventory
# I also need to add a random number aspect to the amount of ammo recieved
# also I gotta figure out how combat is gonna work, I guess standard rpg turnbased combat, or maybe I can set a frequency timer thing to enemy attacks. kinda like a rythm thing, and you can block and stuff

# H--------------------H      Health bar? nah probably just do a number display
# |++++++++++++++++++++|
# H--------------------H

# Hp: 100    Ammo: 5   WPN: Handgun 