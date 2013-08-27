def fizzbuzz(n):
    i = 1
    fizzBuzz = []
    while i < n:
        if not i % 15:
            fizzBuzz.append("FizzBuzz")
        elif not i % 3:
            fizzBuzz.append("Fizz")
        elif not i % 5:
            fizzBuzz.append("Buzz")
        else:
            fizzBuzz.append(i)
        i+=1
    return fizzBuzz
