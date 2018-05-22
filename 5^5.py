from getAlltext import methode2
from getLinks import get5random
#from getLinks import get5random_ext
from getAlltext import top5words
from getAlltext import countWords

address = 'https://pl.wikipedia.org/wiki/Piwo'
#address = 'https://morefuzz.net/'

lista_linkow = []

def Crawl(address, num=0):
    '''
    gathers 5 random links from given website
    repeats recursively to each of the links that were found
    '''
    links_list = get5random(address)
    global lista_linkow
    num += 1
    recursion = 2   #CHANGE Int for number of recursions
    if num <= recursion:         
        for link in links_list:
            if link not in lista_linkow:
                lista_linkow.append(link)
            if num < recursion:
                Crawl(link, num)
    return len(lista_linkow)

def GatherWords(links_list):
    LIST = []
    for link in links_list:
        LIST = LIST + methode2(link)
    return LIST


Crawl(address)
All_words_list = GatherWords(lista_linkow)
All_words_dict = countWords(All_words_list)
top_word = top5words(All_words_dict)

