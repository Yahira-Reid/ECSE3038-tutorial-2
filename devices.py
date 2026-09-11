readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

# Print each device's name and temperature

print("\n Task 1: List Devices ")

def list_devices(devices):
    for device in devices:
        print(f"Device: {device['name']}, Temperature: {device['temp']}°C")

list_devices(readings)

# Returning average temperatures

print("\n Task 2: Average Temperature ")

def average_temp(devices):
    total = 0
    for device in devices:
        total = total + device["temp"]

    return total / len(devices)

print(f"Average Temperature: {average_temp(readings):.2f}°C")
