
# coding: utf-8


import json
from utils import naver_search, permute, evaluate

try:
    with open('counter.json', 'r') as fp:
        counter = json.load(fp)
except FileNotFoundError:
    counter = {}

class extract_nouns:
    def __init__(self, counter):
        self.counter = counter

    def count(self, sequences):
        for sequence in sequences:
            for s in permute(sequence.split(' ')):
                for nouns in s:
                    noun = ''.join(nouns)
                    if (noun not in counter):
                        self.counter[noun] = naver_search(noun)
#                         print(noun, self.counter[noun])

    def score(self, sequences, weight):
        result = []
        for sequence in sequences:
            scr_max = 0
            temp = []
            for s in permute(sequence.split(' ')):
                score = 1
                for nouns in s:
                    noun = ''.join(nouns)
                    score *= self.counter[noun] * (weight ** (len(s))) - 0.01
                if (scr_max < score):
                    scr_max = score
                    temp = s
            for t in temp:
                result.append(''.join(t))
        return ' '.join(result)

extract_nouns = extract_nouns(counter)

