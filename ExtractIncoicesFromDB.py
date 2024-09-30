import sqlite3

dbfile = 'data2.db'

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

query = """
SELECT * FROM invoices
WHERE BillingCountry = 'Germany' AND Total > 2
"""

cursor.execute(query)
rows = cursor.fetchall()

# print(rows)
for row in rows:
    print(row)
    # print(f'{row[0]}: {row[1]}')

conn.close()