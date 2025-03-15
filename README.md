# TCP and UDP Compariosn  

## How to Run the Programs  

### **TCP:**  
1. Open a terminal and run the TCP server:  

   ```sh
   python TCP_server.py
   ```  

2. In another terminal, run the TCP client:  

   ```sh
   python TCP_client.py
   ```  

### **UDP:**  
1. Open a terminal and run the UDP server:  

   ```sh
   python UDP_server.py
   ```  

2. In another terminal, run the UDP client:  

   ```sh
   python UDP_client.py
   ```  

---

## Expected Outputs  

### **TCP:**  
- The TCP client sends **100 messages sequentially** each of 1400 bytes.  
- The TCP server responds with a message formatted as **"Received: "** for each incoming message.  
- The TCP client measures and logs the **round-trip time (RTT)** for every message and calculates the **average latency and throughput**.
- RTT should be between 0.05 to 0.13ms.
- Example output provided in **`tcplog.txt`**. 
- All transmission details are recorded in **`tcp_log.txt`**.
- Data utilised in **`ANSWERS.txt`** is logged in **`tcplog.txt`**.   

### **UDP:**  
- The UDP client sends **100 messages sequentially** each of 1400 bytes.  
- The UDP server, while receiving messages, **randomly drops some packets** to simulate packet loss.  
- For messages that are processed, the server sends a response **"Received: ."**  
- The UDP client logs the **RTT for received packets** and notes any **packet loss**.
- RTT should be between 0.03 to 0.12ms.
- Example output provided in **`udplog.txt`**. 
- Detailed results, including **lower RTTs and packet loss statistics**, are recorded in **`udp_log.txt`**.
- Data utilised in **`ANSWERS.txt`** is logged in **`udplog.txt`**.  

---

## **Observations About TCP vs UDP Behavior**

### **1. Latency Comparison:**
UDP has a lower latency on average when compared with TCP. This is because UDP does not have the overhead of establishing and maintaining a connection, and congestion control, which can lead to higher latency. TCP, on average, has a latency (RTT) of **0.000066 sec** (`tcp_log.txt`) and UDP had a latency of **0.000045 sec** (`udp_log.txt`).

In the provided code, latency and throughput vary, with TCP and UDP both having minute differences in latency and throughput. This is due to the nature of the network and the specific conditions of the test. However, in general, **UDP tends to have lower latency than TCP**.

### **2. Reliability and Packet Loss:**
- Nothing happens when UDP packets are lost, and they are not retransmitted.
- TCP ensures all packets arrive correctly since that is its design goal. It is used in applications that do not tolerate packet loss, such as email delivery, ensuring all packets are delivered using different mechanisms such as **checksums, ACKs, and retransmission**.

### **3. Throughput Analysis:**
- **UDP is faster for bulk data transfer** since it is not hindered by retransmissions and other overheads. Although UDP is faster, it is less reliable than TCP, and if the data is loss-intolerant, then **TCP should be used instead of UDP**.
- **TCP introduces overhead** due to acknowledgments (ACKs), as every packet requires an ACK to be received. If an ACK is not received, is corrupted, is duplicated, or is lost, then TCP retransmits the packet, which can lead to duplicate packets and cause congestion, increasing overhead. Flow and congestion control in TCP also contribute to overheads.

### **4. Use Cases:**
- **TCP** should be used when the data being transferred is **loss-intolerant**.
- **UDP** should be used where **fast transmission** is required and **data loss can be tolerated**.
- **TCP** is used in applications such as:
  - Emails
  - File transfers
  - Web browsing
- **UDP** is used in applications such as:
  - Video streaming
  - Online gaming

---

## Implementation Details  

### **Implementation:**  
- Both **TCP and UDP** client-server models were implemented in **Python** using the **socket** library.  
- The **UDP server** simulates **packet loss** by randomly dropping incoming packets.  
- Both applications log detailed execution data (**RTT, throughput, packet loss**) to their respective log files.  
- **Testing** was conducted by running both servers and clients **concurrently** to capture **real-time performance differences**.
- To simulate packet loss a random number generator was introduced in UDP and similar calculation was added but not used in TCP for more accurate RTT calculation.

### **References:**  
- **Python Socket Programming Documentation:**  
  - [https://docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)    
