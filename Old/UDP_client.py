import socket
import time
import random

HOST = '127.0.0.1'
PORT = 65432 # From the dynamic port range
PACKET_LOSS_PROBABILITY = 0.05 # 1% chance of packet loss

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as Client_Socket:
    total_time = 0
    successful_messages = 0
    total_messages = 100

    with open("udp_log.txt", "w") as log:
        for x in range(total_messages):
            if random.random() < PACKET_LOSS_PROBABILITY:
                log.write(f"Message {x + 1} lost\n")
                continue

            msg = f"Message {x + 1}".encode()
            start = time.time()
            Client_Socket.sendto(msg, (HOST, PORT))
            response, address = Client_Socket.recvfrom(1024)
            end_time = time.time()
            rtt = end_time - start
            total_time += rtt  #(simulate rtt for both directions)
            successful_messages += 1

            log.write(f"Sent: {msg.decode()} - RTT: {rtt:.6f} sec\n")

        if successful_messages > 0:
            throughput = successful_messages / total_time
            latency = total_time / successful_messages
            log.write(f"\nUDP average latency: {latency:.6f} seconds | Throughput: {throughput:.6f} messages/sec\n")
            print(f"UDP average latency: {latency:.6f} seconds | Throughput: {throughput:.6f} messages/sec")
        else:
            log.write("\nNo messages were successfully sent.\n")
            print("No messages were successfully sent.")

        packet_loss_percentage = ((total_messages - successful_messages) / total_messages) * 100
        log.write(f"Packet loss percentage: {packet_loss_percentage:.2f}%\n")
        print(f"Packet loss percentage: {packet_loss_percentage:.2f}%")