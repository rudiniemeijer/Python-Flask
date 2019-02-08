# Gaat er vanuit dat de initialisatie van de database handmatig is uitgevoerd

import mysql.connector as mariadb

con = mariadb.connect(host='localhost', \
                      database='test', \
                      user='dbroot', \
                      password='$ecret1')
if con.is_connected:
  print('Connected to the database')

cursor = con.cursor() 
cursor.execute("SELECT * FROM measurements ORDER BY timestamp DESC")

rows = cursor.fetchall()
print("Just fetched",cursor.rowcount,"rows")

for row in rows:
  print(row)

con.close()  
