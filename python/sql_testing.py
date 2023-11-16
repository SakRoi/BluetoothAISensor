import mysql.connector

mydb = mysql.connector.connect(
  host="172.20.241.9",
  user="dbaccess_ro",
  password="vsdjkvwselkvwe234wv234vsdfas",
  database="measurements"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM rawdata WHERE groupid = '5'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
