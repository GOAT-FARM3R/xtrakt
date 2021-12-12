wrapper script for tldextract and urlparse in one place that can be used with pipes.

# usage

got a list of domains and you want to do the following:

get all the tlds:

```
cat domains.lst | xtrakt tld
```

get all the names of domains:

```
cat domains.lst | xtrakt domain
```

 
if you got a list of hostnames with their domains and want to get just the hostname:

```
cat hosts.lst | xtrakt subdomain
```

if you got a lit of urls from either burp/gau/etc and want hosts:

```
cat urls.lst | xtrakt fqdn
```
