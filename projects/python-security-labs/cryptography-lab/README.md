# AES-EAX Cryptography Lab

Small Python lab used to practice authenticated encryption with AES-EAX.

This section keeps two related exercises together because both focus on the same cryptography concepts rather than on reconnaissance or SOC workflows.

## Exercises

### AES-EAX Login Demo

Practices:

- Secure random password generation with `secrets`
- AES-128 encryption
- AES-EAX authenticated encryption
- Nonce handling
- Authentication tags
- Basic integrity verification

### AES-EAX CTF Challenge

Practices:

- UTF-8 encoding before encryption
- Random AES key generation
- Encryption and decryption
- Nonce handling
- Integrity verification
- Basic exception handling

## What I learned

These exercises helped me understand the difference between confidentiality and integrity and how authenticated encryption can provide both in the same operation.

> These are educational exercises. Real password storage should normally use a secure password-hashing algorithm instead of reversible encryption.
