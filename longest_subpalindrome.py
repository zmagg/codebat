def longest_subpalindrome(string):
    j = len(string)
    i = 0
    while i < len(string):
        j = i
        while j >= 0:
            check_string = string[i-j:len(string)-j]
            if is_palindrome(check_string):
                return check_string
            j -= 1
        i += 1
    return "no palindrome"

def is_palindrome(phrase):
    return phrase == phrase[::-1]
