from Ranker import Ranker 
from Ranker import valMapping
from Ranker import cardMapping
from Cards import Deck
from Cards import Values
from Cards import Suits
from Cards import Card
from random import shuffle
from random import randrange
import itertools
import collections


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




	





