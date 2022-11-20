#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from pprint import pprint


def data_base():
    """ Выводит все фильмы из базы """
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
    """ Вывод фильма по запросу названию """
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
    """
    Выводит список фильмов от .... года до ..... года
    НАПРИМЕР: http://127.0.0.1:5000/movie/2000/to/2005
    """
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
    """
    Это работает если ввести рейтинг в адресной строке
    НАПРИМЕР:
    http://127.0.0.1:5000/rating/Dramas
    """
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
