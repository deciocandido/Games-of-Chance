#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

money = 100

#Write your game of chance functions here

def check_money(amount):
    global money
    
    if amount < 0:
        print("Player do not have enough money")
        exit()

def check_input(inputs):
    if inputs.lower() == "heads":
        print("Valid input")

    elif inputs.lower() == "tails":
        print("Valid input")

    elif inputs.lower() == "even":
        print("Valid input")

    elif inputs.lower() == "odd":
        print("Valid input")

    else:
        print("Player must enter a valid input")
        exit()
        
def flip_coin(bet, choose):
    global money
    money -= bet
    check_money(money)
    check_input(choose)
    #generates coin toss
    coin_toss = random.randint(0, 1)
    
    #checks if coin is Heads or Tails
    if coin_toss == 0:
        coin_side = "heads"
    else:
        coin_side = "tails"
    print("The coin side is: " + coin_side)
    
    #checks if the player was correct and returns bet result
    if coin_side == str(choose):
        print("Guess correct: " + str(bet))
        return +bet
    else:
        print("Guess incorrect: -" + str(bet))
        return -bet
        

def cho_han(bet, prediction):
    global money
    money -= bet
    check_money(money)
    check_input(prediction)
    #generates dice throws
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    results_dice = dice_1 + dice_2
    print("dice1: " + str(dice_1) + " - dice2: " + str(dice_2) + " - Dices number " + str(results_dice))
    
    #checks if results of dice is even or odd
    if(results_dice % 2 == 0):
        hand = "even"
        print("The hand is: " + hand)
    else:
        hand = "odd"
        print("The hand is: " + hand)
    
    #checks if the player was correct and returns bet result
    if hand == str(prediction):
        print("Guess correct: " + str(bet))
        return +bet
    else:
        print("Guess incorrect: -" + str(bet))
        return -bet


def card_desk(bet):
    global money
    money -= bet
    check_money(money)
    
    deck = list(range(1,14))*4
    card_player = deck[random.randint(0, len(deck)-1)]
    deck.remove(card_player)
    card_opp = deck[random.randint(0, len(deck)-1)]
    
    if card_player > card_opp:
        print("Your card was higher")
        print("Player won: " + str(bet))
        return +bet
    elif card_player < card_opp:
        print("Opp card was higher")
        print("Player lost: " + str(bet))
        return -bet
    else:
        print("It was a tie!")


def roulette(bet, prediction):
    
    global money
    money -= bet
    check_money(money)
    #Roulette table division - Outside bets
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 32, 34, 36]
    
    dozen_1 = []
    for i in range(1, 13):
        dozen_1.append(i)
    #print("dozen_1 = %s" % dozen_1)
    dozen_2 = []
    for i in range(13, 25):
        dozen_2.append(i)
    dozen_3 = []
    for i in range(25, 37):
        dozen_3.append(i)
    
    column_1 = []
    for i in range(1, 36, 3):
        column_1.append(i)
    column_2 = []
    for i in range(2, 36, 3):
        column_2.append(i)
    column_3 = []
    for i in range(3, 37, 3):
        column_3.append(i)
        
    low = []
    for i in range(1, 19):
        low.append(i)
    high = []
    for i in range(19, 37):
        high.append(i)
    
    
    
    #generates croupier from 0 to 36
    falls = random.randint(0, 37)
    if falls == 37:
        falls = 00
    
    print("The ball falls on: " + str(falls))
    
    if falls == prediction:
        if falls == 0:
            if (str(falls) == "0" and str(prediction)) or (str(falls) == "00" and str(prediction) == "00"):
                print("Player WINS Straight Up bet: " + str(bet * 35))
                money += bet * 35
        else:
            print("Player WINS Straight Up bet: " + str(bet * 35))
            money += bet * 35
    else:
        print("Player DID NOT WIN on Straight Up bet")
        
        
    if falls != 0:    
        if falls in dozen_1 and prediction in dozen_1:
            print("Player wins on DOZEN 1 bet: " + str(bet * 2))
            money += bet * 2
        elif falls in dozen_2 and prediction in dozen_2:
            print("Player wins on DOZEN 2 bet: " + str(bet * 2))
            money += bet * 2
        elif falls in dozen_3 and prediction in dozen_3:
            print("Player wins on DOZEN 3 bet: " + str(bet * 2))
            money += bet * 2
        else:
            print("Player DID NOT WIN on DOZEN bet")
            #return -bet
        
        if falls in column_1 and prediction in column_1:
            print("Player wins on COLUMN 1 bet: " + str(bet * 2))
            money += bet * 2
        elif falls in column_2 and prediction in column_2:
            print("Player wins on COLUMN 2 bet: " + str(bet * 2))
            money += bet * 2
        elif falls in column_3 and prediction in column_3:
            print("Player wins on COLUMN 3 bet: " + str(bet * 2))
            money += bet * 2
        else:
            print("Player DID NOT WIN on COLUMN bet")    
            
        
        if falls in low and prediction in low:
            print("Player wins on LOW HALF bet: " + str(bet))
            money += bet
        elif falls in high and prediction in high:
            print("Player wins on HIGH HALF bet: " + str(bet))
            money += bet
        else:
            print("Player DID NOT WIN on HALF bet")
            
        
        if falls in red and prediction in red:
            print("Player wins on RED color bet: " + str(bet))
            money += bet
        elif falls not in red and prediction not in red:
            print("Player wins on BLACK color bet: " + str(bet))
            money += bet
        else:
            print("Player DID NOT WIN on color bet")
    
        
        if falls % 2 == 0 and prediction % 2 == 0:
            print("Player wins on EVEN bet: " + str(bet))
            money += bet
        elif falls % 2 != 0 and prediction % 2 != 0:
            print("Player wins on ODD bet: " + str(bet))
            money += bet
        else:
            print("Player DID NOT WIN on ODD bet")
    else:
        print("The ball has fall in: " + str(falls))

    
   
    
    
    
    
 

#Call your game of chance functions here
money += flip_coin(50, "tails")
money += cho_han(50, "odd")
money += card_desk(10)
roulette(10, 23)
