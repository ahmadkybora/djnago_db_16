# Generated by Django 4.2.11 on 2024-04-03 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crud',
            options={'verbose_name': 'Crud', 'verbose_name_plural': 'Cruds'},
        ),
        migrations.AlterModelTable(
            name='crud',
            table='cruds',
        ),
    ]