import socket
import time

HOST = '127.0.0.1'  # Local host
PORT = 65432  # Dynamic port range

# Create UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print("UDP Server is listening on port", PORT)

    with open("udp_log.txt", "w") as log:
        received_packets = 0
        total_packets = 100  # Expected messages

        for _ in range(total_packets):  
            try:
                start = time.time()
                data, address = server_socket.recvfrom(1024)  # Receive message
                end = time.time()

                if not data:
                    continue

                message = data.decode()
                received_packets += 1
                server_socket.sendto(b"ACK", address) # Send ACK to client for rtt compute

                log.write(f"Received: {message} - RTT: {end - start:.6f} sec\n")
                print(f"Received from {address}: {message}")

            except Exception as e:
                print("Error receiving data:", e)

        # Calculate packet loss percentage
        packet_loss = ((total_packets - received_packets) / total_packets) * 100
        log.write(f"\nPacket loss percentage: {packet_loss:.2f}%\n")
        print(f"Packet loss percentage: {packet_loss:.2f}%")









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