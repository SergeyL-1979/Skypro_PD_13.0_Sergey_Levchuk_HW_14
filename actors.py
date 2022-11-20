import sqlite3
from pprint import pprint


def get_actors(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        sqlite_query = """
                        SELECT COUNT(distinct "cast") as 'actor', title, "cast", "type", release_year
                        FROM netflix
                        WHERE "cast" LIKE '%{}%' OR "cast" LIKE '%{}%'
                        GROUP BY "cast"
                        """.format(actor_1, actor_2)

        result = cur.execute(sqlite_query)
        get_genre = result.fetchall()

        genre_list = []
        for i in get_genre:
            point = i['actor']
            title = i["title"]
            description = i["type"]
            release_year = i["release_year"]
            cast = i["cast"]

            genre_list.append(
                {
                    "count": point,
                    "title": title,
                    "description": description,
                    "release_year": release_year,
                    "cast": cast
                }
            )
        return genre_list


# pprint(get_actors('Jack Black', 'Dustin Hoffman'))
pprint(get_actors('Rose McIver', 'Ben Lamb'))

