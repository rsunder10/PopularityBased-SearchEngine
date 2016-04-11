import requests
from bs4 import BeautifulSoup

def yahoo_parser(link):
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		info=soup.find_all('div',class_='serp-item__text')
		link=soup.find_all('h2')
		print(len(info))
		print(len(link))

yahoo_parser('https://www.yandex.com/search/?msid=22890.24003.1460387819.92282&text=sunder&lr=20902&p=0')