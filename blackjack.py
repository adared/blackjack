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

	player_hand = deal_until(lambda hand: raw_input("hand: %s hit? y/n" %hand) == 'y')
	dealer_hand = deal_until(lambda hand: sum(hand) < 17)


	dscore = 0
	pscore = 0
	phand = [hit(), hit()]
	pscore = sum(phand)
	if pscore == 21:
		print 'Blackjack!  You Win!'
	else:
		print 'You were dealt a ' + phand[0] + 'and a ' + phand[1] + '.  Your current total is ' + pscore + '.'
		while pscore <= 21:
			print 'Would you like to hit?'
			action = raw_input('hit? y/n')
			if action == 'y':
				phand = phand.append(hit())
				pscore = sum(phand)
				print  'You were dealt a ' + phand[-1] + '.  Your current total is now ' + pscore + '.'
			else:
				print 'Playing it safe, eh?  Lets see how the dealer does.'
				return pscore


test_value()

blackjack()