### This class respresents a deck of cards
### (c) Tibrewal, Karan 
### Williams College, 2016


# Domain of suits
Suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

# Domain of Card Values
Values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']




## Class for a Card Object
class Card: 
	
	# CONSTRUCTOR
	# @param self pointer to self
	# @param suit suit of this card 
	# @param val val of this card
	def __init__(self, suit, val):
		# Pre: suit, val are valid
		assert suit in Suits
		assert val in Values
		
		self.suit = suit
		self.val = val

	# @param other another Card object
	# @return True if and only if this.suit = other.suit && 
	#							  this.val = other.val
	def __eq__(self, other): 
		if isinstance(other, Card):
			return self.suit == other.suit and self.val == other.val
		else:
			return NotImplemented

	# @return string representation of card object
	def __str__(self):
		return '[' + self.suit + ',' + self.val + ']'

## Function to initialize a deck of cards; 1 card of each val for each suit
## @return deck of 52 cards
def initDeck(): 
	deck = [] 
	for suit in Suits: 
		for val in Values: 
			deck.append(Card(suit, val))

	return deck


## Tests for initDeck() 
testDeck = initDeck()
assert len(testDeck) == 52


from random import shuffle

## Class for a Deck object
## Represents a deck of cards
class Deck: 

	# CONSTRUCTOR
	# @return inits new deck of cards
	def __init__(self): 
		self.deck = initDeck()

	# @return shuffles this deck of cards
	def shuffleDeck(self):
		shuffle(self.deck)


	# @param card card to get from the deck
	# @return reference to card object if present in deck, None else
	#         removes card from deck (DESTRUCTIVE)
	def get(self, card):
	
		if card in self.deck: 
			self.deck.remove(card)
			return card
		else:
			return None 

	# @return first card of deck
	#         removes card from deck (DESTRUCTIVE)
	def getFirstCard(self): 
		card = self.deck[0]
		self.deck.remove(card)
		return card

	# @return prints deck to std out
	def printDeck(self):
		print(len(self.deck))
		for card in self.deck:
			print card

## Tests for Deck
testDeck = Deck()
firstCard = Card('Spades', 'A')
assert testDeck.getFirstCard() == firstCard
assert len(testDeck.deck) == 51

secondCard = Card('Spades', '2')
assert testDeck.getFirstCard() == secondCard
assert len(testDeck.deck) == 50

assert testDeck.get(firstCard) is None
assert testDeck.get(secondCard) is None

thirdCard = testDeck.get(Card('Clubs', 'A'))
assert thirdCard == Card('Clubs', 'A')
assert len(testDeck.deck) == 49