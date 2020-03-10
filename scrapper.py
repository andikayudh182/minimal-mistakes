import requests
import datetime
import json

republika={
	"time":"",
	"categories":"",
	"title":"",
	"publish":""
}

data= []
from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id/")

obj = BeautifulSoup(page.text, "html.parser")

for headline in obj.find_all('div', class_='conten1'):
    
    republika['categories'] = (headline.find('h1').text)
    
    republika['title'] = (headline.find('h2').text)

    date = datetime.datetime.now()
    today = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    republika['time'] = today
    republika['publish']=headline.find('div',class_='date').text

    print(republika)

    data.append(dict(republika)) 

with open("Republika.json", "w") as file:
    json.dump(data, file)