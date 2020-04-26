import re
import os
import PyPDF2 
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
currentDirectory=os.getcwd()
pdfFileObj = open('Springer Ebooks.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# print("pages>>",pdfReader.numPages) 
pages=pdfReader.numPages
downloadLink=[]
pdfText=[]
allUrls=[]
# Create directory path
def createDirectoryPath(cwdir,pageNumber):
    try:
        resolvePath=os.path.join(cwdir,pageNumber)
        os.mkdir(resolvePath)
    except FileExistsError:
        print("Folder ",resolvePath," already exists")
# Find url from the pdf        
def FindNmodifyUrl(string):
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    pdfUrl=[sub.replace("book","content/pdf") for sub in url]
    # print(">>",pdfUrl)
    return pdfUrl

# Create  a folder reading pageNumber from the pdf
for p in range(pages):
    # print("Page Number >>>>",p)
    createDirectoryPath(currentDirectory,str(p))
    pageObj = pdfReader.getPage(p) 
    pdfText.append(pageObj.extractText())
    # print((pageObj.extractText()) )
pdfFileObj.close() 
# print(">>>>",pdfText)
for text in pdfText:
    x=FindNmodifyUrl(text)
    allUrls.append(x)

# print("all URLs>>",allUrls)
# Links for all pdfs
def getPDFs(urls):
    allUrlList=sum(urls,[])
    print("allUrlList>>",allUrlList)
    # i=0
    # for urlarray in allUrls:
    #     for url in urlarray:
    #         print(">>",url)
    for u in allUrlList:
        webResponse=requests.get(u)
        soup=BeautifulSoup(webResponse.text,"html.parser")
    # getClass=soup.select(".cta-button-container__item")
        for a in soup.findAll('div',{"class":"cta-button-container__item"}):
            for b in a.findAll('a'):
                downloadLink.append(b.get('href'))
    # downloadLink=[a['href'] for a in getClass.select('a[href]')]

    # print("web>>","https://link.springer.com"+downloadLink[0])
    print("web>>",downloadLink)

getPDFs(allUrls)

