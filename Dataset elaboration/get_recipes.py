# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import re
import json
import codecs


class Recipe():
    def __init__(self, url):
        self.url = url

    def get(self):
        url = self.url
        http = urllib3.PoolManager()
        urllib3.disable_warnings()
        response = http.request('GET', url)
        html = codecs.decode(response.data, 'utf-8')
        soup = BeautifulSoup(html, 'lxml')

        # Title
        Rtitle = soup.find('h1', class_='gz-title-recipe').text

        # Ingredients
        ingredients = soup.find_all('dd', class_='gz-ingredient')
        Ringredients = list(dict())
        for i in range(len(ingredients)):
            Ringredients.append({'ingredient': ingredients[i].a.text, 'quantity': " ".join(
                ingredients[i].span.text.split())})

        # Preparation
        for i in soup.find_all(class_='num-step'):
            i.string = ''
        Rpreparation = ""
        preparation = soup.find_all('div', class_='gz-content-recipe-step')
        for i in range(len(preparation)):
            Rpreparation += preparation[i].text
        Rpreparation = re.sub('\s+', ' ', Rpreparation)
        
        Recipe = {'title': Rtitle, 'ingredients': Ringredients,
                  'preparation': Rpreparation}
        return Recipe
