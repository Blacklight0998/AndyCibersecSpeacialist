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

[View `aes_eax_login_demo.py`](./aes_eax_login_demo.py)

> Educational note: real-world password storage should normally use secure password hashing rather than reversible encryption.

---

### 🚩 AES-EAX CTF Challenge

A small capture-the-flag style exercise focused on encrypting and recovering a secret message using AES-EAX.

It demonstrates:

- UTF-8 encoding before encryption
- Random AES-128 key generation
- AES-EAX authenticated encryption
- Nonce handling
- Integrity verification using an authentication tag
- Exception handling when verification fails
- Recovery of a CTF-style flag after successful decryption

[View `aes_eax_ctf_challenge.py`](./aes_eax_ctf_challenge.py)

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

[View `scapy_syn_port_scanner.py`](./scapy_syn_port_scanner.py)

---

## Technologies

- Python
- PyCryptodome
- Scapy
- TCP/IP
- AES-EAX

## Purpose

These labs document my progression in Python while applying university programming concepts to cybersecurity use cases.
