# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:06:25 2018

@author: komp
"""

listaa = []

def Crawl(address, num=0):
#    site = Crawler(address)
    global listaa
    links_list = 5
    num += 1
    if num < 6:
        for i in range(links_list):
            listaa.append(num)
            print(num)
            Crawl("a", num)
    return len(listaa)