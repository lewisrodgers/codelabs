FROM node:10.10.0

RUN mkdir /app
COPY *.js /app/
COPY *.json /app/
RUN npm install -g eslint eslint-config-google
CMD ["/usr/local/bin/npm", "run", "lint"]