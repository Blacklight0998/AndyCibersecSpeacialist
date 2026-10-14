# Proposed Observability Stack

## Status

This section of the academic project was a **design and research proposal**. The documentation did not demonstrate a full production deployment of the complete stack, so this portfolio version keeps that distinction explicit.

## Proposed Architecture

```text
Server 1
├── Netdata
├── Prometheus
└── Grafana

Server 2
└── Netdata

Server 3
└── Netdata

Netdata agents
      ↓
Prometheus
      ↓
Grafana
```

## Netdata

The proposal places a Netdata agent on each of the three Ubuntu servers to collect system metrics such as CPU, memory, disk, processes and network activity.

Netdata would expose metrics over TCP port `19999` and could provide Prometheus-compatible metrics through its API.

## Prometheus

Prometheus would run on the primary server and scrape metrics from each Netdata agent.

The academic design proposed a 15-second scrape interval and three static Netdata targets.

## Grafana

Grafana would use Prometheus as its data source and provide centralized dashboards for:

- CPU utilization
- Memory usage
- Disk usage
- Network traffic
- Server availability

## Proposed Alert Thresholds

| Resource | Threshold | Duration | Purpose |
|---|---:|---:|---|
| CPU | > 80% | 5 min | Sustained high load |
| Memory | > 85% | 5 min | Low available memory |
| Disk | > 90% | 10 min | Storage capacity risk |
| Availability | `up = 0` | 2 min | Monitoring target unavailable |

## Security Considerations

The academic design notes that monitoring interfaces and ports should not be exposed unnecessarily to the Internet. Access to monitoring services should be restricted to systems and networks that require it.

## Next Step

A future portfolio upgrade would be to actually deploy this stack in the three-VM lab, collect metrics, build dashboards and trigger a controlled alert. That would convert this architecture from a documented proposal into a fully implemented monitoring project.
