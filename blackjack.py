import random

def make_hit():
	deck = sum([[x] * 4 for x in range(2, 9)], [])
	deck += [10] * 4 * 4
	deck += [11] * 4


	def hit():
		card = random.choice(deck)
		deck.remove(card)
		return card

	return hit


def value(hand):
	val = sum(hand) 
	while val > 21:
		if 11 in hand:
			hand.remove(11)
			hand.append(1)
			val = sum(hand)
		else:
			break
	return val


def test_value():
	hand1 = [11, 10, 9, 10]
	val1 = value(hand1)
	assert val1 == 30, val1

	hand2 = [10, 10, 5]
	val2 = value(hand2)
	assert val2 == 25, val2

	hand3 = [5, 5, 5, 2, 2, 11]
	val3 =value(hand3)
	assert val3 == 20, val3


def blackjack():
	hit = make_hit()

	def deal_until(stop_func):
		hand = []
		while stop_func(hand):
			hand.append(hit())
		return hand

	dealer_hand = deal_until(lambda hand: value(hand) < 17)
	dealer_score = value(dealer_hand)
	
	def player_deal(hand):
		if len(hand) < 2:
			return True
		player_score = value(hand)
		print 'Your hand is now', hand, 'Your current total is', player_score
		if player_score == 21:
			if len(hand) == 2:
				if len(dealer_hand) == 2 and dealer_score == 21:
					print 'Two Blackjacks!  Tie game.'
				else: 
					print "Blackjack! You beat the dealer's", dealer_score, 'You Win!'
			else:
				if dealer_score != 21:
					print "21!  You beat the dealer's", dealer_score, "You Win!"
				else:
					print '21! Unfortunately, the dealer also has a 21. Tie Game.'
		elif player_score > 21:
			print 'Busted! Sorry, you lose.'
		else:
			action = raw_input('hit? y/n')
			return action == 'y'

	player_hand = deal_until(player_deal)
	player_score = value(player_hand)
	
	if player_score < 21:
		if dealer_score > 21:
			print 'The dealer has busted. You win with a', player_score, '. Congrats!'
		else:
			if player_score > dealer_score:
				print 'You win!  Your', player_score, "beat the dealer's", dealer_score, '.  Congrats!'
			elif dealer_score > player_score:
				print 'Sorry, Your', player_score, "can't beat the dealer's", dealer_score, '. You lose.'
			else:
				print 'Both you and the dealer have a', player_score, '. Tie game.'


blackjack()