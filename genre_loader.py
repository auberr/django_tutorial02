import json

with open('genre.json', 'rt', encoding='UTF-8') as f:
    genre_list = json.load(f)
print(genre_list)