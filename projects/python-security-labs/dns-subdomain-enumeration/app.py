import dns.resolver


def enumerate_subdomains(domain, wordlist, dns_server):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]

    with open(wordlist, "r", encoding="utf-8") as wordlist_file:
        for line in wordlist_file:
            subdomain = line.strip()
            target = f"{subdomain}.{domain}"

            try:
                results = resolver.resolve(target, "A")
                for result in results:
                    print(f"{target} {result}")

            except (
                dns.resolver.NXDOMAIN,
                dns.resolver.NoAnswer,
                dns.resolver.NoNameservers,
                dns.resolver.LifetimeTimeout,
            ):
                print(f"{target} not found")


if __name__ == "__main__":
    enumerate_subdomains(
        domain="google.com",
        wordlist="wordlist.txt",
        dns_server="8.8.8.8",
    )
