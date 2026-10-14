# 🐍 Python Security Labs

Small Python exercises adapted to cybersecurity concepts and defensive security practice.

## Projects

### 🔐 AES-EAX Login Demo

A basic authentication lab that demonstrates:

- Secure random password generation with `secrets`
- AES-128 encryption
- AES-EAX authenticated encryption
- Nonce usage
- Authentication tags for integrity verification
- Basic login validation

[View `parte1_login.py`](./parte1_login.py)

> Educational note: real-world password storage should normally use secure password hashing rather than reversible encryption.

---

### 🌐 Scapy TCP SYN Port Scanner

A localhost network-scanning exercise that demonstrates:

- Packet creation with Scapy
- IPv4 and TCP packet construction
- TCP SYN scanning
- SYN-ACK interpretation for open ports
- RST-ACK interpretation for closed ports
- Basic network reconnaissance concepts

The script is configured to scan `127.0.0.1`, keeping the exercise focused on the local host.

[View `parte2_scapy.py`](./parte2_scapy.py)

---

## Technologies

- Python
- PyCryptodome
- Scapy
- TCP/IP
- AES-EAX

## Purpose

These labs document my progression in Python while applying university programming concepts to cybersecurity use cases.
