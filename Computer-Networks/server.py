import socket
counter = 0
# Define the server address and port
HOST = ""
PORT = 48153

# Create a socket object
try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4, TCP

except OSError:
        print(OSError)

# Bind the socket to the server address
try:
        s.bind((HOST, PORT))

except Exception as e:
        print(e)

# Listen for incoming connections
try:
        s.listen()

except ConnectionRefusedError:
        print(ConnectionRefusedError)

while True:
        # Wait for client to connect
        try:
                conn, addr = s.accept()

        except Exception as e:
                print(e)

        with conn:
                # Print a message to indicate the client connection
                print(f"Connected by {addr}")

                # Handle client data
                while True:
                        # Receive data from the client & process it
                        try:
                                data = conn.recv(1024)
                                datastr = data.decode()

                        except Exception as e:
                                print("Error: ", e)

                        try:
                                # Send response to client
                                conn.send(datastr.encode())

                                if not data:
                                        break

                        except Exception as e:
                                print("Error: ", e)



# Close the client socket
s.close()