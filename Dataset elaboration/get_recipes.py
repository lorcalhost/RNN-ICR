import requests
from bs4 import *
import re
import json

url = 'https://ricette.giallozafferano.it/Pancakes-allo-sciroppo-d-acero.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Title
Rtitle = soup.find('h1', class_='gz-title-recipe').text

# Ingredients
ingredients = soup.find_all('dd', class_='gz-ingredient')
Ringredients = list(dict())
for i in range(len(ingredients)):
    Ringredients.append({'ingredient': ingredients[i].a.text, 'quantity': "".join(ingredients[i].span.text.split())})

# Preparation
Rpreparation = ""
preparation = soup.find_all('div', class_='gz-content-recipe-step')
for i in range(len(preparation)):
    Rpreparation += preparation[i].text
Rpreparation = re.sub('\s+', ' ', Rpreparation)

Recipe = {'title':Rtitle,'ingredients':Ringredients,'preparation':Rpreparation}
with open('gz_recipes.json', 'w') as r:
    r.write(json.dumps(Recipe, indent=4, sort_keys=False))
