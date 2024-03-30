
import random

import time

  

# Get the current time in seconds since the epoch

current_time = int(time.time())

# Set the random seed based on the current time

random.seed(current_time)

  

# Generating Full Deck

# Use zip to combine ranks and suits, and convert the result to a list of tuples

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

symbols=['\u2665','\u2666','\u2663','\u2660']

values=[2,3,4,5,6,7,8,9,10,11,12,13,14]

deck=[]


#Generate Full Deck:

for i in range(0,4):
    for j in range(0,13):
     card=(suits[i],ranks[j],symbols[i],values[j])
     deck.append(card)

  

print ("Numbers of Cards left:"+str(len(deck)))

score=0

def PrintCARD(crds):
    # Print the Card in a Professional Way!
    # This section is using the script from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards as a reference:
    
    lines = [[] for i in range(9)]

    for crd_i in crds:
        if (crd_i[3]<=10) or  (crd_i[3]==14):
            if crd_i[1] == '10':  # ten is the only one who's rank is 2 char long
                space = ''  # if we write "10" on the card that line will be 1 char to long
            else:
                space = ' '  # no "10", we use a blank space to will the void


            # add the individual card on a line by line basis
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(crd_i[1], space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(crd_i[2]))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, crd_i[1]))
            lines[8].append('└─────────┘')
        elif (crd_i[3]==11):
                lines[0].append('┌─────────┐')
                lines[1].append('│J        │')  # use two {} one for char, one for space or char
                lines[2].append('│    -∩   │')
                lines[3].append('│  (˙-˙)  │')
                lines[4].append('│  งJ{}ง   │'.format(crd_i[2]))
                lines[5].append('│   | |   │')
                lines[6].append('│         │')
                lines[7].append('│        J│')
                lines[8].append('└─────────┘')
        elif (crd_i[3]==12):
                lines[0].append('┌─────────┐')
                lines[1].append('│Q  … …   │')  # use two {} one for char, one for space or char
                lines[2].append('│   ^M^   │')
                lines[3].append('│  ʕ•ᴥ•ʔ  │')
                lines[4].append('│  ง {}Q   │'.format(crd_i[2]))
                lines[5].append('│   /_\   │')
                lines[6].append('│  *****  │')
                lines[7].append('│        Q│')
                lines[8].append('└─────────┘')
        else:
                lines[0].append('┌─────────┐')
                lines[1].append('│K        │') 
                lines[2].append('│   ^M^   │')
                lines[3].append('│ oʕ•ᴥ•ʔ  │')
                lines[4].append('│ | {}K ว  │'.format(crd_i[2]))
                lines[5].append('│ ||___|  │')
                lines[6].append('│  ------ │')
                lines[7].append('│        K│')
                lines[8].append('└─────────┘')

    result = []

    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    
    for line in result:
        print(line)
    
def Checktype(lst):

#Sort:
    for sl in range(0,5):
       for sk in range(sl+1,5):
            if lst[sl][3]<lst[sk][3]:
                lst[sl],lst[sk]=lst[sk],lst[sl]
    PrintCARD(lst)
    dif=[]
    Flush=True
    chip=lst[0][3]
    multi=1
    cur_suit=lst[0][2]
    prodt=1
    sum=0

# whether it is a flush:
    for i in range(1,5):
        sum=sum+lst[i][3]
        if lst[i][2]!=cur_suit: 
            Flush=False

