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
		for x in info:
			global_list_info.append(x.text)
		for x in link:
			global_list_link.append(x.a['href'])
		for x in link:
			global_list_title.append(x.text)
		print(len(link))
		print(len(info))

def google_parser(link):
	r = requests.get(link)
	# print(r.text)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		info=soup.find_all('span',class_='st')
		link=soup.find_all('h3')
		no=len(link)
		no2=len(info)
		a=min(no,no2)
		for x in range(0,a):
			global_list_link.append(link[x].a['href'])
		for x in range(0,a):
			global_list_title.append(link[x].text)
		for x in range(0,a):
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
		no2=len(info)
		a=min(no,no2)
		for x in range(0,a):
			global_list_info.append(link[x].a['href'])
		for x in range(0,a):
			global_list_title.append(link[x].text)
		for x in range(0,a):
			global_list_info.append(info[x].text)
		print(len(info))
		print(len(link))

def SearchResult(request):
	c={}


	template="search.html"
	if request.method == 'GET' and 'q' in request.GET:
		q=request.GET['q']
		if q is not None and q!='':
			query_bing='http://www.bing.com/search?q=sundermanoj&qs=n&pq='+str(q)+'&sc=0-0&sp=-1&sk=&cvid=CDACA8B6C8A24E0F8ACE265EAB03BC66&first=0&FORM=PERE'
			# query_yandex='https://www.yandex.com/search/?msid=22893.25866.1460399165.05971&text='+str(q)+'&suggest_reqid=687280681146038781391680982376032'
			query_google='https://www.google.co.in/search?q='+str(q)

			bing_parser(query_bing)
			# yandex_parser(query_yandex)
			google_parser(query_google)
			sunder=zip(global_list_title,global_list_link,global_list_info)
			# c={'titles':global_list_title,'links':global_list_link,'infos':global_list_info}
			c={'sunder':sunder}

	return render(request,template,c)