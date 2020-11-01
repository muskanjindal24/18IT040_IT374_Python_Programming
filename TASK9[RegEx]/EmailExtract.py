import requests
import re
from bs4 import BeautifulSoup

url ='https://it.charusat.ac.in/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
email_list=[]
text = soup.get_text()
list = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
for email in list:
    email_list.append(email)
for email in list:
    print(email)