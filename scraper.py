import requests
from bs4 import BeautifulSoup
##url = 'https://www.python.org/~guido/'
##url = 'https://www.khaadi.com/'
def getRawText(url):
    url= 'https://www.quora.com/What-is-the-step-by-step-procedure-to-install-Beautiful-Soup-In-Windows'
    # Package the request, send the request and catch the response: r
    r=requests.get(url)
    # Extracts the response as html: html_doc
    html_doc=r.text
    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc)
    # Prettify the BeautifulSoup object: pretty_soup
    pretty_soup=soup.prettify()
    print(pretty_soup)

def getPretText(url):
    r = requests.get(url)
    html_doc = r.text
    soup=BeautifulSoup(html_doc)
    guido_title=soup.title
    print(guido_title)
    guido_text=soup.get_text()
    print(guido_text)

def getUrl(url):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    print(soup.title)
    a_tags=soup.find_all('a')
    for link in a_tags:
        print(link.get('href'))
        
##getRawText('https://www.python.org/~guido/')
##getPretText('https://www.python.org/~guido/')
getUrl('https://www.python.org/~guido/')

##getRawText('https://www.khaadi.com/')
##getPretText('https://www.khaadi.com/')
##getUrl('https://www.khaadi.com/')
