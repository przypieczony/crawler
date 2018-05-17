import requests
from bs4 import BeautifulSoup

address = "https://help.github.com/articles/about-pull-requests/"
#html = requests.get(address)
#soup = BeautifulSoup(html.content, "lxml")

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
    
    
words = countWords(splitToWord(getAlltext(address)))
TopWord = top5words(words)