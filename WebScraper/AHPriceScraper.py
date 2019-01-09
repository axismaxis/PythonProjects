import requests
from bs4 import BeautifulSoup
from requests.compat import urlparse


class ProductData:
	def __init__(self, price, name):
		self.price = price
		self.name = name

def GetProductLinks(searchQuery):
	soup = BeautifulSoup(requests.get("https://www.ah.nl/zoeken?query=" + searchQuery).content, "lxml")
	divWithProducts = soup.find_all("a", {"class":"productcard__link"})
	listWithLinkHrefs = []
	for temp in divWithProducts:
		listWithLinkHrefs.append(temp.attrs["href"])
	return listWithLinkHrefs

# AH delivers url but uses rest call and json to add information to page
# Example:	 https://www.ah.nl/producten/product/wi211029/robijn-wasmiddel-klein-en-krachtig-color
# Rest call: https://www.ah.nl/service/rest/delegate?url=%2Fproducten%2Fproduct%2Fwi211029%2Frobijn-wasmiddel-klein-en-krachtig-color 
def ConvertUrlToRestCallUrl(url):
	urlPath = urlparse(url)[2]
	
	return urlPath

def GetPriceFromPage(pageHref):
	priceSoup = BeautifulSoup(requests.get("https://www.ah.nl" + pageHref).content, "lxml")
	productURL = priceSoup.find("link", {"rel":"canonical"}).attrs["href"]
	productRestUrl = ConvertUrlToRestCallUrl(productURL)
	productName = "ga"
	productPriceDescription = priceSoup.find("h1", {"class":"product-description__price-per-usage"})
	splitPriceDescription = productPriceDescription.split()
	productPrice = splitPriceDescription.split()[:1]
	return ProductData(productPrice, productName)

productLinks = GetProductLinks("wasmiddel")
product = GetPriceFromPage(productLinks[0])


print("Program finished")