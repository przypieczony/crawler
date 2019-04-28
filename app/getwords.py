import requests
from bs4 import BeautifulSoup
import re
import sys
from collections import Counter


class GetWords():
    def __init__(self, text):
        self.raw_text = text
        self.words = self.collect_words()

    def split_to_word(self):
        '''
        input: list generated by "getAlltext" function
    
        output: splits each word from the text apart and returns as list
        '''
        words = []
        for text in self.raw_text:
            for word in text.split(" "):
                words.append(word)
        return words

    def standarize_words(self, splitted_words):
        '''
        input: list [strings]
    
        deletes all the string containing a number,
        removes any punctuation from each string,
    
        output: list [strings]
        '''
        new_word_list = []
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        p = re.compile("(\.|\!|\,|\?|\:|\;|\)|\(|\\|\/|\'|\")")
        for word in splitted_words:
            is_word = True
            if len(word) <= 3:
                continue
            word = p.sub(" ", word)
            word = word.lower()
            for number in numbers:
                if number in word:
                    is_word = False
                    break
            if is_word == True:
                new_word_list.append(word)
            new_word_list.sort()
        return new_word_list


    def top_words(self, n):
        '''
        input: iterable
    
        output: Tuple of lists with top n words
    
        [('word1', 35), ('word2', 25)]
        '''

        return Counter(self.words).most_common(n)



    def collect_words(self):
        '''
        input: address of existing website
    
        returns tuple (domain name, dictionary { words on site : number of appearences })
        '''
        return self.standarize_words(self.split_to_word())