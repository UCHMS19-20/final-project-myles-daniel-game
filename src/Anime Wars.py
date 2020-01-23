import random
import sys
import pygame
pygame.init()
width, height = 700, 600
screen = pygame.display.set_mode( (width, height) )
default_img = pygame.image.load("src/img/DIO.jpg")

class Cards:
    def __init__ (self,suit,value,img):
    #Constructor for Card class
        self.suit = suit
        self.value = value
        self.img = pygame.image.load("src/img/DIO.jpg")
    
    def __repr__(self):
        return f"<{self.value} of {self.suit}>"
#Create the deck and hands
class Decks:
    #Constructor for the decks
    def __init__ (self):
        self.original_deck = []
        suits=["Sp", "He", "Cl", "Di"] 
        for suit in suits:
            for value in range (1,14):
                #Use the cards class to create cards
                self.original_deck.append(Cards(suit, value, default_img)) 
        #Make a copy of the original deck
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)
    #The full deck with 52 cards        
    def full_deck(self): 
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)

    def player_hands(self):
        hand1 = self.deck[:len(self.deck)//2]
        hand2 = self.deck[len(self.deck)//2:]
        return (hand1, hand2)

def show_cards(p1, p2):
    print(p1, p2)
    screen.blit(p1.img, (10, 10))
    screen.blit(p2.img, (475, 10))


discard1 = []
discard2 = []

deck = Decks()
hand1, hand2 = deck.player_hands()

#Picking cards
p1card = hand1.pop()
p2card = hand2.pop()

show_cards(p1card, p2card)
#Comparing Card
if p1card.value==p2card.value:  
    discard1.extend([p1card]+hand1[-3:])
    hand1 = hand1[:-3]
    hand1.append(discard1.pop())

    discard2.extend([p2card]+hand2[-3:])
    hand2 = hand2[:-3]
    hand2.append(discard2.pop())
elif p1card.value > p2card.value:
    hand1 = [p1card, p2card] + discard1 + discard2 + hand1
    discard1=[]
    discard2=[]
elif p2card.value > p1card.value:
    hand2 = [p2card, p1card] + discard2 + discard1 + hand2
    discard1=[]
    discard2=[]


    #Compare cards

#Automate the picking of cards

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    show_cards(p1card, p2card)

    pygame.display.flip()