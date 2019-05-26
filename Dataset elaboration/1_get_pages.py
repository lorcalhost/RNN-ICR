# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json


def get_max_pages_each():
    global url
    global pages
    max_pages_each = list()
    for i in range(len(pages)):
        response = requests.get(url+str(1)+'/'+pages[i])
        soup = BeautifulSoup(response.text, "html.parser")
        num = soup.find('span', class_='disabled total-pages')
        max_pages_each.append(int(num.text))
    return max_pages_each


url = 'https://ricette.giallozafferano.it/ricette-cat/page'
pages = ['Antipasti', 'Primi', 'Secondi-piatti',
         'Contorni', 'Dolci-e-Desserts', 'Lievitati', 'Piatti-Unici']
max_pages_each = get_max_pages_each()

with open('gz_links.json', mode='w', encoding='utf-8') as fp:
    Rlinks = list()
    for i in range(len(pages)):
        for j in range(max_pages_each[i]):
            page_url = url+str(j+1)+'/'+pages[i]
            print(f'Getting: {page_url}')
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find_all('h2', class_='gz-title')
            for x in range(len(links)):
                links[x] = links[x].a['href']
            Rlinks += links
    
    Rlinks = list(dict.fromkeys(Rlinks)) # Remove possible duplicate links
    fp.write(json.dumps(Rlinks, indent=4, sort_keys=False))
    print('Done collecting links')
