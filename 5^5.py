from webpage import WebPage
from webpage import TooFewLinksOnPage
from gettext import GetText
import pprint


address = 'https://pl.wikipedia.org/wiki/Piwo'
#address = 'https://morefuzz.net/'


global words_list
words_list = {}


def Crawl(address, recursions=2):
    '''
    gathers 5 random links from given website
    repeats recursively to each of the links that were found
    '''
    try:
        web_page = WebPage(address)
        links = web_page.get_links(links_amount=5, only_external_links_allowed=True)
    except TooFewLinksOnPage:
        # skip this page
        return

    if recursions > 0:
        recursions -= 1   #CHANGE Int for number of recursions
        for link in links:
            if link not in words_list.keys():
                all_text = web_page.get_all_text()
                get_text_object = GetText(all_text)
                words_list[link] = get_text_object.collect_words()
                Crawl(link, recursions)


# In Crawl function implement actual object creation
Crawl(address)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(words_list)
print(len(words_list))
print(words_list.keys())

