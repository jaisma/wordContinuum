import random

class WordGenerator:
    def __init__(self, firstLetter):
        self.firstLetter = firstLetter

    def wordGenerator(self):
        alphabets = ['a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

        # To be used later to make sure the word is at least pronounceable
        # Need to implement inserting vowels if it hasn't been chosen in certain iterations.
        # vowels = [0, 4, 8, 14, 20, 24]

        word = self.firstLetter
        wordLength = random.randint(3,8)
        while(len(word) < wordLength):
            alphabet = alphabets[random.randrange(26)]
            word += alphabet

        return word

# For lazy testing purposes right now
testing = WordGenerator("a")
print(testing.wordGenerator())