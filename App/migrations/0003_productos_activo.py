# Generated by Django 4.1.2 on 2024-01-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
