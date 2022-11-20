#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template
from db_connect import data_base, sql_dict, sql_year
from group_rating import sql_rating
from genre import sql_genre

movies = Blueprint('movies', __name__, url_prefix='/')


@movies.route('/all')
def all_movies():
    """ Выводит все фильмы """
    all_mo = data_base()
    return render_template("index.html", all_mo=all_mo)


@movies.route('/movie/<title>')
def page_title(title):
    """ Выводит фильм по названию """
    movies_title = sql_dict(title)
    return render_template("movies.html", movies_title=movies_title)


@movies.route('/genre/<genre>')
def pag_genre(genre):
    """ Выводит по жанру фильмы """
    all_genre = sql_genre(genre)
    return render_template("genre.html", all_genre=all_genre)


@movies.route('/movie/<old_year>/to/<new_year>')
def page_year(old_year, new_year):
    """
    Выводит список фильмов от .... года до ..... года
    НАПРИМЕР: http://127.0.0.1:5000/movie/2000/to/2005
    """
    year_sql = sql_year(old_year, new_year)
    return render_template("year.html", year_sql=year_sql)


# Формат запроса:
@movies.route('/rating/<rat>')
def page_rat(rat):
    """
    Это работает если ввести рейтинг в адресной строке
    НАПРИМЕР:
    http://127.0.0.1:5000/rating/Dramas
    """
    all_rat = sql_rating(rat)
    return render_template("rating.html", all_rat=all_rat)
