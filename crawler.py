from webpage import WebPage
from webpage import TooFewLinksOnPage, BannedExtensionPage
from gettext import GetText
from requests.exceptions import ConnectionError
import pprint


address = 'https://pl.wikipedia.org/wiki/Piwo'
#address = 'https://morefuzz.net/'

global words_list
words_list = {}

def Crawl(address, recursions=2, txt=""):
    '''
    gathers 5 random links from given website
    repeats recursively to each of the links that were found
    '''
    links_amount = 0
    max_links_amount = 5
    web_page = WebPage(address)
    links = web_page.get_links(only_external_links_allowed=True)
    #print("Links on page: {} found: {}".format(address, len(links)))

    if recursions > 0:
        recursions -= 1
        for link in links:
            if links_amount >= max_links_amount:
                break
            if link not in words_list.keys():
                try:
                    Crawl(link, recursions, txt)
                    all_text = web_page.get_all_text()
                    words_parser = GetText(all_text)
                    words_list[link] = words_parser.top_words(5)
                    links_amount += 1
                except (TooFewLinksOnPage, BannedExtensionPage, ConnectionError):
                    #print("Getting page from previous round...")
                    continue


Crawl(address)

print("Number of visited pages: {}".format(len(words_list)))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(words_list)

