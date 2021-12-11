from django.db import models


class Administrator(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'administration'


class Restaurant(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        db_table = 'restaurant'
