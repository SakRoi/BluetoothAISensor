import asyncio
from bleak import BleakScanner

async def getKASA() -> str:
    devices = await BleakScanner.discover()
    for d in devices:
        if "KASA_LBS2" in str(d):
            deviceName = str(d)
            return deviceName[0:19]


if '__Main__':
    asyncio.run(getKASA())