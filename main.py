# This is a prototype of our first app
# Treat comments like pseduocode (https://en.wikipedia.org/wiki/Pseudocode)

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

# Download up to external 5 pages deep. On each page another 5 pages should be analyzed.
# From each page gather 5 most frequent words with word occurences. Put this data
# to file together with page address. After that send this well formated data to
# https://www.datamuse.com/api/ API and save meaning to each page in a file.


