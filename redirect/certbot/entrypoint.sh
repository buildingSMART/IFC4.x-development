#!/bin/sh
set -e

DOMAIN="${DOMAIN:-ifc43-docs.standards.buildingsmart.org}"
EMAIL="${CERTBOT_EMAIL:-}"
STAGING="${CERTBOT_STAGING:-0}"

CERT="/etc/letsencrypt/live/${DOMAIN}/fullchain.pem"

STAGING_FLAG=""
[ "$STAGING" = "1" ] && STAGING_FLAG="--staging"

if [ ! -f "$CERT" ]; then
  if [ -z "$EMAIL" ]; then
    echo "[certbot] CERTBOT_EMAIL is required for the initial certificate request." >&2
    exit 1
  fi

  echo "[certbot] Waiting for nginx to serve the ACME webroot on port 80..."
  until wget -q -O /dev/null "http://nginx/"; do
    echo "[certbot] nginx not ready yet, retrying in 5s..."
    sleep 5
  done

  echo "[certbot] Requesting a certificate for ${DOMAIN}."
  until certbot certonly \
      --webroot \
      -w /var/www/certbot \
      -d "$DOMAIN" \
      --email "$EMAIL" \
      --agree-tos \
      --no-eff-email \
      --non-interactive \
      --rsa-key-size 4096 \
      $STAGING_FLAG; do
    echo "[certbot] Request failed; retrying in 60s..."
    sleep 60
  done
fi

echo "[certbot] Starting the automatic renewal loop."
trap 'exit 0' TERM
while :; do
  echo "[certbot] Checking for renewals..."
  certbot renew --webroot -w /var/www/certbot --non-interactive || true
  sleep 12h & wait $!
done
