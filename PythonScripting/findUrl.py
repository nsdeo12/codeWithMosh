import re
def FindNmodifyUrl(string):
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    # pdfUrl=[sub.replace("book","content/pdf") for sub in url]
    print(">>",pdfUrl)
    return pdfUrl
textString="""OpenURL
1
Fundamentals of Power Electronics
Robert W. Erickson, Dragan
Maksimovic
2nd ed.
2001
http://link.springer.com/openurl?genre=book&isbn=978-0-306-48048-5
2
Handbook of the Life Course
Jeylan T. Mortimer, Michael J.
Shanahan
2003)"""
FindNmodifyUrl(textString)