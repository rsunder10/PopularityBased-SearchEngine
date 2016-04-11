import requests
from bs4 import BeautifulSoup

def bing_parser(link):
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		link=soup.find_all('h2')
		info=soup.find_all('p')
		print(len(link))
		print(len(desc))

bing_parser('http://www.bing.com/search?q=sundermanoj&qs=n&pq=sunderis1000&sc=0-0&sp=-1&sk=&cvid=CDACA8B6C8A24E0F8ACE265EAB03BC66&first=0&FORM=PERE')