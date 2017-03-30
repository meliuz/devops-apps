FROM php:5.6-alpine

RUN apk update
RUN apk add ca-certificates openssl
RUN update-ca-certificates

RUN wget -O /usr/local/bin/composer https://getcomposer.org/download/1.4.1/composer.phar
RUN chmod +x /usr/local/bin/composer

ADD composer.* /app/
RUN cd /app && composer install

ADD . /app
WORKDIR /app
