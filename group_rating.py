#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from utils import db_connection
from pprint import pprint


def sql_rating(rat):

    rating_query = ('G', 'PG', 'PG-13', 'R', 'NC-17')

    if rat.lower() == "children":
        rating_query = ('G', )
    elif rat.lower() == "family":
        rating_query = ('G', 'PG', 'PG-13')
    elif rat.lower() == "adult":
        rating_query = ('R', 'NC-17')

    placeholder = '?'
    placeholders = ', '.join(placeholder for _ in rating_query)

    cursor = db_connection()
    query = """ 
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN (%s)
            """ % placeholders

    cursor.execute(query, rating_query)
    sql_rating_result = cursor.fetchall()

    rating_sql_list = []

    for i in sql_rating_result:
        rating_sql_list.append(
            {
                "title": i["title"],
                "rating": i['rating'],
                "description": i["description"]
            }
        )

    return rating_sql_list


# pprint(sql_rating('family'))
