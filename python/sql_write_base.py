import mysql.connector

mydb = mysql.connector.connect(
  host="800-callmemaybe",
  user="dumbass",
  password="uWishBitch",
  database="measurements"
)
print(mydb)

mycursor = mydb.cursor()

writeInto = ("INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_f ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)")
values = [(3, "nrf5340", "raspi", 1, 800, 85, 100, "KASA")]

mycursor.executemany(writeInto, values)

mydb.commit()

print(mycursor.rowcount, "was inserted.")