import json
import socket
import sensor_reader
import time

with open("config.json") as f:
    config = json.load(f)

HOST = ""
PORT = config["port"]

print("[B] Server waiting for A...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"[B] Connected by {addr}")
        data = conn.recv(1024)
        if data == b"VIBRATION":
            print("[B] Received vibration signal, checking tilt...")
            tilted = sensor_reader.read_gpio(config["sensor_pin"])
            if tilted:
                print("[B] TILT detected! Responding...")
            else:
                print("[B] No tilt detected.")
