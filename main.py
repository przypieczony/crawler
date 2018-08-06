from webpage import WebPage
from webpage import TooFewLinksOnPage, BannedExtensionPage
from getwords import GetWords
from requests.exceptions import ConnectionError
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pprint

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')

import os
print(os.getcwd())
 
class ReusableForm(Form):
    address = TextField('Name:', validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)


global words_list
words_list = {}

@app.route("/", methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)
    
    print(form.errors)
    if request.method == 'POST':
        address=request.form['address']
 
        if form.validate():
            Crawl(address)
            flash("Number of visited pages: {}".format(len(words_list)))
            flash(words_list)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('index.html', form=form)

def Crawl(address, recursions=2, txt=""):
    '''
    gathers 5 random links from given website
    repeats recursively to each of the links that were found
    '''
    links_amount = 0
    max_links_amount = 5
    web_page = WebPage(address)
    links = web_page.get_links(only_external_links_allowed=True)
    #print("Links on page: {} found: {}".format(address, len(links)))

    if recursions > 0:
        recursions -= 1
        for link in links:
            if links_amount >= max_links_amount:
                break
            if link not in words_list.keys():
                try:
                    Crawl(link, recursions, txt)
                    all_text = web_page.get_all_text()
                    words_parser = GetWords(all_text)
                    words_list[link] = words_parser.top_words(5)
                    links_amount += 1
                except (TooFewLinksOnPage, BannedExtensionPage, ConnectionError):
                    #print("Getting page from previous round...")
                    continue


#Crawl(address)

print("Number of visited pages: {}".format(len(words_list)))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(words_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)