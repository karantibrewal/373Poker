from Player import Player
from Cards import Deck
from Cards import Card
from Ranker import Ranker


Player1 = Player(0)
Player2 = Player(0.45)
firstWin = 0
numberOfSims = 5000000
for i in range(numberOfSims):
	if i in [x for x in range(1, 5000000, 1000000)]:
		print str(i*100/numberOfSims) + "% DONE..." 
		print str(firstWin/float(i))
	K1 = 2000
	K2 = 6000
	firstPlayerBlind = True

	while K1 > 0 and K2 > 0: 

		if firstPlayerBlind:
			deck = Deck()
			deck.shuffleDeck()
			player1Card1 = deck.getFirstCard()
			player1Card2 = deck.getFirstCard()
			action = Player1.action(K1, K2, 200, 400, player1Card1, player1Card2)
			if action == -1: # first player folds 
				K1 = K1 - 200
				K2 = K2 + 200
			else: # first player jams
				player2Card1 = deck.getFirstCard()
				player2Card2 = deck.getFirstCard()
				action = Player2.action(K2, K1, 400, 200, player2Card1, player2Card2)
				if action == -1: #second player folds
					K1 = K1 + 400
					K2 = K2 - 400
				else: 
					handA = [player1Card1, player1Card2]
					handB = [player2Card1, player2Card2] 
					for _ in range(5):
						card = deck.getFirstCard()
						handA.append(card)
						handB.append(card)
				winner = Ranker.rank(handA, handB)
				if winner == 1: 
					pot = min(K1, K2)
					K1 = K1 + pot
					K2 = K2 - pot
				elif winner == -1: 
					pot = min(K1, K2)
					K1 = K1 - pot
					K2 = K2 + pot
		else: 
			deck = Deck()
			deck.shuffleDeck()
			player2Card1 = deck.getFirstCard()
			player2Card2 = deck.getFirstCard()
			action = Player2.action(K2, K1, 200, 400, player2Card1, player2Card2)
			if action == -1: # second player folds 
				K1 = K1 + 200
				K2 = K2 - 200
			else: # second player jams
				player1Card1 = deck.getFirstCard()
				player1Card2 = deck.getFirstCard()
				action = Player1.action(K1, K2, 400, 200, player1Card1, player1Card2)
				if action == -1: #second player folds
					K1 = K1 - 400
					K2 = K2 + 400
				else: 
					handA = [player1Card1, player1Card2]
					handB = [player2Card1, player2Card2] 
					for _ in range(5):
						card = deck.getFirstCard()
						handA.append(card)
						handB.append(card)
				winner = Ranker.rank(handA, handB)
				if winner == 1: 
					pot = min(K1, K2)
					K1 = K1 + pot
					K2 = K2 - pot
				elif winner == -1: 
					pot = min(K1, K2)
					K1 = K1 - pot
					K2 = K2 + pot

		firstPlayerBlind = not firstPlayerBlind

	if K1 > 0:
		firstWin += 1



print(firstWin/float(numberOfSims))





