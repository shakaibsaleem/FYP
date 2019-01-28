import requests
import urllib
import os
from bs4 import BeautifulSoup
import pandas as pd
import csv 
from pathlib import Path

def getUrl(url):
    r = requests.get(url)
    link=[]
    html_doc = r.text
    soup = BeautifulSoup(html_doc,features="html.parser")
    a_tags=soup.find_all('a',class_="product photo product-item-photo")
    for i in range (len(a_tags)):
        link.append(a_tags[i]['href'])
    return link

def getRawText(url):
    l=[]
    r=requests.get(url)
    html_doc=r.text
    soup = BeautifulSoup(html_doc,"html.parser")
    c=soup.find('div',class_="MagicToolboxContainer").find_all('a',class_='mt-thumb-switcher ')
    for i in c:
        l.append(i['href'])
    return l

def getInfo(url,ParUrl):
    colors = ['Black','Blue','Yellow','Red']
    description = []
    l=[]
    r=requests.get(url)
    html_doc=r.text
    soup = BeautifulSoup(html_doc,"html.parser")
    name=soup.find('div',class_ = "page-title-wrapper")
    name=name.text.replace('\n','')
    details = soup.find('table',class_ = "data table additional-attributes")
    # category = soup.find('a', href = 'https://www.khaadi.com/pk/woman/pret.html' )
    # details1 = details.find_all('td',class_ = 'col data', 'Material')
    # try:
    details1 = details.find_all('td',class_ = 'col data')
    for i in details1:
        l.append(i.text)
    if len(l) == 1:
        color = l[0]
        material = 'NULL'
    else:
        material = l[0]
        color = l[1]
    # color = details.find('td',class_ = '')
    price = soup.find('span', class_ = 'price').text
    price = int(price[3:].replace(',',''))
    descrip = soup.find('div', class_ = 'product attribute overview')
    if descrip == None:
        descript = 'Null'
    else:
        descript = descrip.find('div', class_ = 'value').text

    fName = getCode(url)
    description.append(fName)
    description.append(name)
    description.append(price)
    description.append(material)
    description.append(color)
    description.append(descript)
    description.append('Khaadi')
    description.append(url)
    description.append(getCategory(ParUrl))

    return description

def getCategory(url):
    category = url.split('/')[-1].split('.')[0]
    return category

def Write_File(list_dict):
    # list_of_dict = []
    myFile = open('khaadi.csv', 'w', newline='')  
    with myFile:  
        myFields = ['Dress Code','Name', 'Price', 'Material', 'Color', 'Description', 'Brand', 'url','Category','isAvailable']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        # linksToInner=getUrl(link)
        # writer.writerow({'Name' : a[0], 'Price':a[1], 'Material':a[2], 'Color':a[3], 'Description': a[4]})
        for data in list_dict:
            writer.writerow(data)

def main(url):
    
    #urls=['https://www.khaadi.com/pk/woman/unstitched.html','https://www.khaadi.com/pk/woman/pret.html','https://www.khaadi.com/pk/woman/khaas.html']
    linksToInner=getUrl(url)
    listOfIms=[]

    for i in linksToInner:
        # try:
        ParentDir = Path(__file__).parent.parent
        fName = getCode(i)
        newpath = str(ParentDir) +'/imagesFromScrapper/'+str(fName)
        # print('i0',i)
        if not os.path.isdir(newpath):
            os.makedirs(newpath)
            print('new dir made')
        k = getRawText(i)
        # print('k',k)
        for j in k:
            fName2 = getCode(j)
            subpath = newpath+"/"+str(fName2)+".jpg"
            print(type(subpath))
            print(subpath)
            urllib.request.urlretrieve(j,subpath)

            # listOfIms.append(getRawText(i))
        # except:   
        #     continue
    # return listOfIms
  
def getCode(link):
    # fName=((((((link.split('/'))[-1]).split('.'))[0]).split('_'))[0].split('-'))[0]
    fName=((((((link.split('/'))[-1]).split('.'))[0])))

    return fName

# def downloader(listM):
#     c=0
#     # print(listM)
#     for i in listM:
#         for j in i:
#             fName = getCode(j)
#             ParentDir = Path(__file__).parent.parent
#             newpath = str(ParentDir) +'/imagesFromScrapper/'+str(fName)
#             if not os.path.isdir(newpath):
#                 os.makedirs(newpath)
#             urllib.request.urlretrieve(j,newpath+fName+".jpg")
                  
#             c+=1           
#     return
# #downloader(links)


def khadiS():
    u=['https://www.khaadi.com/pk/woman/unstitched.html', 'https://www.khaadi.com/pk/woman/pret.html', 'https://www.khaadi.com/pk/woman/khaas.html']
    # u=['https://www.khaadi.com/pk/woman/pret.html']
    urls=[]
    list_of_dict=[]
    
    #f1=open('test.txt','w')
    #f2=open('test2.txt','w')
    for j in u:
        for i in range(1,13):
            urls.append(j+'?p='+str(i))
    if not os.path.isdir:
        os.makedirs(r'images/')
    for url in urls: 
        main(url)
        linksToInner=getUrl(url)
        for i in linksToInner:
            a = getInfo(i,url)
            dict_of_details = {'Dress Code': a[0],'Name' : a[1], 'Price':a[2], 'Material':a[3], 'Color':a[4], 'Description': a[5], 'Brand': a[6], 'url': a[7], 'Category': a[8]}
            list_of_dict.append(dict_of_details)
        
        Write_File(list_of_dict)
        # downloader(links)
    return
khadiS()
# Write_File('https://www.khaadi.com/pk/woman/pret.html')
