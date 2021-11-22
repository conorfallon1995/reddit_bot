import sqlite3

# Create a construction of database
con = sqlite3.connect('movies.db')

#Text of nominees from Exasol DB

nominees_text = "Joaquin Phoenix, David Strathairn, Philip Seymour Hoffman, Terrence Howard, Heath Ledger, George Clooney, Jake Gyllenhaal, Matt Dillon, William Hurt, Paul Giamatti, Charlize Theron, Keira Knightley, Judi Dench, Reese Witherspoon, Felicity Huffman, Frances McDormand, Catherine Keener, Rachel Weisz, Amy Adams, Michelle Williams"

#Cast to a list

nominees = nominees_text.split(', ')

# Create a cursor object to perform SQL commands

cur = con.cursor()

bacon_movies = []

bacon_dict = {}

for name in nominees:
    bacon_dict[name] = 0

# Iterate using cursor
for name in nominees:
    for row in cur.execute('SELECT title FROM movies '
                           'JOIN people ON stars.person_id=people.id '
                           'JOIN stars on stars.movie_id=movies.id '
                           'WHERE people.name =:name '
                           'INTERSECT select title FROM movies '
                           'JOIN people ON stars.person_id=people.id '
                           'JOIN stars ON stars.movie_id=movies.id '
                           'WHERE people.name="Kevin Bacon" AND people.birth=1958;', {'name': name}):
        bacon_movies.append(row)
        bacon_dict[name] = len(bacon_movies)

    # Reset list for next name
    bacon_movies = []

# Print non-empties
for key in bacon_dict:
    if bacon_dict[key] != 0:
        print(key + " " + str(bacon_dict[key]))

print('\nNone of these people won the Oscar. From this we must each draw our own conclusions.')