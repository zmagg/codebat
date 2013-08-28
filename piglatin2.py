def piglatin(word):
    return capitalize(word, characterize(word))

def characterize(word):
    vowels = 'aeiouAEIOU'

    consonantString = "" 
    word = word.lower()
    if word[0] in vowels:
        return word + "way"
    else:
        i = 0
        while i < len(word):
            char = word[i]
            if char not in vowels and char.isalpha():
                if char is 'q' and i+1 < len(word) and word[i+1] is 'u':
                    consonantString += "qu"
                    i+=1
                elif char is 'y' and i is not 0:
                    return vowel_return(word, consonantString)
                else:
                    consonantString += char
            elif char in vowels:
                return vowel_return(word, consonantString)
            i+=1
        return consonantString + "ay"

def capitalize(word, char_word):
    if word.isupper():
        return char_word.upper()
    if word[0].isupper():
        return char_word[0].upper() + char_word[1:]
    return char_word

def vowel_return(word, consonantString):
    return ''.join(word[len(consonantString):] + word[0:len(consonantString)]) + "ay"

