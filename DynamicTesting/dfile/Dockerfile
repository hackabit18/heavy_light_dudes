
FROM node:7
ARG VERSION=1.0.0

WORKDIR /usr/src/app
COPY /node/package.json /node/app.js node/LICENSE /usr/src/app/
COPY /node/lib /usr/src/app/lib/
LABEL license=MIT       version=$VERSION

ENV NODE_ENV production

RUN npm update

CMD ["node", "app.js"]
