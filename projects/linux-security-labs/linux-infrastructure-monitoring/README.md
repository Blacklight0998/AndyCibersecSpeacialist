# Phase 1 — Linux Infrastructure, Administration & Monitoring

This is the first part of the larger [Linux Security Administration & Monitoring Lab](../).

For this university activity we worked with three Linux virtual machines on the same network. I used this part of the project to practice the basic administration work I would need before doing anything more security-focused.

## What I worked on

- cloning and using Linux VMs
- static IPv4 configuration with Netplan
- connectivity testing with `ping`
- Linux file and directory management
- pipes, redirection, `grep`, `find` and regular expressions
- process and memory monitoring
- user and group administration
- listening-port/service inspection with `ss -tunlp`
- hourly monitoring with `cron`

More detailed notes:

- [Virtualization and Networking](./virtualization-and-networking.md)
- [Linux Administration](./linux-administration.md)
- [Monitoring and Automation](./monitoring-and-automation.md)
- [Users, Groups and Network Inspection](./users-groups-network.md)
- [Proposed Observability Stack](./observability-stack.md)

## Monitoring proposal

The academic project also included a design using Netdata, Prometheus and Grafana. I did not deploy that full stack, so I keep it documented as a proposed architecture rather than presenting it as completed work.

That distinction matters to me because I want the portfolio to show what I actually configured versus what I only researched or designed.

## What I learned

This activity gave me a better foundation for later Linux security work. Commands for users, processes, networking and logs make more sense when I have already used them to manage a system instead of only memorizing them for an exam.
