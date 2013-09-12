def collatz(n):
    return_list = []
    while n != 1:
       return_list.append(n)
       n = next_collatz(n)
    return_list.append(1)
    return return_list

def next_collatz(n):
    if n%2 == 0:
        return n/2
    else:
        return 3 * n + 1
