import random, math

runTime = True
x = 0
y = 0
z = 0
i = 4
Difficulty = 0
difficulties = ["House", "Amateur", "Professional"]
#Card & Deck Setup
discardPile = []
def cardSet(suit, reversed):
        list = []
        i = 1

        while i < 11:
                list.append(suit + str(i))
                i += 1

        list.append(suit + "J")
        list.append(suit + "Q")
        list.append(suit + "K")

        if reversed:
                list.reverse()

        return list

def AddCardSuit(SuitDeck, NewDeck):
        for card in SuitDeck:
                NewDeck.append(card)

        return NewDeck

def Shuffle(deck):
        shuffledDeck = []
        while len(deck) > 0:
                i = random.randint(0, len(deck)-1)
                shuffledDeck.append(deck[i])
                deck.remove(deck[i])

        return shuffledDeck

def ShuffleIn(Pile1, Pile2):
        list = Pile1 + Pile2
        return Shuffle(list)

Hearts   = cardSet("H", False)
Diamonds = cardSet("D", True)
Clubs    = cardSet("C", False)
Spades   = cardSet("S", True)

NewDeck = []
NewDeck = AddCardSuit(Hearts, NewDeck)
NewDeck = AddCardSuit(Clubs, NewDeck)
NewDeck = AddCardSuit(Diamonds, NewDeck)
NewDeck = AddCardSuit(Spades, NewDeck)

print("Blank Deck: ", NewDeck)

Deck = Shuffle(NewDeck)
print("Shuffled Deck: ", Deck)

while i > 3:
        print("Please select a difficulty level, Home, Amateur or Casino")
        i = int(input("Enter 1-3 for difficulty or 4 for information: "))
        if i > 3:
                print("Difficulty in Blackjack is increased by adding and removing decks of cards, Home has 1 deck, Amateur has 2 decks, Casino has 4 decks")
Difficulty = i-1
print(difficulties[Difficulty], "Difficulty Selected")



while runTime:
        print("")