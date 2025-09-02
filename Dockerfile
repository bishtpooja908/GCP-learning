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

RUN mkdir -p /tmp/nginx/client_temp \
           /tmp/nginx/proxy_temp \
           /tmp/nginx/fastcgi_temp \
           /tmp/nginx/uwsgi_temp \
           /tmp/nginx/scgi_temp \
           /var/cache/nginx /var/run \
 && chown -R 1000:3000 /var/cache/nginx /var/run /tmp


# Copy built React app from builder stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy default Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
