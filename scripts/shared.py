#!/usr/bin/env python3
"""Shared utilities for Pantheon pipeline scripts."""

import subprocess
import sys


def get_secret(key: str) -> str:
    """Fetch a secret from the Nexus vault."""
    result = subprocess.run(
        ["bash", "-c",
         f"set -o pipefail; cd ~/Dev-Projects/nexus && source .env && "
         f"nexus-secrets get {key} | sed 's/^{key}[[:space:]]*=[[:space:]]*//' | tr -d '\\n[:space:]'"],
        capture_output=True, text=True
    )
    val = result.stdout.strip()
    if result.returncode != 0 or not val:
        sys.exit(f"✗ Secret '{key}' not found in vault")
    return val
