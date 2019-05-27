import csv
import json
import os
import sys


def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


file_count = len(os.listdir('dataset'))
dir_name = 'dataset'

try:
    os.mkdir(dir_name)
except FileExistsError:
    pass

with open('gz_dataset.csv', mode='w+') as fp:
    fp_csv = csv.writer(fp, delimiter='|')
    fp_csv.writerow(['title', 'ingredients', 'preparation'])

    for i in range(file_count):
        delete_last_line()
        print(f'Processing {i} of {file_count} - {round(i/file_count*100,2)}% done.')
        filename = 'dataset/gzd'+str(i)+'.json'
        with open(filename, 'r', encoding='utf-8') as json_in:
            recipe = json.loads(json_in.read())
            gz_title = recipe['title']
            gz_ingredients = ''
            for j in range(len(recipe['ingredients'])):
                gz_ingredients += f"{recipe['ingredients'][j]['ingredient']}: {recipe['ingredients'][j]['quantity']}    "
            gz_preparation = recipe['preparation']
            fp_csv.writerow([gz_title, gz_ingredients, gz_title])
    print(f'Done processing {file_count} files')
