# Django Shell Commands

List of useful commands to open a shell prompt using either the standard `python` interpreter, `ipython` or `bpython`.

With a virtual environment activated, this loads all of the environment variables and project settings.

### Python

```sh
docker-compose exec web python manage.py shell -i python
```

### iPython

```sh
docker-compose exec web python manage.py shell -i ipython
```

### bPython

```sh
docker-compose exec web python manage.py shell -i bpython
```

### bPython in Shell Plus

This method means that all of the Django models are loaded upon start-up to save any importing. This requires `django-extensions` to be installed.

```sh
docker-compose exec web python manage.py shell_plus --bpython
```

### iPython in Shell Plus

This method means that all of the Django models are loaded upon start-up to save any importing. This requires `django-extensions` to be installed.

```sh
docker-compose exec web python manage.py shell_plus --ipython
```
