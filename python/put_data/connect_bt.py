import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic

import find_device
import sql_write_base


address = str(asyncio.run(find_device.getKASA()))

global dataList #This is awful
dataList = []

def send_data():
    sql_write_base.write_data(dataList)

def notify_handler(sender: BleakGATTCharacteristic, data: bytearray):
    #print(f"{data}")
    data.reverse()
    hex = data.hex()
    #print(hex)
    hexInt = int(hex, 16)
    print(hexInt)
    if hexInt == 666: #666 value signifies the start of datastream
        if len(dataList) == 4:
            send_data()

        dataList.clear()
    else:
        dataList.append(hexInt)

async def main(address):
    async with BleakClient(address) as client:
        characteristicList = []
        for service in client.services:
           for characteristic in service.characteristics:
              if characteristic.handle == 22:
                 print(characteristic.handle)
                 characteristicList.append(characteristic)
        print(characteristicList[-1])

        await client.start_notify(characteristicList[-1], notify_handler)

        await asyncio.sleep(260)

        await client.stop_notify(characteristicList[-1])

asyncio.run(main(address))
