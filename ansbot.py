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

con_data = "concert_data.txt"
with open(con_data, "r", encoding="utf-8") as f:
	tmp = f.read()
con_list = tmp.splitlines()

#---- 読み込んだ外部データを辞書に変換
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
		while True:
			stcnum = input(" stock> 銘柄コードは？")
			if "bye" in stcnum:
				break
			main_stock(stcnum)

	if "Crawling 演奏会" in ans:
		print('知りたい項目を選択してください')
		print('\n'.join(con_list))
		while True:
			conc = input(" concert> ")
			if "bye" in conc:
				break
			elif conc == "1":
				main_concert(conc, 0)
			elif conc == "2":
				print("何月ですか？")
				mnth = input(" concert> ")
				print("{0}月開催の演奏会は以下の通りです".format(mnth))
				main_concert(conc, mnth)
			else:
				print("現在準備中のため、別の項目を選択してください(>_<)")
				#main_concert(conc, 0)

