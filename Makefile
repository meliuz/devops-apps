build: build-php build-python

build-php:
	docker-compose build php
	docker-compose run --rm php composer install

build-python:
	docker-compose build python

clean: down
	rm -rf php_app/vendor/

down:
	docker-compose down

up:
	docker-compose up
