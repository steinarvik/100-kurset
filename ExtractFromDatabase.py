import sqlite3

dbfile = 'data.db'

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

query = """
SELECT * FROM albums
WHERE title LIKE '%Live%' AND LENGTH(title) > 10
"""

cursor.execute(query)
rows = cursor.fetchall()

# print(rows)
for row in rows:
    # print(row)
    print(f'{row[0]}: {row[1]}')

conn.close()