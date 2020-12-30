import sqlite3

conn = sqlite3.connect("test.db")



#c=conn.execute("""CREATE TABLE TESTTABLE(
#            first text,
#            last text,
#            pay integer
#            ) """)
#"""

c.execute("INSERT INTO test values('FirstName','LastName',1000)")
conn.commit
conn.close()