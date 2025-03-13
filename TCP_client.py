import socket
import time

HOST = '127.0.0.1' 
PORT = 65432 # From the dynamic port range

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as CLient_Socket:
    CLient_Socket.connect((HOST, PORT))
    total_time = 0

    with open("tcp_log.txt", "w") as log:
        for x in range(100):
            msg = f"Message {x + 1}".encode()
            start = time.time()
            CLient_Socket.sendall(msg)
            response = CLient_Socket.recv(1024)
            end_time = time.time()
            rtt = end_time - start
            total_time += rtt

            log.write(f"Sent: {msg.decode()} - RTT: {rtt:.6f} sec\n")

        throughput = 100 / total_time
        latency = total_time / 100
        log.write(f"\nTCP average latency: {latency:.6f} seconds | Throughput: {throughput:.6f} messages/sec\n")
    print(f"TCP average latency: {latency:.6f} seconds | Throughput: {throughput:.6f} messages/sec")