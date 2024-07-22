FROM node:20.8.1-alpine AS base

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./


# Install project dependencies
RUN npm install --only=production

# Copy app source code
COPY . .

# Expose port and start application
EXPOSE 3000
CMD [ "node", "server.js" ]
