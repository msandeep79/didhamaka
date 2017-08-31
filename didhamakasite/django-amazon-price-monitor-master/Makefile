help:
	@echo "docker-build-base: - builds the base docker image (not necessary normally as image is on docker hub)"
	@echo "docker-build-web:  - builds the web docker image"
	@echo "docker-up:         - uses docker-compose to bring the containers up"
	@echo "docker-stop:       - uses docker-compose to stop the containers"
	@echo "docker-ps:         - runs docker-compose ps"

docker-build-base:
	docker build -t pricemonitor/base docker/base/

docker-build-web:
	cp setup.py docker/web/django-amazon-price-monitor/setup.py
	sed -i 's/readme = .*/readme = ""/g' docker/web/django-amazon-price-monitor/setup.py
	sed -i 's/history = .*/history = ""/g' docker/web/django-amazon-price-monitor/setup.py
	docker build -t pricemonitor/web docker/web/

docker-up:
	cd docker && docker-compose -p "pm" up -d

docker-stop:
	cd docker && docker-compose -p "pm" stop

docker-ps:
	cd docker && docker-compose -p "pm" ps

docker-reload: docker-build-web docker-up
