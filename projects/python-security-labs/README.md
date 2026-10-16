# Python Security Projects

This section is where I keep the Python work that is most relevant to cybersecurity.

I started with small exercises from class and then tried to organize them in a way that makes technical sense instead of listing every script as a separate project.

## Python Network Reconnaissance Tool

[View project](./python-network-reconnaissance-tool/)

This is the main Python project in the portfolio right now.

It grew from two earlier exercises: a DNS enumeration script and a Scapy TCP SYN scanner. Since both are part of the same discovery process, I combined them into one workflow and added JSON reporting.

```text
Target domain
    |
    v
DNS enumeration
    |
    v
Resolved IP addresses
    |
    v
TCP port scanning
    |
    v
JSON report
```

What I am practicing here:

- Python structure and functions
- DNS resolution
- TCP/IP and TCP flags
- Scapy
- dnspython
- Wordlist-based enumeration
- Error handling
- JSON output

## AES-EAX Cryptography Lab

[View lab](./cryptography-lab/)

This stays separate because it has a different purpose. The two exercises in this folder were made to understand AES-EAX, nonces, authentication tags and integrity verification.

I do not consider it a full cryptography project; it is a small learning lab that I kept because it shows another way I have used Python in security-related coursework.

> Network testing in this repository is intended only for systems I own or have explicit permission to test.
