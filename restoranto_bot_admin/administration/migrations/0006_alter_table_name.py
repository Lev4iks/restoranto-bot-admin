# Generated by Django 4.0 on 2021-12-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_table_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
