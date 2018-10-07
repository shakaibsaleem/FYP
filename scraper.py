import requests
import urllib
import os
from bs4 import BeautifulSoup
##url = 'https://www.python.org/~guido/'
##url = 'https://www.khaadi.com/'
##def getRawText(url):
##    r=requests.get(url)
##    html_doc=r.text
##    soup = BeautifulSoup(html_doc,features="html.parser")
##    pretty_soup=soup.prettify()
##    print(pretty_soup)
##
##def getPretText(url):
##    f=open('prettified.html','w')
##    r = requests.get(url)
##    html_doc = r.text
##    soup=BeautifulSoup(html_doc,features="html.parser")
##    guido_title=soup.title
##    #f.write(guido_title)
##    guido_text=soup.get_text()
##    f.write(guido_text)
##
##def getUrl(url):
##    r = requests.get(url)
##    f=open('scraped.txt','w')
##    html_doc = r.text
##    soup = BeautifulSoup(html_doc,features="html.parser")
##    #print(soup.title)
##    a_tags=soup.find_all('a')
##    for link in a_tags:
##        print(link.get('href')+'\n')
##        print('--------------------------------------------------')
##    f.close()
####getRawText('https://www.python.org/~guido/')
####getPretText('https://www.python.org/~guido/')
####getUrl('https://www.python.org/~guido/')
##
####getRawText('https://www.khaadi.com/')
##getPretText('https://nishatlinen.com/')
##getUrl('https://www.khaadi.com/pk/woman/pret.html')
##def getRawText(url):
##    r=requests.get(url)
##    html_doc=r.text
##    soup = BeautifulSoup(html_doc,"html.parser")
##    container=soup.find_all('img',class_='product-image-photo')
##    for i in range (len(container)):
##        print(container[i]['src'])

#print(type(getUrl('https://www.khaadi.com/pk/woman/pret.html')))

##def getRawText(url):
##    l=[]
##    r=requests.get(url)
##    html_doc=r.text
##    soup = BeautifulSoup(html_doc,"html.parser")
##    container=soup.find('div',{"id":"MagicToolboxSelectors80841"}).find_all('a')
##    for i in container:
##        l.append(i['href'])
##    return l

def getUrl(url):
    r = requests.get(url)
    link=[]
    html_doc = r.text
    soup = BeautifulSoup(html_doc,features="html.parser")
    a_tags=soup.find_all('a',class_="product photo product-item-photo")
    for i in range (len(a_tags)):
        link.append(a_tags[i]['href'])
    #print(link)
    return link

def getRawText(url):
    l=[]
    r=requests.get(url)
    html_doc=r.text
    soup = BeautifulSoup(html_doc,"html.parser")
    c=soup.find('div',class_="MagicToolboxContainer").find_all('a',class_='mt-thumb-switcher ')
    #print(c)
    for i in c:
        #print(i)
        l.append(i['href'])
    #print(l)
    return l

def main(url):
    #urls=['https://www.khaadi.com/pk/woman/unstitched.html','https://www.khaadi.com/pk/woman/pret.html','https://www.khaadi.com/pk/woman/khaas.html']
    linksToInner=getUrl(url)
    print(len(linksToInner))
    listOfIms=[]
    for i in linksToInner:
        try:
            listOfIms.append(getRawText(i))
        except:
            print ('here')
            continue
    return listOfIms

#links=main('https://www.khaadi.com/pk/woman/pret.html')

def downloader(listM):
    print('entered')
    c=0
    for i in listM:
        #print(i)
        for j in i:
            fName=(((((j.split('/'))[-1]).split('.'))[0]).split('_'))[0]
            newpath=r'images/'+str(fName)
            if not os.path.isdir(newpath):
                os.makedirs(newpath)
            urllib.request.urlretrieve(j,newpath+"/local"+str(c)+".jpg")
            c+=1           
    return
#downloader(links)
def khadiS():
    u=['https://www.khaadi.com/pk/woman/pret.html','https://www.khaadi.com/pk/woman/unstitched.html','https://www.khaadi.com/pk/woman/khaas.html']
    urls=[]
    for j in u:
        for i in range(1,11):
            urls.append(j+'?p='+str(i))
    if not os.path.isdir:
        os.makedirs(r'images/')
    for url in urls:
        links=main(url)
        downloader(links)
    return
khadiS()
