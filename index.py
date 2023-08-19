import requests
from bs4 import BeautifulSoup
import time 
import csv
url="https://ecolabelindex.com/ecolabels/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
time.sleep(3)
soup=BeautifulSoup(r.text,'html.parser')  
span=soup.find("div",{"class":"ecolabel-result article"})

unique_links=set()
for links in  span.find_all('a'):
    
    link=links.get('href')
    if link:
        unique_links.add(link)
   
csv_file="links.csv"
with open(csv_file,"w",newline="") as file:
    csv_write=csv.writer(file)

    for linktext in unique_links:
         if linktext.startswith("/"):
             complate_link=f"https://ecolabelindex.com{linktext}"
             csv_write.writerow([complate_link])
         else:
             csv_write.writerow([linktext])

