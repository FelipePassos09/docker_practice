FROM node:14.16.0-buster

# RUN addgroup app && adduser -S -G app app
# USER app

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . . 

EXPOSE 3001 

CMD ["npm", "start"]