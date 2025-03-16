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

# Performance Test Results

| Test Type    | Test PORT                                          | Testing Device | Device Type | Method | Send bites bits_per_second | receive bits_per_second | LINKS2                                                                                                                                  |   |   |   |   |   |   |   |
|--------------|----------------------------------------------------|----------------|-------------|--------|----------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---|---|---|---|
| two-way test | RG45                                               | QM118L         | receiver    | iperf3 | 948116219                  | 947553995               | https://github.com/gandibin/iperf3/tree/main/log/bidirectional_thread_1_192.168.5.31_to_192.168.5.21_2025-03-14_20-10-01.txt            |   |   |   |   |   |   |   |
| two-way test | SFP                                                | QM118L         | receiver    | iperf3 | 948408730                  | 947809455               | https://github.com/gandibin/iperf3/tree/main/log/bidirectional_thread_1_192.168.5.39_to_192.168.5.29_2025-03-14_20-11-18.txt            |   |   |   |   |   |   |   |
| two-way test | All 10 port together                               | QM118L         | receiver    | iperf3 | 296567999                  | 296292748               | https://github.com/gandibin/iperf3/tree/main/log/bidirectional_thread_10_192.168.5.31_to_192.168.5.21_2025-03-14_20-15-35.txt           |   |   |   |   |   |   |   |
| Multi-thread | All 10 port together 100 socket (too many failure) | QM118L         | receiver    |        | 783824566                  | 804527741               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_10_192.168.5.38_to_192.168.5.28_2025-03-14_18-51-13.json            |   |   |   |   |   |   |   |
| Multi-thread | All 10 port together 100 socket (All success)      | QM118L         | sender      |        | 386793155                  | 380293303               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_10_192.168.5.21_to_192.168.5.31_2025-03-15_04-41-08.json            |   |   |   |   |   |   |   |
| Multi-thread | All 10 port together 50 socket (too many failure)  | QM118L         | receiver    |        | 866383652                  | 853629431               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_10_192.168.5.37_to_192.168.5.27_2025-03-14_18-52-34.json            |   |   |   |   |   |   |   |
| Multi-thread | All 10 port together 50 socket (All success)       | QM118L         | sender      |        | 379152391                  | 376557562               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_10_192.168.5.21_to_192.168.5.31_2025-03-15_04-39-16.json            |   |   |   |   |   |   |   |
| Multi-thread | All 10 port together 10 socket (All success)       | QM118L         | receiver    |        | 299996443                  | 298521793               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_10_10_sockets_192.168.5.32_to_192.168.5.22_2025-03-15_03-53-50.json |   |   |   |   |   |   |   |
| TCP          | All 10 port together                               | QM118L         | receiver    |        | 276677160                  | 276393668               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_10_192.168.5.31_to_192.168.5.21_2025-03-14_18-36-55.json                    |   |   |   |   |   |   |   |
| TCP          | All 10 port together                               | QM118L         | sender      |        | 79672829                   | 79576719                | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_10_192.168.5.26_to_192.168.5.36_2025-03-15_04-14-39.json                    |   |   |   |   |   |   |   |
| TCP          | 1 SPF                                              | QM118L         | receiver    |        | 948155569                  | 947558884               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_1_192.168.5.39_to_192.168.5.29_2025-03-14_18-04-54.json                     |   |   |   |   |   |   |   |
| UDP          | RG45, 1G target                                    | QM118L         | receiver    |        | 722858966                  | 722107379               | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_1_192.168.5.31_to_192.168.5.21_2025-03-14_18-46-59.json                     |   |   |   |   |   |   |   |
| UDP          | ALL 10 port, 1G target 46% lost                    | QM118L         | receiver    |        | 567436750                  | 2915070                 | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_10_192.168.5.40_to_192.168.5.30_2025-03-14_18-49-37.json                    |   |   |   |   |   |   |   |
| UDP          | ALL 10 port, 1G target 16% lost                    | QM118L         | sender      |        | 193859760                  | 161544198               | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_10_192.168.5.26_to_192.168.5.36_2025-03-15_04-35-00.json                    |   |   |   |   |   |   |   |
| UDP          | ALL 10 port, 100M targer 0% lost                   | QM118L         | sender      |        | 99983565                   | 99983377                | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_10_192.168.5.21_to_192.168.5.31_2025-03-15_05-01-25.json                    |   |   |   |   |   |   |   |
| UDP          | ALL 10 port, 10M target 0% lost                    | QM118L         | receiver    |        | 9998016                    | 9996735                 | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_10_192.168.5.40_to_192.168.5.30_2025-03-15_03-22-14.json                    |   |   |   |   |   |   |   |
| UDP          | ALL 10 port, 100M targer 26% lost                  | QM118L         | receiver    |        | 99981304                   | 77222310                | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_10_192.168.5.40_to_192.168.5.30_2025-03-15_03-24-53.json                    |   |   |   |   |   |   |   |
|              |                                                    |                |             |        |                            |                         |                                                                                                                                         |   |   |   |   |   |   |   |
| two-way test | RG45                                               | J19EB6L        | sender      |        | 945544000                  | 945526000               | https://github.com/gandibin/iperf3/tree/main/log/bidirectional_thread_1_192.168.5.21_to_192.168.5.31_2025-03-13_11-36-38.txt            |   |   |   |   |   |   |   |
| two-way test | ALL 6 port                                         | J19EB6L        | sender      |        | 388503663                  | 388501760               | https://github.com/gandibin/iperf3/tree/main/log/bidirectional_thread_6_192.168.5.31_to_192.168.5.21_2025-03-13_20-42-17.txt            |   |   |   |   |   |   |   |
| Multi-thread | 1 RJ45, 100 socket all ok                          | J19EB6L        | sender      |        | 948111000                  | 947779000               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_1_192.168.5.21_to_192.168.5.31_2025-03-13_11-01-01.json             |   |   |   |   |   |   |   |
| Multi-thread | ALL 6 port 50 socket all ok                        | J19EB6L        | receiver    |        | 434678888                  | 432531513               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_6_192.168.5.31_to_192.168.5.21_2025-03-13_15-02-19.json             |   |   |   |   |   |   |   |
| Multi-thread | ALL 6 port 100 socket all ok                       | J19EB6L        | sender      |        | 453792000                  | 453566000               | https://github.com/gandibin/iperf3/tree/main/log/multithread_thread_6_192.168.5.21_to_192.168.5.31_2025-03-13_11-12-47.json             |   |   |   |   |   |   |   |
| TCP          | 1 port                                             | J19EB6L        | sender      |        | 941756000                  | 941739000               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_1_192.168.5.21_to_192.168.5.31_2025-03-13_10-33-34.json                     |   |   |   |   |   |   |   |
| TCP          | 1 port                                             | J19EB6L        | receiver    |        | 943902142                  | 943894985               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_1_192.168.5.31_to_192.168.5.21_2025-03-13_12-20-38.json                     |   |   |   |   |   |   |   |
| TCP          | ALL 6 port                                         | J19EB6L        | sender      |        | 439950000                  | 436930000               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_6_192.168.5.23_to_192.168.5.33_2025-03-13_11-14-24.json                     |   |   |   |   |   |   |   |
| TCP          | ALL 6 port                                         | J19EB6L        | receiver    |        | 397935037                  | 397930303               | https://github.com/gandibin/iperf3/tree/main/log/TCP_thread_6_192.168.5.33_to_192.168.5.23_2025-03-13_12-30-13.json                     |   |   |   |   |   |   |   |
| UDP          | 1 port  0% lost                                    | J19EB6L        | receiver    |        | 771413125                  | 23506639                | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_1_192.168.5.21_to_192.168.5.31_2025-02-20_01-19-41.json                     |   |   |   |   |   |   |   |
| UDP          | ALL PORT                                           | J19EB6L        | sender      |        | 117755000                  | 117755000               | https://github.com/gandibin/iperf3/tree/main/log/UDP_thread_6_192.168.5.26_to_192.168.5.36_2025-02-20_01-06-47.json                     |   |   |   |   |   |   |   |


