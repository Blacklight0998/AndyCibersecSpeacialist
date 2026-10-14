# Connectivity and Performance Tests

## Objective

The connectivity tests were performed to validate communication between the local host, the default gateway, public Internet destinations and DNS-resolved domains.

## Default Gateway Test

A `ping` test was performed against the local router at `192.168.1.1`.

Purpose:

- Verify that the local wireless interface was working
- Confirm Layer 3 communication with the gateway
- Check for packet loss inside the local network

Result:

The gateway responded successfully, confirming local connectivity between the assessed computer and the router.

## Internet Connectivity Test

A second `ping` test targeted the public IP address `8.8.8.8`.

Purpose:

- Confirm routing beyond the local network
- Verify that the router was forwarding traffic toward the Internet
- Distinguish local connectivity problems from DNS problems

Result:

The public destination responded, confirming external IP connectivity.

## DNS Resolution Test

A third test used `ping google.com`.

Purpose:

- Validate domain-name resolution
- Confirm that DNS services were functioning
- Verify end-to-end connectivity using a hostname instead of an IP address

Result:

The domain resolved successfully and returned replies.

## Route Analysis

The Windows `tracert` command was used to observe the path from the local computer toward a Google destination.

Observed behavior:

- The first hop was the local default gateway
- Later hops belonged to the ISP path
- Some intermediate hops did not answer ICMP requests
- The final destination was still reached successfully

The timeouts on intermediate hops were not treated as proof of failure because routers may be configured not to respond to traceroute probes.

## Bandwidth Test

A Speedtest measurement reported approximately:

- **Download:** 155.20 Mbps
- **Upload:** 157.18 Mbps
- **Latency:** 4 ms

The measured throughput was consistent with the documented 150 Mbps residential service and showed no obvious performance limitation during the test period.

## Operational Observation

No QoS prioritization was identified in the analyzed network. The original project noted that QoS could be considered in the future for latency-sensitive services such as video calls, online classes or gaming when multiple devices compete for bandwidth.

## Skills Demonstrated

- `ping`
- `tracert`
- Default gateway validation
- DNS troubleshooting
- Basic routing analysis
- Network performance testing
- Interpreting latency and throughput
