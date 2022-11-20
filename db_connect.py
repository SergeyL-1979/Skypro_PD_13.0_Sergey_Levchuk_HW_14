#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import db_connection
from pprint import pprint


def data_base():
    """ Выводит все фильмы из базы """
    cursor = db_connection()
    query = """ SELECT * FROM netflix"""
    cursor.execute(query)
    result = cursor.fetchall()

    list_sql = []
    for i in result:
        list_sql.append({
            "title": i["title"],
            "country": i["country"],
            "release_year": i["release_year"],
            "listed_in": i["listed_in"],
            "description": i["description"],
        })

    return list_sql


def sql_dict(title):
    """
    Вывод фильма по запросу названию.

    WHERE title = (?) - регистрозависима
    WHERE title LIKE (?) - не регистрозависима
    """
    cursor = db_connection()
    query = """ 
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE (?)
            """
    cursor.execute(query, (title,))
    sql_result = cursor.fetchall()

    dict_sql_result = []
    for i in sql_result:
        dict_sql_result.append(
            {
                "title": i["title"],
                "country": i["country"],
                "release_year": i["release_year"],
                "listed_in": i["listed_in"],
                "description": i["description"],
            }
        )
    return dict_sql_result


def sql_year(old_year, new_year):
    """
    Выводит список фильмов от .... года до ..... года
    НАПРИМЕР: http://127.0.0.1:5000/movie/2000/to/2005
    """
    cursor = db_connection()
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
        sql_year_dict.append(
            {
                "title": i["title"],
                "country": i["country"],
                "release_year": i["release_year"],
                "listed_in": i["listed_in"],
                "description": i["description"],
            }
        )

    return sql_year_dict
