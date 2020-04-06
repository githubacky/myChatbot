import csv
from typing import List
import requests
import lxml.html
import sqlite3
from bs4 import BeautifulSoup

def main_concert(num, mnth):
	num = int(num)
	if num == 1:
		url = 'https://i-amabile.com/'
	elif num == 2:
		url = "https://i-amabile.com/archives/2020-" + str(mnth).zfill(2)
	else:
		url = 'https://i-amabile.com/'
	html = fetch(url)
	if num == 1:
		books = scrape_pickup(html, url)
	elif num == 2:
		books = scrape_month(html, url)
	else:
		books = scrape_pickup(html, url)
	#save('concert.csv', books)
	save_sqlite3('concert.db', books)

def fetch(url: str) -> str:
	r = requests.get(url)
	return r.text

def scrape_pickup(html: str, base_url: str) -> List[dict]:
	books =[]
	html = lxml.html.fromstring(html)
	html.make_links_absolute(base_url)

	for idx in range(2, 12, 2):
		# cssel = '#content > div > div:nth-child(3) > table:nth-child(' + str(idx) + ') > tbody' # > tr > td:nth-child(1)' # > a'
		cssel = '#content > div > div:nth-child(3) > table:nth-child(' + str(idx) + ') > tr > td:nth-child(1) > a'
		a = html.cssselect(cssel)
		url = a[0].get('href')
		p = a[0].cssselect('b')
		title = p[0].text_content()
		books.append({'url':url, 'title':title[3:]})
		#print(url, title)

	return books

def scrape_month(html: str, base_url: str) -> List[dict]:
	books =[]

	response = requests.get(base_url)
	response.encoding = response.apparent_encoding

	bs = BeautifulSoup(response.text, 'html.parser')

	cname = bs.select("#content > div > b > a")

	cnt = 1
	for cn in cname:
		flag = cn.getText()[0]
		if flag == "●":
			title = cn.getText().replace("●","")
			url = cn.get('href')
			#print(str(cnt).zfill(2) + ". " + title, url)
			cnt += 1
			books.append({'url':url, 'title':title})
	return books


def save(file_path: str, books: List[dict]):
	with open(file_path, 'w', newline='') as f:
		writer = csv.DictWriter(f, ['url', 'title'])
		writer.writeheader()
		writer.writerows(books)

def save_sqlite3(file_path: str, books: List[dict]):
	conn = sqlite3.connect(file_path)
	c = conn.cursor()
	c.execute('DROP TABLE IF EXISTS concerts')
	c.execute("""
		CREATE TABLE concerts(
			url text,
			title text
		)	
	""")
	c.executemany('INSERT INTO concerts VALUES (:url, :title)', books)
	conn.commit()
	c.execute('SELECT * FROM concerts')
	for row in c.fetchall():
		print(row[1])
	conn.close()

if __name__ == '__main__':
	main_concert()
