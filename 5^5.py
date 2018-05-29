from getAlltext import collect_words
from getLinks import get_random_links
#from getLinks import get5random_ext
from getAlltext import top5words
from getAlltext import countWords
from getLinks import TooFewLinksOnPage

address = 'https://pl.wikipedia.org/wiki/Piwo'
#address = 'https://morefuzz.net/'

# remove this global variable
lista_linkow = []

def Crawl(address, num=0):
    '''
    gathers 5 random links from given website
    repeats recursively to each of the links that were found
    '''
    try:
        links_list = get_random_links(address, 5)
    except TooFewLinksOnPage:
        # skip this page
        return

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
    words_list = []
    for link in links_list:
        words_list = words_list + collect_words(link)
    return words_list

# In Crawl function implement actual object creation
Crawl(address)
# Create wepage object and execute below methods from class instead functions
All_words_list = GatherWords(lista_linkow)
All_words_dict = countWords(All_words_list)
top_word = top5words(All_words_dict)
