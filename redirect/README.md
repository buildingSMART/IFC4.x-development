# ifc43-docs redirect

Redirects the legacy docs host to the new GitHub Pages location:

| From | To |
| --- | --- |
| `https://ifc43-docs.standards.buildingsmart.org/<anything>` | `https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/<anything>` |

Stack: **Flask** (single redirect route) + **nginx** (TLS termination and proxy) +
**certbot** (automatic Let's Encrypt), orchestrated with **docker compose**.

## Behaviour

- One Flask catch-all route returns `301 Moved Permanently` for every request,
  including paths that would previously have been a `404`.
- Paths and query strings are preserved by default (`PRESERVE_PATH=1`).
- Set `PRESERVE_PATH=0` to send every request straight to `REDIRECT_TARGET`,
  dropping the path entirely.

## Prerequisites

1. DNS: point `ifc43-docs.standards.buildingsmart.org` (A record) at this host.
2. Open inbound TCP ports `80` and `443` (required for the Let's Encrypt
   HTTP-01 challenge and for HTTPS).

## Setup

```sh
cp .env.example .env    # then edit CERTBOT_EMAIL (and DOMAIN if needed)
docker compose up -d --build
docker compose logs -f
```

### First boot

1. nginx starts in *bootstrap* mode (port 80 only, serving the ACME webroot).
2. certbot waits for nginx, then requests the certificate.
3. nginx notices the new certificate and switches to the final config
   (port 80 → HTTPS redirect, port 443 → Flask).

If the certificate request fails (for example DNS is not live yet), certbot
retries automatically.

### Certificate renewal

certbot renews automatically on a 12-hour cycle, and nginx reloads every
6 hours to pick up renewed certificates. No manual action is needed.

## Useful commands

```sh
docker compose up -d --build     # (re)build and start
docker compose logs -f           # tail all logs
docker compose logs -f certbot   # tail certbot only
docker compose restart nginx     # pick up config/cert changes immediately
docker compose down              # stop
```

Test a redirect:

```sh
curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n' \
  https://ifc43-docs.standards.buildingsmart.org/some/path?x=1
```

## Changing the redirect target

Edit `REDIRECT_TARGET` in `.env` (and optionally `PRESERVE_PATH`), then run
`docker compose up -d` to apply.
