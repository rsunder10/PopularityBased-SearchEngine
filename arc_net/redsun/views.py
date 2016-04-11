from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
global_list_link=[]
global_list_title=[]
global_list_info=[]
global_list_ranking=[]

def bing_parser(link):
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		link=soup.find_all('h2')
		info=soup.find_all('p')
		for x in info.text:
			global_list_info.append(x)
		for x in link.a['href']:
			global_list_link.append(x)
		for x in link[0].text:
			global_list_title.append(x)
		print(len(link))
		print(len(desc))

def google_parser(link):
	r = requests.get(link)
	# print(r.text)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		info=soup.find_all('span',class_='st')
		link=soup.find_all('h3',class_='r')
		no=len(link)
		for x in range(0,no):
			global_list_link.append(link[x].a['href'])
		for x in range(0,no):
			global_list_title.append(link[x].text)
		for x in range(0,no):
			global_list_info.append(info[x].text)
		print(len(info))
		print(len(link))

def yandex_parser(link):
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		info=soup.find_all('div',class_='serp-item__text')
		link=soup.find_all('h2')
		no=len(link)
		for x in range(0,no):
			global_list_info.append(link[x].a['href'])
		for x in range(0,no):
			global_list_title.append(link[x].text)
		for x in range(0,no):
			global_list_info.append(info[x].text)
		print(len(info))
		print(len(link))

def SearchResult(request):
	c={}
	template="search.html"
	

	return render(request,template,c)