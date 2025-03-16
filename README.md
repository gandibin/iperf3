# Test Objective
The purpose of this test is to evaluate the network performance of two network devices using iPerf3. The test covers TCP and UDP transmission performance, multi-threaded processing capability, and bidirectional transmission performance. Additionally, it assesses both single-port performance and overall performance during multi-port concurrent transmissions.

# Device Configuration
The test computer is equipped with **6 SFP ports and 4 Gigabit Ethernet ports**, with IP addresses ranging from `192.168.5.31 ~ 192.168.5.40`.  
The tested devices include:
- **Small Device**: 6 Gigabit Ethernet ports, IP addresses: `192.168.5.21 ~ 192.168.5.26`.
- **Large Device**: 8 Gigabit Ethernet ports and 2 SFP ports, IP addresses: `192.168.5.21 ~ 192.168.5.30`.

# Test Report Naming Convention
Test reports are saved in `JSON` format. If the data cannot be parsed into JSON, it is stored as a `TXT` file.  
The file naming convention is as follows:
1. **Test Type** (e.g., `tcp`, `udp`).
2. **Number of Network Ports Tested** (ranging from 1 to 10).
3. **IP Address of the Sending Device**.
4. **IP Address of the Receiving Device**.
5. **Timestamp of the Report Generation**.

All test reports are stored in the `log` folder.

# Test Conclusion
Key findings from the test results:
- **Single-port testing**: The maximum bandwidth can reach close to **1 Gbps**.
- **Multi-port concurrent testing**: The maximum speed per port is reduced to **30% ~ 40%** of its theoretical limit.
- **Large device UDP performance is weak**:
  - Packet loss occurs when transmitting **over 100MB** in a single session.
  - When transmitting **1GB or more**, packet loss can reach **30%**.
- **Poor multi-threading performance**:
  - When a **single port** handles **more than 50 threads**, **latency and crashes** occur.

The test results indicate that regardless of whether a single-port or 10-port concurrent test is performed, the packet loss rate and crash probability remain consistently high.
