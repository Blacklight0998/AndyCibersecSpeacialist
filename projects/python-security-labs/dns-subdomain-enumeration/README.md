# DNS Subdomain Enumeration Lab

Small Python lab used to practice DNS resolution and basic reconnaissance.

The script reads possible subdomain names from a wordlist and checks their `A` records using a custom DNS resolver.

## What I worked on

The original script was not returning useful results, so during the activity I made a few changes to understand what was happening:

- Changed the resolver to Google DNS (`8.8.8.8`)
- Expanded the wordlist with more common subdomain names
- Added output for failed lookups to make troubleshooting easier
- Tested the modified script and reviewed the DNS results

## Things practiced

- Python file handling
- DNS resolution
- DNS `A` record queries
- Wordlist-based subdomain enumeration
- Basic network reconnaissance
- Troubleshooting
- `dnspython`

## How it works

```text
wordlist
   |
   v
Python script
   |
   v
DNS resolver (8.8.8.8)
   |
   v
subdomain.domain
   |
   +--> A record found
   |
   +--> no result / error
```

## Files

- [`app.py`](./app.py) - DNS enumeration script
- [`wordlist.txt`](./wordlist.txt) - small wordlist used in the exercise
- `screenshots/` - selected execution evidence from the original activity

## What I learned

This exercise helped me connect Python with DNS concepts instead of treating DNS only as theory. I also practiced troubleshooting a script when the first execution did not return the expected information.

## Project context

This was completed as a university programming/networking exercise and adapted for this portfolio.

> Educational use only. DNS enumeration should be performed only against systems you own or are authorized to test.
