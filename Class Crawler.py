import requests
from bs4 import BeautifulSoup

class Crawler(object):
    def __init__(self, address):
        
        self.address = address
        self.html = requests.get(address)
        self.soup = BeautifulSoup(self.html.content, "lxml")
        
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
    
    
    