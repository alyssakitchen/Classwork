import socket
response = ""

# Define the server address and port
HOST = "34.16.129.141" #server IP
PORT = 48153

# FOR TESTING WITH LONG MESSAGE - COMMENT OUT LINE 28 TO USE
#with open("1MB_String.txt", "r") as file:
#        message = file.read()

# Create a socket object
try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4, TCP

except OSError:
        print(OSError)

# Connect to the server
try:
        s.connect((HOST, PORT))

except ConnectionRefusedError:
        print(ConnectionRefusedError)

while True:
        # Get user input and convert it to bytes
        message = input("Enter a message to send to the server (or 'exit' to quit): ")

        message_in_bytes = message.encode()

        if message == "exit":
                print("Quit")
                break

        # Send the message to the server
        try:
                s.sendall(message_in_bytes)
                s.send(b'end of transmission')
        except BlockingIOError:
                print(BlockingIOError)
        while True:
                # Receive the server's response
                try:
                        data = s.recv(1024)

                        # Convert data to string
                        data_as_string = data.decode()
                        if "end of transmission" in data_as_string:
                                break

                        response += data_as_string
#                        print(response)

                except TimeoutError:
                        print(TimeoutError)

        if data:
                break

# FOR TESTING WITH LONG MESSAGE
#with open("response.txt", "w") as file:
#        file.write(response)

# Print server response
print(f"Server Reponse: {response!r}")

# Close the client socket
s.close()