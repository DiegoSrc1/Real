# Generated by Django 4.1.2 on 2024-01-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_productos_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]