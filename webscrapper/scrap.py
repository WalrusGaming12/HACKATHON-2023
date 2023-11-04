from bs4 import BeautifulSoup
import requests
#Gets HTML page
url = "https://www.fisheries.noaa.gov/species/yelloweye-rockfish"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

species = doc.find_all(["div"], class_="wyswyg-edit field field--name-body field--type-text-with-summary field--label-hidden field--item")

print(species)