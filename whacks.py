def whacks(moles, holes):
    for hole in holes:
        moles = whack(moles, hole)
    return moles

def whack(moles, hole):
    if moles[hole] >= 0:
        moles[hole] = -moles[hole]
        next_mole = (hole+1) % len(moles)
        moles[next_mole] = moles[next_mole] - moles[hole]
        moles[hole-1] = moles[hole-1] - moles[hole]
    return moles
