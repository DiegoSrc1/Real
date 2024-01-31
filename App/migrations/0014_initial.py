# Generated by Django 4.1.2 on 2024-01-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0013_delete_contacto_delete_productos_delete_servilletas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=20, null=True)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('precio_x_mayor', models.IntegerField()),
                ('categoria', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servilletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='servilletas')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]