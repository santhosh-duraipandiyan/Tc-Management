# Generated by Django 3.2.8 on 2021-11-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211123_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='Due',
            new_name='Hostel',
        ),
        migrations.RemoveField(
            model_name='due',
            name='Due',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='Year',
        ),
        migrations.AddField(
            model_name='due',
            name='Year',
            field=models.IntegerField(blank=True, default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='Labs',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='Library',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='Office',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='Dept',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]