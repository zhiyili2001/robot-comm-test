import json
import socket
import time
import sensor_reader

with open("config.json") as f:
    config = json.load(f)

HOST = config["host"]
PORT = config["port"]

print("[A] Client started, waiting for vibration...")

while True:
    if sensor_reader.read_gpio(config["sensor_pin"]):
        print("[A] Vibration detected, sending to B...")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b"VIBRATION")
        except:
            print("[A] Failed to connect to B")
    time.sleep(0.2)

