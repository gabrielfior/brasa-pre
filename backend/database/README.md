# Creating/updating models in the database

1. Update models
2. Create migration

```shell
python backend/manage.py db migrate -m "my-cool-migration"
```

3. Upgrade head

```shell
python backend/manage.py db upgrade head
```

* If needed, downgrade
```shell
python backend/manage.py db downgrade
```


Reference:
- https://flask-migrate.readthedocs.io/en/latest/
