import sqlite3

# Create connection to file
FILENAME = "intro.db"
con = sqlite3.connect(FILENAME)

# Call on database cursor to execute queries
cur = con.cursor()


# Create a table
cur.execute("CREATE TABLE movie(title, year, score)")

# Verify Table is created
res = cur.execute("SELECT name FROM sqlite_master")

print(res)
print(res.fetchone())
# returns a tuple containing the tables name, return None if table is nonexistent
TABLE_NAME = 'spam'
res = cur.execute(f"SELECT name FROM sqlite_master WHERE name='{TABLE_NAME}'")
table_exist = res.fetchone() is None  # True

# Insert data into table
cur.execute("""
INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('Star Wars: The Phantom Menace', 1900, 9.9)
""")

# Commit Transaction
con.commit()

# Verify Data Insertion
res = cur.execute("SELECT score FROM movie")
res.fetchall()



# Insert multiple rows
"""
Notice that ? placeholders are used to bind data to the query. 
Always use placeholders instead of string formatting 
for binding Python values to SQL statements, 
(to avoid SQL injection attacks) 

"""
data = [
    ("Name 1", 1700, 10.0),
    ("Name 2", 1800, 9.1),
    ("Name 3", 1900, 8.2),
]

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

# Verify
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# Close Connection
con.close()



# Adaptable Objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.x};{self.y}"


con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute('SELECT ?', (Point(4.0, -3.2),))
print(cur.fetchone()[0])
con.close()


# Registering adapter callablers
def adapt_point(point: Point):
    return f"{point.x};{point.y}"

# Converters
def convert_point(s):
    """ s is a bytes object """
    x, y = map(float, s.split(b";"))
    return Point(x, y)

sqlite3.register_adapter(Point, adapt_point)
sqlite3.register_converter("point", convert_point)


# 1 - Parse declared types
p = Point(4.0, -3.2)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

# cur = con.cursor()
cur = con.execute("CREATE TABLE test(p point)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute('SELECT p FROM test')

print(cur.fetchone()[0])
cur.close()
con.close()


# 2 - Parse using column names
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)

# cur = con.cursor()
cur = con.execute("CREATE TABLE test(p)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute('SELECT p AS "p [point]" FROM test')
print(cur.fetchone()[0])
cur.close()
con.close()


