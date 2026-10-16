# Blacklight Security Analyzer

Python project focused on basic reconnaissance and security assessment in authorized lab environments.

The idea of this project is to combine DNS enumeration, TCP port scanning and simple reporting into one workflow instead of keeping each exercise as a separate script.

## Workflow

```text
Target domain
    |
    v
DNS enumeration
    |
    v
Resolved hosts / IP addresses
    |
    v
TCP port scan
    |
    v
JSON report
```

## What it does

1. Reads possible subdomains from a wordlist.
2. Resolves DNS `A` records using a configurable DNS server.
3. Collects the IP addresses found during enumeration.
4. Scans a selected list of TCP ports against the discovered hosts.
5. Saves the results in a JSON report for later review.

## Why I built it this way

The first versions of these exercises were separate university labs: a DNS enumeration script and a TCP SYN scanner. I combined them into one project because they belong to the same reconnaissance workflow and can produce one set of findings.

This project is also a way for me to practice moving from small scripts into a more organized Python security tool.

## Structure

```text
blacklight-security-analyzer/
├── main.py
├── modules/
│   ├── dns_enum.py
│   ├── port_scan.py
│   └── reporting.py
├── data/
│   └── subdomains.txt
├── reports/
└── requirements.txt
```

## Skills practiced

- Python
- DNS resolution
- DNS `A` records
- Wordlist-based enumeration
- TCP SYN scanning
- Scapy
- Basic reconnaissance
- Error handling
- JSON reporting
- Modular Python structure

## Notes

The port scanner is based on the TCP SYN exercise I previously created with Scapy. The DNS module comes from a university exercise where I changed the resolver, expanded the wordlist and added better error handling while troubleshooting the script.

This is a learning project, not a production security scanner.

> Use only against systems you own or have explicit permission to test.
