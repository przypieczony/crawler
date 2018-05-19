import getAlltext
from getLinks import get5random
from bs4 import BeautifulSoup
import re
import requests
import random
import datetime

lista_linkow = []


def Crawl(address, num=0):
    links_list = get5random(address)
    global lista_linkow
    num += 1
    if num < 6:
        for link in links_list:
            lista_linkow.append(link)
            Crawl(link, num)
    return len(listaa)