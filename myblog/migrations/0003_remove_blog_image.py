# Generated by Django 3.0.6 on 2020-05-31 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200531_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]