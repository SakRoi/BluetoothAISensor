import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host="172.20.241.9",
  user="dbaccess_rw",
  password="fasdjkf2389vw2c3k234vk2f3",
  database="measurements"
)
print(mydb)

mycursor = mydb.cursor()

writeInto = ("INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_f ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)")
values = [(3, "nrf5340", "raspi", 1, 800, 85, 100, "KASA")]

mycursor.executemany(writeInto, values)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

if 'main':
  write_data([0, 0, 0, 0])
