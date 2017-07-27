import random

class WordGenerator:
    def __init__(self):
        print("This is the coolest init ever")

    alphabets = ['a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = [0, 4, 8, 14, 20, 24]

    def wordGenerator(self):
        return self.alphabets[0] + self.alphabets[1]
