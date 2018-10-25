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
            matchHour = match.find(class_="h sep").text
            matchInfos = match.find(class_="infos")
            matchSport = matchInfos.find("span")['class'][1]
            matchOpposant = matchInfos.text.split("\n")[0]
            matchDesc = matchInfos.text.split("\n")[2]
            matchId = match.find(class_="nr").text
            matchCote1 = match.find(class_="nr").find_next("td")
            matchCoteN = matchCote1.find_next("td")
            matchCote2 = matchCoteN.find_next("td")
            matchCotes = [matchCote1.text, matchCoteN.text, matchCote2.text]
            matchSiteProno = matchCote2.find_next("td", class_="prono").text
            print(date + "  " + matchSiteProno + "  " + matchId)

searchDatas()
