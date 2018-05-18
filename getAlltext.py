import requests
from bs4 import BeautifulSoup
import re

address = "https://morefuzz.net/reviews/cegvera-creations-ep/"
#html = requests.get(address)
#soup = BeautifulSoup(html.content, "lxml")

#ZAMIENIC LITERY W SLOWIE NA MALE

def getAlltext(address):
    html = requests.get(address)
    soup = BeautifulSoup(html.content, "lxml")
    text_list = []
    text_tags = ('p')
    for tag in text_tags:
        for text in soup.findAll(tag):
            text_list.append(text.get_text())
    return text_list

def splitToWord(text_list):
    words = []
    for text in text_list:
        for word in text.split(" "):
            words.append(word)
    return words

#def removePunctation(words_list):
#    p = re.compile("(\.|\!|\,|\?|\:|\;|\)|\(|\\|\/|\'|\")")
#    new_word_list = []
#    for word in words_list:
#        word = p.sub(" ", word)        
#        new_word_list.append(word)
#    return new_word_list

#def isWord(words_list):
#    new_word_list = []
#   numbers = ["0","1","2","3","4","5","6","7","8","9"]
#    for word in words_list:
#        word = word.lower()
#        is_word = True
#        for number in numbers:
#            if number in word:
#                is_word = False
#                break
#        if is_word == True:
#            new_word_list.append(word)
#    return new_word_list

def standarizeWords(words_list):
    new_word_list = []
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    p = re.compile("(\.|\!|\,|\?|\:|\;|\)|\(|\\|\/|\'|\")")
    for word in words_list:
        is_word = True
        word = p.sub(" ", word)
        word = word.lower()
        for number in numbers:
            if number in word:
                is_word = False
                break
        if is_word == True:
            new_word_list.append(word)
    return new_word_list

def countWords(words_list):
    words_count = {}
    for word in words_list:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1        
    return words_count

def top5words(countWords_dict):
    top_num = 1
    top_word = ""
    keys = countWords_dict.keys()
    for key in keys:
        if len(key) > 2 and key != 'the':      
            if countWords_dict[key] > top_num:
                top_num = countWords_dict[key]
                top_word = key
    return top_word
    
#def methode1(address):
#    words = countWords(isWord(splitToWord(removePunctation(getAlltext(address)))))
#    return words

def methode2(address):
    words = countWords(standarizeWords(splitToWord(getAlltext(address))))
    return words

#words1 = methode1(address)
words2 = methode2(address)
#TopWord1 = top5words(words1)
TopWord2 = top5words(words2)