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

    with open("udp_log.txt", "w") as log:
        #test_start = time.time()
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
                log.write(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec\n")
                print(f"Message {i}: Sent 1400 bytes, Received {len(data)} bytes, RTT: {rtt:.6f} sec") #Concise print
            except socket.timeout:
                lpackets += 1
                log.write(f"Message {i}: Sent 1400 bytes, No response (packet lost)\n")
                print(f"Message {i}: Sent 1400 bytes, No response (packet lost)")

        #test_end = time.time()
        client_socket.close()

        if latencies:
            avg_latency = sum(latencies) / len(latencies)
            total = sum(latencies)
        else:
            avg_latency = 0
            total= 0

        #test_duration = test_end - test_start  # Total time taken for the test
        #throughput = totalBytes / test_duration if test_duration > 0 else 0
        throughput = totalBytes / total if total > 0 else 0

        log.write("\nUDP Test Summary:\n")
        log.write(f"Average RTT (for received packets): {avg_latency:.6f} sec\n")
        log.write(f"Packet Loss Rate: {lpackets / num_msg * 100:.2f}%\n")
        log.write(f"Throughput (approx.): {throughput:.2f} bytes/sec\n")

        print("\nUDP Test Summary:")
        print(f"Average RTT (for received packets): {avg_latency:.6f} sec")
        print(f"Packet Loss Rate: {lpackets / num_msg * 100:.2f}%")
        print(f"Throughput (approx.): {throughput:.2f} bytes/sec")

if __name__ == "__main__":
    main()