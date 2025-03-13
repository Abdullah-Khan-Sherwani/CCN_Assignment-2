import socket
import time

HOST = '127.0.0.1'  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("TCP Server is listening on port", PORT)

    while True:  # Keep accepting new clients
        connection, address = server_socket.accept()
        with connection:
            print("Connected by", address)

            with open("tcp_log.txt", "w") as log:
                while True:
                    try:
                        data = connection.recv(1024)  
                        if not data:
                            break  # Client disconnected

                        response = b"Received: " + data  # Acknowledge message
                        connection.sendall(response)

                        #log.write(f"Received: {data.decode()}\n")

                    except Exception as e:
                        print("Error:", e)
                        break  # Exit loop on error





'''import socket
import time

# Random port numbers
HOST = '127.0.0.1' # local host 
PORT = 65432 # From the dynamic port range

# IpV4 (AF_INET), TCP (SOCK_STREAM) socket made
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket: 
    Socket.bind((HOST, PORT)) 
    Socket.listen()
    print("TCP Server is listening on port", PORT)
    connection, address = Socket.accept() # Communicate and store client Ip and port

    with connection:
        print("Connected by", address)
        with open("tcp_log.txt", "w") as log:
            for x in range(100):
                start = time.time()
                data = connection.recv(1024) # max number of bytes to be received is 1024
                if not data:
                    break
                ACK = b"Recieved: " + data
                connection.sendall(ACK)
                end = time.time()
                log.write(f"{data.decode()} - RTT: {end - start:.6f} sec\n")'''