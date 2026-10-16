# Azure Red Team vs Blue Team Lab

**Status: In progress**

This is a university group project currently being developed as part of my Cybersecurity Engineering degree.

The lab is designed around an Azure environment where one side acts as Red Team and the other as Blue Team. The goal is to practice both attack simulation and defensive monitoring in a controlled environment while using Python to automate part of the work.

## Project goal

The project requires a realistic lab in Microsoft Azure with one or more virtual machines that can be attacked, monitored and hardened. Red Team activities are performed only inside the authorized lab environment, while the Blue Team is responsible for system hardening, monitoring, logging and defensive response.

The academic brief includes Python-based tooling for scanning, packet analysis, authentication testing, operating-system auditing, logging and automated defensive actions.

## Planned workflow

```text
Azure lab environment
        |
        v
Red Team reconnaissance and attack simulation
        |
        v
Blue Team monitoring and detection
        |
        v
Hardening / defensive response
        |
        v
Evidence and final report
```

## Red Team side

The Red Team portion is expected to include controlled exercises such as:

- Network and service discovery with Nmap
- Python automation around scanning results
- Packet analysis and traffic manipulation practice with Scapy
- Controlled SSH dictionary testing inside the lab
- ARP spoofing in a same-network lab scenario
- Documentation of findings and weaknesses

## Blue Team side

The Blue Team portion is expected to include:

- Azure VM hardening
- User, service and operating-system auditing
- Review of open ports and running services
- Monitoring of authentication and system logs
- Packet monitoring with Scapy
- Simple detection rules for suspicious traffic
- Firewall hardening with UFW or iptables
- Security event logging
- Automated defensive actions where appropriate

## Technologies included in the project brief

- Microsoft Azure
- Linux or Windows virtual machines
- Azure Network Security Groups (NSG)
- Python 3
- Nmap / python-nmap
- Scapy
- Paramiko
- Linux logging and system tools
- UFW / iptables
- Azure Monitor / Logs (optional in the academic brief)

## Planned project structure

```text
azure-red-blue-team-lab/
├── red-team/
│   ├── scanner.py
│   ├── packet-testing.py
│   ├── ssh-auth-testing.py
│   └── findings.md
├── blue-team/
│   ├── os-audit.py
│   ├── traffic-monitor.py
│   ├── firewall-hardening.sh
│   └── alert-logger.py
├── architecture/
├── screenshots/
└── README.md
```

This structure is a portfolio adaptation of the university requirements. I will only add files and capabilities here as they are actually implemented and tested.

## What I want this project to show

I want this lab to connect several areas I am studying instead of treating them as separate exercises:

- Cloud infrastructure
- Networking
- Python automation
- Red Team fundamentals
- Blue Team monitoring
- Linux administration
- Security logging
- Incident response
- Technical documentation

## Current state

The project is still under development. I am currently treating this section as documentation of the work in progress rather than presenting planned features as completed.

As the lab develops, I plan to add architecture diagrams, screenshots, scripts, findings and a clearer description of my own contribution to the group work.

> All offensive testing in this project is intended only for the authorized university lab environment.
