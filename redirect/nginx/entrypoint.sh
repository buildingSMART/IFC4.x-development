#!/bin/sh
set -e

DOMAIN="${DOMAIN:-ifc43-docs.standards.buildingsmart.org}"
CERT="/etc/letsencrypt/live/${DOMAIN}/fullchain.pem"

# The stock nginx image ships a default site; we manage our own.
rm -f /etc/nginx/conf.d/default.conf

render() {
  envsubst '$DOMAIN' < "$1" > /etc/nginx/conf.d/site.conf
}

if [ ! -f "$CERT" ]; then
  echo "[nginx] No certificate for ${DOMAIN} yet; starting in bootstrap mode (ACME webroot only)."
  render /opt/nginx/bootstrap.conf
  nginx -g 'daemon off;' &
  NGINX_PID=$!

  echo "[nginx] Waiting for the certificate to be issued..."
  while [ ! -f "$CERT" ]; do
    sleep 5
  done

  echo "[nginx] Certificate found; switching to the final HTTPS config."
  nginx -s quit
  wait "$NGINX_PID" || true
fi

render /opt/nginx/app.conf

# Reload periodically so renewed certificates are picked up automatically.
( while :; do sleep 6h; nginx -s reload 2>/dev/null || true; done ) &

echo "[nginx] Starting nginx."
exec nginx -g 'daemon off;'
