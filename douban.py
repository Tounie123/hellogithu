from urllib import request
from bs4 import BeautifulSoup as bs
import ssl
import jieba
context = ssl._create_unverified_context()
resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/', context=context)
html_data = resp.read().decode('utf-8')
#print(html_data)
soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li',class_='list-item')
#print(nowplaying_movie_list[0])
#print(len(nowplaying_movie_list))
nowplaying_list = []
for item in nowplaying_movie_list:
	nowplaying_dict = {}
	nowplaying_dict['id'] = item['data-subject']
	for tag_img_item in item.find_all('img'):
		nowplaying_dict['name'] = tag_img_item['alt']
		nowplaying_list.append(nowplaying_dict)

#for lists in nowplaying_list:
#	print(lists)
#print(nowplaying_list)

requrl = 'https://movie.douban.com/subject/' + nowplaying_list[0]['id'] + '/comments'# + '?' + 'start=0' + '&limit=20'
resp = request.urlopen(requrl, context=context)
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
comments_div_list = soup.find_all('div', class_='comment')
#print(comments_div_list)
#print(requrl)
eachCommentList = [];
for item in comments_div_list:
	if item.find_all('p')[0].string is not None:
		eachCommentList.append(item.find_all('p')[0].string)

for lists in eachCommentList:
	print(lists)
