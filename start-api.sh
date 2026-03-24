#!/bin/bash
export PATH="/Users/danaschreiber/.pyenv/versions/3.10.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export HOME="/Users/danaschreiber"
cd /Users/danaschreiber/Dev-Projects/pantheon
exec /Users/danaschreiber/.pyenv/versions/3.10.6/bin/uvicorn scripts.pantheon_api:app --host 0.0.0.0 --port 8401
