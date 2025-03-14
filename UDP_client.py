import socket
import time

def main():
    HOST = '127.0.0.1'  
    PORT = 65432 # From the dynamic port range       

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(0.0001)  #timeout

    num_msg = 100
    latencies = []
    totalBytes = 0
    lpackets = 0 # lost

    for i in range(1, num_msg + 1):
        payload = ("X" * 1400).encode() #1400 bytes transferred
        totalBytes += len(payload)
        start = time.time()
        client_socket.sendto(payload, (HOST, PORT))
        try: #added error handling
            data, addr = client_socket.recvfrom(2048) #increased buffer size to 1024 bytes (1400 coming in)
            end = time.time()
            rtt = end - start
            latencies.append(rtt)
            print(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec") #Concise print
        except socket.timeout:
            lpackets += 1
            print(f"Message {i}: Sent 1400 bytes, No response (packet lost)")

    client_socket.close()

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        total = sum(latencies)
    else:
        avg_latency = 0
        total= 0

    throughput = totalBytes / total if total > 0 else 0

    print("\nUDP Test Summary:")
    print(f"Average RTT (for received packets): {avg_latency:.6f} sec")
    print(f"Packet Loss Rate: {lpackets / num_msg * 100:.2f}%")
    print(f"Throughput (approx.): {throughput:.2f} bytes/sec")

if __name__ == "__main__":
    main()



'''import socket
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
        print(f"Packet loss percentage: {packet_loss_percentage:.2f}%")'''