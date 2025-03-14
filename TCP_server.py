import socket
import random

def main():
    HOST = '127.0.0.1'
    PORT = 65432 # From the dynamic port range       

    # creating a tcp socket bound to address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP server listening on {HOST}:{PORT}")

    #accept connection
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break 
        message = data.decode()
        print("Received:", message[0])

        if random.random() < 0.05: # Random int generation to provide a fair test eith udp (else time discrepancy)
            safeguard = 1 # no logic here, just to keep the code running
            #print("Packet loss for message:", message)
            #continue

        response = "Received: " + message
        conn.sendall(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()





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