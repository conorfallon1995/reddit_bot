import sqlite3

# Create a construction of database
con = sqlite3.connect('movies.db')

# Create a cursor object to perform SQL commands
cur = con.cursor()


def string_query(_film: str) -> str:
    _movie_id = 0
    _director_name = ""
    _director_id = 0
    for _row in cur.execute('SELECT * FROM movies WHERE title LIKE ? LIMIT 1;', (_film,)):
        _movie_id = _row[0]
        print("The movie this bot detects you've selected is " + str(_row[1]) + " released in " + str(_row[2]))

    for _row in cur.execute('SELECT name, id FROM people WHERE id=(SELECT person_id FROM directors WHERE movie_id= ?);',
                            (_movie_id,)):
        _director_name = _row[0]
        _director_id = _row[1]
        print('This movie was directed by ' + str(
            _director_name) + '. Here is a selection of the top 5 other movies they have done as per their IMDB '
                              'ranking. Maybe you\'ll enjoy these!')

    # _movie_id_list allows the program to keep track of the director's films

    _movie_id_list = []
    _string_list = []
    for _row in cur.execute('select * from ratings '
                            'join movies on movies.id=ratings.movie_id '
                            'join directors on directors.movie_id=ratings.movie_id '
                            'where directors.person_id=? '
                            'ORDER BY ratings.rating DESC LIMIT 5;', (_director_id,)):
        _movie_id_list.append(_row[0])
        _string_list.append(str(_row[4]) + " has an IMDB rating of " + str(_row[1]) + '  \n')
    return_string = 'This movie was directed by ' + str(
        _director_name) + '. Here is a selection of their top 5 movies as per their IMDB ranking. Maybe you\'ll enjoy these!  \n\n' + ''.join(
        _string_list)

    return return_string
