# Network Architecture

## Environment Summary

The assessed residential network used a fiber Internet connection connected to a single wireless router that provided routing, switching, Wi-Fi access and DHCP services.

The documented environment included:

- 1 wireless router
- 1 laptop
- 3 mobile devices
- 1 smart TV / set-top box
- 1 IoT smart speaker

The network used a single local IPv4 segment with a /24 subnet mask. The assessed laptop received an address in the `192.168.1.0/24` network and used `192.168.1.1` as the default gateway.

## Simplified Physical Topology

```text
Internet
   |
Fiber ISP
   |
Main Router / DHCP / Wi-Fi
   |
   +-- Laptop
   +-- Smartphone
   +-- Smartphone
   +-- Smartphone
   +-- Smart Speaker / IoT
   +-- Smart TV / Set-top Box
```

## Addressing and DHCP

The router provided dynamic addressing through DHCP. This simplified device onboarding and reduced the need for manual IPv4 configuration.

Observed network characteristics included:

- Private IPv4 addressing
- `/24` subnet mask (`255.255.255.0`)
- Dynamic host configuration through DHCP
- A single default gateway for Internet access

## Security Perspective

All endpoints were located on the same local network segment. From a security perspective, this increases the amount of direct communication possible between trusted user devices and less-trusted IoT devices.

A stronger design would separate IoT and multimedia devices from trusted endpoints using a guest network or VLAN when supported by the network equipment.

## Improved Logical Design

```text
Internet
   |
Router / Firewall
   |
   +-- Trusted Network
   |     +-- Laptop
   |     +-- Smartphones
   |
   +-- IoT / Guest Network
         +-- Smart Speaker
         +-- Smart TV / Set-top Box
```

This separation would reduce the impact of a compromise on an IoT or multimedia device and limit lateral communication between device groups.
