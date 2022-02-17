#!/bin/sh

# Abort on any error (including if wait-for-it fails).
set -e

# Wait for the backend to be up, if we know where it is.
if [ -n "$BACK_HOST" ]; then
  /frontend/wait-for-it.sh -t 150 "$BACK_HOST:${8000:-8000}"
fi

# Run the main container command.
exec "$@"
