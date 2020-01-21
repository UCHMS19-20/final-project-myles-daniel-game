import random
import sys
import pygame
pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode( (width, height) )

class Cards:
    def __init__ (self,suit,value,img):
    #Constructor for Card class
        self.suit = suit
        self.value = value
        self.img = pygame.image.load("src/img/DIO.jpg")
#Create the deck and hands
class Decks:
    #Constructor for the decks
    def __init__ (self, name):
        self.deck = []
    #The full deck with 52 cards        
    def full_deck(self): 
        suits=["Sp", "He", "Cl", "Di"] 
        for suit in suits:
            for value in range (1,14):
                #Use the cards class to create cards
                self.deck.append(Cards(suit, value, img)) 
        random.shuffle(deck)
        return deck

    def player_hands(deck):
        hand1 = deck[:len(deck)/2]
        hand2 = deck[len(deck)/2:]
       
discard1 = []
discard2 = []

    
Dio=Card("Cl", 13,)
Vegeta=Card("Di", 13)
#showing cards
def draw():
    p1card=hand1.pop()
    discard1.append(plcard)
    p2card = hand2.pop()
    discard2.append(p2card)    
    #Compare cards
def compare (self, other_card):
    if self > other_card:
         self wins
    elif self < other_card
        other_card wins

#Automate the picking of cards
