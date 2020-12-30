import sqlite3

conn = sqlite3.connect("test.db")

c=conn.cursor()
#Creates table on db
#c=conn.execute("""CREATE TABLE TESTTABLE(
#            first text,
#            last text,
#            pay integer
#            ) """)
#"""

# Insert test data
c.execute("INSERT INTO testtable values(datetime('now'),datetime('now', 'localtime'),3000)")
conn.commit()

c.execute("SELECT * FROM TESTTABLE")

print(c.fetchall())


conn.close()
