# Phase 1 — Linux Infrastructure, Administration & Monitoring

This section is part of the broader [Linux Security Administration & Monitoring Lab](../).

It documents the infrastructure and administration foundation used to practice Linux skills with security relevance.

## Overview

For this academic project we used three Linux virtual machines configured on the same network. The practical work included VM cloning, static IP configuration with Netplan, connectivity validation, Linux command-line administration, users and groups, system monitoring, scheduled tasks and network/service inspection.

The final section also proposed a centralized monitoring architecture using Netdata, Prometheus and Grafana. That observability stack is documented here as a **proposed architecture**, not as a completed deployment.

Personal information from the original academic document is intentionally omitted.

## Technical sections

- [Virtualization and Networking](./virtualization-and-networking.md)
- [Linux Administration](./linux-administration.md)
- [Monitoring and Automation](./monitoring-and-automation.md)
- [Users, Groups and Network Inspection](./users-groups-network.md)
- [Proposed Observability Stack](./observability-stack.md)

## Skills practiced

- Linux virtual machine administration
- Static IPv4 configuration with Netplan
- Connectivity testing with `ping`
- File and directory management
- Pipes and I/O redirection
- `grep`, regular expressions and `find`
- Process and memory monitoring
- Scheduled monitoring with `cron`
- User and group administration
- Network inspection with `ip a` and `ss -tunlp`
- Basic infrastructure monitoring concepts
- Prometheus/Grafana architecture planning

## Progression

```text
3 Ubuntu VMs
     ↓
Static networking with Netplan
     ↓
Linux administration fundamentals
     ↓
Process / memory / kernel monitoring
     ↓
Cron-based monitoring automation
     ↓
Users, groups and open-port inspection
     ↓
Proposed centralized observability
Netdata → Prometheus → Grafana
```
