from bs4 import BeautifulSoup
import requests
downloadLink=[]
allUrls= [['http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-306-48048-5', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-306-48247-2', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-387-21736-9', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-387-68566-3'], ['http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-387-72071-5', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-0-387-72579-6',  'http://link.springer.com/openurl?genre=content/pdf&isbn=978-3-319-03762-2', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-3-319-56194-3'], ['http://link.springer.com/openurl?genre=content/pdf&isbn=978-1-4614-0400-2', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-3-319-27877-3', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-3-030-25943-3', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-3-030-19128-3', 'http://link.springer.com/openurl?genre=content/pdf&isbn=978-1-4939-9621-6']]
allUrlList=sum(allUrls,[])
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
