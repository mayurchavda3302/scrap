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
    # print(linktext)

'''
when we save all url to the csv file than links does not stroge in the set()
it wii show error becuase set has only unique elements and it wii not preserve the insertion.

so we store the data in list
'''


data={'link':all_links}
# here the link is key and  all_links has value
df=pd.DataFrame(data)
# here we create the data frame 
csv_file="links.csv"

df.to_csv(csv_file,index=False,encoding='utf-8')
# here the data wii in character/string form so wii wii send it in 'utf-8'.
#  
print(f"the links wii storge in the :{csv_file}  file")       