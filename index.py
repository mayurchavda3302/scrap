import requests
import time
from bs4 import BeautifulSoup
import csv

r=requests.get('https://www.geeksforgeeks.org/')
time.sleep(2)
all_link=[]
soup=BeautifulSoup(r.content,'html.parser')
for link in soup.find_all('a'):
    link= link.get('href')
    all_link.append(link)
    # print(link)
    csv_flie='links.csv'    
    with open(csv_flie,'w')as file:
      csv_write = csv.writer(file)
      csv_write.writerow(['links'])
      for linktext in all_link:
            csv_write.writerow([linktext])
      
