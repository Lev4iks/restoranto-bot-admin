from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField(default="")
    user_login = models.CharField(max_length=255, default="")

    class Meta:
        db_table = 'restaurant'


class Table(models.Model):
    auth = models.CharField(max_length=64, default="test")
    login = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'table'
