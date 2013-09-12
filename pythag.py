def pythag(p):
    c = p - 2
    b = 1
    while c > b:
        # a + b = p - c
        p_neg_c = p - c
        b = p_neg_c - 1
        a = 1
        while b > a:
            # check to see if pythag triplet
            if a**2 + b**2 == c**2:
                return [a, b, c]
            b -= 1
            a = p_neg_c - b
        c -= 1
    return False
