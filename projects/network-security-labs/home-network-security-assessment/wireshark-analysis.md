# Wireshark Traffic Analysis

## Objective

Wireshark was used to inspect traffic generated on the residential network and identify the main protocols present during the capture period.

## Observed Protocols

### TCP

TCP was one of the predominant protocols observed in the capture. This was consistent with common residential activities such as web browsing and application traffic that rely on reliable transport.

### TLS 1.2

A significant amount of TLS 1.2 traffic was observed. This indicated that many Internet communications were encrypted in transit rather than being exchanged as plaintext application data.

### SSDP

SSDP traffic was identified in the local network. SSDP is commonly used by smart and multimedia devices for automatic service discovery inside a LAN.

Its presence was consistent with the environment because the network contained IoT and multimedia devices.

### IGMP

IGMP messages were present in the capture. This protocol is associated with management of IPv4 multicast group membership and can appear in networks carrying multimedia or discovery traffic.

### ICMPv6

ICMPv6 traffic was also observed. The project associated this traffic with IPv6 functions such as connectivity and neighbor-related operations.

## Capture Assessment

The analyzed capture showed behavior consistent with normal residential traffic during the observation period.

The project did not identify:

- Clear malicious communication patterns
- Significant communication errors
- Excessive retransmission behavior

The presence of TLS-protected connections was considered a positive observation because much of the Internet traffic was encrypted.

## Security Relevance

The Wireshark portion of the project demonstrates how packet analysis can be used to:

- Identify protocols operating on a network
- Understand normal traffic patterns
- Recognize local discovery and multicast traffic
- Observe the use of encrypted communications
- Establish a baseline for future comparisons

## Important Limitation

This analysis represents only the traffic captured during the project period. The absence of obvious malicious traffic in a limited capture does not prove that a network is free from threats.

## Skills Demonstrated

- Packet capture review
- Protocol identification
- TCP traffic interpretation
- TLS awareness
- Local service discovery analysis
- Multicast protocol awareness
- Basic traffic baselining
