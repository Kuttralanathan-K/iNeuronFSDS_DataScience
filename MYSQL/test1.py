import mysql.connector as conn

mydb = conn.connect(host="localhost",user = "root", passwd = "Kuttral25/04")

print(mydb)

cursor = mydb.cursor()
cursor.execute("create database ineuronFSDS_Learnings")  #Create database with name "kuttral"
cursor.execute("show databases")

#cursor.execute("create table if not exist dbname.tablename(column1 datatype(size),column2 datatype(size))") #Create table with schema
print(cursor.fetchall())

#mydb.commit() Inorder to reflect in DB

#Hiring Drive link - https://docs.google.com/forms/d/e/1FAIpQLSekHwCzf0Rzi_9wABGo71qyjQLJjMhqv6vMQOSLWRQbj-dUww/viewform?vc=0&c=0&w=1&flr=0