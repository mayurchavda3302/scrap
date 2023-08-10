import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://ecolabelindex.com/ecolabels/"
r = requests.get(url)
time.sleep(2)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

csv_file = "links.csv"
with open(csv_file, 'w') as file:
    csv_write = csv.writer(file)
    csv_write.writerow(['links'])
    all_link=set()
    for link in soup.find_all('a'):
        linktext = link.get('href')
        if linktext and not linktext.startswith(('http', 'https')):
            linktext = url + linktext if linktext.startswith('/') else linktext 
           
            if linktext not in all_link:
               csv_write.writerow([linktext])
               all_link.add(linktext)
               

print(f"The links will be stored in {csv_file} file.")
