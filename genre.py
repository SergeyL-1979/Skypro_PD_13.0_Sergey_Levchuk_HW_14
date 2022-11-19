#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from pprint import pprint


def sql_genre(genre):
    with sqlite3.connect("netflix.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        sqlite_query = """
                        SELECT listed_in, title, description, release_year
                        FROM netflix
                        WHERE listed_in IN ('{}')
                        ORDER BY release_year DESC 
                        LIMIT 10
                        """.format(genre)
        result = cur.execute(sqlite_query)
        get_genre = result.fetchall()

        genre_list = []
        for i in get_genre:
            if genre == i[0]:
                title = i["title"]
                description = i["description"]

                genre_list.append(
                    {
                        "title": title,
                        "description": description
                    }
                )

    return genre_list

