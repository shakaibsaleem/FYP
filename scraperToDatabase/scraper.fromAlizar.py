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
    # print(details1)
    for i in details1:
        l.append(i.text)
    # except:
    #     details1 = details.find('td',class_ = 'col data')
    #     details1 = details1.text
    #     if details1 in colors:
    #         color = details1
    #         material = 'NULL'
    #     else:
    #         material = details1
    #         color = 'NULL'
    # try:
    # details2 = details.find('td',class_ = 'col data', data = 'Color')
    # color = details2.text
    # except:
    #     color = 'NULL'
    # for i in details:
    #     l.append(i.text)
    if len(l) == 1:
        color = l[0]
        material = 'NULL'
    else:
        material = l[0]
        # print(material)
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
        myFields = ['Dress Code','Name', 'Price', 'Material', 'Color', 'Description', 'Brand', 'url','Category']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        # linksToInner=getUrl(link)
        
            # writer.writerow({'Name' : a[0], 'Price':a[1], 'Material':a[2], 'Color':a[3], 'Description': a[4]})
        for data in list_dict:
            writer.writerow(data)

def main(url):
    
    #urls=['https://www.khaadi.com/pk/woman/unstitched.html','https://www.khaadi.com/pk/woman/pret.html','https://www.khaadi.com/pk/woman/khaas.html']
    linksToInner=getUrl(url)
    # print(len(linksToInner))
    listOfIms=[]
    for i in linksToInner:
        try:
            listOfIms.append(getRawText(i))
        except:
            print ('here')
            continue
    return listOfIms

#links=main('https://www.khaadi.com/pk/woman/pret.html')

# def WriteDescrip(a):
# 	with open('description.csv', 'w') as csvfile:
# 		fieldnames = ['Name', 'Price', 'Material', 'Color', 'Description']
# 		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
# 	i = getInfo(a)
# 	writer.writeheader()
# 	writer.writerow({'Name' : i[0], 'Price':i[1], 'Material':i[2], 'Color':i[3], 'Description':i[4]})

def getCode(link):
    fName=(((((link.split('/'))[-1]).split('.'))[0]).split('_'))[0]
    return fName

def downloader(listM):
    print('entered')
    c=0
    
    for i in listM:
        
        for j in i:
            #f1.write(j+'\n')
            fName = getCode(j)
            #f2.write(fName+'\n')         
            # newpath=r'images/'+str(fName)
            ParentDir = Path(__file__).parent.parent
            # print(ParentDir)
            newpath = str(ParentDir) +'/imagesNoHuman/'+str(fName)
            if not os.path.isdir(newpath):
                os.makedirs(newpath)
            urllib.request.urlretrieve(j,newpath+"/local"+str(c)+".jpg")
            
            c+=1           
    return
#downloader(links)


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
    # print(urls)
    for url in urls: 
        links=main(url)
        print(url)
        linksToInner=getUrl(url)
        for i in linksToInner:
            # print(i)
            a = getInfo(i,url)
            dict_of_details = {'Dress Code': a[0],'Name' : a[1], 'Price':a[2], 'Material':a[3], 'Color':a[4], 'Description': a[5], 'Brand': a[6], 'url': a[7], 'Category': a[8]}
            list_of_dict.append(dict_of_details)
        # print(links)
        # Write_File(url)
        print(list_of_dict)
        Write_File(list_of_dict)
        downloader(links)
    return
khadiS()
# print(Write_File('https://www.khaadi.com/pk/etej18426-off-white.html'))
# Write_File('https://www.khaadi.com/pk/woman/pret.html')