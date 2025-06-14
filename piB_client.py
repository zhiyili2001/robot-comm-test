import json
import socket
import time
import sensor_reader

with open("config.json") as f:
    config = json.load(f)

HOST = config["host"]  # A 机 IP 地址
PORT = config["port"]
PIN = config["sensor_pin"]

print("[B] Client started, waiting for tilt...")

while True:
    if sensor_reader.read_gpio(PIN):
        print("[B] TILT detected, sending to A...")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b"TILT")
        except Exception as e:
            print("[B] Failed to connect to A:", e)
    time.sleep(0.3)
