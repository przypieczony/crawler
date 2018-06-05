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


class WebPage():
    def __init__(self, address):
        self.address = address
        self.page_content = self._get_page_content()
        self.links_on_site = []
        self.domain = self._domain_name(self.address)

    def _get_page_content(self):
        '''
        inout: web page address
        return: obj BeautifulSoup
        '''
        raw_html = self._fetch_page()
        html = BeautifulSoup(raw_html.content, "html.parser")
        return html

    def _fetch_page(self):
        '''
        Function which gets url link as a arg and reurns raw data page.
        This function must be well protected since it will be used many times.
        '''
        return requests.get(self.address)

    def _domain_name(self, address):
        '''
        return domain name of given website
        '''
        if "https://" in address:
            short_addr = address.replace("https://", "")
        if "http://" in address:
            short_addr = address.replace("http://", "")
        if "www." in address:
            short_addr = address.replace("www.", "")
        domain = short_addr.split('.')
        # We may consider better mechanism of getting domain name
        return domain

    def _collect_all_links(self, min_links_amount):
        '''
        returns list of links (strings) that appears on given website
        '''
                
        for link in self.page_content.findAll('a', attrs={'href': re.compile("^(http|www)")}):
            self.links_on_site.append(link.attrs['href'])
        if len(self.links_on_site) < min_links_amount:
            raise TooFewLinksOnPage(len(self.links_on_site), self.address)

    def _is_external_link(self, link):
        for part in self._domain_name(link):
            if part in self.domain:
                return False
        return True

    def get_links(self, links_amount=5, only_external_links_allowed=True):
        self._collect_all_links(links_amount)
        random_links = []
        # limit amount of interation in case there is no external links on page
        limit = 4*len(self.links_on_site) 
        random.seed(datetime.datetime.now())
        while (len(random_links) < links_amount) and (limit > 0):
            limit -= 1
            link = self.links_on_site[random.randint(0, len(self.links_on_site)-1)]
            if link not in random_links:
                if only_external_links_allowed:
                    if self._is_external_link(link):
                        print("Adding link {}".format(link))
                        random_links.append(link)
                    else:
                        continue
                else:
                    print("Adding link {}".format(link))
                    random_links.append(link)
        return random_links

    def getAlltext(self):
        # This function should be moved to WebPage class - DONE by maslakos
        '''
        input: address of existing website

        output: list containing whole raw text found between tags chosen as "text_tags" argument
        '''
        html = requests.get(self.address)
        print("Get text: ", self.address)
        soup = BeautifulSoup(html.content, "html.parser")
        text_list = []
        text_tags = ('p')  # add html tags that contains text you want to download,
        # type each tag as string, dont use comma signs
        for tag in text_tags:
            for text in soup.findAll(tag):
                text_list.append(text.get_text())
        return text_list

#list = WebPage("http://blog.muscle-zone.pl/piwo-14-niesamowitych-zalet/")._get_page_content()
#print(list)