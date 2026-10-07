#!/bin/sh
set -eu
mkdir -p /workspace/.home /workspace/.cache /workspace/output
exec "$@"
