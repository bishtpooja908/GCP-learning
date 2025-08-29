# Stage 1: Build the React app
FROM node:24-alpine AS build

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy project files and build
COPY . .
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy built React app from builder stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy default Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
