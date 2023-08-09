import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url="https://ecolabelindex.com/ecolabels/"

r=requests.get(url)
time.sleep(2)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
#here th soup wii copy the html of the link 
# print(soup)

anchores=soup.find_all('a')
all_links=[]

for link in anchores:
    linktext=url+link.get('href')
    all_links.append(link)

csv_file="links.csv"
with open(csv_file,'w',newline='',encoding='utf-8') as file:
    csv_write=csv.writer(file)
    csv_write.writerow(['links'])
    for links in all_links :
        csv_write.writerow([link])

print(f"the links  wii be store in {csv_file} file ")
