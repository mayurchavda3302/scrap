import requests
from bs4 import BeautifulSoup

import time
import csv
url="https://ecolabelindex.com/ecolabels/"
r=requests.get(url)
time.sleep(2)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
anchores=soup.find_all('a')
all_links=[]


for links in anchores:
    linktext=url+links.get('href')
    all_links.append(linktext)
    

csv_file="links.csv"
with open(csv_file,'w',newline='',encoding='utf-8') as file:
    csv_write=csv.writer(file)
    csv_write.writerow(['links'])
    for link in all_links:
        csv_write.writerow([link])

print(f"the links  wii be store in {csv_file} file ")

