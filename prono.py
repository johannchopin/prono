from bs4 import BeautifulSoup
from urllib.request import urlopen


URL = "http://www.pronosoft.com/fr/parions_sport/liste-parions-sport-plein-ecran.htm"

page = BeautifulSoup(urlopen(URL).read(), "lxml")

def searchDatas():
	htmlDataTable = page.find("div", id="match-list").find_all("table")
	
	for table in htmlDataTable:
		date = table.find("thead").find("th").string
		allMatches = table.find("tbody").find_all("tr")
		
		for match in allMatches:
			matchId = match.select(".nr")[0].text
		
			print(matchId)

searchDatas()