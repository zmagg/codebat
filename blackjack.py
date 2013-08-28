def blackjack(player, dealer):
    player_sum = count_cards(player)
    dealer_sum = count_cards(dealer)

    if player_sum > 21:
        return False
    elif dealer_sum > 21:
        return True
    else:
        if player_sum > dealer_sum:
            return True
        else:
            return False

def count_cards(hand):
    hand_value = 0
    for card in hand:
        if card is 1:
            if hand_value > 10:
                hand_value +=1
            else:
                hand_value += 11
        else:
            hand_value += card
    return hand_value
