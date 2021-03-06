from Cards import Card
from Cards import Deck
from Cards import Suits
from Cards import Values
from Ranker import Ranker
import thread
import threading

# Runs simulation for pair hole cards 
def runOnePairSimulation(val, NO_OF_SIMS = 5000000):
	wins = 0
	loss = 0
	tie = 0
	for i in range(NO_OF_SIMS):
		if i in [x for x in range(1, NO_OF_SIMS, 1000000)]:
			print str(i * 100/ NO_OF_SIMS) + "% DONE..."

			wins_ = wins/float(i) * 100
			loss_ = loss/float(i) * 100
			tie_ = tie/float(i) * 100

			print str(wins_) + "\t" + str(tie_) + "\t" + str(loss_)

		deck = Deck()
		deck.shuffleDeck()
		handA = [] 
		handB = []
		handA.append(deck.get(Card(Suits[0], val)))
		handA.append(deck.get(Card(Suits[1], val)))
		handB.append(deck.getFirstCard())
		handB.append(deck.getFirstCard())
		for _ in range(5):	
			card = deck.getFirstCard()
			handA.append(card)
			handB.append(card)

		result = Ranker.rank(handA, handB)
		if result == 1:
			wins = wins + 1
		elif result == -1:
			loss = loss + 1
		else: 
			tie = tie + 1

	wins = wins/float(NO_OF_SIMS) * 100
	loss = loss/float(NO_OF_SIMS) * 100
	tie = tie/float(NO_OF_SIMS) * 100

	return [wins, loss, tie]



for val in Values:
	print "########### STARTING FOR " + str(val) + " ###############"
	res = runOnePairSimulation(val)
	print "########### FINAL FOR " + str(val) + " ###############"
	print str(res[0]) + "\t" + str(res[2]) + str(res[1])
