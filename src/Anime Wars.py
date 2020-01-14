import sys
import pygame
pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode( (width, height) )
deck1=[]
discard1=[]
deck2=[]
discard2=[]
class Card:
    def __init__ (self,suit,value,img):
    #Constructor for Card class
        self.suit = suit
        self.value = value
        self.img = pygame.image.load("src/img/DIO.jpg")
    #showing cards
    def draw():
        p1card=deck1.pop()
        discard1.append(plcard)
        
    #Compare cards
    def compare (self, other_card):
        if self > other_card:
            self wins
        elif self < other_card
            other_card wins

Dio=Card("Cl", 13,)
Vegeta=Card("Di", 13)

#Automate the picking of cards
 deck=[]
        for suit in ["Cl", "Di", "He", "Sp"]:
            for value in range (1,14):
                deck.append(Card(suit, value))