import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qurl='https://books.toscrape.com/'

qheader={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

resp= rq.get(url= qurl,headers= qheader)

bSoup= BeautifulSoup(resp.content,'html.parser')

#print(ab)

def removeNavigablestring(list_data):
    return list(filter(lambda x: type(x) != NavigableString,list_data))

c1= removeNavigablestring(bSoup.ol.children)

#print(c1[0].children)

S = c1[4]

S= c1[4].h3.a.attrs['title']

print('Title 1 :-' , S )

print('////')
print('////')
print('////')
print('////')

S= c1[5].h3.a.attrs['title']

print('Title 2 :-' , S )

print('******')
print('******')
print('******')

S = c1[6].h3.a.attrs['title']

print('Title 3 :-' , S )

print('++++++')
print('++++++')
print('++++++')

S = c1[7].h3.a.attrs['title']

print('Title 4 :-' , S )