# Generated by Django 2.1 on 2018-11-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='dpCreationTime',
            field=models.DateTimeField(default=None, verbose_name='过包时间戳'),
        ),
        migrations.AddField(
            model_name='block',
            name='timestamp',
            field=models.DateTimeField(default=None, verbose_name='区块时间戳'),
        ),
    ]