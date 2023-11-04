from bs4 import BeautifulSoup
import requests
import json
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
        picture = tr.contents[1:2]
        #get IMG
        tag = tr.contents[3:4]
        img=picture[0].img.get("data-src")
        #get species name and link
        Name=tag[0].a.text
        href=tag[0].a.get("href")
       
        #store species
        species[Name]=[href,img]

"""
for i in species:
    print("SPECIES NAME:",i)
    print("PAGE:",species[i][0])
    print("IMG:",species[i][1])
    print()
"""
#GETS DESCRIPTION
for i in species:
    url="https://www.fisheries.noaa.gov"+species[i][0]
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    description = doc.find(["div"], class_="wyswyg-edit field field--name-body field--type-text-with-summary field--label-hidden field--item")
    species[i].append(description.text)

print(species)
for i in species:
    print("SPECIES NAME:",i)
    print("PAGE:",species[i][0])
    print("IMG:",species[i][1])
    print("DESCRIPTIONS:")
    print(species[i][2].encode("utf-8"))
    print()

with open('data.json', 'w') as fp:
    json.dump(species, fp)