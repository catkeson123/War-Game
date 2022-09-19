#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:

# stores the suits, ranks, and values of cards in arrays
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[3]:

# Card class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[4]:

# Deck Class
class Deck:
    
    def __init__(self):
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
    # shuffle deck    
    def shuffle(self):
        random.shuffle(self.cards)
    
    # deal a card from the deck
    def deal(self):
        return self.cards.pop()


# In[5]:

# Player Class
class Player:
    
    def __init__(self,name):
        self.name = name
        self.cards = []
    
    # remove a card from a players hand
    def remove_card(self):
        return self.cards.pop(0)

    # add a card to a players hand
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
        
    def __str__(self):
        return (f'{self.name} has {len(self.cards)} cards')       


# In[8]:


#game logic

game_on = True

player1 = Player('Player 1')
player2 = Player('Player 2')

deck = Deck()
deck.shuffle()

# deal cards from the deck to players
for x in range(26):
    player1.add_cards(deck.deal())
    player2.add_cards(deck.deal())

round_num = 0
    
while game_on:
    
    round_num += 1
    print(f'Currently on round {round_num}')
    
    if len(player1.cards) == 0 or len(player2.cards) == 0:
          if len(player1.cards) == 0:
              print('Player 2 wins!')
          if len(player2.cards) == 0:
              print('Player 1 wins!')
          game_on = False
          break
    
    # Start a new round
    player1_cards = []
    player2_cards = []
    
    player1_cards.append(player1.remove_card())
    player2_cards.append(player2.remove_card())
    
    at_war = True
    
    # logic for being at war
    while at_war:
          
          if player1_cards[-1].value > player2_cards[-1].value:
              player1.add_cards(player1_cards)
              player1.add_cards(player2_cards)
              at_war = False
          elif player1_cards[-1].value < player2_cards[-1].value:
              player2.add_cards(player1_cards)
              player2.add_cards(player2_cards)
              at_war = False
          else:
              print("War!")
              
              if len(player1.cards) < 10:
                  print("Player 1 is out of cards. Player 2 wins!")
                  game_on = False
                  break
              elif len(player2.cards) < 10:
                  print("Player 2 is out of cards. Player 1 wins!")
                  game_on = False
                  break
              else:
                  for card in range(10):
                      player1_cards.append(player1.remove_card())
                      player2_cards.append(player2.remove_card())
