
'''

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="neha", passwd="neha",)
mycursor = mydb.cursor()

mycursor.execute("show databases")
for x in mycursor:
    print(x)
mycursor.execute("use railway")
mycursor.execute("select * from reservedseats")
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)

mydb.commit()
'''
'''

def pattern():
    a=1
    while a<5:
        print("5 4 3 2 1")
        a=a+1
pattern()
'''

for a in range(-5,6):
    print("* ")
    a=a+1
