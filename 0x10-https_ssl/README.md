Tasks
-----

 Done?\
Help

#### 0\. HTTPS ABC 

As for project [0x07](https://intranet.hbtn.io/rltoken/xusoLfeQ9T4J9WiojuZsVA "0x07"), use numbers in your answer file.

What is HTTPS?

1.  A secure version of HTTP
2.  A faster version of HTTP
3.  A superior version of HTTP

Why do you need HTTPS?

1.  To encrypt credit card and social security number information going between the client and the website servers
2.  To encrypt all communication between the client and the website servers
3.  To accelerate the communication between the client and the website servers

You want to setup HTTPS on your website, where shall you place the certificate?

1.  In a secure location where nobody can access it
2.  You can host it anywhere but you have to share the link to it on your website
3.  On your website web server(s)

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x10-https_ssl`
-   File: `0-https_abc`

Check your code?

 Done?\
Help

#### 1\. World wide web 

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let's also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

-   Add the subdomain `www` to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
-   Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
-   Add the subdomain `web-01` to your domain, point it to your `web-01` IP
-   Add the subdomain `web-02` to your domain, point it to your `web-02` IP
-   Your Bash script must accept 2 arguments:
    1.  `domain`:
        -   type: string
        -   what: domain name to audit
        -   mandatory: yes
    2.  `subdomain`:
        -   type: string
        -   what: specific subdomain to audit
        -   mandatory: no
-   Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
-   When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
-   When passing `domain` and `subdomain` parameters, display information for the specified subdomain-   Ignore `shellcheck` case `SC2086`
-   Must use:
    -   `awk`
    -   at least one Bash function
-   You do not need to handle edge cases such as:
    -   Empty parameters
    -   Nonexistent domain names
    -   Nonexistent subdomains

Example:

```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x10-https_ssl`
-   File: `1-world_wide_web`

Check your code?Get a container

 Done?\
Help

#### 2\. HAproxy SSL termination 
"Terminating SSL on HAproxy" means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

Requirements:

-   HAproxy must be listening on port TCP 443
-   HAproxy must be accepting SSL traffic
-   HAproxy must serve encrypted traffic that will return the `/` of your web server
-   When querying the root of your domain name, the page returned must contain `Holberton School`
-   Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `2-haproxy_ssl_termination` must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, [SSL termination](https://intranet.hbtn.io/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q "SSL termination") is not available before v1.5.

Example:

```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.onlineHolberton School for the win!
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x10-https_ssl`
-   File: `2-haproxy_ssl_termination`

Check your code?Get a container

[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/276/unlock_optionals))
