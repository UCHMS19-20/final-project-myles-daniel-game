import random
import sys
import pygame
pygame.init()
width, height = 700, 600
screen = pygame.display.set_mode( (width, height) )
imgs_dict = {
    'He': {
        1: 'src/img/NATSUUUUUUUUUUUU.jpg',
        2: 'src/img/AIZEN.jpg',
        3: 'src/img/ASTA.jpg',
        4: 'src/img/BEERUS.jpg',
        5: 'src/img/ZORA.jpg',
        6: 'src/img/ESDEATH.jpg',
        7: 'src/img/ERZA.jpg',
        8: 'src/img/TETSU TESTU.jpg',
        9: 'src/img/PIKACHU.jpg',
        10: 'src/img/GON.jpg',
        11: 'src/img/BAKUGO.jpg',
        12: 'src/img/KILLUA.jpg',
        13: 'src/img/TOSHURA.jpg',
        }
        'Di': {
        1: 'src/img/SAITAMA.jpg',
        2: 'src/img/MEWTWO.jpg',
        3: 'src/img/AKAME.jpg',
        4: 'src/img/ESCANOR.jpg',
        5: 'src/img/BACCHUS.jpg',
        6: 'src/img/TOSHIRO.jpg',
        7: 'src/img/YUKIHIRA SOMA.jpg',
        8: 'src/img/ROCK LEE.jpg',
        9: 'src/img/DENKI.jpg',
        10: 'src/img/MELIODAS.jpg',
        11: 'src/img/SHINRA.jpg',
        12: 'src/img/TODOROKI.jpg',
        13: 'src/img/VEGETA.jpg',
        }
        'Sp': {
        1: 'src/img/GOKU.jpg',
        2: 'src/img/FRIEZA.jpg',
        3: 'src/img/MIHAWK.jpg',
        4: 'src/img/ARCEUS.jpg',
        5: 'src/img/LEVII.jpg',
        6: 'src/img/RUKIA.jpg',
        7: 'src/img/MIKOTO.jpg',
        8: 'src/img/LUFFY.jpg',
        9: 'src/img/LUCK.jpg',
        10: 'src/img/YANG.jpg',
        11: 'src/img/ACE.jpg',
        12: 'src/img/HIEI.jpg',
        13: 'src/img/ZEREF.jpg',
        }
        'Cl': {
        1: 'src/img/NARUTO.jpg',
        2: 'src/img/MADARA.jpg',
        3: 'src/img/ICHIGO.jpg',
        4: 'src/img/SINBAD.jpg',
        5: 'src/img/BAN.jpg',
        6: 'src/img/GRAY.jpg',
        7: 'src/img/RUBY.jpg',
        8: 'src/img/KIRISHIMA.jpg',
        9: 'src/img/LAXUS.jpg',
        10: 'src/img/MIDORIYA.jpg',
        11: 'src/img/MEGUMIN.jpg',
        12: 'src/img/SASUKE.jpg',
        13: 'src/img/DIO.jpg',
        }}
    

class Cards:
    def __init__ (self,suit,value,img,rect):
    #Constructor for Card class
        self.suit = suit
        self.value = value
        self.img = pygame.image.load(imgs_dict)
        self.rect = self.img.get_rect()
    
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
                self.original_deck.append(Cards(suit, value, imgs_dict)) 
        #Make a copy of the original deck
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)
    #The full deck with 52 cards        
    def full_deck(self): 
        self.deck = self.original_deck[:]
        random.shuffle(self.deck)
    #Give each player half of the full deck
    def player_hands(self):
        hand1 = self.deck[:len(self.deck)//2]
        hand2 = self.deck[len(self.deck)//2:]
        return (hand1, hand2)
#Show the players cards
def show_cards(p1, p2):
    print(p1, p2)
    screen.blit(p1.img, (10, 10))
    screen.blit(p2.img, (475, 10))

#Empty lists so that the cards that the players play can be easily moved to the other players hand
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    show_cards(p1card, p2card)

    pygame.display.flip()