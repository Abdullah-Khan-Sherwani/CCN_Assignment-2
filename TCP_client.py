import socket
import time

def main():
    HOST = '127.0.0.1'  
    PORT = 65432 # From the dynamic port range       

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    num_messages = 100
    latencies = []
    tbs = 0 #total bytes sent

    with open("tcp_log.txt", "w") as log_file:
        for i in range(1, num_messages + 1):
            payload = ("X" * 1400).encode() #change here to simulate real life application msgs (1400 bytes approx each)
            start = time.time()
            client_socket.sendall(payload) 
            tbs += len(payload)
            data = client_socket.recv(2048) #same change as in udp
            end = time.time()
            rtt = end - start
            latencies.append(rtt)
            log_file.write(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec\n")
            print(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec") #so as to not clutter logfile

        client_socket.close()

        avg_latency = sum(latencies) / len(latencies)
        total = sum(latencies)
        throughput = tbs / total if total > 0 else 0
        log_file.write("\nTCP Test Summary:\n")
        log_file.write(f"Average RTT: {avg_latency:.6f} sec\n")
        log_file.write(f"Throughput: {throughput:.2f} bytes/sec\n")
        print("\nTCP Test Summary:")
        print(f"Average RTT: {avg_latency:.6f} sec")
        print(f"Throughput: {throughput:.2f} bytes/sec")

if __name__ == "__main__":
    main()