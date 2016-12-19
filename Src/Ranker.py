### Class to manage ranking of Texas Holdem Poker hands
### (c) Tibrewal, Karan. 
### Williams College, 2016


from Cards import Deck
from Cards import Values
from Cards import Suits
from Cards import Card
from random import shuffle
from random import randrange
import itertools
import collections


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
		vals = [card.val for card in hand]
		# explicitly check for '10,J,Q,K,A'
		if '10' in vals and 'J' in vals and 'Q' in vals and 'K' in vals \
			and 'A' in vals: 
			return True
		vals = [valMapping[x] for x in vals]
		vals.sort()
		countIncreasing = 1
		for i in range(len(hand) - 1):
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


	# @Pre Hand1, Hand2 are straight flushes
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherStraightFlush(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		maxA = 2
		for hand in handACombos:
			if Ranker.isStraightFlush(hand): 
			   if 'A' in [x.val for x in hand] and \
				max([valMapping[x.val] for x in hand]) == 13: 
			   		maxA = 14 
			   maxA = max(maxA, max([valMapping[x.val] for x in hand]))
		## All combos of handB 
		handBCombos = itertools.combinations(handB, 5)
		maxB = 2
		for hand in handBCombos:
			if Ranker.isStraightFlush(hand): 
				if 'A' in [x.val for x in hand] and \
				max([valMapping[x.val] for x in hand]) == 13: 
			   		maxB = 14 
			   	maxB = max(maxB, max([valMapping[x.val] for x in hand]))

		if maxA == maxB: 
			return 0
		elif maxA > maxB:
			return 1
		else:
			return 0

	# @Pre Hand1, Hand2 are straights
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherStraight(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		maxA = 2
		for hand in handACombos:
			if Ranker.isStraight(hand): 
			   if 'A' in [x.val for x in hand] and \
				max([valMapping[x.val] for x in hand]) == 13: 
			   		maxA = 14 
			   maxA = max(maxA, max([valMapping[x.val] for x in hand]))
		## All combos of handB 
		handBCombos = itertools.combinations(handB, 5)
		maxB = 2
		for hand in handBCombos:
			if Ranker.isStraight(hand): 
				if 'A' in [x.val for x in hand] and \
				max([valMapping[x.val] for x in hand]) == 13: 
			   		maxB = 14 
			   	maxB = max(maxB, max([valMapping[x.val] for x in hand]))


		if maxA == maxB: 
			return 0
		elif maxA > maxB:
			return 1
		else:
			return 0

	# @Pre Hand1, Hand2 are flush
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherFlush(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		maxA = 2
		for hand in handACombos:
			if Ranker.isFlush(hand): 
			   if 'A' in [x.val for x in hand]: 
			   		maxA = 14 
			   maxA = max(maxA, max([valMapping[x.val] for x in hand]))
		## All combos of handB 
		handBCombos = itertools.combinations(handB, 5)
		maxB = 2
		for hand in handBCombos:
			if Ranker.isFlush(hand): 
				if 'A' in [x.val for x in hand]: 
			   		maxB = 14 
			   	maxB = max(maxB, max([valMapping[x.val] for x in hand]))

	
		if maxA == maxB: 
			return 0
		elif maxA > maxB:
			return 1
		else:
			return -1

	# @Pre Hand1, Hand2 are 4 of a kind
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherFourOfAKind(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		max4A = 0

		for hand in handACombos:
			if Ranker.isFourOfAKind(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 4:
			   			max4A = max(max4A, \
			   				valMapping[key] if valMapping[key] != 1 else 14)
			   		else:
			   			kickerA = valMapping[key] if valMapping[key] != 1 else 14
			   
		handBCombos = itertools.combinations(handB, 5)
		max4B = 0
		for hand in handBCombos:
			if Ranker.isFullHouse(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 4:
			   			max4B = max(max4B, \
			   				valMapping[key] if valMapping[key] != 1 else 14)
			   		else:
			   			kickerB = valMapping[key] if valMapping[key] != 1 else 14

		if max4A > max4B:
			return 1
		elif max4A < max4B:
			return -1
		elif kickerA > kickerB:
			return 1
		elif kickerB < kickerA:
			return -1
		else:
			return 0

	# @Pre Hand1, Hand2 are 3 of a kind
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherThreeOfAKind(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		max4A = 0

		for hand in handACombos:
			if Ranker.isFourOfAKind(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 3:
			   			max4A = max(max4A, \
			   				valMapping[key] if valMapping[key] != 1 else 14)
			   		else:
			   			kickerA = valMapping[key] if valMapping[key] != 1 else 14
			   
		handBCombos = itertools.combinations(handB, 5)
		max4B = 0
		for hand in handBCombos:
			if Ranker.isFullHouse(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 3:
			   			max4B = max(max4B, \
			   				valMapping[key] if valMapping[key] != 1 else 14)
			   		else:
			   			kickerB = valMapping[key] if valMapping[key] != 1 else 14

		if max4A > max4B:
			return 1
		elif max4A < max4B:
			return -1
		elif kickerA > kickerB:
			return 1
		elif kickerB < kickerA:
			return -1
		else:
			return 0




	# @Pre Hand1, Hand2 are full house
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherFullHouse(handA, handB): 
		## All combos of handA
		handACombos = itertools.combinations(handA, 5)
		max3A = 0
		max2A = 0
		for hand in handACombos:
			if Ranker.isFullHouse(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 3:
						this3 = key
					else:
			   			this2 = key
			   	max3A = max(max3A, valMapping[this3] if valMapping[this3] != 1 else 14)
			   	max2A = max(max2A, valMapping[this2] if valMapping[this2] != 1 else 14)
		handBCombos = itertools.combinations(handB, 5)
		max3B = 0
		max2B = 0
		for hand in handBCombos:
			if Ranker.isFullHouse(hand): 
				freq = collections.Counter([card.val for card in hand])
				for key in freq: 
					if freq[key] == 3:
						this3 = key
					else:
			   			this2 = key
			   	max3B = max(max3B, valMapping[this3] if valMapping[this3] != 1 else 14)
			   	max2B = max(max2B, valMapping[this2] if valMapping[this2] != 1 else 14)

		if max3A > max3B:
			return 1
		elif max3A < max3B:
			return -1
		elif max2A > max2B:
			return 1
		elif max2A < max2B:
			return -1
		else: 
			return 0



		## All combos of handB 
		handBCombos = itertools.combinations(handB, 5)
		maxB = 2
		for hand in handBCombos:
			if Ranker.isFlush(hand): 
				if 'A' in [x.val for x in hand]: 
			   		maxB = 14 
			   	maxB = max(maxB, max([valMapping[x.val] for x in hand]))

	
		if maxA == maxB: 
			return 0
		elif maxA > maxB:
			return 1
		else:
			return -1


	# @Pre Hand1, Hand2 are just high cards
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherHighCard(handA, handB):
		assert len(handA) == len(handB) 
		valsA = [valMapping[x.val] if valMapping[x.val] != 1 else 14 for x in handA]
		valsB = [valMapping[x.val] if valMapping[x.val] != 1 else 14 for x in handB]
		valsA.sort(reverse = True)
		valsB.sort(reverse = True)

		for i in range(5): 
			if valsA[i] > valsB[i]:
				return 1
			elif valsA[i] < valsB[i]:
				return -1
		return 0

		
	# @Pre Hand1, Hand2 have pairs
	# @return 1 if handA > handB
	# 			0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def higherPairs(handA, handB): 
		pairsA = []
		kickerA = 0
		freq = collections.Counter([card.val for card in handA])
		for key in freq: 
			if freq[key] == 2:
			   			pairsA.append(valMapping[key] if valMapping[key] != 1 else 14)
			else:
	   			kickerA = max(kickerA, \
		   				valMapping[key] if valMapping[key] != 1 else 14)
		pairsB = []
		kickerB = 0
		freq = collections.Counter([card.val for card in handB])
		for key in freq: 
			if freq[key] == 2:
			   			pairsB.append(valMapping[key] if valMapping[key] != 1 else 14)
	   		else:
	  	  		kickerB = max(kickerB, \
			   				valMapping[key] if valMapping[key] != 1 else 14)
		pairsA.sort(reverse = True)
		pairsB.sort(reverse = True)

		if len(pairsA) >= 2 and len(pairsB) == 1:
			return 1
		elif len(pairsA) == 1 and len(pairsB) >= 2:
			return -1

		for i in range(min(len(pairsA), 2)): 
			if pairsA[i] > pairsB[i]:
				return 1
			elif pairsA[i] < pairsB[i]:
				return -1

		if kickerA > kickerB:
			return 1
		elif kickerA < kickerB:
			return -1
		else:
			return 0






	# @ return 1 if handA > handB
	# 		 0 if handA = handB
	#          -1 if handA < handB 
	@staticmethod
	def rank(handA, handB): 
		# ROYAL FLUSH? 
		if Ranker.isRoyalFlush(handA) and Ranker.isRoyalFlush(handB):
			return 0
		elif Ranker.isRoyalFlush(handA):
			return 1
		elif Ranker.isRoyalFlush(handB):
			return -1
		# STRAIGHT FLUSH? 
		elif Ranker.isStraightFlush(handA) and Ranker.isStraightFlush(handB):
			return Ranker.higherStraightFlush(handA, handB)
		elif Ranker.isStraightFlush(handA):
			return 1
		elif Ranker.isStraightFlush(handB):
			return -1
		# FOUR OF A KIND?
		elif Ranker.isFourOfAKind(handA) and Ranker.isFourOfAKind(handB):
			return Ranker.higherFourOfAKind(handA, handB)
		elif Ranker.isFourOfAKind(handA):
			return 1
		elif Ranker.isFourOfAKind(handB):
			return -1
		# FULL HOUSE? 
		elif Ranker.isFullHouse(handA) and Ranker.isFullHouse(handB):
			return Ranker.higherFullHouse(handA, handB)
		elif Ranker.isFullHouse(handA):
			return 1
		elif Ranker.isFullHouse(handB):
			return -1
		# FLUSH? 
		elif Ranker.isFlush(handA) and Ranker.isFlush(handB):
			return Ranker.higherFlush(handA, handB)
		elif Ranker.isFlush(handA):
			return 1
		elif Ranker.isFlush(handB):
			return -1
		# STRAIGHT? 
		elif Ranker.isStraight(handA) and Ranker.isStraight(handB):
			return Ranker.higherStraight(handA, handB)
		elif Ranker.isStraight(handA):
			return 1
		elif Ranker.isStraight(handB):
			return -1
		# THREE OF A KIND?
		elif Ranker.isThreeOfAKind(handA) and Ranker.isThreeOfAKind(handB):
			return Ranker.higherStraight(handA, handB)
		elif Ranker.isThreeOfAKind(handA):
			return 1
		elif Ranker.isThreeOfAKind(handB):
			return -1
		# TWO PAIRS?
		elif Ranker.isTwoPairs(handA) and Ranker.isTwoPairs(handB):
			return Ranker.higherPairs(handA, handB)
		elif Ranker.isTwoPairs(handA):
			return 1
		elif Ranker.isTwoPairs(handB):
			return -1
		# PAIR?
		elif Ranker.isPair(handA) and Ranker.isPair(handB):
			return Ranker.higherPairs(handA, handB)
		elif Ranker.isPair(handA):
			return 1
		elif Ranker.isPair(handB):
			return -1
		# HIGH CARD?
		else:
			return Ranker.higherHighCard(handA, handB)






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

for val in Values: 
	if val in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
		suit = Suits[0] 
		num = valMapping[val]
		testHand1 = []
		testHand1 = [
					Card(suit, val), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck1 = Deck()
		for card in testHand1: 
			testDeck1.get(card)

		testDeck1.shuffleDeck() 
		testHand1.append(testDeck1.getFirstCard())
		testHand1.append(testDeck1.getFirstCard())

		num = valMapping[val] - 1
		testHand2 = []
		testHand2 = [
					Card(suit, cardMapping[num]), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck2 = Deck()
		for card in testHand2: 
			testDeck2.get(card)

		testDeck2.shuffleDeck() 
		testHand2.append(testDeck2.getFirstCard())
		testHand2.append(testDeck2.getFirstCard())

		for _ in range(20): 
			shuffle(testHand1)
			shuffle(testHand2)
			assert Ranker.higherStraightFlush(testHand1, testHand2) >= 0



for val in Values: 
	if val in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
		suit = Suits[0] 
		num = valMapping[val]
		testHand1 = []
		testHand1 = [
					Card(suit, val), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck1 = Deck()
		for card in testHand1: 
			testDeck1.get(card)

		testDeck1.shuffleDeck() 
		testHand1.append(testDeck1.getFirstCard())
		testHand1.append(testDeck1.getFirstCard())

		num = valMapping[val] - 1
		testHand2 = []
		testHand2 = [
					Card(suit, cardMapping[num]), Card(suit, cardMapping[num + 1]), 
					Card(suit, cardMapping[num + 2]), Card(suit, cardMapping[num + 3]),
					Card(suit, cardMapping[num + 4])
			       ]
		testDeck2 = Deck()
		for card in testHand2: 
			testDeck2.get(card)

		testDeck2.shuffleDeck() 
		testHand2.append(testDeck2.getFirstCard())
		testHand2.append(testDeck2.getFirstCard())

		for _ in range(20): 
			shuffle(testHand1)
			shuffle(testHand2)
			assert Ranker.higherStraight(testHand1, testHand2) >= 0

# Test for higher high card
for _ in range(10000):
	deck1 = Deck()
	deck1.shuffleDeck()
	handA = []
	maxA = 0
	for _ in range(5):
		card = deck1.getFirstCard()
		val = valMapping[card.val] if valMapping[card.val] != 1 else 14
		maxA = max(maxA, val)
		handA.append(card)

	deck2 = Deck()
	deck2.shuffleDeck()
	handB = []
	maxB = 0
	for _ in range(5):
		card = deck2.getFirstCard()
		val = valMapping[card.val] if valMapping[card.val] != 1 else 14
		maxB = max(maxB, val)
		handB.append(card)

	if maxB == maxA:
		result = Ranker.higherHighCard(handA, handB)
	elif maxA > maxB:
		result = 1
	else:
		result = -1
	assert result == Ranker.higherHighCard(handA, handB)

	


## Test for higherFlush
for suit in Suits:
	for _ in range(1000):

		testDeck1 = Deck()
		testHand1 = [] 
		max1 = 2
		for _ in range(5):
			card = testDeck1.get(Card(suit, \
						Values[randrange(0, len(Values), 1)]))
			while card is None: 
				card = testDeck1.get(Card(suit, \
						Values[randrange(0, len(Values), 1)]))
			if card.val == 'A':
				max1 = 14
			max1 = max(max1, valMapping[card.val])
			testHand1.append(card)

		testDeck1.shuffleDeck() 
		card = testDeck1.getFirstCard()
		while(card.suit == suit): 
			card = testDeck1.getFirstCard()
		testHand1.append(card)
		card = testDeck1.getFirstCard()
		while(card.suit == suit): 
			card = testDeck1.getFirstCard()
		testHand1.append(card)
		testHand1.append(card)

		testDeck2 = Deck()
		testHand2 = [] 
		max2 = 2
		for _ in range(5):
			card = testDeck2.get(Card(suit, \
						Values[randrange(0, len(Values), 1)]))
			while card is None: 
				card = testDeck2.get(Card(suit, \
						Values[randrange(0, len(Values), 1)]))
			if card.val == 'A':
				max2 = 14
			max2 = max(max2, valMapping[card.val])
			testHand2.append(card)

		testDeck2.shuffleDeck() 
		card = testDeck2.getFirstCard()
		while(card.suit == suit): 
			card = testDeck2.getFirstCard()
		testHand2.append(card)
		card = testDeck2.getFirstCard()
		while(card.suit == suit): 
			card = testDeck2.getFirstCard()
		testHand2.append(card)
		testHand2.append(card)


		if max1 == max2: 
			result = 0
		elif max1 > max2:
			result = 1
		else:
			result = -1
		
		for _ in range(20): 
			shuffle(testHand1)
			shuffle(testHand2)
			assert Ranker.higherFlush(testHand1, testHand2) == result

## Test for higher full house
for val in Values:
	testDeck = Deck()
	testHandA = [] 
	testHandA.append(testDeck.get(Card(Suits[0], val)))
	testHandA.append(testDeck.get(Card(Suits[1], val)))
	max2A = valMapping[val] if valMapping[val] != 1 else 14
	x = randrange(0, len(Values), 1)
	while Values[x] == val:
			x = randrange(0, len(Values), 1)
	testHandA.append(testDeck.get(Card(Suits[0], Values[x])))
	testHandA.append(testDeck.get(Card(Suits[1], Values[x])))
	testHandA.append(testDeck.get(Card(Suits[2], Values[x])))
	max3A = valMapping[Values[x]] if valMapping[Values[x]] != 1 else 14

	testDeck = Deck()
	testHandB = [] 
	testHandB.append(testDeck.get(Card(Suits[0], val)))
	testHandB.append(testDeck.get(Card(Suits[1], val)))
	max2B = valMapping[val] if valMapping[val] != 1 else 14
	x = randrange(0, len(Values), 1)
	while Values[x] == val:
			x = randrange(0, len(Values), 1)
	testHandB.append(testDeck.get(Card(Suits[0], Values[x])))
	testHandB.append(testDeck.get(Card(Suits[1], Values[x])))
	testHandB.append(testDeck.get(Card(Suits[2], Values[x])))
	max3B = valMapping[Values[x]] if valMapping[Values[x]] != 1 else 14
	
	if max3A > max3B:
		result = 1
	elif max3A < max3B:
		result = -1
	else: 
		result = Ranker.higherFullHouse(testHandA, testHandB)

	assert result == Ranker.higherFullHouse(testHandA, testHandB)


# Test for higher four of a kind
## Test for four of a kind
for _ in range(1000):
	valsA = valMapping[Values[randrange(0, len(Values))]]
	valsB = valMapping[Values[randrange(0, len(Values))]]
	valsA = 14 if valsA == 1 else valsA
	valsB = 14 if valsB == 1 else valsB
	if valsA == valsB:
		valsB = (13 + valsB) % 14 if (13 + valsB) % 14 != 1 else 4
	if valsA < valsB: 
		valsA, valsB = valsB, valsA
	
	testDeck = Deck()
	testHandA = [] 
	for suit in Suits: 
		testHandA.append(testDeck.get(Card(suit, cardMapping[valsA])))
	testDeck.shuffleDeck() 
	testHandA.append(testDeck.getFirstCard())
	testHandA.append(testDeck.getFirstCard())
	testHandA.append(testDeck.getFirstCard())
	
	testDeck = Deck()
	testHandB = [] 
	for suit in Suits: 
		testHandB.append(testDeck.get(Card(suit, cardMapping[valsB])))
	testDeck.shuffleDeck() 
	testHandB.append(testDeck.getFirstCard())
	testHandB.append(testDeck.getFirstCard())
	testHandB.append(testDeck.getFirstCard())
	assert Ranker.higherFourOfAKind(testHandA, testHandB) == 1




	





