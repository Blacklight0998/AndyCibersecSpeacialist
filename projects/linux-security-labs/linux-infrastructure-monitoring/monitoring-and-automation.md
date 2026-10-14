# Monitoring and Automation

## Implemented Monitoring Tasks

The project used standard Linux tools to inspect system health and activity:

- `dmesg` for recent kernel/system messages
- `ps aux` for running processes
- `top` for real-time CPU/process monitoring
- `free -h` for memory usage

## Cron-Based Monitoring

A monitoring script was scheduled with `cron` to run every hour. The script collected information such as CPU usage, memory usage and disk space and wrote the results to a log file.

This introduced the idea of converting manual system checks into repeatable monitoring tasks.

## Cybersecurity Relevance

Periodic system monitoring can support detection of unusual resource consumption, service failures and other operational indicators that may require investigation.

The project later connected this manual monitoring approach with a proposed centralized monitoring architecture using Netdata, Prometheus and Grafana.
