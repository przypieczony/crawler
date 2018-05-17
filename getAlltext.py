import requests
from bs4 import BeautifulSoup
import re

address = "https://help.github.com/articles/about-pull-requests/"
#html = requests.get(address)
#soup = BeautifulSoup(html.content, "lxml")

#ZAMIENIC LITERY W SLOWIE NA MALE

def getAlltext(address):
    html = requests.get(address)
    soup = BeautifulSoup(html.content, "lxml")
    text_list = []
    text_tags = ('p','span')
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

def removePunctation(words_list):
    p = re.compile("(\.|\!|\,|\?|\:|\;|\)|\(|\\|\/|\'|\")")
    new_word_list = []
    for word in words_list:
        word = p.sub(" ", word)
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
    
    
words = countWords(splitToWord(removePunctation(getAlltext(address))))
TopWord = top5words(words)