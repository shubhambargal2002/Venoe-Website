FROM node:18.16

WORKDIR /home/app

COPY . .

RUN yarn install

RUN yarn build

ENV PORT=4005

CMD yarn serve