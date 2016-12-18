### Class to manage ranking of Texas Holdem Poker hands
### (c) Tibrewal, Karan. 
### Williams College, 2016


from Cards import Deck
from Cards import Values
from Cards import Suits
from Cards import Card
from random import shuffle
from random import randrange

class Result(): 
	win = 1
	tie = 0
	loss = -1

class Ranker: 

	# # @return true if and only if hand represents a royal flush
	# def isRoyalFlush(hand): 

	# # @return true if and only if hand represents a straight flush
	# def isStraightFlush(hand): 
	# 	return isStraight(hand) and isFlush(hand)

	# @return true if and only if hand represents a four of a kind
	@staticmethod
	def isFourOfAKind(hand):
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.val] = freq.get(card.val, 0) + 1
		
		# check if a freq equals 4
		for key in freq: 
			if freq[key] == 4: 
				return True 

		return False

	# @return true if and only if hand represents a full house
	@staticmethod
	def isFullHouse(hand):
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.val] = freq.get(card.val, 0) + 1
		count3 = 0
		count2 = 0
		for key in freq: 
			count3 += freq[key] >= 3
			count2 += freq[key] >= 2

		return count3 >= 1 and count2 >= 1

	# @return true if and only if hand represents a flush
	@staticmethod
	def isFlush(hand): 
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.suit] = freq.get(card.suit, 0) + 1

		count = 0
		for key in freq: 
			count += freq[key] >= 5

		return count >= 1

	# # @return true if and only if hand represents a straight
	# def isStraight(hand): 

	# @return true if and only if hand represents a three of a kind
	@staticmethod
	def isThreeOfAKind(hand):
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.val] = freq.get(card.val, 0) + 1
		
		# check if a freq equals 4
		for key in freq: 
			if freq[key] == 3: 
				return True 

		return False

	# @return true if and only if hand represents a two pair
	@staticmethod
	def isTwoPairs(hand): 
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.val] = freq.get(card.val, 0) + 1
		count = 0
		# check if a freq equals 4
		for key in freq: 
			count += freq[key] == 2
				
		return count >= 2

	# @return true if and only if hand represents a pair
	@staticmethod
	def isPair(hand): 
		assert len(hand) == 7
		freq = {}
		# record freq of vals
		for card in hand: 
				freq[card.val] = freq.get(card.val, 0) + 1
		
		# check if a freq equals 4
		for key in freq: 
			if freq[key] == 2: 
				return True 

		return False

	# # @ return Result.win if handA > handB
	# # 		   Result.tie if handA = handB
	# #          Result.loss if handA < handB 
	# def rank(handA, handB): 



## Test for four of a kind
for val in Values:
	testDeck = Deck()
	testHand = [] 
	for suit in Suits: 
		testHand.append(testDeck.get(Card(suit, val)))
	testDeck.shuffleDeck() 
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	for _ in range(20): 
		shuffle(testHand)
		assert Ranker.isFourOfAKind(testHand)


## Test for pairs
for val in Values:
	testDeck = Deck()
	testHand = [] 
	testHand.append(testDeck.get(Card(Suits[0], val)))
	testHand.append(testDeck.get(Card(Suits[1], val)))
	testDeck.shuffleDeck() 
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())

	for _ in range(20): 
		shuffle(testHand)
		assert Ranker.isPair(testHand) or \
		Ranker.isThreeOfAKind(testHand) or \
		Ranker.isFourOfAKind(testHand)



# Test for three of a kind
for val in Values:
	testDeck = Deck()
	testHand = [] 
	testHand.append(testDeck.get(Card(Suits[0], val)))
	testHand.append(testDeck.get(Card(Suits[1], val)))
	testHand.append(testDeck.get(Card(Suits[2], val)))
	testDeck.shuffleDeck() 
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	for _ in range(20): 
		shuffle(testHand)
		assert Ranker.isThreeOfAKind(testHand) \
		or Ranker.isFourOfAKind(testHand)



## Test for two pairs
for val in Values:
	testDeck = Deck()
	testHand = [] 
	testHand.append(testDeck.get(Card(Suits[0], val)))
	testHand.append(testDeck.get(Card(Suits[1], val)))
	x = randrange(0, len(Values), 1)
	while Values[x] == val:
			x = randrange(0, len(Values), 1)
	testHand.append(testDeck.get(Card(Suits[0], Values[x])))
	testHand.append(testDeck.get(Card(Suits[1], Values[x])))

	testDeck.shuffleDeck() 
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())
	
	for _ in range(20): 
		shuffle(testHand)
		assert Ranker.isTwoPairs(testHand) or \
			   Ranker.isThreeOfAKind(testHand) or \
			   Ranker.isFourOfAKind(testHand)


## Test for full house
for val in Values:
	testDeck = Deck()
	testHand = [] 
	testHand.append(testDeck.get(Card(Suits[0], val)))
	testHand.append(testDeck.get(Card(Suits[1], val)))
	x = randrange(0, len(Values), 1)
	while Values[x] == val:
			x = randrange(0, len(Values), 1)
	testHand.append(testDeck.get(Card(Suits[0], Values[x])))
	testHand.append(testDeck.get(Card(Suits[1], Values[x])))
	testHand.append(testDeck.get(Card(Suits[2], Values[x])))

	testDeck.shuffleDeck() 
	testHand.append(testDeck.getFirstCard())
	testHand.append(testDeck.getFirstCard())

	
	for _ in range(20): 
		shuffle(testHand)
		assert Ranker.isFullHouse(testHand)

## Test for flush
for suit in Suits:
	for _ in range(1000):

		testDeck = Deck()
		testHand = [] 
		for _ in range(5):
			card = testDeck.get(Card(suit, \
									Values[randrange(0, len(Values), 1)]))
			while card is None: 
				card = testDeck.get(Card(suit, \
									Values[randrange(0, len(Values), 1)]))
			testHand.append(card)

		testDeck.shuffleDeck() 
		testHand.append(testDeck.getFirstCard())
		testHand.append(testDeck.getFirstCard())

	
		for _ in range(20): 
			shuffle(testHand)
			assert Ranker.isFlush(testHand)


			  










