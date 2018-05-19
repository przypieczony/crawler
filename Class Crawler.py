import requests
import re
from bs4 import BeautifulSoup
import random
import datetime
random.seed(datetime.datetime.now())

    
class Crawler(object):
    def __init__(self, address):
        
        self.address = address
        self.html = requests.get(address)
        self.soup = BeautifulSoup(self.html.content, "lxml")
        
    
    def getAddress(self):
        
        return self.address
        
    def domainName(self):
        '''
        return domain name of given website
        '''
        address = self.address
        if "https://" in address:
            address = address.replace("https://", "")
        if "http://" in address:
            address = address.replace("http://", "")
        if "www." in address:
            address = address.replace("www.", "")
        domain = address.split('.')[0]
        return domain

    def getLinks(self):
        '''
        returns list of links (strings) that appears on given website
        '''
        links_on_site = []
        soup = self.soup
        for link in  soup.findAll('a', attrs={'href': re.compile("^(http|www)")}):
            links_on_site.append(link.attrs['href'])            
#           print(link.attrs['href'])               # function working check  
#           print(domainName(link.attrs['href']))   # "domainName" function working check
        return links_on_site
    
    def getRandomLink(self):
        '''
        ranomly picks up one of the links from the site en returns it
        '''
        links_list = self.getLinks()
        return links_list[random.randint(0, len(links_list))]

    def getRandomLink_extern(self):
        '''
        ranomly picks up one extern of the links from the site en returns it
        '''
        links_list = self.getLinks()
        current_domain = self.domainName()
        extern_links_list = []
        for link in links_list:
            if current_domain not in domainName(link):
                extern_links_list.append(link)
        return extern_links_list[random.randint(0, len(extern_links_list)-1)]

    # ZWRACA ADRESY WEWNETRZNE ADRESY JAK NP suppor.beatport  JAKO ZEWNETRZNE
    def getExterneLinks(self):
        '''
        returns external links that appears on the website
        '''
        links_list = self.getLinks()
        current_domain = self.domainName()
        extern_links_list = []
        for link in links_list:
            if current_domain not in domainName(link):
                extern_links_list.append(link)
        return extern_links_list

    def get_5_extern(self):
        externe_links = self.getExternalAddresses()
        
    
    def getExternalLinks(self):
        '''
        returns only domain names of external links that appears on the website
        '''
        address = self.address
        all_links = getLinks(address)
        external_links = []
        domain = domainName(address)
        for link in all_links:
            external = True
            for part in domainName_list(link):
                if part == domain:
                    external = False
            if external == True:
                external_links.append(link)
        return external_links    
    
    def getExternalAddresses(self):
        '''
        returns list that includes only domain names of external links that appears on the website
        '''
        list_links = self.getExternalLinks()
        list_address = []
        for link in list_links:
            if "https://" in link:
                link = link.replace("https://", "")
            if "http://" in link:
                link = link.replace("http://", "")
            if "www." in link:
                link = link.replace("www.", "")
            domain = addressSplit(link)
            if domain not in list_address:
                list_address.append(domain)
        return list_address
    
    def getAlltext(self):
        soup = self.soup
        text_list = []
        text_tags = ('p','a','h2','h3','h1','span', 'div')
        for tag in text_tags:
            for text in soup.findAll(tag):
                text_list.append(text.get_text())
        return text_list

def domainName_list(address):
    if "https://" in address:
        address = address.replace("https://", "")
    if "http://" in address:
        address = address.replace("http://", "")
    if "www." in address:
        address = address.replace("www.", "")
    domain_list = address.split('.')
    return domain_list
      
def domainName(address):
    if "https://" in address:
        address = address.replace("https://", "")
    if "http://" in address:
        address = address.replace("http://", "")
    if "www." in address:
        address = address.replace("www.", "")
    domain = address.split('.')[0]
    return domain

def addressSplit(address):
    address = address.split('/')[0]
    return address

beat = Crawler('https://www.beatport.com/')
fuzz = Crawler('https://morefuzz.net/')
wiki = Crawler('https://www.wikipedia.org/')
veg = Crawler('http://www.nutreelab.pl/produkty')

listaa = []

def Crawl(address, num=0):
#    site = Crawler(address)
    global listaa
    links_list = 5
    num += 1
    if num < 3:
        for i in range(links_list):
            listaa.append(num)
            print(num)
            Crawl("a", num)
    return len(listaa)