# Packet Tracer VLSM Network Lab

University networking practice made in Cisco Packet Tracer.

The goal of this lab was to take the network `10.10.0.0/21` and divide it using VLSM for several LANs with different host requirements. The topology uses 3 routers connected with point-to-point links.

## What I worked on

- VLSM subnetting
- IPv4 addressing
- /24, /25, /26 and /30 networks
- Router interface addressing
- Point-to-point links
- Cisco Packet Tracer
- Connectivity testing

## Topology

The lab contains 3 routers. Each router manages two LANs:

- Router 1: Subnet A and B
- Router 2: Subnet C and D
- Router 3: Subnet E and F

The routers are also connected to each other using three point-to-point networks.

## Main network

`10.10.0.0/21`

The subnets were assigned from largest to smallest to avoid wasting address space.

| Network | Hosts needed | Network | Prefix |
|---|---:|---|---:|
| A | 240 | 10.10.0.0 | /24 |
| B | 192 | 10.10.1.0 | /24 |
| C | 150 | 10.10.2.0 | /24 |
| D | 120 | 10.10.3.0 | /25 |
| E | 85 | 10.10.3.128 | /25 |
| F | 40 | 10.10.4.0 | /26 |
| R1-R2 | 2 | 10.10.4.64 | /30 |
| R2-R3 | 2 | 10.10.4.68 | /30 |
| R1-R3 | 2 | 10.10.4.72 | /30 |

More details: [Subnetting plan](./subnetting-plan.md)

## Router addressing

The routers were configured with the first usable addresses for the LANs and addresses from the /30 networks for the serial links.

[View router addressing](./router-addressing.md)

## Testing

After configuring the topology, connectivity was tested between PCs and their gateways and between routers.

[View testing notes](./testing.md)

## Evidence

The original project includes Packet Tracer screenshots showing the topology, interface configuration, routing information and connectivity tests.

A small set of screenshots is kept in the `screenshots` folder instead of uploading the complete university report.

## What I learned

This practice helped me understand why VLSM is useful when networks need different amounts of addresses. It also helped me practice how subnetting connects with the actual router configuration instead of only calculating networks on paper.

## Project context

This was completed as a university group activity for the Principles of Networks and Communications course. This portfolio version only keeps the networking work and technical evidence.
