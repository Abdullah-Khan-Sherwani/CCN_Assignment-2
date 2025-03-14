import socket
import random

def main():
    HOST = '127.0.0.1'  
    PORT = 65432 # From the dynamic port range
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(2048)

        if not data:
            break

        message = data.decode()
        print(f"Received from {addr}: {message[0]}")

        if random.random() < 0.05: # 5% chance of packet loss
            print("Packet loss for message:", message[0])
            continue

        response = "Received: " + message
        server_socket.sendto(response.encode(), addr)

    server_socket.close()

if __name__ == "__main__":
    main()









'''import socket
import time

# Random port numbers
HOST = '127.0.0.1' # local host 
PORT = 65432 # From the dynamic port range

# IpV4 (AF_INET), UDP (SOCK_DGRAM) socket made
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as Socket:
    Socket.bind((HOST, PORT))
    print("UDP Server is listening on port", PORT)

    with open("udp_log.txt", "w") as log:
        expected_seq_num = 1
        lost_packets = 0
        for x in range(100):
            start = time.time()
            data, address = Socket.recvfrom(1024) # max number of bytes to be received is 1024
            if not data:
                break
            message = data.decode()
            try:
                seq_num = int(message.split()[1]) # "Message {x + 1} just use x + 1 to track lost packets"
            except ValueError:
                print(f"Received non-numeric sequence number: {message}")
                continue
            if seq_num != expected_seq_num:
                lost_packets += seq_num - expected_seq_num
                expected_seq_num = seq_num
            expected_seq_num += 1
            ACK = b"Received: " + data
            Socket.sendto(ACK, address)
            end = time.time()
            log.write(f"{message} - RTT: {end - start:.6f} sec\n")
            #print(f"Connected by {address}")
        log.write(f"Total lost packets: {lost_packets}")
        print(f"Total lost packets: {lost_packets}")'''