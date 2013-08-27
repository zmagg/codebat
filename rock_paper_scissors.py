def rock_paper_scissors(a, b):
    if a is b:
        return 0
    if a is 'rock':
        return 1 if b is 'scissors' else -1
    if a is 'paper':
        return 1 if b is 'rock' else -1
    if a is 'scissors':
        return 1 if b is 'paper' else -1
        

