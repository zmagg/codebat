def number_perfect_shuffles(n):
    deck = [x for x in range(n)]
    count = 1
    new_deck = perfect_shuffles(deck)
    while deck != new_deck:
        count += 1
        print count
        new_deck = perfect_shuffles(new_deck)
    return count

def perfect_shuffles(deck):
    M = len(deck)/2
    top, bottom = deck[:M], deck[M:]
    result = []
    while top and bottom:
        result.extend((top.pop(0), bottom.pop(0)))
    return result
