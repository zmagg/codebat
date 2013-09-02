def is_palindrome(phrase):
    # Strip everything out of phrase except alphabet
    strippedphrase = ''.join(char for char in phrase if char.isalpha())
    return strippedphrase == strippedphrase[::-1]
