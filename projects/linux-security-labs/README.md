# Linux Security Administration & Monitoring Lab

This portfolio project consolidates several related university Linux activities into one security-focused case study.

The original exercises were completed separately, but they all support the same practical objective: learning how to administer, monitor and investigate a Linux environment from a cybersecurity perspective.

## Project flow

```text
Linux infrastructure setup
        ↓
System administration
        ↓
Users and access control
        ↓
Monitoring and automation
        ↓
Log and process analysis
        ↓
Basic security investigation
```

## Phase 1 — Infrastructure, Administration & Monitoring

[View phase](./linux-infrastructure-monitoring/)

This phase covers the Linux environment and day-to-day administration tasks used as the foundation for the project.

**Work included:**

- Three Ubuntu virtual machines
- Static IPv4 configuration with Netplan
- Connectivity testing
- Linux CLI and file management
- Process and memory monitoring
- Network and service inspection
- Cron-based monitoring automation
- Users and groups
- Proposed Netdata → Prometheus → Grafana monitoring architecture

> The Netdata, Prometheus and Grafana section is a proposed architecture from the academic project, not a completed deployment.

## Phase 2 — Identity & Access Management

[View phase](./linux-user-access-management/)

This phase focuses on account management, privileges and traceability.

**Work included:**

- User creation and removal
- `/etc/passwd` and `/etc/group` review
- Group membership
- `su` and `sudo`
- Session review with `who` and `w`
- Password aging with `chage`
- Account cleanup

## Phase 3 — System Diagnosis & Log Analysis

[View phase](./linux-system-diagnosis/)

This phase applies Linux administration knowledge to troubleshooting and basic investigation.

**Work included:**

- `auth.log`, `kern.log` and `dmesg` review
- Failed authentication analysis
- Process inspection with `ps`
- Real-time monitoring with `top`
- Memory review with `free`
- Evaluation of kernel and virtualization warnings
- Evidence-based conclusions instead of assuming the cause of an issue

## Security relevance

The project connects Linux fundamentals with tasks that are useful in Blue Team and SOC work:

- account and privilege review
- active-session auditing
- log analysis
- process inspection
- service and port inspection
- system health monitoring
- troubleshooting
- basic incident investigation

## Tools and commands

`Ubuntu` · `Netplan` · `sudo` · `su` · `chage` · `who` · `w` · `ps` · `top` · `free` · `dmesg` · `grep` · `find` · `ss` · `cron`

## Project context

The material comes from university Linux and operating-system activities and has been reorganized here as one portfolio case study. Screenshots and findings remain based on the original exercises; the portfolio structure does not imply that every activity was executed as one continuous lab environment.
