import csv
from typing import List
import requests
import lxml.html

def main():
	url = 'https://i-amabile.com/'
	html = fetch(url)
	books = scrape(html, url)
	save('concert.csv', books)

def fetch(url: str) -> str:
	r = requests.get(url)
	return r.text

def scrape(html: str, base_url: str) -> List[dict]:
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

def save(file_path: str, books: List[dict]):
	with open(file_path, 'w', newline='') as f:
		writer = csv.DictWriter(f, ['url', 'title'])
		writer.writeheader()
		writer.writerows(books)

if __name__ == '__main__':
	main()
