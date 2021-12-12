from urllib.parse import urlparse

import tldextract
import sys
import click


@click.group()
def cli():
    pass


@cli.command()
def domain():
    for domain in sys.stdin:
        print(f"{tldextract.extract(domain).domain}")


@cli.command()
def tld():
    for tld in sys.stdin:
        print(f"{tldextract.extract(tld).suffix}")


@cli.command()
def subdomain():
    for subdomain in sys.stdin:
        print(f"{tldextract.extract(subdomain).subdomain}")


@cli.command()
def fqdn():
    for url in map(str.rstrip, sys.stdin):
        parsed_uri = urlparse(url)

        if parsed_uri.hostname is None:
            continue

        print(parsed_uri.hostname)




