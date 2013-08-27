def piglatin(word):
    chars = list(word)
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    consonantString = "" 
    if chars[0] in vowels:
        return word + "way"
    else:
        for char in chars:
            if char not in vowels and char.isalpha():
                consonantString += char
            elif char in vowels:
                return ''.join(chars[len(consonantString):] + chars[0:len(consonantString)]) + "ay"
        return consonantString + "ay"
