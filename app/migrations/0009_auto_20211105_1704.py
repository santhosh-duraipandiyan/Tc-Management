# Generated by Django 3.2.8 on 2021-11-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_student_scholarship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(default=None, max_length=20, null=True)),
                ('due', models.CharField(default=None, max_length=20, null=True)),
                ('Due_Date', models.DateField(default=None, null=True)),
                ('is_Paid', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(default=None, max_length=20, null=True)),
                ('Fees', models.CharField(default=None, max_length=20, null=True)),
                ('Due_Date', models.DateField(default=None, null=True)),
                ('is_Paid', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LAB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(default=None, max_length=20, null=True)),
                ('Instrument', models.CharField(default=None, max_length=20, null=True)),
                ('Due_Date', models.DateField(default=None, null=True)),
                ('is_Paid', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(default=None, max_length=20, null=True)),
                ('Book', models.CharField(default=None, max_length=20, null=True)),
                ('Initial_Date', models.DateField(default=None, null=True)),
                ('Due_Date', models.DateField(default=None, null=True)),
                ('is_Returened', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_No', models.CharField(default=None, max_length=20, null=True)),
                ('Type', models.CharField(default=None, max_length=20, null=True)),
                ('Due_Date', models.DateField(default=None, null=True)),
                ('is_Paid', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='requests',
            name='NSS',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='PE',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Due_NSS',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Due_PE',
        ),
    ]