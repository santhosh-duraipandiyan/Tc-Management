# Generated by Django 3.2.8 on 2021-11-22 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='Name',
        ),
    ]