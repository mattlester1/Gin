#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   Gin.py
@Time    :   2024/02/04 15:05:29
@Author  :   Matt Lester 
@Version :   1.0
'''

import random

class Player:

    def __init__(self, name, wins = 0, loses = 0):
      self.name = name
      self.wins = wins
      self.loses = loses
      self.hand = []    
      
    def __repr__(self):
      output = f"{self.name} has {self.wins} wins and {self.loses} loses."
      return output 
  
    def deal(self, card):
      self.hand.append(card)   
       
    def showHand(self):
        print(f"{self.name}'s hand: {self.hand}")

    def getHand(self):
        return self.hand

    def card_exchange(self, old_card, new_card):

        self.hand.remove(old_card)
        self.hand.append(new_card)


    def get_playerName(self):
        return self.name    
    
    def win(self):
        self.wins += 1
        return self.wins
    
    def lose(self):
        self.loses += 1
        return self.loses
    
class Deck:  
    
    def __init__(self):
        self.spades = ["2_S",
                       "3_S",
                       "4_S",
                       "5_S",
                       "6_S",
                       "7_S",
                       "8_S",
                       "9_S",
                       "10_S",
                       "Jack_S",
                       "Queen_S",
                       "King_S",
                       "Ace_S"]
        self.hearts = ["2_H",
                       "3_H",
                       "4_H",
                       "5_H",
                       "6_H",
                       "7_H",
                       "8_H",
                       "9_H",
                       "10_H",
                       "Jack_H",
                       "Queen_H",
                       "King_H",
                       "Ace_H"]
        self.diamonds = ["2_D",
                       "3_D",
                       "4_D",
                       "5_D",
                       "6_D",
                       "7_D",
                       "8_D",
                       "9_D",
                       "10_D",
                       "Jack_D",
                       "Queen_D",
                       "King_D",
                       "Ace_D"]
        self.clubs = ["2_C",
                       "3_C",
                       "4_C",
                       "5_C",
                       "6_C",
                       "7_C",
                       "8_C",
                       "9_C",
                       "10_C",
                       "Jack_C",
                       "Queen_C",
                       "King_C",
                       "Ace_C"]
        self.deck = self.spades + self.hearts + self.diamonds + self.clubs
        self.discard = ""

    def __repr__(self):
        string = ""
        for values in self.deck:
            string = string + "  " + values

        return string
    
    def getDiscard(self):
        return self.discard

    def shuffle(self):

        random.shuffle(self.deck)
    
        return self.deck
    
    def deal (self, player1, player2):
        i = 0
        # print(self.deck)
        
        for i in range(10):
            card = self.deck[0]
            player1.hand.append(card)
            self.deck.pop(0)
            # print(self.deck)
            card = self.deck[0]
            player2.hand.append(card)
            self.deck.pop(0)
            # print(self.deck)
            
        card = self.deck[0]
        player1.hand.append(card)
        self.deck.pop(0)
        
    def deal_oneCard(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card
        
    def cardSwap(self, player):
        
        if len(player.hand) > 10:
            
            playerDiscard = input(f"{player.get_playerName()} what card do you want to discard? ")
            player.hand.remove(playerDiscard)
            self.discard = playerDiscard
            
            return self.discard
        
        else:
            print(f"This is the current discard {self.getDiscard()} . ")
            answer = input("Would you like the discard or one off the top? Answer with D for discard or T for top: ")
            
            if answer.lower() == "d":
                player.hand.append(self.discard)
                print(player.getHand())
                playerDiscard = input(f"{player.get_playerName()} what card do you want to discard? ")
                player.hand.remove(playerDiscard)
                self.discard = playerDiscard
                
            else:
                player.hand.append(self.deal_oneCard())
                print(player.getHand())
                playerDiscard = input(f"{player.get_playerName()} what card do you want to discard? ")
                player.hand.remove(playerDiscard)
                self.discard = playerDiscard
                
        

        
Matt = Player("Matt")
Andrew = Player("Andrew")

deck = Deck()
deck.shuffle()

deck.deal(Matt, Andrew)
print()
Matt.showHand()
print()
Andrew.showHand()
print()
# deck.showDeck()
winner = False

while winner == False:
    
    deck.cardSwap(Matt)
    # print(deck.getDiscard())
    print()
    print(Matt.getHand())
    mattWin = input("Do you have gin? y or n: ")
    
    if mattWin.lower() == "y":
        Matt.win()
        Andrew.lose()
        winner = True
    else:
        
        deck.cardSwap(Andrew)
        print(deck.getDiscard())
        print(Andrew.getHand())
        
        andrewWin = input("Do you have gin? y or n: ")
        
        if andrewWin.lower() == "y":
            Andrew.win()
            Matt.lose()
            winner = True
 
