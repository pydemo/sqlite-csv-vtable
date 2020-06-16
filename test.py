import sys

from pysqlite2 import dbapi2 as sqlite3
e=sys.exit
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.load_extension("./csv") 

cur = con.cursor()
cur.execute("CREATE VIRTUAL TABLE temp.sample USING csv(filename='sample.csv')")

q="""SELECT * FROM sample"""
cur = con.cursor()
cur.execute(q)

rows = cur.fetchall()
for row in rows:
    print(row)
