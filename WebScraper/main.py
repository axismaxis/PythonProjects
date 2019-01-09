import requests
import sys
from bs4 import BeautifulSoup

class torrentLink:
	def __init__(self, name, link):
		self.name = name
		self.magnetLink = link

if(len(sys.argv) > 1):
	searchString = sys.argv[1]
else:
	searchString = input("Please enter your anime search: ")

print("Searching for: " + searchString)

request = requests.get("https://nyaa.si/?f=0&c=0_0&q=" + searchString)
if request.status_code != 200:
	print('No handshake with site')
	sys.exit()

soup = BeautifulSoup(request.content, 'lxml')
tableLinks = soup.find_all("table")
torrents = list()

for tempTable in tableLinks:
	for className in tempTable.attrs["class"]:
		if className == "torrent-list":
			torrentListTable = tempTable

trs = torrentListTable.find_all("tr")

torrentLinks = list()
for trElement in trs:
	if len(trElement.find_all("th")) != 0:
		continue

	if trElement.find_all("td")[1].find_all("a")[0].has_attr("class"):
		torrentName = trElement.find_all("td")[1].find_all("a")[1].attrs["title"]
	else:
		torrentName = trElement.find_all("td")[1].find_all("a")[0].attrs["title"]
	
	magnetLink = trElement.find_all("td")[2].find_all("a")[1].attrs["href"]
	torrentLinks.append(torrentLink(torrentName, magnetLink))

for torrent in torrentLinks:
	print("-" * 50)
	print(torrent.name)
	print(torrent.magnetLink)

