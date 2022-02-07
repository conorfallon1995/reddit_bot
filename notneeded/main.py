import sqlite3

# import reddit_bot as bot

# Create a construction of database
con = sqlite3.connect('../../movies.db')

# Create a cursor object to perform SQL commands

cur = con.cursor()
'''
IGNORE THIS PROFESSOR - THIS IS JUST TO HELP ME
dummy_film = "armageddon"

# Set up variables for movie_id and director_name

movie_id = 0
director_name = ""
director_id = 0

# Could create join such that the movie that is returned is actually sensible...
# The final parameter is passed in as a tuple so as to avoid just the characters being passed in
for row in cur.execute('SELECT * FROM movies WHERE title LIKE ? LIMIT 1;', (dummy_film,)):
    movie_id = row[0]
    print("Movie is " + str(row))
    print(movie_id)

# Maybe, instead of getting into ML etc., just return other movies by this director by their score
# If pumping money into it, then can use ML, employ engineers, servers etc.

# This assigns correctly to director_id

for row in cur.execute('SELECT name, id FROM people WHERE id=(SELECT person_id FROM directors WHERE movie_id= ?);',
                       (movie_id,)):
    director_name = row[0]
    director_id = row[1]
    print(row)

movie_id_list = []

# This gets the relevant movie_id and puts them all in a list THINK CAN DELETE THIS
'''
'''
for row in cur.execute('SELECT directors.movie_id FROM directors '
                       'JOIN movies ON directors.movie_id=movies.id '
                       'JOIN ratings on directors.movie_id=ratings.movie_id'
                       'WHERE directors.person_id=631;'):
    movie_id_list.append(row[0])
    print(row)
'''
'''
print("movie_id_list" + str(movie_id_list))

# Okay, this part copy and pasted into sqlite3 returns relevant information; try it in cur.execute

for row in cur.execute('select * from ratings '
                       'join movies on movies.id=ratings.movie_id '
                       'join directors on directors.movie_id=ratings.movie_id '
                       'where directors.person_id=? '
                       'ORDER BY ratings.rating DESC LIMIT 5;', (director_id,)):
    movie_id_list.append(row[0])
    print(str(row[4]) + " has an IMDB rating of " + str(row[1]))
    print(row)

print(str(movie_id_list))

'''


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
            _director_name) + '. Here is a selection of their top 5 movies as per their IMDB ranking. Maybe you\'ll enjoy these!  \n\n' + ''.join(_string_list)
    # this can probably be turned into a unit test of some description, to account for when there's no IMDB result found
    return return_string


