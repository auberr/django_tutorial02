import json

genre_list = ["sf", "가족", "공표", "드라마", "로맨스", "먼치킨", "모험", "미스테리", "범죄", "서스펜스", "스포츠", "시대", "옴니버스", "요괴", "이세계", "일상", "전투", "코미디", "판타지", "학원"]

with open('animation.json', 'r', encoding='UTF-8') as f:
    animations = json.load(f)

# Output : {'name': 'Bob', 'languages': ['English', 'French']}

new_list = []
for animation in animations:
    new_data = {"model": "animations.animation"}
    if animation["genre"]:
        genres = eval(animation["genre"])
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre) + 1
            genre_int_list.append(genre_int)
        animation['genre'] = genre_int_list

    else:
        animation["genre"] = []
    new_data["fields"] = animation
    new_list.append(new_data)

with open('animations_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
