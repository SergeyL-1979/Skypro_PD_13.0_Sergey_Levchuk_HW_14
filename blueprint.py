#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template
from db_connect import data_base, sql_dict, sql_year, sql_rating
from genre import sql_genre

movies = Blueprint('movies', __name__, url_prefix='/')


@movies.route('/all')
def all_movies():
    all_mo = data_base()
    return render_template("index.html", all_mo=all_mo)


@movies.route('/movie/<title>')
def page_title(title):
    movies_title = sql_dict(title)
    return render_template("movies.html", movies_title=movies_title)

# TODO =====  разобраться как работает данная вьюшка с БД ============== TODO ===
# @movies.route('/movies/<title>')
# def search_title(title):
#     query = f"SELECT title, country, release_year, listed_in, description FROM netflix " \
#             f"WHERE title = '{title}' " \
#             f"ORDER BY release_year DESC " \
#             f"LIMIT 1"
# TODO ======= TODO ======= TODO =========== TODO =========== TODO ===============


@movies.route('/genre/<genre>')
def pag_genre(genre):
    all_genre = sql_genre(genre)
    return render_template("genre.html", all_genre=all_genre)


@movies.route('/movie/<old_year>/to/<new_year>')
def page_year(old_year, new_year):
    year_sql = sql_year(old_year, new_year)
    return render_template("year.html", year_sql=year_sql)


# Формат запроса:
@movies.route('/rating/<rat>')
def page_rat(rat):
    all_rat = sql_rating(rat)
    return render_template("rat.html", all_rat=all_rat)

# @movies.route('/rating/<rating>')
# def page_rating(rating):
#     if rating == 'family':
#         return """
#                 SELECT rating, title
#                 FROM netflix
#                 WHERE rating IN ('G', 'PG', 'PG-13')
#                 """
#     elif rating == 'children':
#         return 'children'
#     elif rating == 'adult':
#         return 'adult'

# @movies.route('/rating/<children>')  #(включаем сюда рейтинг G)
# def page_rating_children(children):
#
#     return render_template("children.html")
#
#
# @movies.route('/rating/<family>')    #(G, PG, PG-13)
# def page_rating_family(family):
#
#     return render_template("family.html")
#
#
# @movies.route('/rating/<adult>')     #(R, NC-17)
# def page_rating_adult(adult):
#
#     return render_template("adult.html")
