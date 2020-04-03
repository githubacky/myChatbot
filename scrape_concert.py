import csv
from typing import List
import requests
import lxml.html

def main_concert():
	url = 'https://i-amabile.com/'
	html = fetch(url)
	scrape(html, url)

def fetch(url: str) -> str:
	r = requests.get(url)
	return r.text

def scrape(html: str, base_url: str) -> List[dict]:
	html = lxml.html.fromstring(html)
	html.make_links_absolute(base_url)

	for idx in range(2, 12, 2):
		# cssel = '#content > div > div:nth-child(3) > table:nth-child(' + str(idx) + ') > tbody' # > tr > td:nth-child(1)' # > a'
		cssel = '#content > div > div:nth-child(3) > table:nth-child(' + str(idx) + ') > tr > td:nth-child(1) > a'
		a = html.cssselect(cssel)
		url = a[0].get('href')
		p = a[0].cssselect('b')
		title = p[0].text_content()[3:]
		print(title)

if __name__ == '__main__':
	main_concert()
