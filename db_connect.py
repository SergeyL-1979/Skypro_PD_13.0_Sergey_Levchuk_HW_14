#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from pprint import pprint


def data_base():
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """ SELECT * FROM netflix"""
        cursor.execute(query)
        result = cursor.fetchall()

    list_sql = []
    for i in result:
        title = i["title"]
        country = i["country"]
        release_year = i["release_year"]
        listed_in = i["listed_in"]
        description = i["description"]

        list_sql.append({
            "title": title,
            "country": country,
            "release_year": release_year,
            "listed_in": listed_in,
            "description": description
        })

    return list_sql


def sql_dict(title):

    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """ 
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title = (?)
                """
        cursor.execute(query, (title,))
        sql_result = cursor.fetchall()

        dict_sql_result = []
        for i in sql_result:
            title = i["title"]
            country = i["country"]
            release_year = i["release_year"]
            listed_in = i["listed_in"]
            description = i["description"]

            dict_sql_result.append(
                {
                    "title": title,
                    "country": country,
                    "release_year": release_year,
                    "listed_in": listed_in,
                    "description": description
                }
            )
        return dict_sql_result


def sql_year(old_year, new_year):

    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """ 
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE release_year BETWEEN @old_year AND @new_year
                LIMIT 100
                """
        cursor.execute(query, (old_year, new_year))
        sql_result = cursor.fetchall()

        sql_year_dict = []
        for i in sql_result:
            title = i["title"]
            country = i["country"]
            release_year = i["release_year"]
            listed_in = i["listed_in"]
            description = i["description"]

            sql_year_dict.append(
                {
                    "title": title,
                    "country": country,
                    "release_year": release_year,
                    "listed_in": listed_in,
                    "description": description
                }
            )

    return sql_year_dict


def sql_rating(rat):
    # Формат запроса:
    # /rating/children #(включаем сюда рейтинг G)
    # /rating/family   #(G, PG, PG-13)
    # /rating/adult    #(R, NC-17)

    rat_year = ['TV-PG', 'TV-MA', 'R', 'PG-13', 'TV-14', 'TV-PG', 'NR', 'TV-G', 'TV-Y7', 'TV-Y', 'G', 'PG', 'NC-17']
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = """ 
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN ('{}')
                """.format(rat)
        cursor.execute(query,)
        sql_rating_result = cursor.fetchall()

        rating_sql_list = []
        for i in sql_rating_result:
            if rat == i[1]:
                title = i["title"]
                rating = i['rating']
                description = i["description"]

                rating_sql_list.append(
                    {
                        "title": title,
                        "rating": rating,
                        "description": description
                    }
                )

    return rating_sql_list


# def sql_group_rating(rat_rat):
#     # Формат запроса:
#     # /rating/children #(включаем сюда рейтинг G)
#     # /rating/family   #(G, PG, PG-13)
#     # /rating/adult    #(R, NC-17)
#     # rat_tat = ['TV-PG', 'TV-MA', 'R', 'PG-13', 'TV-14', 'TV-PG', 'NR', 'TV-G', 'TV-Y7', 'TV-Y', 'G', 'PG', 'NC-17']
#     with sqlite3.connect('netflix.db') as connection:
#         # connection.row_factory = sqlite3.Row
#         cursor = connection.cursor()
#         query = """
#                 SELECT rating, title
#                 FROM netflix
#                 WHERE rating IN ('{}')
#                 """.format(rat_rat)
#         cursor.execute(query)
#
#     # children = []
#     # family = []
#     # adult = []
#     group_sql = []
#     for cur in cursor.fetchall():
#         if rat_rat == cur[0]:
#             group_sql.append(cur)
#
#         # if 'G' == cur[0]:
#         #     children.append(cur)
#         #     family.append(cur)
#         # elif 'PG' == cur[0]:
#         #     family.append(cur)
#         # elif 'PG-13' == cur[0]:
#         #     family.append(cur)
#         # elif 'R' == cur[0]:
#         #     adult.append(cur)
#         # elif 'NC-17' == cur[0]:
#         #     adult.append(cur)
#
#     return group_sql


# def sql_group_rating():
#     # Формат запроса:
#     # /rating/children #(включаем сюда рейтинг G)
#     # /rating/family   #(G, PG, PG-13)
#     # /rating/adult    #(R, NC-17)
#     # rat_tat = ['TV-PG', 'TV-MA', 'R', 'PG-13', 'TV-14', 'TV-PG', 'NR', 'TV-G', 'TV-Y7', 'TV-Y', 'G', 'PG', 'NC-17']
#     with sqlite3.connect('netflix.db') as connection:
#         # connection.row_factory = sqlite3.Row
#         cursor = connection.cursor()
#         query = """
#                 SELECT rating, title
#                 FROM netflix
#                 WHERE rating IN ('G', 'PG', 'PG-13')
#                 """
#
#         cursor.execute(query)
#         for cur in cursor.fetchall():
#             print(cur)

# g_rat = sql_group_rating()
# pprint(g_rat)
# pprint(data_base())
