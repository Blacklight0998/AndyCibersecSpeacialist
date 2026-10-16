# Python Cybersecurity Toolkit

Collection of small Python security exercises grouped as one project.

I built these modules while practicing how Python can be applied to cybersecurity topics such as cryptography, network reconnaissance and DNS enumeration.

## Modules

| Module | Purpose | Main concepts |
|---|---|---|
| [AES-EAX Login Demo](./crypto/aes_eax_login_demo.py) | Practice authenticated encryption in a login-style exercise | AES-EAX, nonce, authentication tag, secure random generation |
| [AES-EAX CTF Challenge](./crypto/aes_eax_ctf_challenge.py) | Small encryption/decryption challenge | AES-128, integrity verification, encoding |
| [TCP SYN Port Scanner](./network/scapy_syn_port_scanner.py) | Localhost port discovery exercise | Scapy, TCP SYN, SYN-ACK, RST-ACK |
| [DNS Subdomain Enumeration](./network/dns_subdomain_enumeration.py) | Wordlist-based DNS enumeration | DNS, A records, dnspython, troubleshooting |

## Project structure

```text
python-security-labs/
├── README.md
├── crypto/
│   ├── aes_eax_login_demo.py
│   └── aes_eax_ctf_challenge.py
├── network/
│   ├── scapy_syn_port_scanner.py
│   └── dns_subdomain_enumeration.py
├── wordlists/
│   └── subdomains.txt
└── screenshots/
```

## Cryptography practice

The AES exercises were used to understand authenticated encryption and how confidentiality and integrity can be combined.

Things practiced:

- AES-128
- AES-EAX
- Random key generation
- Nonce handling
- Authentication tags
- UTF-8 encoding
- Encryption and decryption

> The login demo is an educational exercise. Real password storage should normally use secure password hashing instead of reversible encryption.

## Network reconnaissance practice

The networking modules focus on basic reconnaissance concepts in controlled environments.

The TCP SYN scanner uses Scapy and is configured to scan `127.0.0.1`.

The DNS module reads possible subdomains from a wordlist and queries DNS `A` records using a custom resolver. During the original activity I changed the resolver to Google DNS (`8.8.8.8`), expanded the wordlist and added error output because the first version was not returning useful results.

Things practiced:

- TCP/IP
- TCP flags
- Scapy packet creation
- DNS resolution
- DNS `A` record queries
- Wordlist-based enumeration
- File handling
- Error handling
- Troubleshooting

## Tools and libraries

- Python
- PyCryptodome
- Scapy
- dnspython

## What I learned

These exercises helped me connect Python programming with security and networking concepts instead of practicing the language only with general programming examples.

They also helped me understand how small scripts can be useful for testing, troubleshooting and learning how protocols behave.

## Safety

The network scripts are intended for educational use in local or authorized environments only.
