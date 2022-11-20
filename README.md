# Skypro_PD_13.0_Sergey_Levchuk_HW_14

## Выполнил:
   * Шаг 1
   * Шаг 2
   * Шаг 4

## Получилось реализовать частично
   * Шаг 3

Выводит рейтинг по запросу в адресной строке но не распределяет 
ее по группам.

Вывод рейтинга работает так:
*http://127.0.0.1:5000/rating/Dramas*

## Нужна помощь в реализации
   * Шаг 5

Это работает но мне не понятен один момент в задании
Правильно ли сделано ТЗ ШАГ_5?


   * Шаг 6
Но тоже сомневаюсь в правильности решения
```python
import sqlite3
from pprint import pprint


def get_sql_films(listed_in, release_year, type_films):

    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """ 
                SELECT listed_in, "type", release_year, title
                FROM netflix
                WHERE listed_in IN ('{}', '{}', '{}')
                LIMIT 10
                """.format(listed_in, release_year, type_films)
        cursor.execute(query)
        result_sql = cursor.fetchall()

        films_list = []
        for i in result_sql:
            listed_in = i["listed_in"]
            release_year = i["release_year"]
            type_films = i['type']
            title = i['title']

            films_list.append(
                {
                    "GENRE": listed_in,
                    "RELEASE EAR": release_year,
                    "TYPE FILMS": type_films,
                    "TITLE": title,
                }
            )

        return films_list


pprint(get_sql_films('TV Shows', 2017, 'Movie'))
```


