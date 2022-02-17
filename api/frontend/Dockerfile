FROM node:lts-alpine3.15

WORKDIR /frontend/

COPY . /frontend/

RUN apk add --upgrade make
RUN apk add --no-cache bash

RUN chmod +x ./wait-for-it.sh ./docker-entrypoint.sh
EXPOSE 3000

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["make"]