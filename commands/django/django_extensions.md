# Django Shell Commands

List of useful commands to use with Django Extensions

### View an Image of Your App's Models

```sh
docker-compose exec web python manage.py graph_models -a -o <app_name>_models.png
```

### Produce a tab-separated list of (url_pattern, view_function, name) tuples for a project

```sh
docker-compose exec web python manage.py show_urls
```

### Check templates for rendering errors

```sh
docker-compose exec web python manage.py validate_templates
```

### Show each field's class

```sh
docker-compose exec web python manage.py list_model_info --field-class
```

### Show each field's database type representation

```sh
docker-compose exec web python manage.py list_model_info --db-type
```

### Show each method's signature

```sh
docker-compose exec web python manage.py list_model_info --signature
```

### Show all model methods, including private methods and django's default methods

```sh
docker-compose exec web python manage.py list_model_info --all-methods
```
