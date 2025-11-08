#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

./gradlew -p "$ROOT_DIR/apps" build

(cd "$ROOT_DIR/docker" && docker compose up -d)
