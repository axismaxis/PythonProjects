import requests
import json
import sys
import shutil
import os

def DownloadImagePng(imgLink, name):
	response = requests.get(imgLink, stream=True)
	with open("C:/Projects/Python/WebScraper/img/" + name + ".png", 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

def DownloadImageJpg(imgLink, name):
	response = requests.get(imgLink, stream=True)
	with open("C:/Projects/Python/WebScraper/img/" + name + ".jpg", 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

url = "https://api.thetvdb.com/search/series"

querystring = {"name":"altered carbon"}

payload = ""
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDcwNTY5OTAsImlkIjoiTWFnbmlmaWVyIiwib3JpZ19pYXQiOjE1NDY5NzA1OTAsInVzZXJpZCI6NTE2OTA1LCJ1c2VybmFtZSI6InRpbW9uLmJvcmdsYTgifQ.MavwYAewVj96iCU2O1yFtiR9Re7bD3drAzK3udZSXHTXOYqdAA8E_mUhoKZ8Pcrge3chjUN1-GwOAx6wHw3F_8a6lxuuTvqY1znnhwx1bW1urzaki8sYEUJMF93KO4OfzFLtgjiYuAqIAxnM5gGvivkeYc0M0oSbVjg62dVyMdhF8kfJ8i9FD8q8RGGtUbR9LO0BIVoZ_1jGAgmIwoEHwA3fjA4iIGnkC8Px8mj9RUucm2pheU0WFvCPjKxaXIqByma58M43FlI_JNtX-oAePQhV7bWbosXXWatu1qWpmgVx9Px2I8PRRgmlT7pt-_hU8-JzNoAxo77X6vxUo2MDGQ"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

if(response.status_code != 200):
	print("Failed request")
	sys.exit()

rJson = response.json()
#TVDBToken = rJson["token"]
print(rJson)

SerieID = rJson["data"][0]["id"]

url = "https://api.thetvdb.com/series/" + str(SerieID) + "/images/query"

querystring = {"keyType":"fanart"}

payload = ""
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDcwNTY5OTAsImlkIjoiTWFnbmlmaWVyIiwib3JpZ19pYXQiOjE1NDY5NzA1OTAsInVzZXJpZCI6NTE2OTA1LCJ1c2VybmFtZSI6InRpbW9uLmJvcmdsYTgifQ.MavwYAewVj96iCU2O1yFtiR9Re7bD3drAzK3udZSXHTXOYqdAA8E_mUhoKZ8Pcrge3chjUN1-GwOAx6wHw3F_8a6lxuuTvqY1znnhwx1bW1urzaki8sYEUJMF93KO4OfzFLtgjiYuAqIAxnM5gGvivkeYc0M0oSbVjg62dVyMdhF8kfJ8i9FD8q8RGGtUbR9LO0BIVoZ_1jGAgmIwoEHwA3fjA4iIGnkC8Px8mj9RUucm2pheU0WFvCPjKxaXIqByma58M43FlI_JNtX-oAePQhV7bWbosXXWatu1qWpmgVx9Px2I8PRRgmlT7pt-_hU8-JzNoAxo77X6vxUo2MDGQ",
    }

fairytailRequest = requests.request("GET", url, data=payload, headers=headers, params=querystring)
fReqJson = fairytailRequest.json()

listWithFanArt = fReqJson["data"]
counter = 0
for fanart in listWithFanArt:
    counter += 1
    extensionType = os.path.splitext(fanart["fileName"])[1]
    if extensionType == ".png":
        DownloadImagePng("https://www.thetvdb.com/banners/" + fanart["fileName"], str(counter))
    elif extensionType == ".jpg":
        DownloadImageJpg("https://www.thetvdb.com/banners/" + fanart["fileName"], str(counter))
    else:
        print("You done fucked up")
        sys.exit()

print("fReqText")
