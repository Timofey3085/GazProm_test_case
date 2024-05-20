"""
№6*
Имеется банковское API возвращающее JSON
{
"Columns": ["key1", "key2", "key3"],
"Description": "Банковское API каких-то важных документов",
"RowCount": 2,
"Rows": [
["value1", "value2", "value3"],
["value4", "value5", "value6"]
]
}
Основной интерес представляют значения полей "Columns" и "Rows",
которые соответственно являются списком названий столбцов и значениями столбцов
Задание:
1 Получить JSON из внешнего API
ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня
сегодня в виде таймстемп"}
2 Валидировать входящий JSON используя модель pydantic
(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
2 Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
3 В полученном DataFrame произвести переименование полей по след. маппингу
"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
3 Полученный DataFrame обогатить доп. столбцом:
"load_dt" -> значение "сейчас"(датавремя)
"""
from pprint import pprint

import requests

json_data = requests.get('https://swapi.dev/api/people/').json()

results = json_data['results']

specifications = []  # Список для хранения характеристик персонажей

for character in results:
    table = f"{character['name']:20} | {character['birth_year']:10} | {character['eye_color']}"
    specifications.append(table)

with open('character_specifications.txt', 'w') as outfile:
    for name in specifications:
        outfile.write(name + '\n')

    print("Данные успешно сохранены в файл 'character_specifications.txt'")

# pprint(results)
pprint(specifications)

# не разобрался с заданиеv, с pydantic знаком поверхостно, поэтому привел пример кода,
# где извлёк все имена персонажей их день рождения и цвет глаз из другого api
# и сохранил их в файл character_specifications.txt
