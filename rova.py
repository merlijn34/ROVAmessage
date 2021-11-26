from bs4 import BeautifulSoup
import requests
from datetime import date

zipcode = "3824CA"
house   = "31";

date = date.today()
day = date.strftime("%d")
month = date.strftime("%B")
year = date.strftime("%Y")


print(day + month + year)

##get url
url = "https://inzamelkalender.rova.nl/nl/" + zipcode + "/" + house + "/";

##create a session
session = requests.session()

##do the login with the credentials
response = session.post(url)

##content after logging in
response_content = response.content

##make a soup
soup = BeautifulSoup(response_content, 'html.parser')

##only get the right soup
mydivs = soup.find_all("div", {"id": "jaar-2021"})


#get the trash date and type
trash_type_p = soup.findAll(class_='papier')
trash_type_pmd = soup.findAll(class_='pmd')
trash_type_gft = soup.findAll(class_='gft')

trash_date = soup.findAll(class_='span-line-break', text=True)
# trash_type = soup.findAll(class_='afvaldescr')


for x in mydivs:
        #array = {'trash date: ':str(trash_date), 'trash type: ':str(trash_type)}
        array = [trash_date + trash_type_p + trash_type_gft + trash_type_pmd]

        print(array)
