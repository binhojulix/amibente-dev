FROM nginx:1.21

RUN apt-get update \
    && apt-get install -y git

COPY index.html /etc/nginx/html/index.html
COPY conf /etc/nginx/conf.d/default.conf