# pigLatin.py
# Ira Goldstein

# Pig Latin is a language game in which words in English are altered.

# There are two rules that need to be followed to convert text to Pig Latin:
#
# 1) If the word begins with a consonant sound, the initial consonant or
# consonant cluster (i.e., all of the letters that come before the initial vowel)
# is moved to the end of the word, and "ay" is added at the end; or
#
# 2) If the word begins with a vowel, just add "way" to the end of the word.


# Locate and return the position of the first vowel in the string
# If there isn't a vowel, return -1
def findVowel(string):

    return position


# Move the initial consonants to the end of the word
def moveConsonant(string, vowelPos):

    return string


# Add the ay/way to the end of the word
def addSuffix(string, vowelPos):

    return string


# ...?
def pigLatin(string):
    vowelPos = findVowel(string)
    if vowel > 0:
      string = moveConsonant(string, vowelPos)
    string = addSuffix(string, vowelPos)
    return string


#  Define functions above
#  Call functions below

# Ask the user for their text.
myString =  input("What text do you want to translate? ")

# Translate it to Pig Latin
pigString = pigLatin(myString)

# ...?
print (pigString)
