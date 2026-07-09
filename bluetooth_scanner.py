from bleak import BleakScanner
import asyncio

async def scan():
    devices = await BleakScanner.discover(timeout=8)

    result = []

    for device in devices:
        result.append({
            "name": device.name if device.name else "Unknown",
            "mac": device.address
        })

    return result

def scan_devices():
    return asyncio.run(scan())
