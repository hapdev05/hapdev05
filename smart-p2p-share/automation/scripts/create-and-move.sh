#!/usr/bin/env bash
# Usage: create-and-move.sh <label> <source-path>
# Creates a label-based folder under the mounted shared directory and moves the file there.

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <label> <source-path>" >&2
  exit 1
fi

LABEL="$1"
SOURCE="$2"
TARGET_ROOT="${HOST_SHARED_DIR:-/data/shared}"
TARGET_DIR="$TARGET_ROOT/$LABEL"

mkdir -p "$TARGET_DIR"

if [ -f "$SOURCE" ]; then
  mv "$SOURCE" "$TARGET_DIR/"
else
  echo "Warning: source $SOURCE not found" >&2
fi
