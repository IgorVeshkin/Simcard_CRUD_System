# Generated by Django 4.2.2 on 2023-06-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_System', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffplan',
            name='Gigabytes',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tariffplan',
            name='Minutes',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tariffplan',
            name='SMS',
            field=models.CharField(max_length=20),
        ),
    ]
