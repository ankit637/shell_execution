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

def main():

    host = input('Enter Your IP To Listen (Server): ')
    port = int(input("Enter The Port: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, client_address = server.accept()
    print(f"Connected by {client_address}")

    while True:
        command = input("Enter a command: ")
        if command.strip().lower() == 'quit':
            break

        client_socket.send(command.encode("utf-8"))
        response = client_socket.recv(4096).decode("utf-8")
        print(response)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    main()
