import mysql.connector
from dotenv import load_dotenv
import os

def write_data(data: list) -> None:
  '''Write the data into the MySQL database'''

  #Load the parameters from a .env file
  load_dotenv()
  envHost = os.getenv("HOST")
  envUser = os.getenv("SQL_USER")
  print(envUser)
  envPassword = os.getenv("SQL_PASSWORD")

  mydb = mysql.connector.connect(
    host = envHost,
    user = envUser,
    password = envPassword,
    database="measurements"
  )
  mycursor = mydb.cursor()

  writeInto = ("INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_f ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)")
  values = [(3, "nrf5340", "raspi", data[3], data[0], data[1], data[2], "KASA")]

  mycursor.executemany(writeInto, values)

  mydb.commit()

  print(mycursor.rowcount, "was inserted.")

if  "__main__":
  '''Write test data to the MySQL database'''
  write_data([1000, 1000, 1000, 1000])
