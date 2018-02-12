from bs4 import BeautifulSoup
import requests

with open('files/local-file.html') as f:
    soup = BeautifulSoup(f, 'lxml') #or with 'html'

print(soup.prettify(), end='\n\n')
print('-'*100)


match = soup.p
print(match, end='\n\n')        #<p>This is a summary of article 1</p>

match = soup.p.text
print(match, end='\n\n')        #This is a summary of article 1

match = soup.div.text
print(match, end='\n\n')
# Article 1 Headline
# This is a summary of article 1

match = soup.div.a.text
print(match, end='\n\n')    #Article 1 Headline

match = soup.find('div', class_='footer').text
print(match)    #Footer Informantion
print('-'*100)


for article in soup.find_all('div', class_='article'):
    headlines = article.h2.a.text
    print(headlines)

    summary = article.p.text
    print(summary)
    print('-_'*10)
