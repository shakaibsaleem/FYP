import requests
import urllib
import os
from bs4 import BeautifulSoup

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
    descrip
    r=requests.get(url)
    html_doc=r.text
    soup = BeautifulSoup(html_doc,"html.parser")
    c=soup.find('div',class_="slideset").find_all('img')
    #print(c)
    for i in c:
        #print(i)
        l.append(i['src'])
    #print(l)
    return l

def getInfo(url):
	l=[]
	r=requests.get(url)
	html_doc=r.text
	soup = BeautifulSoup(html_doc,"html.parser")
	c=soup.find('span',class_ = "base")
	c=c.text
	return c    
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

##links1=main('https://www.zellbury.com/pink-pretty.html')

def downloader(listM):
    print('entered')
    c=0
    print(listM)
    for i in listM:
        #print(i)
        for j in i:
            print(j)
            fName=(((((j.split('/'))[-1]).split('.'))[0]).split('_'))[0]
            print(fName)
            newpath=r'imagesFromZellbury/'+str(fName)
            if not os.path.isdir(newpath):
                os.makedirs(newpath)
            urllib.request.urlretrieve(j,newpath+"/local"+str(c)+".jpg")
            c+=1           
    return

 
##downloader(links)
def Zellbury():
    u=['https://www.zellbury.com/women/ready-to-wear/pret.html']
    urls=[]
    for j in u:
        for i in range(1,24):
            urls.append(j+'?p='+str(i))
    if not os.path.isdir:
        os.makedirs(r'images/')
    for url in urls:
        links=main(url)
        downloader(links)
    return

print(getInfo('https://www.zellbury.com/flower-flock'))
# Zellbury()
