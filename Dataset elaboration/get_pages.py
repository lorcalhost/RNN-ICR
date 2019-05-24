import requests
from bs4 import *
import re
import json


url = 'https://ricette.giallozafferano.it/ricette-cat/page'
pages = ['Antipasti', 'Primi', 'Secondi-piatti',
         'Contorni', 'Dolci-e-Desserts', 'Lievitati', 'Piatti-Unici']
max_pages_each = [61 ,69, 54, 15, 93, 18, 25]

with open('gz_links.json', 'w') as fp:
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
            Rlinks.append(links)
    fp.write(json.dumps(Rlinks, indent=4, sort_keys=False))
    print('Done collecting links')



