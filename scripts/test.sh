#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
. "$SCRIPT_DIR/env.sh"

curl -s -H "Authorization: Token $SECRET" http://0.0.0.0:8080 | jq