from pymongo import MongoClient
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from scrape_stock import main_stock
from scrape_concert import main_concert

#---- 外部データ読み込み
ext_data = "bot_data.txt"
with open(ext_data, "r", encoding="utf-8") as f:
	tmp = f.read()
bot_list = tmp.splitlines()

#---- 読み込んだ外部データを辞書に変換
bot_dict = {}
for li in bot_list:
	elm = li.split(",")
	bot_dict[elm[0]] = elm[1]

#---- メインルーチン
while True:
	command = input("bot> ")
	for bd in bot_dict:
		if bd in command:
			ans = bot_dict[bd]
			break
		else:
			ans = "もう一度お願いします(>_<)"

	print(ans)

	#---- bot終了処理
	if ("bye" in command) or ("さようなら" in command):
		break
	
	#---- Crawling
	if "Crawling 株価" in ans:
		stcnum = input(" 銘柄コードは？")
		main_stock(stcnum)

	if "Crawling 演奏会" in ans:
		print('おすすめの演奏会をピックアップしました。')
		main_concert()

