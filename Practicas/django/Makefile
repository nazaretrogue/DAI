
all:
	docker-compose up

build:
	docker-compose build

django-startproject:
	sudo docker-compose run web django-admin startproject sitio_web .
	sudo chown -R ${USER}:${USER} .

django-startapp:
	sudo docker-compose run web python manage.py startapp práctica_05
	sudo chown -R ${USER}:${USER} .

django-migrate:
	docker-compose run web python manage.py migrate

django-createsuperuser:
	docker-compose run web python manage.py createsuperuser
