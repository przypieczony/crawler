import requests
from bs4 import BeautifulSoup
import re
import random
import datetime

class TooFewLinksOnPage(Exception):
    def __init__(self, amount_of_links, address):
        self.amount_of_links = amount_of_links
        self.address = address
        print("Warning, there was too few links: {} on page: {}".format(self.amount_of_links, self.address))


def getLinks(address, links_amount):
    '''
    returns list of links (strings) that appears on given website
    '''
    # Below line has to be as separate function
    html = requests.get(address)
    soup = BeautifulSoup(html.content, "html.parser")
    links_on_site = []
    for link in soup.findAll('a', attrs={'href': re.compile("^(http|www)")}):
        links_on_site.append(link.attrs['href'])
    if len(links_on_site) < links_amount:
        raise TooFewLinksOnPage(len(links_on_site), address)
    else:  
        return links_on_site


def domainName(address):
    '''
    return domain name of given website
    '''
    if "https://" in address:
        address = address.replace("https://", "")
    if "http://" in address:
        address = address.replace("http://", "")
    if "www." in address:
        address = address.replace("www.", "")
    domain = address.split('.')
    # We may consider better mechanism of getting domain name
    return str(domain[0])

# def getExternalLinks(address):
#     '''
#     returns only domain names of external links that appears on the website
#     '''
#     all_links = getLinks(address)
#     external_links = []
#     domain = domainName(address)
#     for link in all_links:
#         external = True
#         for part in domainName(link):
#             if part == domain:
#                 external = False
#         if external == True:
#             external_links.append(link)
#     return external_links  


def is_external_link(address, link):
    source_domain = domainName(address)
    destination_domain = domainName(link)
    return destination_domain != source_domain

def get_random_links(address, links_amount, only_external_links_allowed=True):
    links_list = getLinks(address, links_amount)
    random_links = []
    # limit amount of interation in case there is no external links on page
    limit = 4*len(links_list) 
    random.seed(datetime.datetime.now())
    while (len(random_links) < links_amount) and (limit > 0):
        limit -= 1
        link = links_list[random.randint(0, len(links_list)-1)]
        if link not in random_links:
            if only_external_links_allowed:
                if is_external_link(address, link):
                    print("Adding link {}".format(link))
                    random_links.append(link)
                else:
                    continue
            else:
                 print("Adding link {}".format(link))
                random_links.append(link)
    return random_links