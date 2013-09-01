def whack_a_mole(moles):
    return_list = []
    whacked_list = []
    # all positive
    mole_heights = sorted(moles)
    if mole_heights[0] > 0:
        print "all positive"
        return return_list.extend([moles, None])

    tallest_mole_height = mole_heights.pop()
    tallest_mole = moles.index(tallest_mole_height)
    while tallest_mole_height > 0:
        whacked_list.append(tallest_mole)
        moles = whack(moles, tallest_mole)
        mole_heights = sorted(moles)
        tallest_mole_height = mole_heights.pop()
        tallest_mole = moles.index(tallest_mole_height)

    return_list.append(moles)
    return_list.append(whacked_list)
    return return_list

def whack(moles, hole):
    if moles[hole] >= 0:
        moles[hole] = -moles[hole]
        next_mole = (hole+1) % len(moles)
        moles[next_mole] = moles[next_mole] - moles[hole]
        moles[hole-1] = moles[hole-1] - moles[hole]
    return moles
