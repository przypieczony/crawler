import requests
from bs4 import BeautifulSoup
import re
import random
import datetime

def getLinks(address):
    '''
    returns list of links (strings) that appears on given website
    '''
    html = requests.get(address)
    soup = BeautifulSoup(html.content, "lxml")
    links_on_site = []
    for link in soup.findAll('a', attrs={'href': re.compile("^(http|www)")}):
        links_on_site.append(link.attrs['href'])  
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
    return domain          

def getExternalLinks(address):
    '''
    returns only domain names of external links that appears on the website
    '''
    all_links = getLinks(address)
    external_links = []
    domain = domainName(address)[0]
    for link in all_links:
        external = True
        for part in domainName(link):
            if part == domain:
                external = False
        if external == True:
            external_links.append(link)
    return external_links  

def get5random_ext(address):
    links_list = getExternalLinks(address)
    random_links = []
    while len(random_links) < 5:
        random.seed(datetime.datetime.now())
        link = links_list[random.randint(0, len(links_list)-1)]
        if link not in random_links:
            random_links.append(link)
    return random_links

def get5random(address):
    links_list = getLinks(address)
    random_links = []
    while len(random_links) < 5:
        random.seed(datetime.datetime.now())
        link = links_list[random.randint(0, len(links_list)-1)]
        if link not in random_links:
            random_links.append(link)
    return random_links