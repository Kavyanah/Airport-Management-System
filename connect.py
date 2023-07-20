import mysql.connector
cnx=mysql.connector.connect(user='root', password='kavyansh@cs', host='127.0.0.1')
cur=cnx.cursor()
cur.execute('use ams')
cur.execute('select * from passenger_details')
data=cur.fetchall()
for i in data:
    print(i)

