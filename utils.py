#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Подключение к sqlite3
"""
import sqlite3
from pprint import pprint


def db_connection():
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        return cursor
