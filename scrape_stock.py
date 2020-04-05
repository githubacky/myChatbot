from typing import List
import requests
import lxml.html
from bs4 import BeautifulSoup

def main_stock(stcnum):
	url = 'https://kabutan.jp/stock/?code=' + stcnum
	html = fetch(url)
	scrape(html, url)

def fetch(url: str) -> str:
	r = requests.get(url)
	return r.text

def scrape(html: str, base_url: str) -> List[dict]:
	html = lxml.html.fromstring(html)
	html.make_links_absolute(base_url)

	# 銘柄コードが存在しない/上場廃止の場合の処理
	# 存在しない場合
	err1sel = '#header > div.fs0 > div > ol > li:nth-child(2) > span'
	err1 = html.cssselect(err1sel)
	flag = err1[0].text_content()[0]

	if flag == "(":
		print('指定した銘柄は存在しません。')

	else:
		# 銘柄名取得
		stcsel = '#stockinfo_i1 > div.si_i1_1'
		stc = html.cssselect(stcsel)
		stnum = stc[0].cssselect('h2 > span')
		stnm = stc[0].cssselect('h2')
		stcnum = stnum[0].text_content()
		stcnm = stnm[0].text_content().replace(stcnum, '')

		# 上場廃止の場合
		err2sel0 = '#stockinfo_i2 > dl:nth-child(1) > dd'
		err2sel1 = '#stockinfo_i1 > div.si_i1_1 > span'
		err20 = html.cssselect(err2sel0)
		err21 = html.cssselect(err2sel1)
		flag20 = err20[0].text_content()
		if err21 == []:
			flag21 = "None"
		else:
			flag21 = err21[0].text_content()

		# 上場廃止の場合
		if flag20 == "－" and flag21 == "None":
			print('{0}({1})は上場廃止となりました。'.format(stcnm, stcnum))

		else:
			# 株価データ取得
			csssel = '#stockinfo_i1 > div.si_i1_2'
			a = html.cssselect(csssel)
			p = a[0].cssselect('span.kabuka')
			price = p[0].text_content()
			print('{0}({1})の株価は{2}です。'.format(stcnm, stcnum, price))

if __name__ == '__main__':
	main_stock()
