#!/bin/bash
cd ~/Dev-Projects/nexus && source .env
for key in PANTHEON_TG_BOT_TOKEN PANTHEON_TG_CHAT_ID PANTHEON_X_API_KEY PANTHEON_X_API_SECRET PANTHEON_X_ACCESS_TOKEN PANTHEON_X_ACCESS_SECRET PANTHEON_THREADS_ACCESS_TOKEN; do
  echo -n "$key: " && nexus-secrets get $key | grep -q "$key" && echo "✓" || echo "MISSING"
done
