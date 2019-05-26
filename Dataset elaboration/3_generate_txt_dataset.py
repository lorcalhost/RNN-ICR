import json
import os

file_count = len(os.listdir('dataset'))

with open('gz_dataset.txt', mode='a+', encoding='utf-8') as fp:
    for i in range(file_count):
        f'Processing {i} of {file_count} - {round(i/file_count*100,2)}% done.'
        filename = 'dataset/gzd'+str(i)+'.json'
        with open(filename, 'r', encoding='utf-8') as json_in:
            recipe = json.loads(json_in.read())
            gz_title = recipe['title']
            fp.write(f'{gz_title}\n\nIngredienti:\n')
            for j in range(len(recipe['ingredients'])):
                gz_ingredient = f"\t{recipe['ingredients'][j]['ingredient']}: {recipe['ingredients'][j]['quantity']}\n"
                fp.write(gz_ingredient)
            gz_preparation = f"\n\nPreparazione:\n\t{recipe['preparation']}\n\n\n".replace('. ', '.\n\t')
            fp.write(gz_preparation)
    print(f'Done processing {file_count} files')
