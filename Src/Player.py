

import csv

class Probility: 

	def __init__(self, win, tie, loss, fold):
		self.win = win
		self.tie = tie
		self.loss = loss
		self.fold = fold

def loadTransitionModel(filename): 
	file = open(filename, 'rb')
	reader = csv.reader(file)
	map = {}
	rownum = 0
	for row in reader: 
		if rownum == 0: 
			rownum = rownum + 1
		else: 
			cards = row[0]
			space = cards.index(',')
			card1 = cards[0: space]
			cards = cards[space+2: ]
			space = cards.index(' ')
			card2 = cards[0: space]
			suit = cards[len(cards) - 1]
			cards = sorted([card1, card2])
			key = cards[0] + ',' + cards[1] + ' ' + suit
			win = float(row[1])
			tie = float(row[2])
			loss = float(row[3])
			fold = float(row[4])
			map[key] = Probility(win, tie, loss, fold)


	file.close()
	return map


class Player: 

	def __init__(self, riskAversion):
		self.riskAversion = riskAversion
		self.transitionModel = loadTransitionModel('transitionmodel.csv')


	# @return 1 if JAM, -1 if FOLD
	def action(self, K1, K2, A1, A2, card1, card2): 
		card1val = card1.val
		card2val = card2.val
		suit = 's' if card1.suit == card2.suit else 'o'
		cards = sorted([card1val, card2val])
		key = cards[0] + ',' + cards[1] + ' ' + suit
		prob = self.transitionModel[key]
		foldUtility = -A1
		jamExpectation = A2 * prob.fold + min(K1, K2) * (prob.win - prob.loss)
		jamVariance = ((A2 - jamExpectation) ** 2) * prob.fold \
				+ ((min(K1, K2) - jamExpectation) ** 2) * prob.win + \
				((-min(K1, K2) - jamExpectation) ** 2) * prob.loss + \
				 ((- jamExpectation) ** 2) * prob.tie
		jamUtility = jamExpectation - self.riskAversion * (jamVariance ** (0.5))
		if jamUtility > foldUtility: 
			return 1
		else:
			return 0


