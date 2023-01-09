import sqlite3

conn = sqlite3.connect("accounts.db")
c = conn.cursor()
c.execute("SELECT * FROM users")
result = c.fetchall()
conn.commit()
conn.close()
for i in result:
    print(i[0], i[1], i[2], i[3], i[4])