#!/bin/sh
echo -n "[ilia-ecole42-xavier]\n
aws_access_key_id=$AWS_ACCESS_KEY_ID\n
aws_secret_access_key=$AWS_SECRET_ACCESS_KEY\n
aws_region=$AWS_REGION" > ~/.aws/credentials
