# Generated by Django 3.0.8 on 2020-09-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='file_route',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='market',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='market',
            name='swap',
            field=models.CharField(max_length=100),
        ),
    ]
