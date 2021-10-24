# Generated by Django 3.2.8 on 2021-10-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Dept',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Address',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Caste_Community',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Conduct',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Date_Of_Admission',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Date_Of_Leaving',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Dept',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_Department',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_Hostel',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_Labs',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_Library',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_NSS',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_Office',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Due_PE',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Father_Name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Nationality',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='No_Dues_Certificate',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Purpose_Of_TC',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Reg_No',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Religion',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Roll_No',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Scholarship',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Signature_Of_HOD',
            field=models.BooleanField(default=False, null=True),
        ),
    ]