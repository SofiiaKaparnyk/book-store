lint:
	black . && isort . && flake8 .

shell:
	docker exec -it my_site-web-1 /bin/sh -c "python manage.py shell"


