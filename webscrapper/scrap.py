from bs4 import BeautifulSoup
import requests
#Gets HTML page

url="https://www.fisheries.noaa.gov/species-directory?oq=&field_species_categories_vocab=1000000031&field_region_vocab=All&items_per_page=350"
result=requests.get(url).text
doc=BeautifulSoup(result,"html.parser")

tbody= doc.tbody
trs= tbody.contents

species={}

for tr in trs:
    if tr=='\n':
        next
    else:
        name = tr.contents[3:4]
        print(name[0].a.text)
        print()


"""
url = "https://www.fisheries.noaa.gov/species/adriatic-sturgeon"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

species = doc.find(["h2"], class_="species-overview__header-name")
species = species.find(["span"])
print(list(species))

description = doc.find(["div"], class_="wyswyg-edit field field--name-body field--type-text-with-summary field--label-hidden field--item")
print(description.text)
"""