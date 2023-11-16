import mysql.connector


def write_data(data: list) -> None:
  mydb = mysql.connector.connect(
    host="800-callmemaybe",
    user="Dumbas",
    password="youWishBish",
    database="measurements"
  )
  
  mycursor = mydb.cursor()

  writeInto = ("INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_f ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)")
  values = [(3, "nrf5340", "raspi", data[3], data[0], data[1], data[2], "KASA")]

  mycursor.executemany(writeInto, values)

  mydb.commit()