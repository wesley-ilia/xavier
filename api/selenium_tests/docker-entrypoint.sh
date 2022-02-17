#!/bin/sh

# Abort on any error (including if wait-for-it fails).
set -e

# Wait for the backend to be up, if we know where it is.
if [ -n "$FRONT_HOST" ]; then
  /selenium_tests/wait-for-it.sh -t 150 "$FRONT_HOST:${3000:-3000}"
fi

# Run the main container command.
exec "$@"