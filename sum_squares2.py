def sum_squares2(num):
    i = 0
    sum_square = 0
    while i < len(num):
        sum_square += num[i] * num[i]
        i += 1
    print sum_square
