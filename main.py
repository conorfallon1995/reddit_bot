# FYI, documentation can be found here https://docs.python.org/3/library/sqlite3.html

import sqlite3

# import reddit_bot as bot

# Create a construction of database
con = sqlite3.connect('movies.db')

# Create a cursor object to perform SQL commands

cur = con.cursor()

dummy_film = "blade runner"

# Set up variables for movie_id and director_name

movie_id = 0
director_name = ""

# Could create join such that the movie that is returned is actually sensible...
# The final parameter is passed in as a tuple so as to avoid just the characters being passed in
for row in cur.execute('SELECT * FROM movies WHERE title LIKE ? LIMIT 1;', (dummy_film,)):
    movie_id = row[0]
    print("Movie is " + str(row))
    print(movie_id)

# Maybe, instead of getting into ML etc., just return other movies by this director by their score
# If pumping money into it, then can use ML, employ engineers, servers etc.

# This should return goodfellas' id, which returns Marty's id, which returns Marty's name; this works

for row in cur.execute('SELECT name FROM people WHERE id=(SELECT person_id FROM directors WHERE movie_id= ?);',
                       (movie_id,)):
    director_name = row[0]
    print(row)

movie_id_list = []

# This gets the relevant movie_id and puts them all in a list

for row in cur.execute('SELECT movie_id FROM directors '
                       'JOIN movies ON directors.movie_id=movies.id '
                       'JOIN ratings on directors.movie_id=ratings.movie_id'
                       'WHERE directors.person_id=631;'):
    movie_id_list.append(row[0])
    print(row)

print(str(movie_id_list))

#Okay, this part copy and pasted into sqlite3 returns relevant information; try it in cur.execute
select * from ratings
join movies on movies.id=ratings.movie_id
join directors on directors.movie_id=ratings.movie_id
where directors.person_id=631
ORDER BY ratings.rating DESC;
