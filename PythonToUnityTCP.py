import socket
import random
import time

HOST = "127.0.0.1"
PORT = 10001

def generate_random_direction():
    return random.choice([-1, 0, 1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        joint1_val = generate_random_direction()  # Left/Neutral/Right
        ##joint2_val = generate_random_direction()  # Backward/Neutral/Forward

        data = f"{joint1_val}"
        print("Sending:", data)

        s.sendall((data + "\n").encode())
        time.sleep(0.5)  # Adjust for faster/slower changes
