# -*- coding: utf-8 -*-
from get_recipes import Recipe
import json

links = json.loads(open('gz_links.json', mode='r', encoding='utf-8').read())
n_links = len(links)
for i in range(n_links):
    print(f'Getting {i} of {n_links} - {round(i/n_links*100,2)}% done.')
    filename = 'dataset/gzd' + str(i) + '.json'
    with open(filename, mode='w', encoding='utf-8') as fp:
        R = Recipe(links[i]).get()
        json.dump(R, fp, indent=4, sort_keys=False, ensure_ascii=False)
print(f'Done getting all {n_links} recipes.')
