#! /bin/sh
case $1 in
  "test")
    echo REACT_APP_BASE_URL="backend" > frontend/.env
    docker-compose --profile test build && docker-compose --profile test up && bash -c rm frontend/.env
    ;;
  *)
    echo REACT_APP_BASE_URL="localhost" > frontend/.env
    docker-compose build && docker-compose up && bash -c rm frontend/.env
    ;;
esac