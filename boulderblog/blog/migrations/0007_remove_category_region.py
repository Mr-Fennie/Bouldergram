# Generated by Django 3.2.2 on 2021-05-11 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210511_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='region',
        ),
    ]
