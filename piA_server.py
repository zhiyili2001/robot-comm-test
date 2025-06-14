import socket

with open("config.json") as f:
    import json
    config = json.load(f)

HOST = "0.0.0.0"
PORT = config["port"]

print("[A] Server listening on port", PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print("[A] Connected by", addr)
            data = conn.recv(1024)
            if data == b"TILT":
                print("[A] Received TILT from B — responding...")
