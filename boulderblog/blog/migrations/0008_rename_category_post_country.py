# Generated by Django 3.2.2 on 2021-05-11 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_category_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='country',
        ),
    ]