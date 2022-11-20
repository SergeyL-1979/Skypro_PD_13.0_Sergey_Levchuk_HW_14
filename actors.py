import sqlite3
from pprint import pprint


with sqlite3.connect("netflix.db") as con:
    # con.row_factory = sqlite3.Row
    cur = con.cursor()
    # sqlite_query = """
    #                 SELECT COUNT(distinct "cast"), "cast", "type", release_year
    #                 FROM netflix
    #                 WHERE "cast" LIKE '%Rose McIver%' OR "cast" LIKE '%Ben Lamb%'
    #                 GROUP BY "cast"
    #                 """
    sqlite_query = """
                    SELECT COUNT(distinct "cast") as 'actor', "cast", "type", release_year
                    FROM netflix
                    WHERE "cast" LIKE '%Jack Black%' OR "cast" LIKE '%Dustin Hoffman%'
                    GROUP BY "cast"
                    """
    result = cur.execute(sqlite_query)
    get_genre = result.fetchall()
    pprint(get_genre)
    # for i in get_genre:
    #     pprint(i)

    # genre_list = []
    # for i in get_genre:
    #
    #     title = i["title"]
    #     description = i["type"]
    #     release_year = i["release_year"]
    #     cast = i["cast"]
    #
    #     genre_list.append(
    #         {
    #             "title": title,
    #             "description": description,
    #             "release_year": release_year,
    #             "cast": cast
    #         }
    #     )
    # pprint(genre_list)


