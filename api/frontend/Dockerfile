FROM node:lts-alpine3.15 as build-stage

WORKDIR /usr/app

COPY . /usr/app

RUN npm install

ENV PATH /usr/src/app/node_modules/.bin:$PATH

RUN npm run build

FROM nginx:alpine 

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=build-stage /usr/app/build .

ENTRYPOINT ["nginx", "-g", "daemon off;"]
