import requests
import sys
import shutil
from bs4 import BeautifulSoup

def DownloadImage(imgLink, name):
	response = requests.get("http:" + imgLink, stream=True)
	with open("img/" + name + ".png", 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

currentComicNumber = 2094

while currentComicNumber != 0:
	request = requests.get("http://xkcd.com/" + str(currentComicNumber) + "/")
	soup = BeautifulSoup(request.content, 'lxml')
	divList = soup.find_all("div")
	imgLinkList = []
	for div in divList:
		if div.has_attr("id"):
			if div.attrs["id"] == "comic":
				imgLink = div.find("img").attrs["src"]
				DownloadImage(imgLink, "Image_" + str(currentComicNumber))
			
	currentComicNumber -= 1

	

