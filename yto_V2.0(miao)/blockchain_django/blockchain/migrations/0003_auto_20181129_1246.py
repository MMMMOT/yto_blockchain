# Generated by Django 2.1 on 2018-11-29 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_auto_20181129_1226'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CommonUser',
        ),
    ]
