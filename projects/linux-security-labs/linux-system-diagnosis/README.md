# Linux System Diagnosis & Log Analysis

This lab came from a university simulation focused on diagnosing an Ubuntu system and reviewing possible security or performance issues.

## What I worked on

- Reviewing `auth.log`, `kern.log` and `dmesg`
- Checking failed authentication attempts
- Reviewing kernel warnings in a virtualized environment
- Inspecting running processes with `ps`
- Monitoring CPU and processes with `top`
- Reviewing memory usage with `free`
- Writing basic conclusions from the evidence collected

## Main findings

During the activity I found failed authentication attempts in `auth.log`, but they did not appear to be the cause of the simulated performance issue.

Kernel messages included warnings related to WSL2 and Hyper-V. These were treated as virtualization-related messages instead of assuming they were a system failure.

The process and memory checks did not show abnormal resource consumption. CPU usage was low and the system had a large amount of available memory.

## Why this matters for security

The lab helped me practice checking logs and system activity before making assumptions about an incident. It also showed me how commands such as `ps`, `top`, `free` and `dmesg` can support troubleshooting and basic investigation.

## Evidence

The original activity includes terminal screenshots from the Ubuntu environment. For the portfolio I keep only selected screenshots with personal system identifiers removed.

Screenshots will be stored in the `screenshots` folder.

## Project context

This was completed as part of the Basic Operating Systems course at Universidad Fidélitas. This portfolio version focuses only on the technical work and evidence.