# whether it is a straight:
    for i in range(0,4):
        dif.append(lst[i][3]-lst[i+1][3])
        prodt=dif[i]*prodt
    if dif[0:4]==[9,1,1,1]:prodt=1
    if (prodt==1) and Flush and lst[0][3]==14:
        multi=16
        chip=sum 
        print("You've got Royal Straight Flush!!!!!!!Chips="+str(lst[0][3])+"+"+str(lst[1][3])+"+"+str(lst[2][3])+"+"+str(lst[3][3])+"+"+str(lst[4][3]))
    elif (prodt==1) and Flush:
        multi=8
        chip=sum
        print("You've got Straight Flush!!!!Chips="+str(lst[0][3])+"+"+str(lst[1][3])+"+"+str(lst[2][3])+"+"+str(lst[3][3])+"+"+str(lst[4][3]))
    elif (prodt==1):
        multi=4
        chip=sum
        print("You've got Straight!!Chips="+str(lst[0][3])+"+"+str(lst[1][3])+"+"+str(lst[2][3])+"+"+str(lst[3][3])+"+"+str(lst[4][3]))
    elif Flush:
        multi=5
        chip=sum
        print("You've got Flush!!Chips="+str(lst[0][3])+"+"+str(lst[1][3])+"+"+str(lst[2][3])+"+"+str(lst[3][3])+"+"+str(lst[4][3]))
    

#Deciding Repetition Level：Four of a Kind？or Full House？or Single Pair？
    if 0 in dif:
        count_0 = dif.count(0)
        index_0 = dif.index(0)
        if count_0==1: 
            multi=2
            chip=lst[index_0][3]*2
            print("You've got a pair! Chips= "+str(lst[index_0][3])+" + "+str(lst[index_0][3]))
        if (count_0==2) and ((2 ** (dif[index_0]) * 2 ** (dif[index_0 + 1]) == 1)): 
            multi=3
            chip=lst[index_0][3]*3
            print("You've got Three of a Kind!!! Chips= "+str(lst[index_0][3])+" + "+str(lst[index_0][3])+" + "+str(lst[index_0][3]))
        elif (count_0==2):
            multi=3
            chip=lst[1][3]*2+lst[3][3]*2
            print("You've got Two Pair!! Chips= "+str(lst[1][3])+" *2 +"+str(lst[3][3])+" *2")
        if (count_0==3) and ((2 ** (dif[index_0]) * 2 ** (dif[index_0 + 1])* 2 ** (dif[index_0 + 2]) == 1)): 
            multi=7
            chip=lst[2][3]*4
            print("You've got Four of a Kind!!!! Chips= "+str(lst[2][3])+" *4")
        elif (count_0==3):
            multi=6
            chip=sum
            print("You've got Full House!!!! Chips= "+str(lst[0][3])+" + "+str(lst[1][3])+" + "+str(lst[2][3])+" + "+str(lst[3][3])+" + "+str(lst[4][3]))  
    if multi==1:
         print("You've got High Cards.")
    return chip,multi

# GameSetting

print("-" * 25)
print("Welcome to our Penguin Poker Game!")
print("In this game, you randomly get five cards from the deck and win some points")
print("-" * 25)

print("\n")
n=int(input("How many rounds do you want to play\n"))

s=5
while n*s>52:

    print("Not enough cards!")
    n=int(input("Please Reinput the Round Numbers: "))
    s=int(input("Rechoose the Handside: "))

# Game Start
for i in range(0,n):
    
    print("\n")
    print("-" * 25)
    print ("Round No."+str(i+1)+"!")
    print("-" * 25)

    x=int(input("How much pocket money do you want to spend in this round?\n"))

    hcard=[]

    for k in range(0,5): 

        index=random.randint(0, len(deck)-1)
    #    index=int(input("choose card"))
        hcard.append(deck[index])
        deck.pop(index)

    chips,mults=Checktype(hcard)
    Bonus=x*(mults-1)
    score=score-x+chips*mults+Bonus
    print("You EARN:"+str(chips)+" (Chips) * "+str(mults)+"(Multi) + "+str(Bonus)+" (Interest) = "+str(chips*mults)+" in this round")
    print("Your Current Score is:"+str(score))
    print("You have "+str(len(deck))+" cards left!")

print("-" * 25)
print("New Record! You reached "+str(score)+" in this game!")
print("Thank you for playing!")
print("Developed by Untitled Penguin")
print("Version 1.0")
print("-" * 25)