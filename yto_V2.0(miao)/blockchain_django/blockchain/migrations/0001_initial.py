# Generated by Django 2.1 on 2018-11-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('trackNum', models.CharField(default='0', max_length=64)),
                ('deviceId', models.CharField(default='0', max_length=64)),
                ('deviceName', models.CharField(default='0', max_length=64)),
                ('location', models.CharField(default='0', max_length=64)),
                ('image', models.CharField(default='0', max_length=64)),
                ('previous_hash', models.CharField(default='0', max_length=64)),
                ('self_hash', models.CharField(default='0', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='0', max_length=13)),
                ('trackNumSet', models.TextField(default='0')),
                ('name', models.CharField(default='0', max_length=32)),
            ],
        ),
    ]