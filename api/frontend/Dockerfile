FROM node:lts-alpine3.15

WORKDIR /frontend/
COPY . /frontend/

RUN npm install && npm run build

ENTRYPOINT ["npm", "start"]
