# Generated by Django 4.1.2 on 2024-01-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_alter_productos_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
