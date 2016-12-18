### Class to manage ranking of Texas Holdem Poker hands
### (c) Tibrewal, Karan. 
### Williams College, 2016


from Cards import Deck
from Cards import Values
from Cards import Suits
from Cards import Card
from random import shuffle
from random import randrange

valMapping = {}
valMapping['A'] = 1 
valMapping['2'] = 2 
valMapping['3'] = 3 
valMapping['4'] = 4 
valMapping['5'] = 5 
valMapping['6'] = 6 
valMapping['7'] = 7 
valMapping['8'] = 8 
valMapping['9'] = 9 
valMapping['10'] = 10 
valMapping['J'] = 11
valMapping['Q'] = 12 
valMapping['K'] = 13

cardMapping = {}
cardMapping[1] = 'A' 
cardMapping[2] = '2' 
cardMapping[3] = '3' 
cardMapping[4] = '4' 
cardMapping[5] = '5' 
cardMapping[6] = '6' 
cardMapping[7] = '7' 
cardMapping[8] = '8' 
cardMapping[9] = '9' 
cardMapping[10] = '10' 
cardMapping[11] = 'J' 
cardMapping[12] = 'Q' 
cardMapping[13] = 'K' 
cardMapping[14] = 'A' 


class Result(): 
	win = 1
	tie = 0
	loss = -1

class Ranker: 

	# @return true if and only if hand represents a royal flush
	@staticmethod
	def isRoyalFlush(hand): 
		for suit in Suits: 
			if Card(suit, '10') in hand and Card(suit, 'J') in hand \
			and Card(suit, 'Q') in hand and Card(suit, 'K') in hand \
			and Card(suit, 'A') in hand: 
				return True
		return False

	# @return true if and only if hand represents a straight flush
	@staticmethod
	def isStraightFlush(hand): 
		return Ranker.isStraight(hand) and Ranker.isFlush(hand)

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

	# @return true if and only if hand represents a straight
	@staticmethod
	def isStraight(hand): 
		assert len(hand) == 7
		vals = [card.val for card in hand]
		# explicitly check for '10,J,Q,K,A'
		if '10' in vals and 'J' in vals and 'Q' in vals and 'K' in vals \
			and 'A' in vals: 
			return True
		vals = [valMapping[x] for x in vals]
		vals.sort()
		countIncreasing = 1
		for i in range(6):
			if vals[i] + 1 == vals[i+1]: 
				countIncreasing += 1
			elif vals[i] == vals[i+1]:
				countIncreasing += 0
			else:
				countIncreasing = 1
			if countIncreasing >= 5:
				return True

		return countIncreasing >= 5





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


for val in Values: 
	if val in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
		suit = Suits[0] 
		num = valMapping[val]
		testHand = []
		testHand = [
					Card(suit, val), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck = Deck()
		for card in testHand: 
			testDeck.get(card)

		testDeck.shuffleDeck() 
		testHand.append(testDeck.getFirstCard())
		testHand.append(testDeck.getFirstCard())

		for _ in range(20): 
			shuffle(testHand)
			assert Ranker.isStraight(testHand)


for val in Values: 
	if val in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
		suit = Suits[0] 
		num = valMapping[val]
		testHand = []
		testHand = [
					Card(suit, val), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck = Deck()
		for card in testHand: 
			testDeck.get(card)

		testDeck.shuffleDeck() 
		testHand.append(testDeck.getFirstCard())
		testHand.append(testDeck.getFirstCard())

		for _ in range(20): 
			shuffle(testHand)
			assert Ranker.isStraightFlush(testHand)

hand = [Card(Suits[0], '10'), Card(Suits[0], 'J'), 
		Card(Suits[0], 'Q'), Card(Suits[0], 'K'), 
		Card(Suits[0], 'A')]
assert Ranker.isRoyalFlush(hand)

hand = [Card(Suits[1], '10'), Card(Suits[1], 'J'), 
		Card(Suits[1], 'Q'), Card(Suits[1], 'K'), 
		Card(Suits[1], 'A')]
assert Ranker.isRoyalFlush(hand)
  
  
hand = [Card(Suits[1], '10'), Card(Suits[2], 'J'), 
		Card(Suits[2], 'Q'), Card(Suits[2], 'K'), 
		Card(Suits[2], 'A')]
assert not Ranker.isRoyalFlush(hand)









