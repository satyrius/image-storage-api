install: env pip

env:
	[[ -d env ]] || virtualenv env

pip:
	env/bin/pip install -r requirements.txt
	env/bin/pip install -r requirements-dev.txt
	env/bin/pip install -r requirements-test.txt

test:
	cd storage && python manage.py test
