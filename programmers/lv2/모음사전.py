from itertools import permutations

def solution(word):
    wordList = ['A', 'A', 'A', 'A', 'A', 'E', 'E', 'E', 'E', 'E', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'U', 'U', 'U', 'U', 'U',]
    words = []
    for i in range(1, 6):
        words += list(map(''.join, permutations(wordList, i)))    
    words = list(set(words))
    words.sort()
    return words.index(word) + 1
solution("I")