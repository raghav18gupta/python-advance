from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
csv_file = open('files/scrap_file.csv', 'w')

csv_write = csv.writer(csv_file)
csv_write.writerow(['headline', 'summary', 'youtube_link'])

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
print('-'*100)

article = soup.find('article')
print(article.prettify())
print('-'*100)

for article in soup.find_all('article'):
    try:
        headline = article.header.h2.a.text

        summary = article.div.p.text  # my way
        # summary = article.find('div', class_='entry-content').p.text

        link = article.iframe['src']  # my way
        # link = article.find('iframe', class_='youtube-player')['src']
        # print(link, end='\n')

        link_id = link.split('/')[4].split('?')[0]
        # print(link_id, end='\n')

        youtube_link = 'https://youtube.com/watch?v=' + link_id
    except Exception as e:
        headline, summary, link, link_id, youtube_link = None

    print(headline, end='\n')
    print(summary, end='\n')
    print(youtube_link, end='\n')
    print()
    csv_write.writerow([headline, summary, youtube_link])

csv_file.close()
