# Python Security Projects

Python work focused on cybersecurity, networking and security automation.

Instead of keeping every exercise as an individual project, I am organizing related work around larger technical goals.

## Main Project

### [Blacklight Security Analyzer](./blacklight-security-analyzer/)

A Python reconnaissance workflow that combines DNS enumeration, TCP port scanning and JSON reporting into one tool.

The project grew from two earlier exercises: a DNS enumeration script and a Scapy TCP SYN scanner. They were combined because both belong to the same discovery workflow and can produce one set of findings.

**Current workflow:**

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
TCP port scanning
    |
    v
JSON report
```

**Skills:** Python · DNS · TCP/IP · Scapy · dnspython · reconnaissance · error handling · JSON reporting

---

## Supporting Lab

### [AES-EAX Cryptography Lab](./cryptography-lab/)

Two related Python exercises used to understand authenticated encryption, nonces, authentication tags and integrity verification with AES-EAX.

I keep these together as a cryptography lab because they support a different learning objective from the reconnaissance project.

**Skills:** Python · AES-128 · AES-EAX · PyCryptodome · secure random generation · integrity verification

---

## Why the projects are organized this way

The goal is not to present every university exercise as a separate portfolio project. Related exercises are combined when they form a logical technical workflow, while unrelated topics remain separate.

This keeps the portfolio easier to review and better reflects how I am progressing from individual scripts to more structured cybersecurity projects.

> Network testing is intended only for systems I own or have explicit permission to test.
