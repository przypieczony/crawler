# This is a prototype of our first app
# Treat comments like pseduocode (https://en.wikipedia.org/wiki/Pseudocode)
# # Write tests for each function (http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html)

# We will be using 2 third-party libs: 
# - BeautifulSoup (bs4)
# - requests

# Yes, all code will be written in English ;)


# Regular expression (regexp in short) which finds web addresses 
# through out page. It may be usefull in future crawling.

# Function which gets url link as a arg and reurns data page.
# This function must be well protected since it will be used many times.

# Class which will find all links on page, returns only not yet visited
# and differentiate external links from internal ones. It should use regexp 
# from first paragrpah

# Function which collects as much as it can text from page. It may return list.

# Function which gets words as an input and returns dictionary of dictionaries:
# for example {page_addr: {word1: count1, word2: count2 ... }}

# Function which returns only words with most occurances and amount of 
# reurned words.
# Input: dict {page_addr: {word1: count1, word2: count2 ... }}
# 		 int 5
# Return: dict of tuple {page_addr: (word1, word2, workd3)}
# 

# Function which saves dicts to file and format it as json (https://pl.wikipedia.org/wiki/JSON)

# Function which formats data for datamuse API

# Function which sends well formatted data to https://www.datamuse.com/api/

# Function which saves returned data from datamuse API  together with page addres to, again, json file

# Download up to external 5 pages deep. On each page another 5 pages should be analyzed.
# From each page gather 5 most frequent words with word occurences. Put this data
# to file together with page address. After that send this well formated data to
# https://www.datamuse.com/api/ API and save meaning to each page in a file.


