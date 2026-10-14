# 🏠 Home Network Security & Traffic Analysis

University group project adapted for a cybersecurity portfolio.

## Overview

This project documents the assessment of a residential network with the objective of understanding its infrastructure, validating connectivity, reviewing wireless security, analyzing network traffic and identifying potential security weaknesses.

The original academic project included network design, subnetting, device configuration, connectivity validation, security analysis, bandwidth testing, redundancy analysis, vulnerability identification and a logical/physical topology.

## Environment

The analyzed environment included:

- Fiber Internet connection
- Wireless router with DHCP
- Laptop
- Mobile devices
- Smart TV / set-top box
- IoT smart speaker

All identifying details from the original household have been intentionally omitted from this portfolio version.

## Tools and Techniques

- Wireshark
- `ipconfig`
- `ping`
- `tracert`
- Speedtest
- Cisco Packet Tracer
- IPv4 addressing analysis
- DHCP analysis
- Wireless security review

## Connectivity Validation

The project validated:

- Communication with the default gateway
- Internet connectivity using a public IP address
- DNS resolution using a domain name
- Route visibility using `tracert`

These tests were used to confirm local connectivity, routing to the Internet and DNS functionality.

## Wireless Security Review

The analyzed network used:

- WPA2-Personal authentication
- CCMP encryption
- 5 GHz Wi-Fi
- IEEE 802.11ac

The project also recommended using strong credentials, maintaining router firmware and disabling unused features such as WPS when possible.

## Traffic Analysis with Wireshark

Wireshark was used to inspect traffic patterns and identify common protocols.

Observed protocols included:

- TCP
- TLS 1.2
- SSDP
- IGMP
- ICMPv6

The capture showed behavior consistent with normal residential traffic. No obvious malicious traffic was identified during the analyzed capture period.

## Security Findings

### 1. Lack of Network Segmentation

All devices were connected to the same local network.

**Risk:** If an IoT or user device were compromised, it could potentially communicate with other devices on the same LAN.

**Recommendation:** Place IoT and less-trusted devices on a separate guest network or VLAN when the network equipment supports it.

### 2. Single Point of Failure

The network depended on a single router and Internet connection.

**Risk:** A router or ISP outage would affect every device in the household.

**Recommendation:** Maintain an alternative connectivity method such as mobile tethering for temporary redundancy.

### 3. Router and Wireless Security

Potential risks include outdated firmware, weak credentials and unnecessary services.

**Recommendations:**

- Keep router firmware updated
- Use a strong Wi-Fi password
- Disable WPS if it is not required
- Review connected devices periodically
- Use WPA3 if supported in a future upgrade

## Performance Review

A network speed test showed performance consistent with the contracted residential service, with low latency and upload/download throughput sufficient for common household activities.

QoS was identified as a possible future improvement for prioritizing latency-sensitive applications such as video calls or online classes.

## Network Topology

The physical topology followed a simple residential star-style design where the Internet connection reached the main router and the router distributed connectivity to endpoints such as laptops, smartphones, IoT devices and multimedia equipment.

## Key Lessons

This project helped reinforce practical concepts including:

- IPv4 addressing
- DHCP
- Default gateways
- DNS
- Wireless security
- Network troubleshooting
- Packet analysis
- Network segmentation
- Availability and redundancy
- Basic vulnerability assessment

## Project Context

This was a university group project completed for a networking course. This portfolio version focuses on the technical and cybersecurity-related aspects of the work and intentionally removes household-specific personal information.

## Portfolio Note

The complete original academic report is not published here because it contains personal names and identifiable network details from a real residential environment. This sanitized documentation preserves the technical analysis while reducing unnecessary exposure of private information.
