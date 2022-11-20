#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from pprint import pprint


def sql_group_rating(rating):
    """
    Тут я пытался реализовать именно распределение по группам
    # Формат запроса:
    # /rating/children #(включаем сюда рейтинг G)
    # /rating/family   #(G, PG, PG-13)
    # /rating/adult    #(R, NC-17)
    Но так не получилось
    """

    # rat_tat = ['TV-PG', 'TV-MA', 'R', 'PG-13', 'TV-14', 'TV-PG', 'NR', 'TV-G', 'TV-Y7', 'TV-Y', 'G', 'PG', 'NC-17']
    with sqlite3.connect('netflix.db') as connection:
        # connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        children_query = """
                SELECT rating, title
                FROM netflix
                WHERE rating IN ('G')
                """.format(rating)
        family_query = """
                SELECT rating, title
                FROM netflix
                WHERE rating IN ('G', 'PG', 'PG-13')
                """.format(rating)
        adult_query = """
                SELECT rating, title
                FROM netflix
                WHERE rating IN ('R', 'NC-17')
                """.format(rating)

        cur_children = cursor.execute(children_query)
        cur_family = cursor.execute(family_query)
        cur_adult = cursor.execute(adult_query)
        for cur in cur_adult.fetchall():
            print(cur)


pprint(sql_group_rating('NC-17'))

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

