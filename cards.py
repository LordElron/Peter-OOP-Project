import random

class Card(object):
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit
        if self.__value == 11:
            self.__value = "Jack"
        elif self.__value == 12:
            self.__value = "Queen"
        elif self.__value == 13:
            self.__value = "King"
        elif self.__value == 1 or value == 14:
            self.__value = "Ace"
        if self.__suit == 1:
            self.__suit = "Hearts"
        elif self.__suit == 2:
            self.__suit = "Spades"
        elif self.__suit == 3:
            self.__suit = "Diamonds"
        elif self.__suit == 4:
            self.__suit = "Clubs"
        else:
            pass
         
    def show(self):
        return (str(self.__value)+ " " + str(self.__suit))
        #sue = str(self.__suit)       
        #numb = str(self.__value)
        #y = sue +" "+ numb

        
class Deck(object):
    def __init__(self):
        self.__cards = []
        self.__suits = ['♥','♦','♠','♣']
        for suit in self.__suits:
            for value in range(1,14):
                self.__cards.append(Card(value,suit))

    def shuffle(self):
        size = len(self.__cards)
        for i in range(size-1,0,-1):
            swap = random.randint(0,i)
            self.__cards[i], self.__cards[swap] = self.__cards[swap], self.__cards[i]
            
        return(self.__cards)

    def deal(self,size):
      dealt = []
      for i in range(size):
        dealt.append(self.__cards.pop(0))
      return dealt

    def show(self):
        for m in self.__cards:
            print(m.show())
    
class Player(object):
    def __init__(self,deck):
        self.hand = deck.deal()


def numIn(message,top=None,bottom=0):
    valid = False
    while valid == False: 
        try:
            number = abs(int(input(message)))
            if top != None:
                if number > top or number <= bottom:
                    print('That is not a valid number.')
                else:
                    valid = True
                    return number
            else:
                valid = True
                return number
        except:
            print('That is not a valid number.')
            
        
            

#value = random.randint(1,14)
#suit = random.randint(1,4)
#x = Card(value,suit)
#x.show()
z = Deck()
z.shuffle()
z.show()
players = []
for i in range(numIn("Enter the number of players: ",11,2)):
  players.append(Player(z))