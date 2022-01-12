#!/bin/sh
mkdir -p ~/.aws
echo "[ilia-ecole42-xavier]
aws_access_key_id=$AWS_ACCESS_KEY_ID
aws_secret_access_key=$AWS_SECRET_ACCESS_KEY
aws_region=$AWS_REGION" > ~/.aws/credentials

exec "$@"
