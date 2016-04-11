import requests
from bs4 import BeautifulSoup 
def parser(link):
	r = requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')


