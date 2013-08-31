def perfect_shuffle(deck):
    i = 0
    j = 1
    shuffled_deck = []
    while i < len(deck):
        if i < len(deck)/2:
            shuffled_deck.insert(i*2, deck[i])
        else:
            shuffled_deck.insert(j, deck[i])
            j += 2
        i += 1
    return shuffled_deck
