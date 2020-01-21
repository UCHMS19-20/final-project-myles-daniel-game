import random
import sys
import pygame
pygame.init()
width, height = 400, 300
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
        # random.shuffle(self.original_deck)
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)
    #The full deck with 52 cards        
    def full_deck(self): 
        # suits=["Sp", "He", "Cl", "Di"] 
        # for suit in suits:
        #     for value in range (1,14):
        #         #Use the cards class to create cards
        #         self.deck.append(Cards(suit, value, img)) 
        # random.shuffle(deck)
        # return deck
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)

    def player_hands(self):
        hand1 = self.deck[:len(self.deck)//2]
        hand2 = self.deck[len(self.deck)//2:]
        return (hand1, hand2)

def show_cards(p1, p2):
    print(p1, p2)
    screen.blit(p1.img, (10, 10))
    screen.blit(p2.img, (100, 10))
    # pygame.draw.rect(screen, (255, 0, 0), (10,10,100,100))
    # pygame.draw.rect(screen, (0,0,255), (200, 10, 100, 100))

discard1 = []
discard2 = []

deck = Decks()
hand1, hand2 = deck.player_hands()

#Picking cards
p1card = hand1.pop()
p2card = hand2.pop()

show_cards(p1card, p2card)
#Comparing Card
if p1card==p2card:  
    discard1.extend
    #Compare cards

#Automate the picking of cards

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    show_cards(p1card, p2card)

    pygame.display.flip()