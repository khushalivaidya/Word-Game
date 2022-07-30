# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:58:18 2021

@author: khush
"""
hand = {'r': 1, 'e': 1, 'h': 2, 't': 1, 'k': 1, 's': 1, 'o': 1}

for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end="_")       # print all on the same line
print()

hand_backup = hand.copy()

word = input("Type a word..")
#for letter in word:
    #hand_backup[letter] -= 1

print(hand_backup)

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    backup_hand = hand.copy()
    
    if word in wordList:
        for letter in word:
            if letter in backup_hand:
                backup_hand[letter] -= 1
            else:
                return False
        for value in backup_hand.values():
            if value < 0:
                return False
            else:
                return True
    else:
        return False  
    
print(isValidWord(word, hand, ['shoe', 'the', 'so']))
print(isValidWord(word, hand, ['shoe', 'the', 'so']))