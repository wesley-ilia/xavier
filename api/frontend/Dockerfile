FROM node:lts-alpine3.15

WORKDIR /frontend/

COPY . /frontend/

RUN apk add --upgrade make

ENTRYPOINT ["make"]
