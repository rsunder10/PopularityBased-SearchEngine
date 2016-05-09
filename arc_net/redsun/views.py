from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
global_list_link=[]
global_list_title=[]
global_list_info=[]
global_address=[]
global_list_ranking=[]
def bing_parser(link):
	del global_list_link[:]
	del global_list_title[:]
	del global_list_ranking[:]
	del global_list_info[:]
	del global_address[:]
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		link=soup.find_all('h2')
		info=soup.find_all('p')
		no=len(link)
		no2=len(info)
		a=min(no,no2)
		for x in range(0,a):
			try:
				global_list_info.append(info[x].text)
			except:
				global_list_info.append('None')

		for x in range(0,a):

			try:
				global_list_link.append(link[x].a['href'])
			except:
				global_list_link.append('None')
		for x in range(0,a):
			try:
				global_list_title.append(link[x].text)
			except:
				global_list_link.append('None')
				
		print(len(link))
		print(len(info))
def alexa(link):
	r=requests.get(link)
	if(r.status_code==200):
		soup=BeautifulSoup(r.text,'html.parser')
		api=soup.find_all('span',class_='ss')
		
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
			try:
				global_list_link.append(link[x].a['href'])
			except:
				global_list_link.append('None')


		for x in range(0,a):
			try:
				global_list_title.append(link[x].text)
			except:
				global_list_title.append('None')
		for x in range(0,a):
			try:
				global_list_info.append(info[x].text)
			except:
				global_list_info.append('None')
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
			try:
				global_list_link.append(link[x].a['href'])
			except:
				global_list_link.append('None')


		for x in range(0,a):
			try:
				global_list_title.append(link[x].text)
			except:
				global_list_title.append('None')
		for x in range(0,a):
			try:
				global_list_info.append(info[x].text)
			except:
				global_list_info.append('None')
		print(len(info))
		print(len(link))

def SearchResult(request):
	c={}

	template="search.html"
	if request.method == 'GET' and 'q' in request.GET:
		q=request.GET['q']
		if q is not None and q!='':
			# global_list_info=[]
			# global_list_title=[]
			# global_list_link=[]
			query_bing='http://www.bing.com/search?q='+str(q)+'&qs=n&pq=sunderis1000&sc=0-0&sp=-1&sk=&cvid=CDACA8B6C8A24E0F8ACE265EAB03BC66&first=0&FORM=PERE'
			query_yandex='https://www.yandex.com/search/?text='+str(q)
			query_google='https://www.google.co.in/search?q='+str(q)

			bing_parser(query_bing)
			yandex_parser(query_yandex)
			google_parser(query_google)
			sunder=zip(global_list_title,global_list_link,global_list_info)
			# c={'titles':global_list_title,'links':global_list_link,'infos':global_list_info}
			c={'sunder':sunder}

	return render(request,template,c)